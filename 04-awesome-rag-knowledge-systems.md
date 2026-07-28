# RAG & Knowledge-intensive Systems

<a id="top"></a>

## Contents

- [Foundational retrieval-augmented language models](#foundational-retrieval-augmented-language-models)
- [Retrieval control, correction, and adaptive RAG](#retrieval-control-correction-and-adaptive-rag)
- [GraphRAG and structured knowledge retrieval](#graphrag-and-structured-knowledge-retrieval)
- [Retrieval-augmented reasoning and agentic search](#retrieval-augmented-reasoning-and-agentic-search)
- [RAG surveys and taxonomies](#rag-surveys-and-taxonomies)
- [RAG evaluation, benchmarks, and datasets](#rag-evaluation-benchmarks-and-datasets)
- [Upstream source lists](#upstream-source-lists)

## Scope

Retrieval-augmented generation, GraphRAG, retrieval-augmented reasoning, knowledge-intensive benchmarks, and RAG evaluation. Tables are organized by concrete RAG sub-direction.

## Foundational retrieval-augmented language models

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-07 | ACL 2026 | UniversalRAG: Retrieval-Augmented Generation over Corpora of Diverse Modalities and Granularities | [paper](https://aclanthology.org/2026.acl-long.177/) | - | ★★★★☆ | Unifies retrieval over heterogeneous modalities and document granularities. |
| 2026-07 | ICML 2026 | Token-Free Hierarchical Indexing for RAG beyond LLM-based Summarization | [paper](https://icml.cc/virtual/2026/poster/63668) | - | ★★★★☆ | Builds hierarchical retrieval indexes without spending generation tokens on summaries. |
| 2026-05 | MLSys 2026 | LEANN: A Low-Storage Overhead Vector Index | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/e27ea0cd50b798ff8942caf9203f0992-Abstract-Conference.html) | - | ★★★★☆ | Reduces vector-index storage overhead for local and resource-constrained retrieval. |
| 2020-04 | EMNLP 2020 | Dense Passage Retrieval for Open-Domain Question Answering | [paper](https://arxiv.org/abs/2004.04906) | [code](https://github.com/facebookresearch/DPR) ![](https://img.shields.io/github/stars/facebookresearch/DPR.svg?style=social) | ★★★★☆ | Standard dense retriever baseline behind many RAG pipelines. |
| 2020-04 | SIGIR 2020 | ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT | [paper](https://arxiv.org/abs/2004.12832) | [code](https://github.com/stanford-futuredata/ColBERT) ![](https://img.shields.io/github/stars/stanford-futuredata/ColBERT.svg?style=social) | ★★★★☆ | Late-interaction retriever that remains important for high-quality RAG retrieval. |
| 2020-02 | ICML 2020 | REALM: Retrieval-Augmented Language Model Pre-Training | [paper](https://arxiv.org/abs/2002.08909) | [code](https://github.com/google-research/language/tree/master/language/realm) ![](https://img.shields.io/github/stars/google-research/language.svg?style=social) | ★★★★☆ | Early learned retrieval-augmented pretraining system. |
| 2020-05 | NeurIPS 2020 | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | [paper](https://arxiv.org/abs/2005.11401) | [code](https://github.com/huggingface/transformers) ![](https://img.shields.io/github/stars/huggingface/transformers.svg?style=social) | ★★★★★ | Canonical RAG formulation. |
| 2020-07 | EACL 2021 | Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering | [paper](https://arxiv.org/abs/2007.01282) | [code](https://github.com/facebookresearch/FiD) ![](https://img.shields.io/github/stars/facebookresearch/FiD.svg?style=social) | ★★★★☆ | Fusion-in-decoder baseline for retrieval-conditioned generation. |
| 2021-12 | NAACL 2022 | ColBERTv2: Efficient and Effective Retrieval via Lightweight Late Interaction | [paper](https://arxiv.org/abs/2112.01488) | [code](https://github.com/stanford-futuredata/ColBERT) ![](https://img.shields.io/github/stars/stanford-futuredata/ColBERT.svg?style=social) | ★★★★☆ | Compression and denoised supervision for scalable late-interaction retrieval. |
| 2021-12 | ICML 2022 | Improving Language Models by Retrieving from Trillions of Tokens | [paper](https://arxiv.org/abs/2112.04426) | - | ★★★★☆ | RETRO reference for retrieval at pretraining/inference scale. |
| 2021-12 | TMLR 2022 | Unsupervised Dense Information Retrieval with Contrastive Learning | [paper](https://arxiv.org/abs/2112.09118) | [code](https://github.com/facebookresearch/contriever) ![](https://img.shields.io/github/stars/facebookresearch/contriever.svg?style=social) | ★★★★☆ | Contriever baseline for unsupervised dense retrieval. |
| 2022-08 | ICML 2023 | Atlas: Few-shot Learning with Retrieval Augmented Language Models | [paper](https://arxiv.org/abs/2208.03299) | [code](https://github.com/facebookresearch/atlas) ![](https://img.shields.io/github/stars/facebookresearch/atlas.svg?style=social) | ★★★★☆ | Strong few-shot retrieval-augmented LM baseline. |
| 2022-12 | ACL 2023 | Precise Zero-Shot Dense Retrieval without Relevance Labels | [paper](https://arxiv.org/abs/2212.10496) | [code](https://github.com/texttron/hyde) ![](https://img.shields.io/github/stars/texttron/hyde.svg?style=social) | ★★★★☆ | HyDE query-generation approach for zero-shot retrieval. |

## Retrieval control, correction, and adaptive RAG

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-07 | ACL 2026 | SARA: Selective and Adaptive Retrieval-augmented Generation with Context Compression | [paper](https://aclanthology.org/2026.acl-long.661/) | - | ★★★★☆ | Jointly decides whether to retrieve and how aggressively to compress the returned context. |
| 2026-07 | ACL 2026 | R^3AG: Retriever Routing for Retrieval-Augmented Generation | [paper](https://aclanthology.org/2026.acl-long.939/) | - | ★★★★☆ | Routes each query among retrievers instead of relying on one fixed retrieval stack. |
| 2026-07 | ACL 2026 | RAG-on-a-Diet: A Reinforcement Learning-Based Dynamic Resource Optimization Framework for RAG | [paper](https://aclanthology.org/2026.acl-long.1562/) | - | ★★★★☆ | Learns dynamic retrieval and context budgets under quality-cost constraints. |
| 2026-07 | ICML 2026 | Retriever Portfolios: A Principled Approach to Adaptive RAG | [paper](https://icml.cc/virtual/2026/poster/64403) | [code](https://github.com/mstou/retriever-portfolios) ![](https://img.shields.io/github/stars/mstou/retriever-portfolios.svg?style=social) | ★★★★☆ | Selects from a portfolio of retrievers based on query-dependent utility. |
| 2026-07 | ICML 2026 | Less Is More: Elevating RAG via Performance-Driven Context Compression | [paper](https://icml.cc/virtual/2026/poster/65862) | [code](https://github.com/ziqiangcui/CORE-RAG-ICML26) ![](https://img.shields.io/github/stars/ziqiangcui/CORE-RAG-ICML26.svg?style=social) | ★★★★☆ | Tunes context compression against downstream answer quality rather than proxy salience. |
| 2026-07 | ICML 2026 | Predictive Prefetching for Retrieval-Augmented Generation | [paper](https://icml.cc/virtual/2026/poster/66231) | - | ★★★☆☆ | Predicts future retrieval needs to overlap retrieval with generation. |
| 2026-05 | MLSys 2026 | TeleRAG: Efficient Retrieval-Augmented Generation Inference with Lookahead Retrieval | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/7fd522b89ac21009b7bbe7560a9a5add-Abstract-Conference.html) | - | ★★★★☆ | Uses lookahead queries to hide retrieval latency behind generation. |
| 2026-07 | ACL 2026 | SpecCache: Speculative KV Cache Reuse for Efficient RAG Serving | [paper](https://aclanthology.org/2026.acl-long.859/) | - | ★★★★☆ | Speculatively reuses retrieved-context KV state across related RAG requests. |
| 2023-05 | arXiv | Active Retrieval Augmented Generation | [paper](https://arxiv.org/abs/2305.06983) | - | ★★★☆☆ | FLARE-style generation-time retrieval triggering. |
| 2023-01 | arXiv | RePlug: Retrieval-Augmented Black-Box Language Models | [paper](https://arxiv.org/abs/2301.12652) | - | ★★★☆☆ | Useful black-box retrieval augmentation baseline. |
| 2023-10 | ICLR 2024 | Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection | [paper](https://arxiv.org/abs/2310.11511) | [code](https://github.com/AkariAsai/self-rag) ![](https://img.shields.io/github/stars/AkariAsai/self-rag.svg?style=social) | ★★★★★ | Retrieval control plus critique tokens for adaptive RAG. |
| 2024-01 | arXiv | Corrective Retrieval Augmented Generation | [paper](https://arxiv.org/abs/2401.15884) | - | ★★★★☆ | Adds correction when retrieved evidence is insufficient or misleading. |
| 2024-03 | arXiv | DRAGIN: Dynamic Retrieval Augmented Generation based on the Information Needs of Large Language Models | [paper](https://arxiv.org/abs/2403.10081) | [code](https://github.com/oneal2000/DRAGIN) ![](https://img.shields.io/github/stars/oneal2000/DRAGIN.svg?style=social) | ★★★★☆ | Decides when and what to retrieve based on generation-time information needs. |
| 2024-03 | arXiv | RAFT: Adapting Language Model to Domain Specific RAG | [paper](https://arxiv.org/abs/2403.10131) | [code](https://github.com/ShishirPatil/gorilla/tree/main/raft) ![](https://img.shields.io/github/stars/ShishirPatil/gorilla.svg?style=social) | ★★★★☆ | Retrieval-augmented fine-tuning recipe for in-domain open-book QA. |
| 2024-03 | NAACL 2024 | Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity | [paper](https://arxiv.org/abs/2403.14403) | [code](https://github.com/starsuzi/Adaptive-RAG) ![](https://img.shields.io/github/stars/starsuzi/Adaptive-RAG.svg?style=social) | ★★★★☆ | Routes between no retrieval, single-step retrieval, and iterative retrieval by query complexity. |
| 2024-06 | arXiv | LongRAG: Enhancing Retrieval-Augmented Generation with Long-context LLMs | [paper](https://arxiv.org/abs/2406.15319) | [code](https://github.com/TIGER-AI-Lab/LongRAG) ![](https://img.shields.io/github/stars/TIGER-AI-Lab/LongRAG.svg?style=social) | ★★★★☆ | Uses long retrieval units and long-context readers to rebalance retriever/reader cost. |
| 2024-07 | NeurIPS 2024 | RankRAG: Unifying Context Ranking with Retrieval-Augmented Generation in LLMs | [paper](https://arxiv.org/abs/2407.02485) | - | ★★★★☆ | Tunes a single LLM for both context ranking and answer generation. |
| 2024-08 | arXiv | RAG Foundry: A Framework for Enhancing LLMs for Retrieval Augmented Generation | [paper](https://arxiv.org/abs/2408.02545) | [code](https://github.com/IntelLabs/RAGFoundry) ![](https://img.shields.io/github/stars/IntelLabs/RAGFoundry.svg?style=social) | ★★★☆☆ | Useful engineering/research framework for RAG tuning and evaluation. |
| 2025-01 | arXiv | CoRAG: Chain-of-Retrieval Augmented Generation | [paper](https://arxiv.org/abs/2501.14342) | - | ★★★★☆ | Trains models to iteratively retrieve and reason before answering. |
| 2025-03 | arXiv | RAG-RL: Advancing Retrieval-Augmented Generation via RL and Curriculum Learning | [paper](https://arxiv.org/abs/2503.12759) | - | ★★★☆☆ | Uses RL and curriculum learning to improve retrieval and evidence use. |
| 2025-04 | arXiv | CDF-RAG: Causal Dynamic Feedback for Adaptive Retrieval-Augmented Generation | [paper](https://arxiv.org/abs/2504.12560) | [code](https://github.com/elakhatibi/CDF-RAG) ![](https://img.shields.io/github/stars/elakhatibi/CDF-RAG.svg?style=social) | ★★★☆☆ | Adaptive retrieval with causal dynamic feedback during generation. |
| 2026-02 | ICML 2026 | RAG without Forgetting: Continual Query-Infused Key Memory | [paper](https://arxiv.org/abs/2602.05152) | - | ★★★★☆ | Converts transient query expansion gains into persistent retrieval-index memory. |

## GraphRAG and structured knowledge retrieval

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2024-04 | arXiv | From Local to Global: A Graph RAG Approach to Query-Focused Summarization | [paper](https://arxiv.org/abs/2404.16130) | [code](https://github.com/microsoft/graphrag) ![](https://img.shields.io/github/stars/microsoft/graphrag.svg?style=social) | ★★★★★ | Key GraphRAG reference for graph community summaries and global queries. |
| 2024-05 | arXiv | HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models | [paper](https://arxiv.org/abs/2405.14831) | [code](https://github.com/OSU-NLP-Group/HippoRAG) ![](https://img.shields.io/github/stars/OSU-NLP-Group/HippoRAG.svg?style=social) | ★★★★☆ | Graph-structured long-term memory for retrieval-augmented reasoning. |
| 2024-05 | arXiv | G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering | [paper](https://arxiv.org/abs/2402.07630) | [code](https://github.com/XiaoxinHe/G-Retriever) ![](https://img.shields.io/github/stars/XiaoxinHe/G-Retriever.svg?style=social) | ★★★☆☆ | RAG over graph-structured inputs and graph QA. |
| 2024-09 | arXiv | KAG: Boosting LLMs in Professional Domains via Knowledge Augmented Generation | [paper](https://arxiv.org/abs/2409.13731) | [code](https://github.com/OpenSPG/KAG) ![](https://img.shields.io/github/stars/OpenSPG/KAG.svg?style=social) | ★★★★☆ | Hybrid KG/vector professional-domain RAG framework with logical reasoning components. |
| 2024-10 | arXiv | LightRAG: Simple and Fast Retrieval-Augmented Generation | [paper](https://arxiv.org/abs/2410.05779) | [code](https://github.com/HKUDS/LightRAG) ![](https://img.shields.io/github/stars/HKUDS/LightRAG.svg?style=social) | ★★★★☆ | Lightweight graph-enhanced RAG system with fast indexing/querying. |
| 2025-03 | arXiv | HiRAG: Retrieval-Augmented Generation with Hierarchical Knowledge | [paper](https://arxiv.org/abs/2503.10150) | [code](https://github.com/hhy-huang/HiRAG) ![](https://img.shields.io/github/stars/hhy-huang/HiRAG.svg?style=social) | ★★★☆☆ | Recent hierarchical-knowledge GraphRAG direction. |
| 2025-07 | ICLR 2026 | Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning | [paper](https://openreview.net/forum?id=PkwJjGJ7aN) | - | ★★★★☆ | Connects GraphRAG retrieval actions with RL-style agentic reasoning. |
| 2026-01 | arXiv | ProGraph-R1: Progress-aware Reinforcement Learning for Graph Retrieval Augmented Generation | [paper](https://arxiv.org/abs/2601.17755) | - | ★★★☆☆ | Recent progress-aware RL formulation for multi-step graph retrieval. |
| 2026-01 | ICLR 2026 | When to use Graphs in RAG: A Comprehensive Analysis for Graph Retrieval-Augmented Generation | [paper](https://openreview.net/forum?id=i9q9xDMjG7) | - | ★★★★☆ | ICLR 2026 analysis of where GraphRAG helps or hurts relative to vector RAG. |
| 2026-01 | ICLR 2026 | LinearRAG: Linear Graph Retrieval Augmented Generation on Large-scale Corpora | [paper](https://openreview.net/forum?id=mCtfkypdm6) | - | ★★★★☆ | Efficient GraphRAG framework for large-corpus graph construction and passage retrieval. |
| 2026-01 | ICLR 2026 | Youtu-GraphRAG: Vertically Unified Agents for Graph Retrieval-Augmented Complex Reasoning | [paper](https://openreview.net/forum?id=yCtgZ2G39E) | - | ★★★☆☆ | Agentic GraphRAG pipeline for complex multi-hop reasoning over structured evidence. |
| 2026-04 | ICLR 2026 | Topology of Reasoning: Retrieved Cell Complex-Augmented Generation for Textual Graph Question Answering | [paper](https://iclr.cc/virtual/2026/poster/10009292) | - | ★★★☆☆ | Topology-enhanced RAG over textual graphs with higher-order relational structure. |

## Retrieval-augmented reasoning and agentic search

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-07 | ACL 2026 | SPARKLE: A Structured and Plug-and-play Agentic Retrieval Policy for Adaptive RAG Models | [paper](https://aclanthology.org/2026.acl-long.1793/) | - | ★★★★☆ | Adds a structured retrieval policy that can be attached to existing RAG models. |
| 2026-07 | ACL 2026 | The Retrieval Bottleneck: Scaling Laws for Reinforcement Learning in RAG | [paper](https://aclanthology.org/2026.acl-long.1478/) | - | ★★★★☆ | Quantifies how retrieval quality limits returns from additional RL compute. |
| 2022-12 | ACL 2023 | Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions | [paper](https://arxiv.org/abs/2212.10509) | [code](https://github.com/StonyBrookNLP/ircot) ![](https://img.shields.io/github/stars/StonyBrookNLP/ircot.svg?style=social) | ★★★★☆ | IRCoT baseline for retrieval interleaved with reasoning. |
| 2024-02 | arXiv | Adaptive Retrieval-Augmented Generation for Conversational Systems | [paper](https://arxiv.org/abs/2402.19473) | - | ★★★☆☆ | Survey-style reference for RAG in generated content and applications. |
| 2025-01 | arXiv | Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG | [paper](https://arxiv.org/abs/2501.09136) | - | ★★★☆☆ | Useful taxonomy for RAG systems that plan, retrieve, and revise. |
| 2025-03 | arXiv | R1-Searcher: Incentivizing the Search Capability in LLMs via Reinforcement Learning | [paper](https://arxiv.org/abs/2503.05592) | [code](https://github.com/RUCAIBox/R1-Searcher) ![](https://img.shields.io/github/stars/RUCAIBox/R1-Searcher.svg?style=social) | ★★★☆☆ | Trains reasoning models to invoke search through outcome-based RL. |
| 2025-03 | arXiv | Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning | [paper](https://arxiv.org/abs/2503.09516) | [code](https://github.com/PeterGriffinJin/Search-R1) ![](https://img.shields.io/github/stars/PeterGriffinJin/Search-R1.svg?style=social) | ★★★★☆ | Multi-turn search interactions integrated into RL reasoning trajectories. |
| 2025-04 | arXiv | DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments | [paper](https://arxiv.org/abs/2504.03160) | - | ★★★☆☆ | RL-oriented deep research agent with real web search interactions. |
| 2025-05 | NeurIPS 2025 | WebDancer: Towards Autonomous Information Seeking Agency | [paper](https://arxiv.org/abs/2505.22648) | [code](https://github.com/Alibaba-NLP/WebAgent) ![](https://img.shields.io/github/stars/Alibaba-NLP/WebAgent.svg?style=social) | ★★★★☆ | End-to-end agentic information-seeking pipeline with SFT and RL stages. |
| 2025-07 | EMNLP 2025 | Search-o1: Agentic Search-Enhanced Large Reasoning Models | [paper](https://arxiv.org/abs/2501.05366) | - | ★★★☆☆ | Representative search-augmented reasoning-model work. |

## RAG surveys and taxonomies

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2023-12 | arXiv | Retrieval-Augmented Generation for Large Language Models: A Survey | [paper](https://arxiv.org/abs/2312.10997) | - | ★★★★☆ | Broad RAG survey and taxonomy. |
| 2024-04 | arXiv | A Survey on Retrieval-Augmented Text Generation for Large Language Models | [paper](https://arxiv.org/abs/2404.10981) | - | ★★★☆☆ | Text-generation-focused RAG survey. |
| 2025-03 | arXiv | A Survey on Knowledge-Oriented Retrieval-Augmented Generation | [paper](https://arxiv.org/abs/2503.10677) | - | ★★★☆☆ | Recent knowledge-oriented RAG survey. |
| 2025-04 | arXiv | A Survey of Multimodal Retrieval-Augmented Generation | [paper](https://arxiv.org/abs/2504.08748) | - | ★★★☆☆ | Recent multimodal RAG taxonomy. |
| 2025-07 | arXiv | Towards Agentic RAG with Deep Reasoning: A Survey of RAG-Reasoning Systems in LLMs | [paper](https://arxiv.org/abs/2507.09477) | - | ★★★☆☆ | Recent survey connecting RAG, reasoning, and agents. |

## RAG evaluation, benchmarks, and datasets

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-07 | ACL 2026 | CiteGuard: Faithful Citation Attribution for LLMs via Retrieval-Augmented Validation | [paper](https://aclanthology.org/2026.acl-long.282/) | - | ★★★★☆ | Validates generated citations against retrieved evidence and flags unsupported attribution. |
| 2026-07 | ACL 2026 | ViDoRe V3: A Comprehensive Evaluation of Retrieval Augmented Generation in Complex Real-World Scenarios | [paper](https://aclanthology.org/2026.acl-long.755/) | - | ★★★★☆ | Broadens visual-document RAG evaluation to complex realistic retrieval and generation tasks. |
| 2020-09 | NAACL 2021 | KILT: a Benchmark for Knowledge Intensive Language Tasks | [paper](https://arxiv.org/abs/2009.02252) | [code](https://github.com/facebookresearch/KILT) ![](https://img.shields.io/github/stars/facebookresearch/KILT.svg?style=social) | ★★★★☆ | Standard benchmark suite for grounded knowledge-intensive tasks. |
| 2021-04 | NeurIPS 2021 | BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models | [paper](https://arxiv.org/abs/2104.08663) | [code](https://github.com/beir-cellar/beir) ![](https://img.shields.io/github/stars/beir-cellar/beir.svg?style=social) | ★★★★☆ | Retrieval benchmark used heavily for RAG retriever evaluation. |
| 2023-09 | EACL 2024 | RAGAS: Automated Evaluation of Retrieval Augmented Generation | [paper](https://arxiv.org/abs/2309.15217) | [code](https://github.com/explodinggradients/ragas) ![](https://img.shields.io/github/stars/explodinggradients/ragas.svg?style=social) | ★★★★☆ | Popular RAG evaluation metrics and tooling. |
| 2023-11 | NAACL 2024 | ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems | [paper](https://arxiv.org/abs/2311.09476) | [code](https://github.com/stanford-futuredata/ARES) ![](https://img.shields.io/github/stars/stanford-futuredata/ARES.svg?style=social) | ★★★★☆ | Uses lightweight judges plus prediction-powered inference for RAG evaluation. |
| 2024-01 | arXiv | RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models | [paper](https://arxiv.org/abs/2401.00396) | [code](https://github.com/ParticleMedia/RAGTruth) ![](https://img.shields.io/github/stars/ParticleMedia/RAGTruth.svg?style=social) | ★★★★☆ | RAG hallucination corpus with fine-grained annotations. |
| 2024-01 | arXiv | CRUD-RAG: A Comprehensive Chinese Benchmark for Retrieval-Augmented Generation of Large Language Models | [paper](https://arxiv.org/abs/2401.17043) | - | ★★★☆☆ | Chinese RAG benchmark built around create/read/update/delete knowledge operations. |
| 2025-01 | arXiv | MTRAG: A Multi-Turn Conversational Benchmark for Evaluating Retrieval-Augmented Generation Systems | [paper](https://arxiv.org/abs/2501.03468) | - | ★★★☆☆ | Multi-turn conversational RAG benchmark for context updates and answer grounding. |
| 2025-02 | arXiv | RAG vs. GraphRAG: A Systematic Evaluation and Key Insights | [paper](https://arxiv.org/abs/2502.11371) | - | ★★★☆☆ | Empirical comparison of vector RAG and GraphRAG across common tasks. |
| 2025-02 | arXiv | Benchmarking Retrieval-Augmented Generation in Multi-Modal Contexts | [paper](https://arxiv.org/abs/2502.17297) | - | ★★★☆☆ | M2RAG benchmark for multimodal retrieved evidence. |
| 2024-07 | arXiv | RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems | [paper](https://arxiv.org/abs/2407.11005) | [code](https://github.com/rungalileo/ragbench) ![](https://img.shields.io/github/stars/rungalileo/ragbench.svg?style=social) | ★★★☆☆ | Large-scale explainable RAG benchmark dataset. |
| 2024-08 | NeurIPS 2024 | RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation | [paper](https://arxiv.org/abs/2408.08067) | [code](https://github.com/amazon-science/RAGChecker) ![](https://img.shields.io/github/stars/amazon-science/RAGChecker.svg?style=social) | ★★★★☆ | Fine-grained diagnostic metrics for retriever and generator components. |
| 2025-01 | ACL 2025 | SafeRAG: Benchmarking Security in Retrieval-Augmented Generation of Large Language Model | [paper](https://arxiv.org/abs/2501.18636) | - | ★★★☆☆ | Security benchmark for RAG data-injection risk. |
| 2025-05 | arXiv | mmRAG: A Modular Benchmark for Retrieval-Augmented Generation over Text, Tables, and Knowledge Graphs | [paper](https://arxiv.org/abs/2505.11180) | - | ★★★☆☆ | Modular RAG benchmark spanning text, tables, and KGs. |
| 2025-05 | arXiv | XRAG: Cross-lingual Retrieval-Augmented Generation | [paper](https://arxiv.org/abs/2505.10089) | - | ★★★☆☆ | Benchmark for cross-lingual generation when retrieved evidence is in another language. |
| 2025-06 | arXiv | GraphRAG-Bench: Challenging Domain-Specific Reasoning for Evaluating Graph Retrieval-Augmented Generation | [paper](https://arxiv.org/abs/2506.02404) | - | ★★★☆☆ | Domain-specific GraphRAG benchmark covering graph construction, retrieval, and reasoning. |
| 2025-06 | arXiv | T2-RAGBench: Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation | [paper](https://arxiv.org/abs/2506.12071) | - | ★★★☆☆ | Financial text-and-table RAG benchmark with large-scale QA triples. |
| 2025-10 | arXiv | Towards Global Retrieval Augmented Generation: A Benchmark for Corpus-Level Reasoning | [paper](https://arxiv.org/abs/2510.26205) | - | ★★★☆☆ | GlobalQA benchmark for counting, extrema, sorting, and top-k reasoning over corpora. |
| 2026-07 | ICML 2026 | Ranking Free RAG: Replacing Re-ranking with Selection in RAG for Sensitive Domains | [paper](https://icml.cc/virtual/2026/poster/64383) | - | ★★★☆☆ | Replaces reranking with evidence selection in sensitive-domain RAG. |

## Upstream source lists

[Back to top](#top)

| Source repo | Scope | Priority | Notes |
|---|---|---|---|
| [jxzhangjhu/Awesome-LLM-RAG](https://github.com/jxzhangjhu/Awesome-LLM-RAG) | RAG papers | P0 | Core RAG paper source. |
| [hymie122/RAG-Survey](https://github.com/hymie122/RAG-Survey) | RAG survey | P0 | Strong survey-backed structure. |
| [YHPeter/Awesome-RAG-Evaluation](https://github.com/YHPeter/Awesome-RAG-Evaluation) | RAG evaluation | P0 | Cross-list under evaluation. |
| [DavidZWZ/Awesome-RAG-Reasoning](https://github.com/DavidZWZ/Awesome-RAG-Reasoning) | RAG + reasoning | P0 | Important for agentic RAG and deep search. |
| [DEEP-PolyU/Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG) | GraphRAG | P0 | Core GraphRAG source. |
| [gomate-community/awesome-papers-for-rag](https://github.com/gomate-community/awesome-papers-for-rag) | RAG papers | P1 | Good component-level taxonomy. |
| [GraphRAG-Bench/GraphRAG-Benchmark](https://github.com/GraphRAG-Bench/GraphRAG-Benchmark) | GraphRAG benchmark | P1 | Benchmark artifact rather than an awesome list. |
