# Contributing

Thanks for helping improve this paper-first AI infrastructure map. The goal is not to collect every AI link; it is to keep a high-signal reading list for systems, serving, compilers, efficient inference, RAG, agents, evaluation, safety, and reliability.

## Scope

Add an entry when it is one of the following:

- A paper, survey, benchmark, dataset, or artifact related to AI infrastructure or LLM application systems.
- A paper-backed system implementation, benchmark harness, reproducibility package, or official code release.
- A paper-centric upstream list that helps readers find research papers with paper/code links.

Avoid adding:

- Pure model zoos, model leaderboards, prompt collections, app galleries, or product directories.
- Framework/tool lists without a clear paper or benchmark connection.
- Duplicate mirrors, stale forks, or SEO-style aggregations.

## Entry format

Use the table schema already present in each topic file:

```markdown
| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2025-02 | MLSys 2025 | Paper title | [paper](https://...) | [code](https://github.com/owner/repo) ![](https://img.shields.io/github/stars/owner/repo.svg?style=social) | ★★★★★ | One-sentence reason why this matters. |
```

Field expectations:

- `Date`: first public date or conference date, preferably `YYYY-MM`.
- `Venue`: accepted venue when known; otherwise use `arXiv`.
- `Title`: official paper title.
- `Paper`: stable paper page, arXiv, OpenReview, ACL Anthology, ACM, USENIX, or project page.
- `Code`: official code/artifact/dataset first. For GitHub repositories, append a stars badge: `![](https://img.shields.io/github/stars/owner/repo.svg?style=social)`. Use `-` if no reliable link is available.
- `Rec`: one of `★☆☆☆☆` through `★★★★★`.
- `Comment`: one concise reason this entry matters.

Do not add `Area`, `Tags`, or `Status` columns to category tables. The subsection heading should carry the area/tag information, and code availability is already visible in `Code`.

## Recommendation guide

Use the README scoring rubric as a guide. Prefer direct fit, official artifacts, venue quality, adoption, reproducibility, recency, and clear systems insight.

Recommendation labels should be conservative:

| Score | Use when |
|---|---|
| ★★★★★ | Core paper or source list most readers in the area should know. |
| ★★★★☆ | Strong and broadly useful. |
| ★★★☆☆ | Good supporting or specialized work. |
| ★★☆☆☆ | Worth tracking but narrow, early, or missing artifacts. |
| ★☆☆☆☆ | Candidate that needs stronger verification. |

## Workflow

1. Add the paper to the most specific topic file.
2. Put it under the most specific technical sub-direction.
3. For `01` vs `03`, use the paper's primary artifact as the tie-breaker: serving platforms and runtime infrastructure that own request/session/cache/worker lifecycle go in `01`; inference optimization methods such as KV compression, speculative decoding, quantization, pruning, or MoE expert movement/routing go in `03`.
4. Cross-list only when the paper is genuinely central to multiple topic areas.
5. Prefer updating an existing row over creating duplicates.
6. When proceedings become available, replace placeholder, author-page, or preprint metadata with the official conference page and venue instead of adding a second row.
7. For periodic sweeps, record the cutoff date and check both newly published proceedings and arXiv submissions after that cutoff.
8. Keep comments short and judgment-oriented.
9. Run the local link check before submitting:

```bash
python3 scripts/check_links.py --local-only
python3 scripts/check_links.py
```

If a source blocks automated HTTP checks but opens in a browser, mention that in the pull request.
