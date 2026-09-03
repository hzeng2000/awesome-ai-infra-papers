# Awesome AI Infra Papers

> A paper-first reading map for AI infrastructure, LLM systems, efficient inference, RAG, agents, and reliable LLM applications.

**Suggested repository name:** `awesome-ai-infra-papers`  
**Last collected:** 2026-09-03, Asia/Shanghai

**Latest sweep:** MLSys 2026, NSDI 2026, OSDI 2026, ISCA 2026, ICML 2026, ACL 2026, SIGCOMM 2026, KDD 2026, USENIX Security 2026, VLDB 2026, and arXiv updates published from 2026-07-29 through 2026-09-03.

**Primary language:** English titles + bilingual notes are welcome. Chinese comments are acceptable when they help readers quickly triage.

## What is this repository?

This repository is a curated, paper-oriented index for people working on AI infrastructure and LLM application systems. It focuses on work that helps us understand, build, optimize, evaluate, or secure modern AI systems.

The scope intentionally covers both low-level AI systems and application-level systems:

- LLM serving platforms, request scheduling, batching, disaggregated prefill/decode, resource management, distributed runtimes, and training systems.
- Tensor compilers, MLIR/IR, kernel generation, GPU/NPU optimization, hardware-aware model execution.
- Inference optimization methods, including attention/KV optimization, speculative decoding, quantization, compression, MoE inference, long-context inference, efficient reasoning, and on-device inference.
- RAG, GraphRAG, retrieval-augmented reasoning, knowledge-intensive systems, and RAG evaluation.
- LLM agents, multi-agent systems, agent memory, tool use, deep research agents, web/computer-use agents, and agent benchmarks.
- Evaluation, reliability, hallucination, safety, security, prompt-injection defense, and production-facing LLM system assessment.

The repository is **not** meant to be a model leaderboard, product directory, prompt collection, app template gallery, or generic AI tools list.

Boundary rule for the two inference-related files:

- Put a paper in `01` when the main contribution is a serving platform or runtime infrastructure that owns request, session, cache, worker, or cluster lifecycle: serving engine, runtime memory manager, request scheduler, admission control, goodput/SLO policy, multi-tenancy, serverless loading, disaggregated cluster runtime, training runtime, or serving benchmark.
- Put a paper in `03` when the main contribution is an inference optimization method that makes model execution cheaper inside a runtime: attention/KV method, speculative decoding, quantization, pruning, compression, MoE expert movement/routing, long-context architecture, or efficient reasoning.
- Example: vLLM/PagedAttention is primarily `01` because the paper's artifact is a deployable serving engine and runtime memory manager; SnapKV, KIVI, Medusa, AWQ, and MoE offloading/routing methods are primarily `03` because they are optimization techniques a serving engine can adopt.
- Cross-list only for canonical papers that are genuinely central to both views; otherwise choose one primary location.

## Repository structure

```text
.
├── README.md
├── COLLECTION.md
├── CONTRIBUTING.md
├── LICENSE
├── 01-awesome-llm-serving-platforms-and-runtime.md
├── 02-awesome-ai-compiler-kernels-hardware.md
├── 03-awesome-llm-inference-optimization-methods.md
├── 04-awesome-rag-knowledge-systems.md
├── 05-awesome-llm-agent-systems.md
├── 06-awesome-llm-evaluation-safety-reliability.md
└── scripts/
    ├── README.md
    └── check_links.py
```

Core files:

- [`README.md`](./README.md): repo purpose, scope, curation policy, ranking rules, and entry template.
- [`COLLECTION.md`](./COLLECTION.md): top-level category map and seed upstream repositories.
- [`CONTRIBUTING.md`](./CONTRIBUTING.md): contribution workflow and field-level entry rules.
- [`LICENSE`](./LICENSE): CC-BY-4.0 licensing note for curated text and documentation.
- [`scripts/check_links.py`](./scripts/check_links.py): local and HTTP Markdown link checker.

Topic files:

| File | Main scope | Example sub-directions |
|---|---|---|
| [`01-awesome-llm-serving-platforms-and-runtime.md`](./01-awesome-llm-serving-platforms-and-runtime.md) | LLM serving platforms and runtime infrastructure | serving engines, runtime memory managers, request scheduling, SLO/goodput, multi-tenancy, serverless loading, disaggregated clusters, training infra, serving benchmarks |
| [`02-awesome-ai-compiler-kernels-hardware.md`](./02-awesome-ai-compiler-kernels-hardware.md) | compiler, kernel, and hardware-aware optimization | tensor compiler, MLIR, auto-tuning, GPU/NPU kernels, LLM-driven kernel generation |
| [`03-awesome-llm-inference-optimization-methods.md`](./03-awesome-llm-inference-optimization-methods.md) | LLM inference optimization methods | attention/KV methods, speculative decoding, quantization, pruning, compression, MoE-specific optimization, long-context architectures, efficient reasoning |
| [`04-awesome-rag-knowledge-systems.md`](./04-awesome-rag-knowledge-systems.md) | RAG and knowledge-intensive systems | RAG survey, GraphRAG, retrieval, RAG-reasoning, RAG evaluation, domain RAG systems |
| [`05-awesome-llm-agent-systems.md`](./05-awesome-llm-agent-systems.md) | agent systems and application-level research | LLM agents, multi-agent systems, tool use, memory, web/computer agents, coding agents, deep research |
| [`06-awesome-llm-evaluation-safety-reliability.md`](./06-awesome-llm-evaluation-safety-reliability.md) | eval, safety, security, reliability | LLM eval, agent eval, hallucination, prompt injection, LLM security, safety benchmarks |

## Curation standards

### Include when at least one is true

1. The entry is a **paper, survey, benchmark, dataset, or artifact** related to AI infra / LLM systems / RAG / agents / evaluation / safety.
2. The paper has **open-source code**, a benchmark implementation, an artifact, reproducibility materials, or a system implementation.
3. The work is **published or accepted** by a conference, journal, workshop, or major archival venue, or is a high-signal arXiv preprint with strong adoption.
4. The entry is a **paper-centric awesome list** or survey repository that organizes research papers with links to paper/code.
5. The work is clearly useful for understanding production LLM systems, even if it is framed as research rather than a product.

### Prefer entries with

- Public code, artifact, benchmark, dataset, or evaluation harness.
- Peer-reviewed venue or high-quality survey.
- Clear taxonomy and reproducible experimental setup.
- Strong system relevance: latency, throughput, memory, cost, reliability, deployment, scheduling, hardware utilization, security, or evaluation.
- Evidence of community adoption: GitHub stars, forks, issues/PRs, citations, downstream usage, or inclusion in other trusted lists.
- Recent updates or active maintenance.

### Exclude by default

- Pure model zoo, checkpoint collection, leaderboard, or model ranking.
- Pure app/demo/template repositories without a paper, benchmark, or research framing.
- Pure engineering/product/tool directories with no paper-centric structure.
- Prompt collections, agent skill collections, MCP server/client catalogs, workflow galleries, or marketplace-style lists.
- Stale forks, duplicate mirrors, or repositories whose value is mostly SEO/aggregation without curation.
- Broad AI news/resources lists unless they have a strong research-paper section relevant to this repo.

Some excluded repositories may still be useful in practice. They belong in a separate `awesome-ai-infra-engineering` or `awesome-llm-apps-engineering` list, not in this paper-first repository.

## Ranking principles

Within each category, sort entries by practical research value rather than chronology alone.

Recommended priority signals:

1. **Open-source code / artifact availability**: code, benchmark, dataset, reproducibility package, Docker, scripts, or public implementation.
2. **Publication quality**: accepted by conferences/journals such as OSDI, SOSP, NSDI, SIGCOMM, EuroSys, ATC, ASPLOS, ISCA, HPCA, SC, MLSys, NeurIPS, ICML, ICLR, ACL, EMNLP, NAACL, KDD, SIGIR, WWW, VLDB, SIGMOD, TOIS, TMLR, ACM CSUR, etc.
3. **Impact signals**: GitHub stars, forks, citations, downstream usage, integration into known systems, or repeated appearance in surveys.
4. **Direct fit**: closer to AI infra / LLM systems / RAG / agents / eval / safety ranks higher than generic ML/NLP work.
5. **Reproducibility**: detailed benchmarks, ablations, workload traces, artifact evaluation, deterministic scripts, and clear hardware/software setup.
6. **Recency and maintenance**: recent papers, updated code, active issues/PRs, and maintained awesome lists rank higher.
7. **System insight**: papers with clear systems lessons, bottleneck analysis, failure modes, or design trade-offs rank higher than purely empirical reports.

A simple scoring rubric can be used when triaging:

```text
Recommendation =
  30% direct relevance
+ 20% open-source code/artifact
+ 15% publication/citation signal
+ 15% practical adoption/GitHub signal
+ 10% reproducibility/evaluation quality
+ 10% recency/maintenance
```

This is a guide, not a strict formula.

## Recommendation index

| Score | Meaning |
|---|---|
| ★★★★★ | Must-read / core infrastructure paper or source list |
| ★★★★☆ | Strongly recommended; useful for most readers in the area |
| ★★★☆☆ | Good supporting work or specialized subtopic |
| ★★☆☆☆ | Worth tracking, but niche, early, or missing artifacts |
| ★☆☆☆☆ | Candidate only; needs verification or stronger evidence |

## Entry template

Use this compact table format inside each sub-direction section. Topic files should be organized like paper-list repositories such as `Zefan-Cai/Awesome-LLM-KV-Cache`: concrete technical sub-directions first, then a short table for each sub-direction.

```markdown
## Sub-direction name

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2025-02 | MLSys 2025 | Paper title | [paper](https://...) | [code](https://github.com/owner/repo) ![](https://img.shields.io/github/stars/owner/repo.svg?style=social) | ★★★★★ | One-sentence reason why this matters. |
```

Field notes:

| Field | Meaning |
|---|---|
| `Date` | First public date or conference date. Use `YYYY-MM` when possible. |
| `Venue` | Conference/journal/workshop/arXiv. Use `arXiv` only when not peer-reviewed yet. |
| `Title` | Official paper title. |
| `Paper` | arXiv, OpenReview, ACL Anthology, ACM, USENIX, conference PDF, or project page. |
| `Code` | Official code/artifact/dataset preferred. For GitHub repositories, append a stars badge: `![](https://img.shields.io/github/stars/owner/repo.svg?style=social)`. Use `-` if unavailable or if only weak unofficial code exists. |
| `Rec` | Recommendation index from ★ to ★★★★★. |
| `Comment` | One short judgment: contribution, system lesson, limitation, or why it is included. |

## Source-list template

For upstream awesome/paper-list repositories, use this table format in `COLLECTION.md` or category headers.

```markdown
| Source repo | Scope | Priority | Notes |
|---|---|---|---|
| [owner/repo](https://github.com/owner/repo) | KV cache optimization | P0 | Best entry point for KV cache papers. |
```

## Maintenance checklist

When adding or updating entries:

- Verify the paper link and code link.
- Prefer official code over unofficial code.
- Add a GitHub stars badge after GitHub code links.
- Mark whether the paper is peer-reviewed, arXiv-only, or accepted but not yet published.
- Add a short comment explaining why the paper matters for systems/application infrastructure.
- Avoid adding a repo merely because it is popular; it must match the paper-first scope.
- Move pure tools, templates, app galleries, model lists, and prompt libraries to an appendix or a separate repository.
- Run the Markdown link checker before committing:

```bash
python3 scripts/check_links.py --local-only
python3 scripts/check_links.py
```

## Automation

Included:

- `scripts/check_links.py`: check local Markdown references and HTTP paper/code links.

Useful scripts to add later:

- `scripts/update_github_stars.py`: refresh stars for code repositories via GitHub API.
- `scripts/update_citations.py`: refresh citation counts via Semantic Scholar / OpenAlex.
- `scripts/sort_tables.py`: sort by recommendation, venue tier, citation count, stars, and date.

## License

Curated text and documentation are licensed under `CC-BY-4.0`. See [`LICENSE`](./LICENSE).

## Acknowledgements

This repository starts from existing paper-centric awesome lists in AI systems, LLM systems, efficient inference, RAG, agents, and evaluation/safety. See [`COLLECTION.md`](./COLLECTION.md) for the initial source map.
