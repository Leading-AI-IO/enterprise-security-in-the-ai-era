# Where the Patch Ends ── Update Runbook (English)

(Added November 15, 2026)<br>
This is an English translation of [UPDATE_RUNBOOK.md](./UPDATE_RUNBOOK.md), added in v1.1. The Japanese file is canonical; if the two differ, the Japanese file prevails. The translation was made by the author with AI assistance and has not been reviewed by an independent translator. Values written in the ledger's Japanese columns (for example 未開封, "not opened") are kept in Japanese, with an English gloss in brackets where needed.

This file is public. The proposal ledger is written by one person, the author (see "Governance" in the README), and this file lets readers verify the procedure by which that one person actually adds and corrects entries. The verifiability this book asked of the world's proposals (open the primary source and check it) is applied here to the author's own operating procedure.

**Target repository**: `https://github.com/Leading-AI-IO/enterprise-security-in-the-ai-era`
**Signing key**: Every commit is signed with the same author key as in the runbooks of the companion books *The Japan Breach Registry 2026* and *The AI Forecast Registry*. The public key is registered on the author's GitHub account and can be matched against the `Verified` badge on each commit. The private key is not included here. **The commits of the first edition (2026-10-30) were uploaded through the GitHub web interface and are signed by GitHub's own key.** Signing with the author's key applies from the next commit.
**Last updated**: 2026-11-18 (v1.2; 281 ledger rows; 224 counted; 44 T3 rows. 18 rows added to the proposal ledger, a column added to the indicator table in the conclusion, and additions to the text of Chapters 1, 6, 7 and 10. Previous update 2026-11-03: indicators 8 to 12 of the companion book's fourth edition added to the indicator table in the conclusion, and the classification of the 229 added rows of Chapter 9 added to Appendix B)

---

## What this runbook protects

The book declares five operating rules in its text (the preface "This book will be updated", Appendix A-6, Appendix B-4 and the conclusion "Where updates go"). **Every step exists to implement these five.**

1. **Count only rows whose wording the author opened and checked in the primary source.** Do not give tiers T1 or T2 on the strength of AI research tool output, press reports or secondary sources. Rows not checked stay in the ledger as T3 and are excluded from the counts.
2. **Keep the wording of each proposal as in the primary source.** If a research summary differs from the wording of the primary source, replace it with the wording of the text and record the replacement in the `issuer` column.
3. **Append only.** Never delete or rewrite a row. A merge is recorded by writing the destination in `merged_into`. A correction is appended, stating that it is a correction and its date.
4. **Updates happen in three places only**: the proposal ledger `data/proposals.csv`, Appendix B (the verification record) and the indicator table in the conclusion. When the prose itself is changed, put "（YYYY年M月D日追記／訂正）" ("(Added/Corrected on D Month YYYY)") immediately before the changed passage.
5. **Sign every commit; never put the private key in the repository.** Same as in the companion book's runbook.

If you are unsure in the middle of a procedure, go back to which of the five this operation protects.

---

## 0. Pre-work checks (every time)

```powershell
cd <the folder where the repository is cloned>
git remote -v
git fetch origin
git log --oneline HEAD..origin/main
git status
git config --get pull.rebase
Get-ChildItem -Recurse -File -Include *.asc,*.rev,*.gpg,*.key,*.pgp
```

- `git remote -v` shows `enterprise-security-in-the-ai-era.git`.
- The output of `git log --oneline HEAD..origin/main` is empty (if not, run `git pull --no-rebase --no-edit`).
- `git status` shows `nothing to commit, working tree clean`.
- `pull.rebase` is `false`.
- The last command prints nothing.

---

## 1. Adding a proposal

### 1-1. Reach the primary source

The author opens and reads, personally, a document on the issuer's own domain (HTML or PDF). AI research tool output, news articles, aggregator sites and other people's summaries are not evidence of having reached it.

If it cannot be reached, a row may be created, but its tier is T3, and the `issuer` column states 未開封 ("not opened") and the reason it could not be reached. T3 rows do not enter the counts in the text.

### 1-2. Record the content in a consistent form

Column definitions are in Appendix A-2. From the primary source, fill in the following.

| Column | Rule |
|---|---|
| `new_id` | The symbol of the issuer type (A to H) and a three-digit serial number. Never reuse an existing number |
| `type` | The issuer type (A government and public bodies / B standards bodies / C AI companies / D security companies / E insurance / F academia / G individual experts / H regulators). Defined in Chapter 4 |
| `proposal` | The wording of the primary source in quotation marks, verbatim. Add a Japanese translation or summary in brackets |
| `issuer` | Issuer, document title, date. Always leave a record of opening (date, full text or excerpt, who opened it). If the author opened it directly, write "（開封：YYYY-MM-DD 全文、著者確認）" ("Opened: YYYY-MM-DD full text, confirmed by the author"); if an AI research assistant opened it at the author's instruction, write the party and the result, as in "（開封：YYYY-MM-DD 全文、AI調査の補助（サブエージェント）がWebFetchで確認。文言一致）" ("Opened: YYYY-MM-DD full text, checked by the AI research assistant (sub-agent) with WebFetch. Wording matches"). Rows opened by the AI research assistant stay in the remaining work of Appendix A-7 until the author opens them directly |
| `tier` | T1 if the wording and the basis (source of the data, population, method) are in the same document. T2 if the wording is there but the basis is not. T3 if it could not be opened |
| `k` | The kind of proposal (K1 to K9). Write the primary classification first, then secondary ones after "/", "・" or ",". Defined in Chapter 6 |
| `evidence` | Whether there is a basis, and what it is. If none, write なし ("none") |
| `status` | Proposal only / institutionalised / effect measured, and so on. "Effect measured" (効果測定あり) only when a description measuring the effect is in the same document |
| `limits` | Limits or criticisms written by the issuer itself or by a third party. If none, write "—" |
| `route` | Correspondence to the intrusion routes of the Japanese ledger. If more than one, join with "・". For prescriptions in announcements that do not state the intrusion route, write 経路非開示への処方 ("prescription for undisclosed route") |
| `urls` | The URLs of the primary sources that were opened |

(Added November 15, 2026)<br>
**English ledger (from v1.1).** When adding a row, add a row with the same `new_id` at the same position in `data/proposals_en.csv` too, and enter the English translation in the ten columns `proposal`, `issuer`, `medium`, `target`, `industry`, `k`, `route`, `status`, `evidence` and `limits`. Copy the same values as in `proposals.csv` for the other columns. `proposals.csv` is canonical, and recounts are made from `proposals.csv`. English quotations from sources are kept as in the original; quotations from Japanese sources are translated and marked "(translated from Japanese)". Translations of the titles of Japanese documents in the `issuer` column are marked "(title translated)". URLs and numbers are the same as in `proposals.csv`. When you add a row to, change the tier of, or correct a row in `proposals.csv`, make the same change in `proposals_en.csv`.

### 1-3. Recount

```powershell
python scripts/count_proposals.py
```

Note the figures in the output (counted rows, effect measured, by K, issuer types of K5, by route).

### 1-4. Reflect in the text

Figures in the text are updated in the following places only.

- The "as of edition N" tables at the head of each chapter (Chapters 1, 4, 6 and so on)
- Add a column for the new edition to the indicator table in the conclusion (never rewrite existing columns)
- The Proposals badge, the Last Updated badge and the update history of the README, and the figures at the head of `llms.txt`

Where the prose mentions a figure, do not rewrite it; put "（YYYY年M月D日追記）" ("(Added on D Month YYYY)") immediately before and write the new value. The first edition's statement stays.

### 1-5. Commit and push

```powershell
git add data/proposals.csv data/proposals_en.csv docs/ README.md README_en.md llms.txt
git commit -S -m "Add proposals <new_id>..<new_id>: <issuer>"
git log --show-signature -1
git push origin main
```

Confirm that `Good signature` appears in `git log --show-signature -1` before pushing.

---

## 2. Changing a tier (a T3 row was opened, or a basis was found for T2)

Do not rewrite the row. Do the following.

1. Change the value of the `tier` column. Append to the end of the `issuer` column, for example, "（YYYY年M月D日 T3→T1：<the document opened and the wording confirmed>）" ("(D Month YYYY T3→T1: <document opened and wording confirmed>)"), giving the date, before and after, and the basis.
2. If the research summary differed from the wording of the primary source, replace the `proposal` column with the wording of the text and note the replacement in the `issuer` column (see the example of A-063 "bringing forward" in the first edition; Appendix A-3).
3. A change of tier changes the number of counted rows, so do 1-3 and 1-4.

The commit subject is `Upgrade tier A-087: T3→T1`.

Lowering T1 or T2 to T3 is not done as a rule. If the primary source disappears, append to the `issuer` column the date it became unreachable, and do not change the tier.

---

## 3. Correcting an existing row (an error was pointed out, or the issuer corrected it)

1. At the end of the `limits` column or the `issuer` column of the row, append `（YYYY年M月D日訂正）` ("(Corrected on D Month YYYY)") followed by what changed and how, the URL of the primary source that is the basis, and the name of the person who pointed it out (if they wish). Keep the original value.
2. Where the text mentions the original value, put `（YYYY年M月D日訂正）` immediately before it, break the line, and write the correction.
3. If the correction concerns the "state of a number" (confirmed / source unknown / denied by the issuer and so on), append with the date to the "history of confirmation" of the relevant row of Appendix B-1 and update the "state". Do not delete the row. If a number is newly denied, or a number could not be traced to a primary source, add a row to B-1.

The commit subject is `Correct row E-010: <content>`.

---

## 4. Updating Appendix B and the indicator table in the conclusion

- **Appendix B-1**: When the state of a number changes, append the date and the basis to the "history of confirmation". Choose the name of the state from the definitions of B-2. If a state is needed that is not defined, add a row to B-2.
- **Appendix B-5** (classification of the announcements in Chapter 9): When rows are added to the companion book's ledger, classify them by the same criteria (notified by an upper limit / narrowed by the records / could not state a number / can be read either way) and add them as a separate dated table. Do not change existing tables.
- **The indicator table in the conclusion**: Add a column for each edition. Of the sixteen indicators, those that can be counted mechanically from the ledger (1 to 4) use the output of `scripts/count_proposals.py`; those confirmed in the text (5, 6 and 14) and those counted from the companion book's ledger (8 to 12) have the date of confirmation written in the column heading. Indicator 13 (announcements that stated in the first report whether a figure was an "upper limit" or "confirmed") was not counted in the first edition; enter the value once it is counted.

---

## 5. Raising the edition

Raise the edition when the number of ledger rows changes greatly, when the criteria for the kind of proposal (K) or for the tier change, or when the wording of the proposals in Parts 3 and 4 changes.

- Update the update history of the README, the head of `llms.txt` and the "as of edition N" headings at the head of each chapter, and create the edition in GitHub Releases.
- Where figures of the first edition are mentioned, add "（YYYY年M月D日追記）" ("(Added on D Month YYYY)") before the addition and keep the first edition's statement.
- If you change a chapter's proposal (the bold sentence at the head of Chapters 7 to 12), write the reason with a date immediately after the conclusion section "Rebuilding the claim from verified facts alone". If you change the book's one-sentence claim (preface, conclusion), raise the edition and write the reason also in the update history of the README.

---

## 6. When something fails

Apply as they are Section 5 of `docs/UPDATE_RUNBOOK.md` of the companion book *The Japan Breach Registry 2026* and Appendices A to C of the runbook of *The AI Forecast Registry* (a mistake in a commit message, a mistake in content, a failed signature, a private key mixed in, a rejected push). The failures specific to this book are the following two, plus a third that happened in the first edition.

**Only the figures in the text were fixed, and the ledger was not (or the reverse).** Run `python scripts/count_proposals.py` and confirm that the output matches the "as of edition N" tables in the text and the indicator table in the conclusion before committing. If any place does not match, treat the ledger as correct and fix the text by addition.

**A row was given T1 or T2 without opening the primary source.** As soon as you notice, append 未開封 ("not opened") and the date to the `issuer` column of that row and return the tier to T3. Recount the figures in the text by the steps of 1-3 and 1-4. Open it and check it, then raise it again by the steps of Section 2.

**A tier was given without leaving a record of opening.** This happened for 121 rows in the first edition. As soon as you notice, open it again (the author or the AI research assistant) and append the result to the `issuer` column. If the wording can be confirmed by opening it, the tier is not changed. Rows where the wording cannot be found, or that cannot be opened, are listed in Appendix A-7, and the tier is decided after the author confirms them directly (response of 2026-10-30: Appendix A-3).

---

## Appendix: the record of collection and checking for the first edition

The ledger of the first edition integrates, in one ledger by the author, five research results collected by giving the same questions to AI research tools (Claude, ChatGPT, Perplexity) on two occasions, 18 October and 30 October 2026 (Appendix A-1). After integration there are 263 rows; 13 rows were merged because they were judged to be the same proposal as another row, and the remaining 250 rows are candidates for inclusion. Two research results from Gemini were excluded in full, because the author opened three of the 13 URLs of primary sources of Japanese experts that it reported and none existed (Appendix B-1 #6).

Of the 250 candidate rows, the rows whose primary-source URL the author opened and whose wording the author checked are T1 (81 rows) and T2 (130 rows), 211 rows in total. The 39 rows that could not be opened remain in the ledger as T3 and are not used in the text.

Four rows changed tier while the first edition was being written (Appendix A-3). E-002 and E-003: Coalition's article of 31 August 2026 was checked in full, T2→T1. A-063: the request of the Financial Services Agency of 9 October 2026 was checked in the original, T3→T1 (the wording of the original is "to respond as promptly as possible without waiting for the effective date"; the word "bringing forward" in the research result is not in the original and was replaced). H-004: the directions of India's CERT-In of 28 April 2022 were checked in the original PDF, T3→T1 (180-day log retention). With these four changes, the counted rows changed from 209 to 211.

The work the author had not been able to complete at the time of the first edition is the seven items of Appendix A-7.
