#!/usr/bin/env python3
"""提言台帳 data/proposals.csv から、本文と終章の指標表が使う件数を数え直す。

使い方:
    python3 scripts/count_proposals.py

出力:
    終章「次の版で数え直す指標」のうち、台帳から機械的に数えられる指標（1〜4、7）と、
    第4章・第6章が使う内訳（階層別、発行元の種類別、提言の種類別、侵入経路との対応）を
    標準出力に表示する。ファイルは変更しない。

数え方（付録A-4）:
    - 集計対象は T1・T2 の非統合行（merged_into が空の行）
    - 提言の種類（K）は副分類を含めて数える。「主分類」は k 列の先頭の種類
    - 「効果測定あり」は status 列にその語を含む行
    - 侵入経路との対応は route 列。複数の経路に対応する行は、各経路に数える
"""
import collections
import csv
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "proposals.csv"

TYPE_NAMES = {
    "A": "政府・公的機関",
    "B": "標準団体",
    "C": "AI企業",
    "D": "セキュリティ企業",
    "E": "保険",
    "F": "学術",
    "G": "個人の有識者",
    "H": "規制当局",
}

K_NAMES = {
    "K1": "脆弱性の発見と修正",
    "K2": "修正できない期間の防御",
    "K3": "攻撃の予期と検知",
    "K4": "委託先・サプライチェーン",
    "K5": "データの最小化と構造",
    "K6": "ガバナンスと経営",
    "K7": "AIモデル固有",
    "K8": "制度・規制・国際協調",
    "K9": "インシデント対応・公表・復旧",
}


def split_k(value: str) -> list[str]:
    """k 列から種類の記号（K1〜K9）を出現順に取り出す。先頭が主分類。"""
    return re.findall(r"K[1-9]", value)


def split_route(value: str) -> list[str]:
    """route 列から経路の一覧を取り出す。末尾の参照リンク（[[…]]）は除き、「・」「、」「/」で区切る。"""
    value = re.sub(r"\[\[.*$", "", value).strip()
    return [p.strip() for p in re.split(r"[・、/]", value) if p.strip()]


def main() -> None:
    with SRC.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    non_merged = [r for r in rows if not r["merged_into"].strip()]
    counted = [r for r in non_merged if r["tier"] in ("T1", "T2")]

    print(f"台帳の行数: {len(rows)}（統合された行 {len(rows) - len(non_merged)} を含む）")
    print(f"非統合行の階層: {dict(sorted(collections.Counter(r['tier'] for r in non_merged).items()))}")
    print(f"集計対象（T1・T2の非統合行）: {len(counted)}件  ← 指標1")
    print()

    effect = [r for r in counted if "効果測定あり" in r["status"]]
    print(f"効果測定あり: {len(effect)}件  ← 指標2")
    for r in effect:
        print(f"  {r['new_id']}  {r['type']}  {r['k']}")
    print()

    k_any = collections.Counter()
    k_primary = collections.Counter()
    for r in counted:
        ks = split_k(r["k"])
        for k in set(ks):
            k_any[k] += 1
        if ks:
            k_primary[ks[0]] += 1
    print("提言の種類（副分類を含む件数 / 主分類での件数）:")
    for k in sorted(K_NAMES):
        print(f"  {k} {K_NAMES[k]:<16} {k_any.get(k, 0):>3} / {k_primary.get(k, 0):>3}")
    print(f"K5 データの最小化: {k_any.get('K5', 0)}件（主分類 {k_primary.get('K5', 0)}件）  ← 指標3")
    k5_types = sorted({r["type"] for r in counted if "K5" in split_k(r["k"])})
    print(f"K5を書いた発行元の種類: {len(k5_types)}種類 {k5_types}  ← 指標4")
    print()

    print("発行元の種類（集計対象）:")
    by_type = collections.Counter(r["type"] for r in counted)
    for t in sorted(TYPE_NAMES):
        print(f"  {t} {TYPE_NAMES[t]:<8} {by_type.get(t, 0):>3}")
    print("個人の有識者（G）の行:  ← 指標7は、このうち日本の有識者の本人名義の一次資料を本文で確認して数える")
    for r in counted:
        if r["type"] == "G":
            print(f"  {r['new_id']}  {r['issuer'][:60]}")
    print()

    print("侵入経路との対応（route 列、複数対応は各経路に数える）:")
    routes = collections.Counter()
    for r in counted:
        for part in split_route(r["route"]):
            routes[part] += 1
    for name, n in routes.most_common():
        print(f"  {name:<24} {n:>3}")


if __name__ == "__main__":
    main()
