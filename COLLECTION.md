# Collection Map

**Suggested repository name:** `awesome-ai-infra-papers`  
**Last collected:** 2026-07-28, Asia/Shanghai

**Latest sweep:** MLSys 2026, NSDI 2026, OSDI 2026, ISCA 2026, ICML 2026, ACL 2026, and arXiv updates published after 2026-05-16.

**Collection principle:** paper-first, infra-oriented, no pure model leaderboard, no pure app/tool directory.

This file is the root-level map of the repository. It defines the top-level taxonomy and seed upstream repositories to mine when building topic-level paper tables.

## Top-level taxonomy

| ID | Category | Topic file | Main sub-directions |
|---|---|---|---|
| 01 | LLM Serving Platforms & Runtime Infrastructure | `01-awesome-llm-serving-platforms-and-runtime.md` | serving engines, runtime memory managers, request scheduling, SLO/goodput, multi-tenancy, serverless loading, disaggregated clusters, training systems, serving benchmarks |
| 02 | Compiler, Kernels & Hardware-aware Optimization | `02-awesome-ai-compiler-kernels-hardware.md` | tensor compiler, MLIR/IR, auto-tuning, compiler ML, GPU/NPU kernel generation, hardware-aware model execution |
| 03 | LLM Inference Optimization Methods | `03-awesome-llm-inference-optimization-methods.md` | attention/KV methods, speculative decoding, quantization, pruning, compression, MoE-specific optimization, long-context architecture, efficient reasoning |
| 04 | RAG & Knowledge-intensive Systems | `04-awesome-rag-knowledge-systems.md` | RAG survey, GraphRAG, retrieval, RAG-reasoning, RAG evaluation, knowledge-intensive applications |
| 05 | Agents & Application-level Systems | `05-awesome-llm-agent-systems.md` | LLM agents, multi-agent systems, agent memory, tool use, web/computer-use agents, coding agents, deep research agents |
| 06 | Evaluation, Safety & Reliability | `06-awesome-llm-evaluation-safety-reliability.md` | LLM evaluation, agent benchmarks, RAG evaluation, hallucination, safety, prompt injection, LLM security, reliability |

## Category 01 — LLM Serving Platforms & Runtime Infrastructure

Use this category for papers and paper lists whose main contribution is a serving platform or runtime infrastructure layer that owns request, session, cache, worker, or cluster lifecycle: serving engines, runtime memory managers, request scheduling, admission control, SLO/goodput policy, multi-tenancy, serverless loading, disaggregated cluster runtime, training runtime, deployment runtime, or serving benchmarks.

Example: vLLM/PagedAttention is primary Category 01 because the paper's artifact is a deployable serving engine and runtime memory manager. If the main contribution is a specific inference optimization method such as KV compression, speculative decoding, quantization, pruning, or MoE expert movement/routing, place it in Category 03 even when the paper contains a prototype serving system.

| Source repo | Sub-direction | Why include | Priority | Notes |
|---|---|---|---|---|
| [xlite-dev/Awesome-LLM-Inference](https://github.com/xlite-dev/Awesome-LLM-Inference) | LLM/VLM inference | Curated LLM/VLM inference papers with code; covers FlashAttention, PagedAttention, quantization, parallelism, TensorRT-LLM, etc. | P0 | Core entry point for inference acceleration. |
| [AmadeusChan/Awesome-LLM-System-Papers](https://github.com/AmadeusChan/Awesome-LLM-System-Papers) | LLM systems | Maintained list of LLM system papers. | P0 | Good for LLM serving/system overview. |
| [AmberLJC/LLMSys-PaperList](https://github.com/AmberLJC/LLMSys-PaperList) | LLM systems | Curated academic papers, articles, tutorials, slides, and projects for LLM systems. | P0 | Broad LLMSys tracking list. |
| [InternLM/Awesome-LLM-Training-System](https://github.com/InternLM/Awesome-LLM-Training-System) | Training systems | Survey-style list of LLM training-system optimizations: infrastructure, parallelism, compute, memory, communication, fault tolerance. | P0 | Training infra counterpart to inference-serving lists. |
| [lambda7xx/awesome-AI-system](https://github.com/lambda7xx/awesome-AI-system) | AI systems paper-code | Paper-code list across serving, compiler, attention, RAG/ANNS, MoE, scheduling, training, evaluation, robustness. | P1 | Broad; needs filtering by category. |
| [HuaizhengZhang/AI-Infra-from-Zero-to-Hero](https://github.com/HuaizhengZhang/AI-Infra-from-Zero-to-Hero) | AI infra research/practice | System for ML / LLM / GenAI papers and industry practice. | P1 | Mixed research + practice; include paper entries only. |
| [zhixin612/awesome-papers-LMsys](https://github.com/zhixin612/awesome-papers-LMsys) | LLM systems tracking | Daily arXiv-oriented LLM systems paper tracking. | P1 | Useful for recency. |
| [Hsword/Awesome-Machine-Learning-System-Papers](https://github.com/Hsword/Awesome-Machine-Learning-System-Papers) | ML systems | Curated ML system papers in recent years. | P1 | Good broader MLSys background. |
| [Shenggan/awesome-distributed-ml](https://github.com/Shenggan/awesome-distributed-ml) | Distributed ML | Distributed training/inference papers and resources. | P2 | Older/broader; filter strongly. |
| [bharathgs/Awesome-Distributed-Deep-Learning](https://github.com/bharathgs/Awesome-Distributed-Deep-Learning) | Distributed DL | Distributed DL frameworks, papers, blogs, and books. | P2 | Mostly background; not LLM-specific. |
| [jeho-lee/Awesome-On-Device-AI-Systems](https://github.com/jeho-lee/Awesome-On-Device-AI-Systems) | On-device AI systems | Efficient on-device AI systems with papers, engines, and benchmarks. | P1 | Good edge/mobile systems bridge. |
| [iamseonghoon/Awesome-On-Device-AI-Inference](https://github.com/iamseonghoon/Awesome-On-Device-AI-Inference) | On-device inference | Academic work focused on efficient AI inference on mobile/edge devices. | P1 | Strong fit for resource-constrained inference. |
| [LumosJiang/Awesome-On-Device-LLMs](https://github.com/LumosJiang/Awesome-On-Device-LLMs) | On-device LLMs | Papers on on-device LLMs, model compression, and system optimization. | P1 | Narrow and paper-centric. |
| [jjxu217/Awesome-LLMs-on-device](https://github.com/jjxu217/Awesome-LLMs-on-device) | On-device LLM survey | Survey hub for LLMs designed for device deployment. | P2 | Use paper/survey sections only. |

## Category 02 — Compiler, Kernels & Hardware-aware Optimization

Use this category for compiler stacks, tensor programs, kernel optimization, hardware-aware code generation, and LLM-assisted systems programming.

| Source repo | Sub-direction | Why include | Priority | Notes |
|---|---|---|---|---|
| [merrymercy/awesome-tensor-compilers](https://github.com/merrymercy/awesome-tensor-compilers) | Tensor compilers | Compiler projects and papers for tensor computation and deep learning. | P0 | Core compiler list. |
| [0xxx/awesome-mlir](https://github.com/0xxx/awesome-mlir) | MLIR | Useful MLIR resources including research papers and AI/ML links. | P1 | Mixed resources; include paper/research entries only. |
| [zwang4/awesome-machine-learning-in-compilers](https://github.com/zwang4/awesome-machine-learning-in-compilers) | ML for compilers | Research papers, datasets, and tools for applying ML to compiler and program optimization. | P0 | Strong fit for compiler optimization. |
| [flagos-ai/awesome-LLM-driven-kernel-generation](https://github.com/flagos-ai/awesome-LLM-driven-kernel-generation) | LLM-driven kernel generation | Tracks papers on automated kernel generation and agentic kernel optimization. | P0 | Emerging, highly relevant for AI infra. |
| [ScalingIntelligence/KernelBench](https://github.com/ScalingIntelligence/KernelBench) | Kernel generation benchmark | Benchmark/environment for evaluating whether LLMs can generate correct and efficient GPU kernels. | P1 | Not an awesome list, but a key benchmark/paper artifact. |

## Category 03 — LLM Inference Optimization Methods

Use this category for method-level work that reduces latency, memory, bandwidth, energy, or serving cost during model execution. The organizing unit is the optimization method, not the request-serving platform.

For serving engines, runtime memory managers, request schedulers, resource managers, serverless systems, disaggregated clusters, and training runtimes, use Category 01.

| Source repo | Sub-direction | Why include | Priority | Notes |
|---|---|---|---|---|
| [horseee/Awesome-Efficient-LLM](https://github.com/horseee/Awesome-Efficient-LLM) | Efficient LLMs | Full-list hub for pruning, distillation, quantization, inference acceleration, MoE, architecture, KV cache, efficient training, reasoning. | P0 | Broadest efficient-LLM entry point. |
| [Zefan-Cai/Awesome-LLM-KV-Cache](https://github.com/Zefan-Cai/Awesome-LLM-KV-Cache) | KV cache | KV cache papers with code; compression, merge, budget allocation, quantization, low-rank, systems. | P0 | Model format/template inspiration. |
| [jjiantong/Awesome-KV-Cache-Optimization](https://github.com/jjiantong/Awesome-KV-Cache-Optimization) | System-aware KV optimization | Serving-time, KV-centric optimization methods organized by temporal/spatial/structural behavior. | P0 | Very aligned with LLM serving. |
| [October2001/Awesome-KV-Cache-Compression](https://github.com/October2001/Awesome-KV-Cache-Compression) | KV cache compression | KV compression/pruning projects and papers. | P1 | More specialized KV cache compression. |
| [TreeAI-Lab/awesome-kv-cache-management](https://github.com/treeai-lab/awesome-kv-cache-management) | KV cache management | Survey-style KV cache management papers with code links. | P1 | Good secondary KV source. |
| [hemingkx/SpeculativeDecodingPapers](https://github.com/hemingkx/SpeculativeDecodingPapers) | Speculative decoding | Regularly updated speculative decoding paper/blog list. | P0 | Core speculative decoding list. |
| [Geralt-Targaryen/Awesome-Speculative-Decoding](https://github.com/Geralt-Targaryen/Awesome-Speculative-Decoding) | Speculative decoding notes | Reading list organized by venues and dates. | P1 | Good for chronology and notes. |
| [hemingkx/Awesome-Efficient-Reasoning](https://github.com/hemingkx/Awesome-Efficient-Reasoning) | Efficient reasoning | Paper list for efficient reasoning. | P1 | Useful for test-time compute and reasoning efficiency. |
| [HuangOwen/Awesome-LLM-Compression](https://github.com/HuangOwen/Awesome-LLM-Compression) | LLM compression | Compression papers/tools: quantization, pruning, distillation, efficient prompting, KV cache compression. | P0 | Core compression entry. |
| [pprp/Awesome-LLM-Quantization](https://github.com/pprp/awesome-llm-quantization) | LLM quantization | LLM quantization paper list with GitHub links for many entries. | P0 | Strong quantization source. |
| [Efficient-ML/Awesome-Model-Quantization](https://github.com/Efficient-ML/Awesome-Model-Quantization) | Model quantization | Papers, documents, and code for model quantization. | P1 | Broader than LLMs. |
| [Zhen-Dong/Awesome-Quantization-Papers](https://github.com/Zhen-Dong/Awesome-Quantization-Papers) | Quantization papers | Comprehensive model quantization paper list across conferences/journals/arXiv. | P1 | Good historical coverage. |
| [tiingweii-shii/Awesome-Resource-Efficient-LLM-Papers](https://github.com/tiingweii-shii/Awesome-Resource-Efficient-LLM-Papers) | Resource-efficient LLMs | High-quality papers tied to a resource-efficient LLM survey. | P1 | Good survey-backed list. |
| [weigao266/Awesome-Efficient-Arch](https://github.com/weigao266/Awesome-Efficient-Arch) | Efficient architecture | Efficient architecture survey: linear attention, sparse attention, MoE, hybrid models, etc. | P1 | Architecture-level efficiency. |
| [NoakLiu/Awesome-Efficient-Foundation-Models-Design](https://github.com/NoakLiu/Awesome-Efficient-Foundation-Models-Design) | Efficient foundation models | Model-system co-design view for efficient foundation models. | P2 | Smaller but conceptually relevant. |
| [htqin/awesome-efficient-aigc](https://github.com/htqin/awesome-efficient-aigc) | Efficient AIGC | Efficient approaches for LLMs and diffusion models to reduce compute demand. | P1 | Good if diffusion efficiency is also in scope. |
| [MoE-Inf/awesome-moe-inference](https://github.com/MoE-Inf/awesome-moe-inference/) | MoE inference | Papers optimizing inference of MoE-based LLMs. | P0 | Direct fit for MoE serving. |
| [pprp/Awesome-Efficient-MoE](https://github.com/pprp/Awesome-Efficient-MoE) | Efficient MoE | Efficient MoE paper list, including pruning, quantization, decomposition, acceleration. | P1 | Complements MoE inference list. |
| [XueFuzhao/awesome-mixture-of-experts](https://github.com/XueFuzhao/awesome-mixture-of-experts) | MoE | Papers, code, open models, MoE systems, applications. | P1 | Broad MoE source; filter out model-only entries. |
| [codecaution/Awesome-Mixture-of-Experts-Papers](https://github.com/codecaution/Awesome-Mixture-of-Experts-Papers) | MoE papers | Curated recent MoE paper list. | P1 | Paper-first MoE coverage. |
| [Xnhyacinth/Awesome-LLM-Long-Context-Modeling](https://github.com/Xnhyacinth/Awesome-LLM-Long-Context-Modeling) | Long context | Papers/blogs on efficient transformers, KV cache, length extrapolation, long-term memory, RAG, benchmarks. | P1 | Good bridge to memory/RAG. |
| [zetian1025/awesome-long-context](https://github.com/zetian1025/awesome-long-context) | Long context | Efficient inference, sparse attention, efficient KV cache, retrieval, context compression. | P2 | Use as secondary long-context source. |

## Category 04 — RAG & Knowledge-intensive Systems

Use this category for RAG, retrieval, GraphRAG, knowledge-intensive reasoning, and RAG system evaluation.

| Source repo | Sub-direction | Why include | Priority | Notes |
|---|---|---|---|---|
| [jxzhangjhu/Awesome-LLM-RAG](https://github.com/jxzhangjhu/Awesome-LLM-RAG) | RAG papers | Records advanced papers on Retrieval-Augmented Generation in LLMs. | P0 | Core RAG paper source. |
| [hymie122/RAG-Survey](https://github.com/hymie122/RAG-Survey) | RAG survey | Collects and categorizes RAG papers according to a survey taxonomy. | P0 | Strong survey-backed structure. |
| [coree/awesome-rag](https://github.com/coree/awesome-rag) | RAG papers/resources | RAG list with paper sections, resources, tools, and other collections. | P1 | Include paper sections; avoid tool-only rows. |
| [YHPeter/Awesome-RAG-Evaluation](https://github.com/YHPeter/Awesome-RAG-Evaluation) | RAG evaluation | Official repository for RAG evaluation survey; focuses on benchmarks, datasets, and metrics. | P0 | Also cross-list under evaluation. |
| [DavidZWZ/Awesome-RAG-Reasoning](https://github.com/DavidZWZ/Awesome-RAG-Reasoning) | RAG + reasoning | Resources, papers, tools, and implementations bridging RAG and reasoning. | P0 | Important for agentic RAG/deep search. |
| [DEEP-PolyU/Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG) | GraphRAG | Surveys, papers, benchmarks, and open-source projects on graph-based RAG. | P0 | Core GraphRAG source. |
| [gomate-community/awesome-papers-for-rag](https://github.com/gomate-community/awesome-papers-for-rag) | RAG papers | Curated RAG paper list organized by RAG pipeline components. | P1 | Good component-level taxonomy. |
| [GraphRAG-Bench/GraphRAG-Benchmark](https://github.com/GraphRAG-Bench/GraphRAG-Benchmark) | GraphRAG benchmark | Benchmark project for evaluating GraphRAG models. | P1 | Not an awesome list, but strong evaluation artifact. |

## Category 05 — Agents & Application-level Systems

Use this category for research papers and paper-oriented lists about agent construction, tool use, multi-agent systems, memory, web/computer agents, coding agents, and deep research agents.

| Source repo | Sub-direction | Why include | Priority | Notes |
|---|---|---|---|---|
| [luo-junyu/Awesome-Agent-Papers](https://github.com/luo-junyu/awesome-agent-papers) | LLM agents | Comprehensive research paper collection on LLM agents: construction, collaboration, evolution, tools, security, benchmarks, applications. | P0 | Core agent paper list. |
| [hyp1231/awesome-llm-powered-agent](https://github.com/hyp1231/awesome-llm-powered-agent) | LLM-powered agents | Papers, repositories, and resources for LLM-powered agents. | P1 | Mixed; include paper rows and research artifacts. |
| [VoltAgent/awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers) | AI agent papers | Curated AI agent research papers, covering engineering, memory, evaluation, workflows, autonomous systems. | P1 | Recent/paper-first source. |
| [TeleAI-UAGI/Awesome-Agent-Memory](https://github.com/TeleAI-UAGI/Awesome-Agent-Memory) | Agent memory | Systems, benchmarks, and papers on memory mechanisms for LLMs/MLLMs. | P0 | Strong fit for long-context/RAG/agent memory. |
| [yyyujintang/Awesome-Agent-Memory-Papers](https://github.com/yyyujintang/Awesome-Agent-Memory-Papers) | Agent memory papers | Papers on memory for LLM/multimodal agents. | P1 | More paper-only memory source. |
| [YoungDubbyDu/LLM-Agent-Optimization](https://github.com/YoungDubbyDu/LLM-Agent-Optimization) | Agent optimization | Reading list for survey on optimization of LLM-based agents. | P0 | Direct fit for agent optimization. |
| [YoungDubbyDu/LLM-based-Multi-Agent-Systems](https://github.com/YoungDubbyDu/LLM-based-Multi-Agent-Systems) | Multi-agent systems | Paper summary for LLM-based multi-agent systems. | P1 | Good multi-agent-specific seed. |
| [zhangxjohn/LLM-Agent-Benchmark-List](https://github.com/zhangxjohn/LLM-Agent-Benchmark-List) | Agent benchmarks | Organizes benchmarks for LLM- and agent-powered evaluation. | P0 | Also cross-list under evaluation. |
| [DavidZWZ/Awesome-Deep-Research](https://github.com/DavidZWZ/Awesome-Deep-Research) | Deep research agents | Agentic deep research resources and papers. | P1 | Useful for search/reasoning/tool-use agents. |
| [ranpox/awesome-computer-use](https://github.com/ranpox/awesome-computer-use) | Computer-use agents | Papers/projects/videos/blogs for computer-use agents. | P2 | Mixed; include papers/benchmarks only. |
| [steel-dev/awesome-web-agents](https://github.com/steel-dev/awesome-web-agents) | Web agents | Resources for browsing/operating web agents. | P2 | Mixed; include research/benchmark entries only. |
| [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/awesome-code-llm) | Coding / software engineering | Curated language-modeling research for code and software engineering activities, plus datasets. | P1 | Use for coding-agent and SE-agent paper entries; exclude model leaderboard rows. |

## Category 06 — Evaluation, Safety & Reliability

Use this category for LLM/RAG/agent evaluation, reliability, hallucination, safety, prompt injection, adversarial robustness, and security.

| Source repo | Sub-direction | Why include | Priority | Notes |
|---|---|---|---|---|
| [alopatenko/LLMEvaluation](https://github.com/alopatenko/LLMEvaluation) | LLM evaluation | Comprehensive guide/compendium for LLM and LLM-application evaluation methods. | P1 | Good eval taxonomy; not all entries are papers. |
| [tjunlp-lab/Awesome-LLMs-Evaluation-Papers](https://github.com/tjunlp-lab/Awesome-LLMs-Evaluation-Papers) | LLM evaluation papers | Survey-linked LLM evaluation paper collection. | P0 | Paper-first evaluation source. |
| [YHPeter/Awesome-RAG-Evaluation](https://github.com/YHPeter/Awesome-RAG-Evaluation) | RAG evaluation | RAG benchmarks, datasets, metrics, and evaluation process. | P0 | Cross-listed from RAG category. |
| [zhangxjohn/LLM-Agent-Benchmark-List](https://github.com/zhangxjohn/LLM-Agent-Benchmark-List) | Agent benchmarks | Benchmark list for LLM- and agent-powered systems. | P0 | Cross-listed from agent category. |
| [ydyjya/Awesome-LLM-Safety](https://github.com/ydyjya/Awesome-LLM-Safety) | LLM safety | Safety-related papers, articles, and resources: privacy, attacks, defenses, hallucination, truthfulness, jailbreaks. | P0 | Strong safety paper source. |
| [corca-ai/awesome-llm-security](https://github.com/corca-ai/awesome-llm-security) | LLM security | Tools, documents, projects, and paper PDFs/summaries around LLM security. | P1 | Mixed; include papers and defensive system artifacts only. |
| [Joe-B-Security/awesome-prompt-injection](https://github.com/Joe-B-Security/awesome-prompt-injection) | Prompt injection | Prompt-injection resources and security references. | P2 | Use for paper/benchmark entries only. |

## Excluded from this paper-first version

These repositories can be useful, but they are not primary sources for this repo because they are mostly tools, app templates, skills, product directories, or engineering catalogs rather than paper-first lists.

| Repo / family | Reason for exclusion |
|---|---|
| `Shubhamsaboo/awesome-llm-apps`, `Arindam200/awesome-ai-apps` | Great runnable app examples, but mostly application templates rather than paper-first research. |
| `VoltAgent/awesome-agent-skills` | Skill catalog, not paper list. |
| `punkpeye/awesome-mcp-servers`, `punkpeye/awesome-mcp-clients` | MCP ecosystem catalogs, not paper-centric. |
| `kaushikb11/awesome-llm-agents`, `e2b-dev/awesome-ai-agents` | More framework/project oriented; use only if a paper section becomes central. |
| `tensorchord/Awesome-LLMOps`, `InftyAI/Awesome-LLMOps`, `jihoo-kim/awesome-production-llm` | Production/tool catalogs; useful for engineering appendix, not this paper-first core. |
| `kyrolabs/awesome-langchain`, `von-development/awesome-LangGraph`, `crewAIInc/awesome-crewai` | Framework ecosystem lists. |
| `dangkhoasdc/awesome-vector-database` | Vector DB/tool directory; include retrieval papers elsewhere instead. |
| `goabiaryan/awesome-gpu-engineering`, `coderonion/Awesome-CUDA-and-HPC`, `zinccat/Awesome-Triton-Kernels` | Excellent engineering resources, but not paper-first; could become an appendix. |
| `quome-cloud/awesome-coding-agents`, `ai-for-developers/awesome-ai-coding-tools`, `hesreallyhim/awesome-claude-code` | Coding-agent/tooling catalogs; not paper-first. |
| Generic model lists / model zoos / leaderboards | Out of scope unless tied to systems/evaluation papers. |

## Topic-file internal structure

Each topic file should use concrete technical sub-directions instead of code-status sections. Code availability belongs in the `Code` column, so do not split files into "with code" and "paper-only" sections.

```markdown
# Category Name

## Scope

What belongs here and what does not.

## Sub-directions

- Sub-direction A
- Sub-direction B
- Sub-direction C

## Sub-direction A

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|

## Sub-direction B

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|

## Upstream source lists

| Source repo | Scope | Priority | Notes |
|---|---|---|---|
```
