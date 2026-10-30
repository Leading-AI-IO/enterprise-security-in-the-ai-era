# パッチの向こう側 ── AI時代のエンタープライズ・セキュリティを、世界の提言から読む

"The race to prevent intrusion is being lost to the attackers on speed. The only things a company can decide for itself are three: what to hold, when to notice and how to tell. And these three are the thinnest part of the world's proposals." <br>
（侵入を防ぐ競争は、速度で攻撃側に負けている。会社が自分で決められるのは「何を持つか」「いつ気づくか」「どう伝えるか」の三つだけであり、この三つは世界の提言の中で最も薄い）

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Language](https://img.shields.io/badge/Language-Japanese%20%7C%20English-blue)](docs/)
[![Proposals](https://img.shields.io/badge/Proposals-211-informational)](data/proposals.csv)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--10--30-brightgreen)](https://github.com/Leading-AI-IO/enterprise-security-in-the-ai-era)

<p align="left">
  <img src="./assets/ogp_design.png" width="80%">
</p>

*Read this in other languages: [English](README_en.md)*

---

> **定義｜What is Where the Patch Ends**
>
> **本書とは**、山内怜史（Satoshi Yamauchi）による、AI時代のエンタープライズ・セキュリティについて
> 世界の8種類の発行元（政府・公的機関、標準団体、AI企業、セキュリティ企業、保険会社、学術、
> 個人の有識者、規制当局）が2025年から2026年にかけて書いた提言を、**一次資料のURLを著者が
> 開いて本文で確かめたものだけ**台帳に並べ、そこから会社が決められることを示す更新型の提言書である。
> 第1版（2026年10月30日）の台帳は263行、うち本文の集計対象は一次資料で確かめた211件。
> 第1部と第2部は断定しない。攻撃側が分で動き防御側が日で動くこと、提言の中身はAI以前と同じだと
> 発行元自身が書いていること、修正が間に合わない期間の手当てが効果の実証なしに制度になったことを、
> 一次資料の言葉で記録し、211件の提言の合意・対立・空白を数える。第3部から著者の主張に入る。
> 効くかどうかが測られていない中で、攻撃が成功しても意味を持ち、会社が他者の協力なしに決められる
> ことを探すと、**何を持つか、いつ気づくか、どう伝えるか**の三つが残り、この三つが世界の提言の中で
> 最も薄い。第4部は、決めたことが止める判断・委託先との契約・稟議と保険と取締役会をどう通るかを書く。
> 本書は、どの対策が攻撃を防ぐかを書かず、AIが漏えいの原因だとも書かず、予測もしない。
> 終章に置くのは、次の版で数え直す16の指標である。姉妹書『The Japan Breach Registry 2026』
> （事実の台帳）と対をなす。
>
> **This book**, by Satoshi Yamauchi, lines up the proposals on enterprise security in the AI era
> written in 2025–2026 by eight kinds of issuer — governments and public bodies, standards bodies,
> AI companies, security companies, insurers, academia, individual experts and regulators — **admitting
> only those whose primary source the author opened and verified in the text**, and from that ledger
> shows what a company can decide. The first edition (30 October 2026) holds 263 rows, of which 211
> verified proposals are counted in the text. Parts 1 and 2 assert nothing: they record, in the words
> of the primary sources, that attackers move in minutes while defenders move in days, that the issuers
> themselves wrote that their proposals are "not new", and that the stop-gap for the period when a fix
> is not in time was written into law without measured evidence, and they count where the 211 proposals
> agree, conflict and fall silent. Part 3 is where the author's claims begin: with no proposal's effect
> measured, the things that still mean something when the attack succeeds and that a company can decide
> without anyone's cooperation come down to three — **what to hold, when to notice and how to tell** —
> and these three are the thinnest part of the world's proposals. Part 4 follows those decisions through
> the decision to stop, the vendor contract, and the approval, the insurance and the board. The book does
> not say which measures prevent attacks, does not say AI caused the breaches, and makes no forecast; the
> conclusion sets out sixteen indicators to be recounted in the next edition. It is the companion to
> *The Japan Breach Registry 2026*, the ledger of facts.
>
> **管理と責任 / Governance**：台帳に書くのは著者一人である。本文の集計に入る基準は「一次資料のURLを
> 著者が開き、提言の文言を本文で確かめたこと」の1つであり（階層T1・T2）、確かめられていない行は
> T3として台帳に残すが数えない。第3部以降の提言は著者の主張であり、一次資料の記述とは分けて書く。
> 著者はセキュリティの専門家ではなく、AIが事業と組織をどう変えるかを書いてきたAIストラテジストである。
> 読者ができるのは、台帳を検証すること、誤りを指摘すること、一次資料の所在を知らせることである。
> The author is the sole writer. One criterion admits a row into the count — the author opened the
> primary source and verified the wording (tiers T1 and T2); unverified rows stay in the ledger as T3
> and are not counted. The claims from Part 3 onward are the author's and are kept apart from what the
> sources say. The author is not a security specialist but an AI strategist. Readers verify, report
> errors, and point to primary sources.
>
> *著者・全書籍一覧 / Author & full catalog: [github.com/Leading-AI-IO](https://github.com/Leading-AI-IO)*

---

## 📖 概要

2026年の秋、日本で個人情報の漏えいが立て続けに公表された。著者はそれを公表文の原文のまま1通ずつ台帳に並べ、姉妹書『The Japan Breach Registry 2026』として公開した。第3版で71通になった。

台帳を閉じたあとに、1つの問いが残った。**では、会社は何を決めるのか。** 公表文を書いた71の組織は、どれも対策をしていた。多要素認証、パッチ、委託先の管理。世界の提言が言うことは、やっていた。それでも漏れた。漏れたあと、会社が書けたのは「不正アクセスを受けた」「漏えいした可能性を否定できない」だった。

**本書は、この問いに答えるために、世界の提言を集めた。**

### 提言台帳

8種類の発行元が2025年から2026年にかけて書いた提言を、一次資料のURLを開いて本文で確かめたものだけ、台帳 `data/proposals.csv` にした。第1版で263行、うち集計対象は211件（階層T1・T2の非統合行）。提言は9種類（K1〜K9）に分類し、日本の台帳の侵入経路との対応を1行ごとに書いた。

集めた提言を、3つの問いで読んだ。どこで一致しているか（第4章）、どこで食い違っているか（第5章）、どこが空白か（第6章）。**211件のうち、効果を測ったものは14件で、どれも条件つきの相関である。データの最小化（K5）は副分類を含めて13件で9種類中最少、書いているのは政府・公的機関と保険1件だけである。**

### 会社が決められる三つ

答えは、空白にあった。提言が厚いのは、攻撃を防ぐ側である。脆弱性の修正、多要素認証、検知の製品。薄いのは、攻撃が成功したあとに意味を持つ側である。

- **持たない（第7章）**：持っている量が、漏れうる最大値を決める
- **気づく（第8章）**：記録があるかどうかが、実際の漏えいをその最大値の内側で絞れるかを決める。ログの保持期間を日数で定めた提言は、インドCERT-Inの1件だけである
- **伝える（第9章）**：絞れるかどうかが、速く上限で知らせるか、絞ってから知らせるかの選択肢を決める。日本の公表文71通は、上限で出した18通、記録で絞った24通、件数を書けなかった14通、どちらとも読めない15通に分かれた

三つは独立ではなく連鎖であり、どれも技術ではなく、決めることである。

### 会社の中で通す

決めたことは、会社の中の三つの場所を通る。止める判断（第10章。日本の金融庁・日本銀行が経営トップに事前の基準を求めた、本書の収集の範囲で類例のない提言）、委託先との契約（第11章。日本では契約自体がない会社が監督の対象になっている）、稟議・保険・取締役会（第12章。通るのは効果の証拠ではなく、自社の数字である）。第4部で新しい決定は増えない。

### 本書が断定しないこと

どの対策が攻撃を防ぐかを、本書は書かない。測った資料がない。「修正できない期間は、代替の防御で攻撃を防げる」を、どの提言の前提にも置かない。AIが漏えいの原因だとは書かない。日本が世界より遅れているとは書かない。公表文を書いた組織を評価しない。そして、次に何が起きるかを予測しない。予測を記録する場所は、別の台帳『The AI Forecast Registry』にある。

---

## 📊 台帳データ

| ファイル | 位置づけ | 内容 |
| --- | --- | --- |
| [proposals.csv](./data/proposals.csv) | **正本** | 提言台帳。263行・18列（UTF-8 BOM付き）。列の定義は付録A-2、数え方は付録A-4 |
| [count_proposals.py](./scripts/count_proposals.py) | 集計スクリプト | 正本から、終章の指標表と第4章・第6章の件数を数え直す。ファイルは変更しない |

**本書の更新は3か所に限る。** 提言台帳 `data/proposals.csv`、付録B（検証記録）、終章の指標表。本文の数字は各章冒頭の「第N版時点」欄とこの3か所から参照し、本文の文章を変えるときは変更箇所の直前に「（YYYY年M月D日追記／訂正）」を置く。読者は本文を読まずに `data/proposals.csv` だけを開いてもよい。

---

## 📄 ドキュメント

| ファイル | 言語 | 内容 |
| --- | --- | --- |
| [enterprise-security-in-the-ai-era_JP.md](./docs/jp/enterprise-security-in-the-ai-era_JP.md) | 🇯🇵 日本語 | 本文（日本語版）。序章・4部12章・終章・付録A/B、図17点 |
| [enterprise-security-in-the-ai-era_EN.md](./docs/en/enterprise-security-in-the-ai-era_EN.md) | 🇺🇸 English | 本文（英語版） |
| [UPDATE_RUNBOOK.md](./docs/UPDATE_RUNBOOK.md) | 🇯🇵 日本語 | 更新手順書。台帳に書くのは著者一人であり、その運用手順を公開している |

---

## 🔄 更新履歴

| 日付 | 版 | 内容 |
| --- | --- | --- |
| 2026-10-30 | v1.0 | 第1版。提言台帳263行（集計対象211件、T3 39行）。序章・第1〜12章・終章・付録A/B。日本語版・英語版 |

---

## 📑 目次

- 序章: 問い ── 公表文を並べ終えたあとに残ったもの
- **第1部　なぜ防げないのか**
  - 第1章: 速度の非対称 ── 29分と43日
  - 第2章: 「not new」と書いた三つの一次資料 ── AIが変えなかったこと
  - 第3章: 実証なき制度化 ── 「緩和で代替してよい」が法になった経緯
- **第2部　世界の提言の地図**
  - 第4章: 合意 ── 8種類の発行元が一致した提言は、すべてAI以前の対策
  - 第5章: 対立 ── 速く直せ vs 直せない前提で動け
  - 第6章: 空白 ── 効果測定ゼロ、データ最小化13件
- **第3部　会社が決められる三つ**
  - 第7章: 持たない ── 侵入の成否と無関係に、被害を減らせる唯一の手段
  - 第8章: 気づく ── ログの保持期間を、誰が決めているか
  - 第9章: 伝える ── 何件に知らせるかを、誰が決めているか
- **第4部　会社の中で通す**
  - 第10章: 能動的に止める判断 ── 誰が、いつ、決めているか
  - 第11章: 委託先と「契約がない」現実 ── 決めたことは、契約のどこに書かれているか
  - 第12章: 保険・稟議・取締役会 ── 決めたことは、どこで通るか
- 終章: 次の版で数え直すこと
- 付録A: 方法 ── どう集め、どう確かめ、どう数えたか
- 付録B: 検証記録 ── 確認できた数字、できなかった数字

---

## 🔗 Related Projects

本書は、以下のOSSプロジェクトと相互に接続されている。

| プロジェクト | 概要 | リンク |
| --- | --- | --- |
| **The Japan Breach Registry 2026**  | 2026年秋、日本の企業・組織を襲った個人情報漏えいの波。本書の姉妹書（事実の台帳） | [GitHub](https://github.com/Leading-AI-IO/the-japan-breach-registry-2026) |
| **The AI Forecast Registry**        | AIをめぐる予測を決着の前に記録し、帰結を発言者自身の言葉で追う台帳。本書が予測を置かない代わりに参照する | [GitHub](https://github.com/Leading-AI-IO/the-ai-forecast-registry)       |
| **The China AI Registry**           | 中国のAI産業を当局の登録名簿988件を母集団として読む。名簿シリーズ第1弾 | [GitHub](https://github.com/Leading-AI-IO/the-china-ai-registry)          |
| **The Anatomy of Anthropic**        | Anthropicの戦略・製品・研究・安全性を包括的に解剖 | [GitHub](https://github.com/Leading-AI-IO/anatomy-of-anthropic)           |
| **The Silence of Intelligence**     | Anthropic CEO ダリオ・アモディの思想を体系化 | [GitHub](https://github.com/Leading-AI-IO/the-silence-of-intelligence)    |
| **Frontier-Grade Open Weights**     | フロンティア級のオープンウェイトモデルは、開かれたのか | [GitHub](https://github.com/Leading-AI-IO/frontier-grade-open-weights)    |
| **US-China AI Competition**         | 米中AI競争の多層構造 | [GitHub](https://github.com/Leading-AI-IO/us-china-ai-competition)        |
| **Earned AI Model Optionality**     | AIモデルは選べる。選べるのは、選べるようにした企業だけだ | [GitHub](https://github.com/Leading-AI-IO/earned-ai-model-optionality)    |
| **The AI Strategist**               | AIストラテジストという職業を定義する | [GitHub](https://github.com/Leading-AI-IO/the-ai-strategist)              |

その他の書籍は [github.com/Leading-AI-IO](https://github.com/Leading-AI-IO) を参照。

---

## 👤 著者

**Satoshi Yamauchi** (山内 怜史)

* **AI Strategist & Business Designer at Sun Asterisk Inc.**
* **Founder / AI Strategist at [Leading.AI](https://www.leading-ai.io/)**
* 15年以上にわたりBusiness・Technology・Creativeの3領域を越境。フューチャーアーキテクトでITコンサルタントとして40案件のPL/PMを推進後、リクルートで事業戦略・新規事業開発に従事。Sun Asteriskでビジネスデザイナー兼AIストラテジストとして、新規事業×生成AIの方法論「Depth & Velocity」を体系化。
* This project is part of the research by Leading.AI.
* [📒 Read my insights on Note](https://note.com/satoshi_yamauchi)
* [🌐 Visit Leading.AI Official Website](https://www.leading-ai.io/)

---

## 🤝 Contributing

**本書は Pull Request を受け付けない。** 台帳に書くのは著者一人であり、これは本書の設計の一部である。一次資料を開いた者だけが階層を付け、提言の文言を本文の語に差し替える、という規律は、書き手が増えるほど揺れる。揺れた台帳は、検証に使えない。

Issues は歓迎する。受け付けるのは次の二種である。

**① 誤りの指摘。** 提言の文言が一次資料と一致しない。階層（T1〜T3）や種類（K1〜K9）の判定が一次資料の記述と合っていない。日付が違う。URLが到達しない。本文の件数が台帳と合わない。著者は一次資料に照らして確認し、誤りであれば訂正を追記する。**元の行は消さない。** 指摘した方の名は、台帳の該当行または付録Bに記す。

**② 一次資料の所在。** 本書が集計の外に置いているT3の39行について、一次資料の本文に到達できるURLをご存知の方からの情報提供を歓迎する。著者が開き、文言を確かめたうえでT1またはT2に格上げする。**基準を満たす行は例外なく数える。**

「この対策は効く」「効かない」という判定を含むIssueは、効果を測った一次資料の所在が添えられている場合に、その部分を受け付ける。本書は、一次資料にある記述だけを記録する。

とくに、第1版の時点で著者が確かめきれていない以下（付録A-7）について、情報提供を歓迎する。

- CISA BOD 26-04の指令本文（現在はCISAの告知、FedRAMPの一次資料、第三者の解説に依拠）
- Mandiant M-Trends 2026 報告書本体（現在は発表記事に依拠）
- EU NIS2 第23条の本文のEUR-Lex上の所在（第1版は前文102のみEUR-Lexで確認）
- 日本の個人の有識者の、本人名義の一次資料（寄稿・講演録・議会証言）

---

## 📝 License

本書は [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) の下で公開されている。出典を明記すれば、自由に引用・転載・改変できる。

Copyright (c) 2026 Leading.AI
