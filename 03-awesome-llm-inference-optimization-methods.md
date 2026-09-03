# LLM Inference Optimization Methods

<a id="top"></a>

## Contents

- [Attention kernels and decode-time attention](#attention-kernels-and-decode-time-attention)
- [KV cache eviction, retention, and compression](#kv-cache-eviction-retention-and-compression)
- [KV cache offloading, reuse, and memory hierarchy](#kv-cache-offloading-reuse-and-memory-hierarchy)
- [KV cache quantization](#kv-cache-quantization)
- [Speculative and parallel decoding](#speculative-and-parallel-decoding)
- [Weight and activation quantization](#weight-and-activation-quantization)
- [Pruning, sparsity, and compression](#pruning-sparsity-and-compression)
- [MoE foundations, runtimes, and workloads](#moe-foundations-runtimes-and-workloads)
- [MoE expert offloading, caching, and prefetching](#moe-expert-offloading-caching-and-prefetching)
- [MoE scheduling and expert-parallel execution](#moe-scheduling-and-expert-parallel-execution)
- [MoE routing, load balancing, and expert skipping](#moe-routing-load-balancing-and-expert-skipping)
- [MoE quantization, compression, and expert merging](#moe-quantization-compression-and-expert-merging)
- [Long-context and efficient architectures](#long-context-and-efficient-architectures)
- [Efficient reasoning and test-time compute](#efficient-reasoning-and-test-time-compute)
- [Upstream source lists](#upstream-source-lists)

## Scope

Method-level work that reduces latency, memory, bandwidth, energy, or serving cost during model execution. The organizing unit is the optimization method: attention, KV cache, decoding, quantization, pruning, compression, MoE routing/offloading, long-context architecture, or test-time compute.

Boundary with `01`: serving engines, runtime memory managers, request schedulers, admission-control policies, multi-tenant/serverless systems, cluster resource managers, disaggregated serving platforms, training runtimes, and serving benchmarks belong in `01-awesome-llm-serving-platforms-and-runtime.md`. This file keeps system papers only when the central idea is a specific inference optimization method.

## Attention kernels and decode-time attention

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-08 | ICML 2026 | Faster Than Flash: Exploiting Attention Sparsity for Efficient Long-Context Decoding | [paper](https://arxiv.org/abs/2609.00097) | - | ★★★★☆ | Co-designs sparse selection and kernels to reduce metadata and compute overhead during decode. |
| 2026-07 | ICML 2026 | Less Is More: Fast and Accurate Reasoning with Cross-Head Unified Sparse Attention | [paper](https://icml.cc/virtual/2026/poster/61079) | [code](https://github.com/DerrickYLJ/LessIsMore) ![](https://img.shields.io/github/stars/DerrickYLJ/LessIsMore.svg?style=social) | ★★★★☆ | Shares sparse-attention structure across heads to reduce reasoning-time attention cost. |
| 2026-05 | MLSys 2026 | MAC-Attention: a Match--Amend--Complete scheme for fast and accurate attention computation | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/7398289396de403d7d0505ed791e704a-Abstract-Conference.html) | - | ★★★★☆ | Combines approximate matching with targeted correction to avoid unnecessary attention work. |
| 2026-05 | MLSys 2026 | BLASST: Dynamic BLocked Attention Sparsity via Softmax Thresholding | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/c6ee784cbe46d854843e4c883a3321ef-Abstract-Conference.html) | - | ★★★★☆ | Selects block sparsity online from softmax behavior instead of a fixed pattern. |
| 2026-05 | MLSys 2026 | IntAttention: A Fully Integer Attention Pipeline for Efficient Edge Inference | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/ea5ffdf7da91256ecd2770f9fd2dade9-Abstract-Conference.html) | [code](https://github.com/WanliZhong/IntAttention) ![](https://img.shields.io/github/stars/WanliZhong/IntAttention.svg?style=social) | ★★★★☆ | Implements the complete attention path with integer arithmetic for edge accelerators. |
| 2019-11 | arXiv | Fast Transformer Decoding: One Write-Head is All You Need | [paper](https://arxiv.org/abs/1911.02150) | - | ★★★★☆ | Multi-query attention reference for reducing KV cache bandwidth. |
| 2023-05 | arXiv | GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints | [paper](https://arxiv.org/abs/2305.13245) | - | ★★★★☆ | Practical middle point between MHA quality and MQA serving efficiency. |
| 2022-05 | NeurIPS 2022 | FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness | [paper](https://arxiv.org/abs/2205.14135) | [code](https://github.com/Dao-AILab/flash-attention) ![](https://img.shields.io/github/stars/Dao-AILab/flash-attention.svg?style=social) | ★★★★★ | Core IO-aware attention kernel. |
| 2023-07 | ICLR 2024 | FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning | [paper](https://arxiv.org/abs/2307.08691) | [code](https://github.com/Dao-AILab/flash-attention) ![](https://img.shields.io/github/stars/Dao-AILab/flash-attention.svg?style=social) | ★★★★★ | Production-relevant attention parallelism improvements. |
| 2024-07 | arXiv | FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision | [paper](https://arxiv.org/abs/2407.08608) | [code](https://github.com/Dao-AILab/flash-attention) ![](https://img.shields.io/github/stars/Dao-AILab/flash-attention.svg?style=social) | ★★★★★ | Hopper-oriented attention kernel with asynchrony and FP8 support. |
| 2024-10 | arXiv | DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads | [paper](https://arxiv.org/abs/2410.10819) | [code](https://github.com/mit-han-lab/duo-attention) ![](https://img.shields.io/github/stars/mit-han-lab/duo-attention.svg?style=social) | ★★★★☆ | Separates retrieval heads from streaming heads to reduce long-context KV memory and latency. |
| 2025-01 | MLSys 2025 | FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving | [paper](https://arxiv.org/abs/2501.01005) | [code](https://github.com/flashinfer-ai/flashinfer) ![](https://img.shields.io/github/stars/flashinfer-ai/flashinfer.svg?style=social) | ★★★★★ | Flexible attention engine for paged, ragged, quantized, and compressed KV layouts. |
| 2025-02 | MLSys 2025 | LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention | [paper](https://arxiv.org/abs/2502.14866) | - | ★★★★☆ | Unified sparse-attention path for long-sequence prefill and decode. |
| 2026-02 | PPoPP 2026 | FlashAttention-T: Towards Fully Tensorized Attention by Exploiting Tensor-Vector Parallelism | [paper](https://ppopp26.sigplan.org/details/PPoPP-2026-papers/15/FlashAttention-T-Towards-Fully-Tensorized-Attention-by-Exploiting-Tensor-Vector-Para) | [artifact](https://zenodo.org/records/17673796) | ★★★★☆ | Tensorizes softmax work inside fused attention to reduce underutilized vector intervals. |
| 2026-02 | PPoPP 2026 | MetaAttention: A Unified and Performant Attention Framework Across Hardware Backends | [paper](https://ppopp26.sigplan.org/details/PPoPP-2026-papers/34/MetaAttention-A-Unified-and-Performant-Attention-Framework-Across-Hardware-Backends) | - | ★★★★☆ | Generates performant implementations for attention variants across hardware backends. |
| 2026-04 | arXiv | Flux Attention: Context-Aware Hybrid Attention for Efficient LLMs Inference | [paper](https://arxiv.org/abs/2604.07394) | [code](https://github.com/qqtang-code/FluxAttention) ![](https://img.shields.io/github/stars/qqtang-code/FluxAttention.svg?style=social) | ★★★☆☆ | Recent layer-level routing between full and sparse attention for long-context speedups. |

## KV cache eviction, retention, and compression

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-07 | arXiv | MemDecay: Region-Aware KV Cache Eviction for Efficient LLM Agent Inference | [paper](https://arxiv.org/abs/2607.10582) | - | ★★★☆☆ | Uses agent-trajectory regions and age-aware decay to evict stale cache state. |
| 2026-07 | ICML 2026 | STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control | [paper](https://icml.cc/virtual/2026/poster/61958) | [code](https://github.com/PriyanshBhatnagar/STAR-KV) ![](https://img.shields.io/github/stars/PriyanshBhatnagar/STAR-KV.svg?style=social) | ★★★★☆ | Adapts low-rank cache budgets with soft thresholding rather than fixed truncation. |
| 2026-07 | ICML 2026 | TGV-KV: Text-Grounded KV Eviction for Vision-Language Models | [paper](https://icml.cc/virtual/2026/poster/61187) | [code](https://github.com/Danielement321/TGV-KV) ![](https://img.shields.io/github/stars/Danielement321/TGV-KV.svg?style=social) | ★★★★☆ | Uses text grounding to retain multimodal KV entries that matter to generation. |
| 2026-05 | MLSys 2026 | SkipKV: Selective Skipping of KV Generation and Storage for Efficient Inference with Large Reasoning Models | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/45c1f6a8cbf2da59ebf2c802b4f742cd-Abstract-Conference.html) | [code](https://github.com/TTTTTTris/SkipKV) ![](https://img.shields.io/github/stars/TTTTTTris/SkipKV.svg?style=social) | ★★★★☆ | Skips both computation and storage for low-value KV states in long reasoning traces. |
| 2026-05 | MLSys 2026 | FlexiCache: Leveraging Temporal Stability of Attention Heads for Efficient KV Cache Management | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/94bcb01789fccf15afe2764d8fe0f40e-Abstract-Conference.html) | - | ★★★★☆ | Exploits stable head behavior to vary cache retention over time. |
| 2026-05 | MLSys 2026 | OPKV: A High-Throughput Plugin-Driven Framework for Recallable Sparsity in Paged KV Cache Systems | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/71381211d0abef73ed1887b83c4547b1-Abstract-Conference.html) | - | ★★★★☆ | Adds recallable sparse-cache policies to paged serving layouts through a plugin interface. |
| 2023-06 | NeurIPS 2023 | H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | [paper](https://arxiv.org/abs/2306.14048) | [code](https://github.com/FMInference/H2O) ![](https://img.shields.io/github/stars/FMInference/H2O.svg?style=social) | ★★★★★ | Heavy-hitter KV retention baseline. |
| 2023-09 | ICLR 2024 | Efficient Streaming Language Models with Attention Sinks | [paper](https://arxiv.org/abs/2309.17453) | [code](https://github.com/mit-han-lab/streaming-llm) ![](https://img.shields.io/github/stars/mit-han-lab/streaming-llm.svg?style=social) | ★★★★★ | Explains attention sinks and enables streaming contexts with bounded KV. |
| 2024-04 | NeurIPS 2024 | SnapKV: LLM Knows What You are Looking for Before Generation | [paper](https://arxiv.org/abs/2404.14469) | [code](https://github.com/FasterDecoding/SnapKV) ![](https://img.shields.io/github/stars/FasterDecoding/SnapKV.svg?style=social) | ★★★★☆ | Compresses prompt KV based on attention observations before generation. |
| 2024-05 | NeurIPS 2024 | MiniCache: KV Cache Compression in Depth Dimension for Large Language Models | [paper](https://arxiv.org/abs/2405.14366) | - | ★★★★☆ | Exploits cross-layer KV similarity instead of only token/head sparsity. |
| 2024-05 | arXiv | PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling | [paper](https://arxiv.org/abs/2406.02069) | [code](https://github.com/Zefan-Cai/PyramidKV) ![](https://img.shields.io/github/stars/Zefan-Cai/PyramidKV.svg?style=social) | ★★★★☆ | Layer-wise KV budget allocation for long-context inference. |
| 2024-06 | arXiv | Quest: Query-Aware Sparsity for Efficient Long-Context LLM Inference | [paper](https://arxiv.org/abs/2406.10774) | - | ★★★★☆ | Query-aware page selection for reducing long-context attention bandwidth. |
| 2024-07 | NeurIPS 2025 | Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference | [paper](https://arxiv.org/abs/2407.11550) | [code](https://github.com/FFY0/AdaKV) ![](https://img.shields.io/github/stars/FFY0/AdaKV.svg?style=social) | ★★★★☆ | Head-wise adaptive KV budget allocation that composes with eviction methods. |
| 2024-07 | ICLR 2025 | RazorAttention: Efficient KV Cache Compression Through Retrieval Heads | [paper](https://arxiv.org/abs/2407.15891) | - | ★★★★☆ | Separates retrieval-head behavior from full-cache retention. |
| 2024-10 | ICML 2025 | ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference | [paper](https://arxiv.org/abs/2410.21465) | [code](https://github.com/ByteDance-Seed/ShadowKV) ![](https://img.shields.io/github/stars/ByteDance-Seed/ShadowKV.svg?style=social) | ★★★★☆ | Low-rank key cache plus value offload for larger long-context serving batches. |
| 2025-02 | arXiv | Can LLMs Maintain Fundamental Abilities under KV Cache Compression? | [paper](https://arxiv.org/abs/2502.01941) | - | ★★★☆☆ | Useful cautionary analysis plus ShotKV method. |
| 2025-03 | arXiv | Rethinking Key-Value Cache Compression Techniques for Large Language Model Serving | [paper](https://arxiv.org/abs/2503.24000) | - | ★★★★☆ | Systems-oriented warning that compression can hurt end-to-end serving latency. |
| 2025-03 | arXiv | WindowKV: Task-Adaptive Group-Wise KV Cache Window Selection for Efficient LLM Inference | [paper](https://arxiv.org/abs/2503.17922) | - | ★★★☆☆ | Selects layer/head window sizes based on task behavior for bounded KV retention. |
| 2025-04 | arXiv | MILLION: Mastering Long-Context LLM Inference Via Outlier-Immunized KV Product Quantization | [paper](https://arxiv.org/abs/2504.03661) | - | ★★★☆☆ | Product-quantized KV cache plus GPU-oriented inference path for very long contexts. |
| 2025-05 | arXiv | KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction | [paper](https://arxiv.org/abs/2505.23416) | [code](https://github.com/snu-mllab/KVzip) ![](https://img.shields.io/github/stars/snu-mllab/KVzip.svg?style=social) | ★★★☆☆ | Recent query-agnostic compression direction. |
| 2025-02 | ICML 2025 | RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression | [paper](https://proceedings.mlr.press/v267/behnam25a.html) | [code](https://github.com/NVlabs/RocketKV) ![](https://img.shields.io/github/stars/NVlabs/RocketKV.svg?style=social) | ★★★★☆ | Two-stage KV pruning/compression pipeline for long-context inference. |
| 2025-06 | arXiv | Inference-Time Hyper-Scaling with KV Cache Compression | [paper](https://arxiv.org/abs/2506.05345) | - | ★★★☆☆ | Dynamic memory sparsification to trade KV memory for more inference-time sampling. |
| 2025-06 | arXiv | Efficient Long-Context LLM Inference via KV Cache Clustering | [paper](https://arxiv.org/abs/2506.11418) | - | ★★★☆☆ | Clusters KV entries to reduce long-context memory while preserving retrieval behavior. |
| 2025-07 | arXiv | HCAttention: Extreme KV Cache Compression via Heterogeneous Attention Computing for LLMs | [paper](https://arxiv.org/abs/2507.19823) | - | ★★★☆☆ | Uses heterogeneous attention behavior to keep only a small fraction of full KV. |
| 2025-09 | Findings EMNLP 2025 | EvolKV: Evolutionary KV Cache Compression for LLM Inference | [paper](https://arxiv.org/abs/2509.08315) | - | ★★★☆☆ | Evolutionary search over cache policies for memory/quality trade-offs. |
| 2025-09 | arXiv | KVCompose: Efficient Structured KV Cache Compression with Composite Tokens | [paper](https://arxiv.org/abs/2509.05165) | - | ★★★☆☆ | Structured composite-token compression compatible with standard decoding pipelines. |
| 2026-03 | arXiv | ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs | [paper](https://arxiv.org/abs/2603.08727) | [code](https://github.com/Large-scale-Sustainable-Computing-LSC/ARKV) ![](https://img.shields.io/github/stars/Large-scale-Sustainable-Computing-LSC/ARKV.svg?style=social) | ★★★☆☆ | Tri-state retain/quantize/evict cache policy for tight memory budgets. |

## KV cache offloading, reuse, and memory hierarchy

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-09 | arXiv | CacheBridge: Efficient Cross-Model KV Cache Transfer | [paper](https://arxiv.org/abs/2609.00891) | - | ★★★★☆ | Maps cache state between heterogeneous models so shared prefixes need not be replayed. |
| 2026-08 | SIGCOMM 2026 | Efficient Remote KV Cache Reuse with GPU-native Video Codec | [paper](https://dl.acm.org/doi/10.1145/3789240.3829120) | - | ★★★★☆ | Encodes remote KV state with GPU video hardware to reduce reuse-transfer overhead. |
| 2026-08 | arXiv | OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching | [paper](https://arxiv.org/abs/2608.08097) | - | ★★★★☆ | Predicts sparse decode access and prefetches offloaded KV state before it is needed. |
| 2026-07 | arXiv | HyMCache: A KV Cache Framework for Multi-Turn LLM Serving with CXL-Hybrid Memory | [paper](https://arxiv.org/abs/2607.18141) | - | ★★★★☆ | Places reusable multi-turn KV state across GPU and CXL-attached memory tiers. |
| 2026-05 | MLSys 2026 | ContextPilot: Fast Long-Context Inference via Context Reuse | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/b0131b6ee02a00b03fc3320176fec8f5-Abstract-Conference.html) | [code](https://github.com/EfficientContext/ContextPilot) ![](https://img.shields.io/github/stars/EfficientContext/ContextPilot.svg?style=social) | ★★★★☆ | Reuses context computation across related long-context requests. |
| 2023-10 | arXiv | CacheGen: KV Cache Compression and Streaming for Fast Large Language Model Serving | [paper](https://arxiv.org/abs/2310.07240) | - | ★★★★☆ | Compresses and streams reusable KV cache to lower context-fetch latency. |
| 2025-03 | arXiv | FastCache: Optimizing Multimodal LLM Serving through Lightweight KV-Cache Compression Framework | [paper](https://arxiv.org/abs/2503.08461) | - | ★★★☆☆ | Multimodal KV compression and cache lifecycle management. |
| 2025-06 | arXiv | Breaking the Boundaries of Long-Context LLM Inference: Adaptive KV Management on a Single Commodity GPU | [paper](https://arxiv.org/abs/2506.20187) | - | ★★★☆☆ | Hierarchical GPU-CPU-disk KV management for private single-GPU long-context inference. |
| 2025-11 | arXiv | CLO: Efficient LLM Inference System with CPU-Light KVCache Offloading via Algorithm-System Co-Design | [paper](https://arxiv.org/abs/2511.14510) | - | ★★★☆☆ | CPU-light KV offload path for reducing PCIe and CPU overhead during decoding. |
| 2026-02 | arXiv | HillInfer: Efficient Long-Context LLM Inference on the Edge with Hierarchical KV Eviction using SmartSSD | [paper](https://arxiv.org/abs/2602.18750) | - | ★★★☆☆ | SmartSSD-assisted KV eviction for edge long-context inference. |
| 2026-04 | arXiv | PolyKV: A Shared Asymmetrically-Compressed KV Cache Pool for Multi-Agent LLM Inference | [paper](https://arxiv.org/abs/2604.24971) | - | ★★★☆☆ | Shared compressed KV cache pool for concurrent multi-agent inference. |
| 2026-04 | arXiv | CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration | [paper](https://arxiv.org/abs/2604.25080) | - | ★★★☆☆ | Restores offloaded/compressed KV cache with token-layer-GPU parallelism. |
| 2026-05 | arXiv | Tutti: Making SSD-Backed KV Cache Practical for Long-Context LLM Serving | [paper](https://arxiv.org/abs/2605.03375) | - | ★★★☆☆ | SSD-backed KV cache design for long-context SLO pressure. |

## KV cache quantization

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-08 | arXiv | SemKV: Semantic Mixed-Precision KV Cache Quantization Guided by the Quality Cliff for Long-Context LLM Inference | [paper](https://arxiv.org/abs/2608.28911) | - | ★★★★☆ | Assigns semantic mixed precision while explicitly locating long-context quality cliffs. |
| 2026-08 | arXiv | SPECTRA: Pushing the KV Cache Beyond the 2-Bit Cliff via Spectral Transform Coding | [paper](https://arxiv.org/abs/2608.07915) | - | ★★★★☆ | Uses transform coding to retain cache quality below conventional two-bit limits. |
| 2026-07 | ICML 2026 | GSRQ: Gain-Shape Residual Quantization for Sub-1-bit KV Cache | [paper](https://icml.cc/virtual/2026/poster/65012) | - | ★★★★☆ | Separates gain and shape before residual quantization to push KV storage below one bit. |
| 2026-05 | MLSys 2026 | Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/e4d8d1b5120be349d3fff8878650cf45-Abstract-Conference.html) | [code](https://github.com/Summer-Summer/Kitty) ![](https://img.shields.io/github/stars/Summer-Summer/Kitty.svg?style=social) | ★★★★☆ | Dynamically raises precision only for sensitive KV channels. |
| 2024-02 | ICML 2024 | KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache | [paper](https://arxiv.org/abs/2402.02750) | [code](https://github.com/jy-yuan/KIVI) ![](https://img.shields.io/github/stars/jy-yuan/KIVI.svg?style=social) | ★★★★★ | Core 2-bit KV quantization method. |
| 2024-01 | arXiv | KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization | [paper](https://arxiv.org/abs/2401.18079) | [code](https://github.com/SqueezeAILab/KVQuant) ![](https://img.shields.io/github/stars/SqueezeAILab/KVQuant.svg?style=social) | ★★★★☆ | Sub-4-bit KV cache quantization for very long contexts. |
| 2025-03 | arXiv | Q-Filters: Leveraging QK Geometry for Efficient KV Cache Compression | [paper](https://arxiv.org/abs/2503.02812) | - | ★★★☆☆ | Uses QK geometry as a selection/filtering signal for compressed KV. |
| 2025-04 | ICLR 2026 | TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate | [paper](https://arxiv.org/abs/2504.19874) | - | ★★★★☆ | Online vector quantization used for near-lossless low-bit KV cache and vector search. |
| 2025-07 | arXiv | CommVQ: Commutative Vector Quantization for KV Cache Compression | [paper](https://machinelearning.apple.com/research/commutative-vector-quantization) | - | ★★★☆☆ | Apple work on vector quantization for long-context KV cache memory reduction. |
| 2025-10 | arXiv | VecInfer: Efficient LLM Inference with Low-Bit KV Cache via Outlier-Suppressed Vector Quantization | [paper](https://arxiv.org/abs/2510.06175) | - | ★★★☆☆ | Outlier-suppressed vector quantization for low-bit KV cache serving. |
| 2025-11 | arXiv | KV Cache Transform Coding for Compact Storage in LLM Inference | [paper](https://arxiv.org/abs/2511.01815) | - | ★★★☆☆ | Applies transform coding ideas to compact KV storage. |
| 2026-02 | PPoPP 2026 | JanusQuant: Accurate and Efficient 2-bit KV Cache Quantization for Long-Context Inference | [paper](https://ppopp26.sigplan.org/details/PPoPP-2026-papers/18/JanusQuant-Accurate-and-Efficient-2-bit-KV-Cache-Quantization-for-Long-context-Infer) | - | ★★★★☆ | Recent 2-bit KV quantization system from PPoPP's mixed-precision track. |

## Speculative and parallel decoding

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-07 | arXiv | SPORK: Self-Speculative Forking to Accelerate Agentic LLM Inference | [paper](https://arxiv.org/abs/2607.03333) | [code](https://github.com/baihuajun24/spork) ![](https://img.shields.io/github/stars/baihuajun24/spork.svg?style=social) | ★★★★☆ | Forks likely agent trajectories and verifies them with the same model to hide sequential latency. |
| 2026-07 | ICML 2026 | DAPD: Dependency-Aware Parallel Decoding via Attention for Diffusion LLMs | [paper](https://icml.cc/virtual/2026/poster/64624) | - | ★★★★☆ | Uses attention-derived dependencies to parallelize diffusion-language-model decoding. |
| 2026-07 | ICML 2026 | ECHO: Elastic Speculative Decoding with Sparse Gating for High-Concurrency Scenarios | [paper](https://icml.cc/virtual/2026/poster/64670) | - | ★★★★☆ | Adapts speculative work to concurrency pressure with sparse gates. |
| 2026-07 | ICML 2026 | SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding | [paper](https://icml.cc/virtual/2026/poster/64011) | - | ★★★☆☆ | Standardizes speculative-decoding evaluation across methods, models, and workloads. |
| 2026-06 | ISCA 2026 | Cassandra: Enabling Reasoning LLMs at Edge via Self-Speculative Decoding | [paper](https://arxiv.org/abs/2605.26558) | - | ★★★★☆ | Co-designs early exits and edge hardware behavior for self-speculative reasoning. |
| 2026-06 | ISCA 2026 | HybridSpec: Exploiting Hybrid-bonding Memory to Accelerate LLM Serving through Heterogeneous Architecture and Speculative Decoding | [paper](https://www.iscaconf.org/isca2026/program/) | - | ★★★★☆ | Couples heterogeneous compute and hybrid-bonded memory with speculative decoding. |
| 2026-05 | MLSys 2026 | SpecDiff-2: Scaling Diffusion Drafter Alignment For Faster Speculative Decoding | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/041dad5ed2191b44ba3ed0e00cdc3187-Abstract-Conference.html) | - | ★★★★☆ | Improves diffusion-drafter alignment to scale parallel speculative proposals. |
| 2026-05 | MLSys 2026 | Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/66a026c0d17040889b50f0dfa650e5e0-Abstract-Conference.html) | - | ★★★★☆ | Uses sparse early layers as an internal draft path for reasoning models. |
| 2022-11 | ICML 2023 | Fast Inference from Transformers via Speculative Decoding | [paper](https://arxiv.org/abs/2211.17192) | - | ★★★★★ | Foundational draft-and-verify speculative decoding paper. |
| 2023-02 | arXiv | Accelerating Large Language Model Decoding with Speculative Sampling | [paper](https://arxiv.org/abs/2302.01318) | - | ★★★★★ | Parallel formulation of speculative sampling for LLM decoding. |
| 2023-05 | arXiv | SpecInfer: Accelerating Generative Large Language Model Serving with Tree-based Speculative Inference and Verification | [paper](https://arxiv.org/abs/2305.09781) | - | ★★★★☆ | Tree-structured speculation for serving workloads. |
| 2023-11 | arXiv | Lookahead Decoding: Accelerating Autoregressive Inference of Large Language Models | [paper](https://arxiv.org/abs/2312.12728) | [code](https://github.com/hao-ai-lab/LookaheadDecoding) ![](https://img.shields.io/github/stars/hao-ai-lab/LookaheadDecoding.svg?style=social) | ★★★★☆ | Draft-free multi-token prediction via n-gram candidate verification. |
| 2024-01 | arXiv | Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads | [paper](https://arxiv.org/abs/2401.10774) | [code](https://github.com/FasterDecoding/Medusa) ![](https://img.shields.io/github/stars/FasterDecoding/Medusa.svg?style=social) | ★★★★☆ | Multi-head decoding framework with accessible implementation. |
| 2024-01 | arXiv | EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty | [paper](https://arxiv.org/abs/2401.15077) | [code](https://github.com/SafeAILab/EAGLE) ![](https://img.shields.io/github/stars/SafeAILab/EAGLE.svg?style=social) | ★★★★☆ | Feature-level draft model that became a practical speculative decoding baseline. |
| 2024-02 | NeurIPS 2024 | Sequoia: Scalable and Robust Speculative Decoding | [paper](https://arxiv.org/abs/2402.12374) | [code](https://github.com/Infini-AI-Lab/Sequoia) ![](https://img.shields.io/github/stars/Infini-AI-Lab/Sequoia.svg?style=social) | ★★★★☆ | Hardware-aware tree construction for robust speculative decoding. |
| 2024-02 | arXiv | Hydra: Sequentially-Dependent Draft Heads for Medusa Decoding | [paper](https://arxiv.org/abs/2402.05109) | [code](https://github.com/zankner/Hydra) ![](https://img.shields.io/github/stars/zankner/Hydra.svg?style=social) | ★★★☆☆ | Improves Medusa-style draft heads by making proposed tokens sequentially dependent. |
| 2024-04 | ACL 2024 | LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding | [paper](https://arxiv.org/abs/2404.16710) | [code](https://github.com/facebookresearch/LayerSkip) ![](https://img.shields.io/github/stars/facebookresearch/LayerSkip.svg?style=social) | ★★★★☆ | Early-exit training recipe plus self-speculation without an external draft model. |
| 2024-06 | NeurIPS 2024 | SpecExec: Massively Parallel Speculative Decoding for Interactive LLM Inference on Consumer Devices | [paper](https://arxiv.org/abs/2406.02532) | [code](https://github.com/yandex-research/specexec) ![](https://img.shields.io/github/stars/yandex-research/specexec.svg?style=social) | ★★★☆☆ | Consumer-device speculative execution path for offloaded large models. |
| 2025-03 | NeurIPS 2025 | EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test | [paper](https://arxiv.org/abs/2503.01840) | [code](https://github.com/SafeAILab/EAGLE) ![](https://img.shields.io/github/stars/SafeAILab/EAGLE.svg?style=social) | ★★★★☆ | Recent EAGLE variant focused on scaling speculative decoding quality. |
| 2025-06 | ICML 2025 | LongSpec: Long-Context Lossless Speculative Decoding with Efficient Drafting and Verification | [paper](https://icml.cc/virtual/2025/51846) | - | ★★★★☆ | Speculative decoding design for long-context agents with compact draft KV. |
| 2026-01 | ICLR 2026 Oral | Overcoming Joint Intractability with Lossless Hierarchical Speculative Decoding | [paper](https://openreview.net/forum?id=LaVrNaBNwM) | - | ★★★★☆ | Hierarchical verification for lossless speculative decoding. |
| 2026-02 | ICML 2026 | DFlash: Block Diffusion for Flash Speculative Decoding | [paper](https://arxiv.org/abs/2602.06036) | - | ★★★★☆ | Uses block-diffusion drafting to increase speculative decoding parallelism. |
| 2026-02 | HPCA 2026 | Adaptive Draft Sequence Length: Enhancing Speculative Decoding Throughput on PIM-Enabled Systems | [paper](https://2026.hpca-conf.org/details/hpca-2026-main-conference/112/Adaptive-Draft-Sequence-Length-Enhancing-Speculative-Decoding-Throughput-on-PIM-Enab) | - | ★★★☆☆ | Hardware-aware adaptive draft lengths for xPU+PIM speculative decoding systems. |
| 2026-05 | arXiv | Component-Aware Self-Speculative Decoding in Hybrid Language Models | [paper](https://arxiv.org/abs/2605.01106) | - | ★★★☆☆ | Early 2026 look at self-speculation for hybrid SSM/attention architectures. |

## Weight and activation quantization

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-09 | VLDB 2026 | QStore: Quantization-Aware Compressed Model Storage | [paper](https://www.vldb.org/pvldb/vol19/p388-li.pdf) | - | ★★★☆☆ | Stores multiple quantized model variants compactly while preserving efficient loading. |
| 2026-08 | KDD 2026 | RUQuant: Towards Refining Uniform Quantization for Large Language Models | [paper](https://doi.org/10.1145/3770854.3780259) | - | ★★★☆☆ | Refines uniform quantization to better handle LLM weight and activation distributions. |
| 2026-07 | ICML 2026 | LO-BCQ: Locally Optimal Block Clustered Quantization for 4-bit (W4A4) LLM Inference | [paper](https://icml.cc/virtual/2026/poster/68796) | - | ★★★★☆ | Optimizes clustered block quantizers for practical W4A4 execution. |
| 2022-10 | ICLR 2023 | GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers | [paper](https://arxiv.org/abs/2210.17323) | [code](https://github.com/IST-DASLab/gptq) ![](https://img.shields.io/github/stars/IST-DASLab/gptq.svg?style=social) | ★★★★★ | Classic post-training quantization baseline. |
| 2022-11 | ICML 2023 | SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models | [paper](https://arxiv.org/abs/2211.10438) | [code](https://github.com/mit-han-lab/smoothquant) ![](https://img.shields.io/github/stars/mit-han-lab/smoothquant.svg?style=social) | ★★★★★ | Practical W8A8 quantization method. |
| 2023-03 | arXiv | SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression | [paper](https://arxiv.org/abs/2306.03078) | [code](https://github.com/Vahe1994/SpQR) ![](https://img.shields.io/github/stars/Vahe1994/SpQR.svg?style=social) | ★★★★☆ | Sparse outlier-aware quantization for near-lossless compression. |
| 2023-06 | MLSys 2024 | AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration | [paper](https://arxiv.org/abs/2306.00978) | [code](https://github.com/mit-han-lab/llm-awq) ![](https://img.shields.io/github/stars/mit-han-lab/llm-awq.svg?style=social) | ★★★★★ | Widely adopted weight-only quantization baseline. |
| 2023-08 | ICLR 2024 | OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models | [paper](https://arxiv.org/abs/2308.13137) | [code](https://github.com/OpenGVLab/OmniQuant) ![](https://img.shields.io/github/stars/OpenGVLab/OmniQuant.svg?style=social) | ★★★★☆ | Calibration-heavy PTQ method with strong low-bit results. |
| 2024-02 | ICML 2024 | QuIP#: Even Better LLM Quantization with Hadamard Incoherence and Lattice Codebooks | [paper](https://arxiv.org/abs/2402.04396) | [code](https://github.com/Cornell-RelaxML/quip-sharp) ![](https://img.shields.io/github/stars/Cornell-RelaxML/quip-sharp.svg?style=social) | ★★★★☆ | Extreme weight-only quantization via incoherence processing and lattice codebooks. |
| 2024-02 | arXiv | The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits | [paper](https://arxiv.org/abs/2402.17764) | [code](https://github.com/microsoft/BitNet) ![](https://img.shields.io/github/stars/microsoft/BitNet.svg?style=social) | ★★★★☆ | Native ternary-weight LLM line with direct hardware/system implications. |
| 2024-04 | NeurIPS 2024 | QuaRot: Outlier-Free 4-Bit Inference in Rotated LLMs | [paper](https://arxiv.org/abs/2404.00456) | [code](https://github.com/spcl/QuaRot) ![](https://img.shields.io/github/stars/spcl/QuaRot.svg?style=social) | ★★★★☆ | Uses rotations to reduce outliers for efficient low-bit inference. |
| 2024-05 | ICLR 2025 | SpinQuant: LLM Quantization with Learned Rotations | [paper](https://arxiv.org/abs/2405.16406) | [code](https://github.com/facebookresearch/SpinQuant) ![](https://img.shields.io/github/stars/facebookresearch/SpinQuant.svg?style=social) | ★★★★☆ | Learns rotation matrices for W/A/KV low-bit quantization. |
| 2025-02 | PPoPP 2025 | MARLIN: Mixed-Precision Auto-Regressive Parallel Inference on Large Language Models | [paper](https://research-explorer.ista.ac.at/record/19877) | - | ★★★★☆ | Mixed-precision autoregressive inference kernel/system for quantized LLM serving. |
| 2026-02 | PPoPP 2026 | RoMeo: Mitigating Dual-dimensional Outliers with Rotated Mixed Precision Quantization | [paper](https://ppopp26.sigplan.org/details/PPoPP-2026-papers/9/RoMeo-Mitigating-Dual-dimensional-Outliers-with-Rotated-Mixed-Precision-Quantization) | - | ★★★★☆ | Rotation-based mixed precision quantization with token- and channel-wise outlier handling. |
| 2026-02 | PPoPP 2026 | High-Throughput Non-Uniformly Quantized 3-bit LLM Inference | [paper](https://ppopp26.sigplan.org/details/PPoPP-2026-papers/13/High-Throughput-Non-Uniformly-Quantized-3-bit-LLM-Inference) | - | ★★★★☆ | Quantix converts 3-bit non-uniform weight compression into batched inference speedups. |
| 2026-05 | arXiv | ADMM-Q: An Improved Hessian-based Weight Quantizer for Post-Training Quantization of Large Language Models | [paper](https://arxiv.org/abs/2605.11222) | - | ★★★☆☆ | Recent Hessian-based quantizer designed to compose with GPTQ, rotations, and scaling. |

## Pruning, sparsity, and compression

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-09 | VLDB 2026 | Unified Static–Dynamic Pruning for Efficient LLM Inference | [paper](https://www.vldb.org/pvldb/vol19/p2950-kim.pdf) | - | ★★★★☆ | Combines reusable static sparsity with input-dependent dynamic pruning. |
| 2026-05 | MLSys 2026 | Attribution-based Sparse Activation in Large Language Models | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/29591f355702c3f4436991335784b503-Abstract-Conference.html) | - | ★★★☆☆ | Uses attribution signals to skip low-impact activation computation. |
| 2023-01 | ICML 2023 | SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot | [paper](https://arxiv.org/abs/2301.00774) | [code](https://github.com/IST-DASLab/sparsegpt) ![](https://img.shields.io/github/stars/IST-DASLab/sparsegpt.svg?style=social) | ★★★★☆ | One-shot pruning baseline for large LMs. |
| 2023-06 | arXiv | Wanda: Pruning by Weights and Activations | [paper](https://arxiv.org/abs/2306.11695) | [code](https://github.com/locuslab/wanda) ![](https://img.shields.io/github/stars/locuslab/wanda.svg?style=social) | ★★★★☆ | Simple pruning metric with strong LLM results. |
| 2023-05 | NeurIPS 2023 | LLM-Pruner: On the Structural Pruning of Large Language Models | [paper](https://arxiv.org/abs/2305.11627) | [code](https://github.com/horseee/LLM-Pruner) ![](https://img.shields.io/github/stars/horseee/LLM-Pruner.svg?style=social) | ★★★☆☆ | Structured pruning framework for LLMs. |
| 2023-10 | ICLR 2024 | Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning | [paper](https://arxiv.org/abs/2310.06694) | [code](https://github.com/princeton-nlp/LLM-Shearing) ![](https://img.shields.io/github/stars/princeton-nlp/LLM-Shearing.svg?style=social) | ★★★★☆ | Targeted structured pruning plus continued training to obtain smaller LLMs cheaply. |
| 2024-01 | ICLR 2024 | SliceGPT: Compress Large Language Models by Deleting Rows and Columns | [paper](https://arxiv.org/abs/2401.15024) | [code](https://github.com/microsoft/TransformerCompression) ![](https://img.shields.io/github/stars/microsoft/TransformerCompression.svg?style=social) | ★★★☆☆ | Structured compression using computational invariance. |
| 2024-03 | ACL 2025 Findings | ShortGPT: Layers in Large Language Models are More Redundant Than You Expect | [paper](https://arxiv.org/abs/2403.03853) | [code](https://github.com/icip-cas/ShortGPT) ![](https://img.shields.io/github/stars/icip-cas/ShortGPT.svg?style=social) | ★★★☆☆ | Layer-removal pruning baseline driven by block influence. |

## MoE foundations, runtimes, and workloads

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-05 | MLSys 2026 | Demystifying the Mixture of Experts Serving Tax | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/42a452cbafa9dd64e9ba4aa95cc1ef21-Abstract-Conference.html) | - | ★★★★☆ | Separates the memory, communication, kernel, and load-imbalance costs behind MoE serving. |
| 2020-06 | arXiv | GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding | [paper](https://arxiv.org/abs/2006.16668) | - | ★★★★☆ | Sparse expert scaling and automatic sharding reference. |
| 2021-01 | JMLR 2022 | Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity | [paper](https://arxiv.org/abs/2101.03961) | - | ★★★★☆ | Widely cited simple MoE architecture. |
| 2021-03 | arXiv | FastMoE: A Fast Mixture-of-Expert Training System | [paper](https://arxiv.org/abs/2103.13262) | [code](https://github.com/laekov/fastmoe) ![](https://img.shields.io/github/stars/laekov/fastmoe.svg?style=social) | ★★★☆☆ | Early open MoE runtime with expert-parallel system support. |
| 2022-01 | ICML 2022 | DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training to Power Next-Generation AI Scale | [paper](https://proceedings.mlr.press/v162/rajbhandari22a.html) | [code](https://github.com/microsoft/DeepSpeed) ![](https://img.shields.io/github/stars/microsoft/DeepSpeed.svg?style=social) | ★★★★★ | Core MoE training and inference system baseline. |
| 2022-06 | SC 2022 | Tutel: Adaptive Mixture-of-Experts at Scale | [paper](https://arxiv.org/abs/2206.03382) | [code](https://github.com/microsoft/tutel) ![](https://img.shields.io/github/stars/microsoft/tutel.svg?style=social) | ★★★★☆ | Systems runtime for large-scale MoE training and serving. |
| 2022-11 | MLSys 2023 | MegaBlocks: Efficient Sparse Training with Mixture-of-Experts | [paper](https://arxiv.org/abs/2211.15841) | [code](https://github.com/stanford-futuredata/megablocks) ![](https://img.shields.io/github/stars/stanford-futuredata/megablocks.svg?style=social) | ★★★★☆ | Block-sparse expert computation with systems impact. |
| 2024-01 | arXiv | Mixtral of Experts | [paper](https://arxiv.org/abs/2401.04088) | [code](https://github.com/mistralai/mistral-src) ![](https://img.shields.io/github/stars/mistralai/mistral-src.svg?style=social) | ★★★☆☆ | Important open MoE model reference for inference-system workloads. |
| 2024-01 | ACL 2024 | DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models | [paper](https://arxiv.org/abs/2401.06066) | [code](https://github.com/deepseek-ai/DeepSeek-MoE) ![](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-MoE.svg?style=social) | ★★★★☆ | Fine-grained and shared-expert design that later systems use as a workload. |
| 2024-04 | arXiv | JetMoE: Reaching Llama2 Performance with 0.1M Dollars | [paper](https://arxiv.org/abs/2404.07413) | [code](https://github.com/myshell-ai/JetMoE) ![](https://img.shields.io/github/stars/myshell-ai/JetMoE.svg?style=social) | ★★★☆☆ | Small open MoE useful for reproducible system experiments. |
| 2024-05 | arXiv | DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model | [paper](https://arxiv.org/abs/2405.04434) | [code](https://github.com/deepseek-ai/DeepSeek-V2) ![](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-V2.svg?style=social) | ★★★★☆ | Combines MLA and DeepSeekMoE, driving many later MoE-serving papers. |
| 2024-09 | ICLR 2025 | OLMoE: Open Mixture-of-Experts Language Models | [paper](https://arxiv.org/abs/2409.02060) | [code](https://github.com/allenai/OLMoE) ![](https://img.shields.io/github/stars/allenai/OLMoE.svg?style=social) | ★★★★☆ | Fully open MoE weights, data, code, and logs for routing/system analysis. |
| 2024-12 | arXiv | DeepSeek-V3 Technical Report | [paper](https://arxiv.org/abs/2412.19437) | [code](https://github.com/deepseek-ai/DeepSeek-V3) ![](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-V3.svg?style=social) | ★★★★☆ | Large open MoE workload with auxiliary-loss-free load balancing and MLA. |
| 2025-05 | arXiv | Qwen3 Technical Report | [paper](https://arxiv.org/abs/2505.09388) | [code](https://github.com/QwenLM/Qwen3) ![](https://img.shields.io/github/stars/QwenLM/Qwen3.svg?style=social) | ★★★☆☆ | Includes large and small MoE variants used by recent serving/offloading work. |

## MoE expert offloading, caching, and prefetching

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-08 | arXiv | S2-MoE: Enabling Efficient Self-Speculative Decoding for Mixture-of-Experts on Edge Devices | [paper](https://arxiv.org/abs/2608.15018) | [code](https://github.com/angerybob/S2-MoE) ![](https://img.shields.io/github/stars/angerybob/S2-MoE.svg?style=social) | ★★★★☆ | Couples self-speculation with expert reuse to reduce edge-device weight traffic. |
| 2026-05 | arXiv | TIDE: Efficient and Lossless MoE Diffusion LLM Inference with I/O-aware Expert Offload | [paper](https://arxiv.org/abs/2605.20179) | - | ★★★★☆ | Schedules expert movement around diffusion reuse and storage I/O constraints. |
| 2026-06 | ISCA 2026 | STEP: Adaptive Spatio-Temporal Expert Prefetching for Low-Latency and Memory-Efficient MoE Inference | [paper](https://www.iscaconf.org/isca2026/program/) | - | ★★★★☆ | Predicts expert use across layers and time to prefetch under tight memory. |
| 2026-05 | arXiv | CoX-MoE: Coalesced Expert Execution for High-Throughput MoE Inference with AMX-Enabled CPU-GPU Co-Execution | [paper](https://arxiv.org/abs/2605.17889) | - | ★★★★☆ | Coalesces expert batches and executes them across GPU and AMX-enabled CPUs. |
| 2023-08 | arXiv | EdgeMoE: Empowering Sparse Large Language Models on Mobile Devices | [paper](https://arxiv.org/abs/2308.14352) | [code](https://github.com/UbiquitousLearning/mllm) ![](https://img.shields.io/github/stars/UbiquitousLearning/mllm.svg?style=social) | ★★★☆☆ | On-device MoE engine with external-storage expert fetch, bit-width adaptation, and preloading. |
| 2023-08 | ACL 2024 | SwapMoE: Serving Off-the-shelf MoE-based Large Language Models with Tunable Memory Budget | [paper](https://arxiv.org/abs/2308.15030) | - | ★★★☆☆ | Virtual-expert mapping for serving MoE models under adjustable memory budgets. |
| 2024-01 | arXiv | MoE-Infinity: Efficient MoE Inference on Personal Machines with Sparsity-Aware Expert Cache | [paper](https://arxiv.org/abs/2401.14361) | [code](https://github.com/EfficientMoE/MoE-Infinity) ![](https://img.shields.io/github/stars/EfficientMoE/MoE-Infinity.svg?style=social) | ★★★★☆ | Personal-machine MoE serving with sparsity-aware expert caching. |
| 2024-02 | ICLR 2025 | Fiddler: CPU-GPU Orchestration for Fast Inference of Mixture-of-Experts Models | [paper](https://arxiv.org/abs/2402.07033) | [code](https://github.com/efeslab/fiddler) ![](https://img.shields.io/github/stars/efeslab/fiddler.svg?style=social) | ★★★★★ | Runs selected expert work on CPU to avoid moving large expert weights over PCIe. |
| 2024-10 | arXiv | ProMoE: Fast MoE-based LLM Serving using Proactive Caching | [paper](https://arxiv.org/abs/2410.22134) | - | ★★★☆☆ | Predicts subsequent expert usage and proactively fetches experts to remove cache misses from the critical path. |
| 2024-11 | arXiv | HOBBIT: A Mixed Precision Expert Offloading System for Fast MoE Inference | [paper](https://arxiv.org/abs/2411.01433) | - | ★★★☆☆ | Couples expert offloading with mixed precision to reduce transfer pressure. |
| 2024-11 | arXiv | MoE-Lightning: High-Throughput MoE Inference on Memory-constrained GPUs | [paper](https://arxiv.org/abs/2411.11217) | - | ★★★★☆ | CPU-GPU-I/O pipelining with paged weights for batched MoE inference on low-cost GPUs. |
| 2025-01 | DATE 2025 | DAOP: Data-Aware Offloading and Predictive Pre-Calculation for Efficient MoE Inference | [paper](https://arxiv.org/abs/2501.10375) | - | ★★★☆☆ | Uses sequence-level activation patterns to place experts and precompute likely CPU-side work. |
| 2025-02 | arXiv | fMoE: Fine-Grained Expert Offloading for Large Mixture-of-Experts Serving | [paper](https://arxiv.org/abs/2502.05370) | - | ★★★☆☆ | Fine-grained offloading policy for latency-memory trade-offs in MoE serving. |
| 2025-02 | arXiv | Fate: Fast Edge Inference of Mixture-of-Experts Models via Cross-Layer Gate | [paper](https://arxiv.org/abs/2502.12224) | - | ★★★☆☆ | Uses adjacent-layer gate inputs for high-accuracy expert prefetching on edge devices. |
| 2025-04 | arXiv | HybriMoE: Hybrid CPU-GPU Scheduling and Cache Management for Efficient MoE Inference | [paper](https://arxiv.org/abs/2504.05897) | - | ★★★☆☆ | Joint CPU-GPU scheduling and expert-cache management for memory-constrained MoE inference. |
| 2025-04 | arXiv | D2MoE: Dual Routing and Dynamic Scheduling for Efficient On-Device MoE-based LLM Serving | [paper](https://arxiv.org/abs/2504.15299) | - | ★★★☆☆ | Co-designs routing, scheduling, and expert bit-width allocation for edge MoE serving. |
| 2025-05 | ICML 2025 | FloE: On-the-Fly MoE Inference on Memory-constrained GPU | [paper](https://openreview.net/forum?id=i5aHAkkhJH) | - | ★★★★☆ | ICML work on exploiting expert redundancy to reduce on-demand transfer cost. |
| 2025-06 | arXiv | HarMoEny: Efficient Multi-GPU Inference of MoE Models | [paper](https://arxiv.org/abs/2506.12417) | - | ★★★☆☆ | Combines dynamic token redistribution with asynchronous expert prefetching across GPUs. |
| 2025-08 | arXiv | Accelerating Mixture-of-Experts Inference by Hiding Offloading Latency with Speculative Decoding | [paper](https://arxiv.org/abs/2508.21706) | - | ★★★☆☆ | SpecMoEOff enlarges expert workloads via speculative decoding to hide offload latency. |
| 2025-10 | arXiv | ExpertFlow: Adaptive Expert Scheduling and Memory Coordination for Efficient MoE Inference | [paper](https://arxiv.org/abs/2510.26730) | - | ★★★☆☆ | Runtime prefetch horizon adjustment and cache-aware routing for memory-limited serving. |
| 2025-11 | arXiv | MoE-SpeQ: Speculative Quantized Decoding with Proactive Expert Prefetching and Offloading for Mixture-of-Experts | [paper](https://arxiv.org/abs/2511.14102) | - | ★★★☆☆ | Co-designs speculative execution, quantization, and expert offloading. |
| 2025-12 | arXiv | OD-MoE: On-Demand Expert Loading for Cacheless Edge-Distributed MoE Inference | [paper](https://arxiv.org/abs/2512.03927) | - | ★★★☆☆ | Distributed edge framework that loads predicted experts just in time instead of maintaining a GPU cache. |
| 2025-12 | arXiv | SliceMoE: Bit-Sliced Expert Caching under Miss-Rate Constraints for Efficient MoE Inference | [paper](https://arxiv.org/abs/2512.12990) | - | ★★★☆☆ | Bit-sliced mixed-precision expert caching with predictive warmup for on-device MoE. |
| 2026-02 | arXiv | DALI: A Workload-Aware Offloading Framework for Efficient MoE Inference on Local PCs | [paper](https://arxiv.org/abs/2602.03495) | - | ★★★☆☆ | Local-PC offloading framework with workload-aware cache replacement. |
| 2026-02 | arXiv | MoE-SpAc: Efficient MoE Inference Based on Speculative Activation Utility in Heterogeneous Edge Scenarios | [paper](https://arxiv.org/abs/2603.09983) | [code](https://github.com/lshAlgorithm/MoE-SpAc) ![](https://img.shields.io/github/stars/lshAlgorithm/MoE-SpAc.svg?style=social) | ★★★☆☆ | Uses speculative utility estimates for partitioning, prefetching, and eviction on heterogeneous edge hardware. |
| 2026-03 | arXiv | Speculating Experts Accelerates Inference for Mixture-of-Experts | [paper](https://arxiv.org/abs/2603.19289) | - | ★★★☆☆ | Internal-state-based expert prefetching that overlaps CPU-GPU transfers with computation. |
| 2026-03 | AAAI 2026 | CommitMoE: Efficient Fallback-Free MoE Inference with Offloading Under GPU Memory Constraints | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/39454) | - | ★★★★☆ | Commit router avoids fallback paths in predicted expert offloading. |
| 2026-03 | AAAI 2026 | CasMoE: A Cascaded Framework for Efficient MoE Inference on Resource-constrained Devices | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/39816) | - | ★★★☆☆ | Cascaded offline-online expert activation prediction for resource-constrained devices. |
| 2026-04 | arXiv | FluxMoE: Decoupling Expert Residency for High-Performance MoE Serving | [paper](https://arxiv.org/abs/2604.02715) | - | ★★★☆☆ | Decouples expert-parameter residency from persistent GPU memory to free capacity for serving state. |
| 2026-04 | arXiv | Efficient Mixture-of-Experts LLM Inference with Apple Silicon NPUs | [paper](https://arxiv.org/abs/2604.18788) | - | ★★★☆☆ | Targets MoE routing, dynamic shapes, and small-kernel overheads on Apple NPUs. |

## MoE scheduling and expert-parallel execution

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-08 | SIGCOMM 2026 | Balancing and Beyond: Communication-Centric Optimizations in Expert Parallelism | [paper](https://dl.acm.org/doi/10.1145/3789240.3829201) | - | ★★★★★ | Combines performance-aware migration, activation handling, and topology-adaptive communication at production scale. |
| 2026-08 | SIGCOMM 2026 | UBEP: Re-architecting Expert Parallelism Communication Library for Production Superpods | [paper](https://dl.acm.org/doi/10.1145/3789240.3829183) | - | ★★★★☆ | Rebuilds the expert-parallel communication path for large production superpods. |
| 2026-09 | arXiv | DynaNDE: Dynamic Near-Data Expert Scheduling for Batched MoE Inference | [paper](https://arxiv.org/abs/2609.00407) | - | ★★★★☆ | Dynamically places batched expert work near weights to reduce movement and imbalance. |
| 2026-06 | arXiv | ViBE: Co-Optimizing Workload Skew and Hardware Variability for MoE Serving | [paper](https://arxiv.org/abs/2606.00735) | - | ★★★★☆ | Jointly handles expert-load skew and heterogeneous accelerator performance. |
| 2026-06 | arXiv | Beyond Task-Agnostic: Task-Aware Grouping for Communication-Efficient Multi-Task MoE Inference | [paper](https://arxiv.org/abs/2606.01007) | - | ★★★☆☆ | Groups requests by task-level routing affinity to reduce expert-parallel communication. |
| 2026-06 | ISCA 2026 | Patterns Behind Chaos: Forecasting Data Movement for Efficient Large-Scale MoE LLM Inference | [paper](https://arxiv.org/abs/2510.05497) | - | ★★★★★ | ISCA best paper that forecasts MoE data movement to improve distributed execution. |
| 2026-06 | ISCA 2026 | MoE-Hub: Taming Software Complexity for Seamless MoE Overlap with Hardware-Accelerated Communication on Multi-GPU Systems | [paper](https://arxiv.org/abs/2605.05888) | - | ★★★★☆ | Provides a unified runtime abstraction for overlapping expert communication and compute. |
| 2026-05 | arXiv | PALS: Power-Aware LLM Serving for Mixture-of-Experts Models | [paper](https://arxiv.org/abs/2605.21427) | - | ★★★☆☆ | Includes power budgets in expert placement and serving decisions. |
| 2026-05 | MLSys 2026 | CRAFT: Fine-Grained Cost-Aware Expert Replication For Efficient Mixture-of-Experts Serving | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/3a7f9e485845dac27423375c934cb4db-Abstract-Conference.html) | - | ★★★★☆ | Replicates experts according to measured communication and imbalance cost. |
| 2026-05 | MLSys 2026 | From Tokens to Layers: Redefining Stall-Free Scheduling for MoE Serving with Layered Prefill | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/c0f460c6d63599ea870ba9db63dc96a9-Abstract-Conference.html) | - | ★★★★☆ | Uses layered prefill to overlap expert movement and execution without token-level stalls. |
| 2022-10 | ATC 2023 | Accelerating Distributed MoE Training and Inference with Lina | [paper](https://arxiv.org/abs/2210.17223) | - | ★★★★☆ | Analyzes all-to-all bottlenecks and dynamically schedules resources for skewed expert popularity. |
| 2023-03 | arXiv | Towards MoE Deployment: Mitigating Inefficiencies in Mixture-of-Expert Inference | [paper](https://arxiv.org/abs/2303.06182) | - | ★★★☆☆ | Early deployment study covering gating, buffering, and load balancing for MoE inference. |
| 2023-07 | ATC 2023 | SmartMoE: Efficiently Training Sparsely-Activated Models through Combining Offline and Online Parallelization | [paper](https://www.usenix.org/conference/atc23/presentation/zhai) | [code](https://github.com/zms1999/SmartMoE) ![](https://img.shields.io/github/stars/zms1999/SmartMoE.svg?style=social) | ★★★☆☆ | Online/offline parallelization ideas useful for expert placement and scheduling. |
| 2024-04 | SC 2024 | APTMoE: Affinity-Aware Pipeline Tuning for MoE Models on Bandwidth-Constrained GPU Nodes | [paper](https://xianweiz.github.io/doc/papers/aptmoe_sc24.pdf) | - | ★★★☆☆ | Affinity-aware pipeline tuning for bandwidth-constrained MoE GPU nodes. |
| 2024-04 | arXiv | Shortcut-connected Expert Parallelism for Accelerating Mixture-of-Experts | [paper](https://arxiv.org/abs/2404.05019) | - | ★★★☆☆ | Expert-parallel acceleration by reducing communication through shortcut connections. |
| 2024-10 | arXiv | EPS-MoE: Expert Pipeline Scheduler for Cost-Efficient MoE Inference | [paper](https://arxiv.org/abs/2410.12247) | - | ★★★★☆ | Dynamically selects GEMM strategy and overlaps expert compute with communication. |
| 2024-11 | arXiv | Lynx: Enabling Efficient MoE Inference through Dynamic Batch-Aware Expert Selection | [paper](https://arxiv.org/abs/2411.08982) | - | ★★★☆☆ | Batch-aware expert selection for improving MoE inference efficiency. |
| 2024-11 | arXiv | HEXA-MoE: Efficient and Heterogeneous-aware MoE Acceleration with ZERO Computation Redundancy | [paper](https://arxiv.org/abs/2411.01288) | [code](https://github.com/UNITES-Lab/HEXA-MoE) ![](https://img.shields.io/github/stars/UNITES-Lab/HEXA-MoE.svg?style=social) | ★★★☆☆ | Heterogeneous-aware MoE acceleration with redundant-computation elimination. |
| 2025-02 | PPoPP 2025 | Harnessing Inter-GPU Shared Memory for Seamless MoE Communication-Computation Fusion | [paper](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1) | - | ★★★★☆ | Fuses MoE expert communication and computation through inter-GPU shared memory. |
| 2025-03 | arXiv | MoE-Gen: High-Throughput MoE Inference on a Single GPU with Module-Based Batching | [paper](https://arxiv.org/abs/2503.09716) | - | ★★★★☆ | Accumulates tokens by module to create large GPU batches for offline MoE inference. |
| 2025-03 | arXiv | Priority-Aware Preemptive Scheduling for Mixed-Priority Workloads in MoE Inference | [paper](https://arxiv.org/abs/2503.09304) | - | ★★★☆☆ | Expert-level preemption for latency-sensitive and best-effort mixed-priority MoE workloads. |
| 2025-03 | ICLR 2026 | Semantic Parallelism: Redefining Efficient MoE Inference via Model-Data Co-Scheduling | [paper](https://arxiv.org/abs/2503.04398) | - | ★★★★☆ | Sem-MoE co-schedules expert placement and request/token routing to reduce all-to-all traffic. |
| 2025-06 | NeurIPS 2025 | FlashMoE: Fast Distributed MoE in a Single Kernel | [paper](https://arxiv.org/abs/2506.04667) | [code](https://github.com/osayamenja/FlashMoE) ![](https://img.shields.io/github/stars/osayamenja/FlashMoE.svg?style=social) | ★★★★☆ | Fuses distributed dispatch, expert compute, and combine into a persistent GPU kernel. |
| 2025-12 | arXiv | Efficient MoE Inference with Fine-Grained Scheduling of Disaggregated Expert Parallelism | [paper](https://arxiv.org/abs/2512.21487) | - | ★★★☆☆ | FinDEP schedules disaggregated expert-parallel tasks to overlap compute and communication. |

## MoE routing, load balancing, and expert skipping

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-08 | ICML 2026 | EasyBalance: Cross-Layer Load Balancing in Distributed MoE Inference | [paper](https://arxiv.org/abs/2608.07964) | - | ★★★★☆ | Coordinates routing imbalance across layers rather than balancing each layer in isolation. |
| 2026-06 | ISCA 2026 | SMoE: An Algorithm-System Co-Design for Pushing MoE to the Edge via Expert Substitution | [paper](https://www.iscaconf.org/isca2026/program/) | - | ★★★★☆ | Substitutes unavailable experts to reduce edge memory and transfer pressure. |
| 2023-08 | ISCA 2024 | Pre-gated MoE: An Algorithm-System Co-Design for Fast and Scalable Mixture-of-Expert Inference | [paper](https://arxiv.org/abs/2308.12066) | [code](https://github.com/ranggihwang/Pregated_MoE) ![](https://img.shields.io/github/stars/ranggihwang/Pregated_MoE.svg?style=social) | ★★★★☆ | Predicts expert use earlier to enable prefetching and scalable MoE inference. |
| 2024-04 | arXiv | Prediction Is All MoE Needs: Expert Load Distribution Goes from Fluctuating to Stabilizing | [paper](https://arxiv.org/abs/2404.16914) | - | ★★★☆☆ | Studies expert-load predictability and its scheduling implications. |
| 2024-08 | arXiv | AdapMoE: Adaptive Sensitivity-based Expert Gating and Management for Efficient MoE Inference | [paper](https://arxiv.org/abs/2408.10284) | [code](https://github.com/PKU-SEC-Lab/AdapMoE) ![](https://img.shields.io/github/stars/PKU-SEC-Lab/AdapMoE.svg?style=social) | ★★★☆☆ | Adaptive expert gating/management for reducing MoE inference cost. |
| 2024-10 | ICLR 2025 Oral | MoE++: Accelerating Mixture-of-Experts Methods with Zero-Computation Experts | [paper](https://arxiv.org/abs/2410.07348) | [code](https://github.com/SkyworkAI/MoE-plus-plus) ![](https://img.shields.io/github/stars/SkyworkAI/MoE-plus-plus.svg?style=social) | ★★★★☆ | Adds zero/copy/constant experts to reduce expert forward cost. |
| 2025-03 | ICLR 2026 | Capacity-Aware Inference: Mitigating the Straggler Effect in Mixture of Experts | [paper](https://openreview.net/forum?id=LuYFpySWA2) | [code](https://github.com/CASE-Lab-UMD/Capacity-Aware-MoE) ![](https://img.shields.io/github/stars/CASE-Lab-UMD/Capacity-Aware-MoE.svg?style=social) | ★★★★☆ | Runtime capacity-aware drop/reroute to reduce overloaded-expert stragglers. |
| 2025-05 | ICLR 2026 | Not All Models Suit Expert Offloading: On Local Routing Consistency of Mixture-of-Expert Models | [paper](https://openreview.net/forum?id=2XMAUP74ig) | - | ★★★★☆ | Defines routing-consistency metrics that predict whether expert caching/offloading will work. |
| 2025-09 | arXiv | LExI: Layer-Adaptive Active Experts for Efficient MoE Model Inference | [paper](https://arxiv.org/abs/2509.02753) | - | ★★★☆☆ | Data-free layer-wise active-expert allocation to reduce redundant compute. |
| 2026-02 | ICLR 2026 | SERE: Similarity-based Expert Re-routing for Efficient Batch Decoding in MoE Models | [paper](https://openreview.net/forum?id=98IxaUQtMY) | [code](https://github.com/JL-Cheng/SERE) ![](https://img.shields.io/github/stars/JL-Cheng/SERE.svg?style=social) | ★★★★☆ | Dynamically reroutes secondary experts and provides a vLLM-friendly CUDA kernel. |

## MoE quantization, compression, and expert merging

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-07 | arXiv | PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization | [paper](https://arxiv.org/abs/2607.16184) | - | ★★★★☆ | Pages experts at dynamically selected precision according to quality and memory pressure. |
| 2026-07 | ICML 2026 | ZipMoE: Efficient On-Device MoE Serving via Lossless Compression and Cache-Affinity Scheduling | [paper](https://icml.cc/virtual/2026/poster/64146) | [code](https://github.com/npnothard/ZipMoE-ICML26) ![](https://img.shields.io/github/stars/npnothard/ZipMoE-ICML26.svg?style=social) | ★★★★☆ | Combines lossless expert compression with cache-aware on-device scheduling. |
| 2026-05 | MLSys 2026 | FP8-Flow-MoE: A Casting-Free FP8 Recipe without Double Quantization Error | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/9cb295d4dce6db99f01e0dd512e46ba0-Abstract-Conference.html) | [code](https://github.com/021ai/FP8-FLOW-MOE-AE) ![](https://img.shields.io/github/stars/021ai/FP8-FLOW-MOE-AE.svg?style=social) | ★★★★☆ | Removes redundant casts and double quantization in FP8 MoE execution. |
| 2023-10 | arXiv | QMoE: Practical Sub-1-Bit Compression of Trillion-Parameter Models | [paper](https://arxiv.org/abs/2310.16795) | [code](https://github.com/IST-DASLab/qmoe) ![](https://img.shields.io/github/stars/IST-DASLab/qmoe.svg?style=social) | ★★★★☆ | Extreme MoE compression with custom GPU decoding kernels. |
| 2023-10 | ICLR 2024 | Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy | [paper](https://arxiv.org/abs/2310.01334) | [code](https://github.com/unites-lab/mc-smoe) ![](https://img.shields.io/github/stars/unites-lab/mc-smoe.svg?style=social) | ★★★★☆ | Expert merging/compression guided by routing behavior. |
| 2024-06 | arXiv | QuantMoE-Bench: Examining Post-Training Quantization for Mixture-of-Experts | [paper](https://arxiv.org/abs/2406.08155) | - | ★★★☆☆ | Benchmark for MoE-specific PTQ behavior and failure modes. |
| 2024-10 | arXiv | MoE-Pruner: Pruning Mixture-of-Experts Large Language Model using the Hints from Its Router | [paper](https://arxiv.org/abs/2410.12013) | - | ★★★☆☆ | Router-informed expert pruning for MoE model-size reduction. |
| 2024-10 | arXiv | MC-MoE: Mixture Compressor for Mixture-of-Experts LLMs Gains More | [paper](https://arxiv.org/abs/2410.06270) | [code](https://github.com/Aaronhuang-778/MC-MoE) ![](https://img.shields.io/github/stars/Aaronhuang-778/MC-MoE.svg?style=social) | ★★★☆☆ | Mixture-compressor approach for reducing MoE memory footprint. |
| 2024-11 | arXiv | MoE-I2: Compressing Mixture of Experts Models through Inter-Expert Pruning and Intra-Expert Low-Rank Decomposition | [paper](https://arxiv.org/abs/2411.01016) | [code](https://github.com/xiaochengsky/MoEI-2) ![](https://img.shields.io/github/stars/xiaochengsky/MoEI-2.svg?style=social) | ★★★☆☆ | Combines inter-expert pruning with intra-expert low-rank decomposition. |
| 2025-03 | DATE 2026 | DynaMo: Runtime Switchable Quantization for MoE with Cross-Dataset Adaptation | [paper](https://arxiv.org/abs/2503.21135) | - | ★★★☆☆ | Expert-level mixed precision plus channel-level dynamic switching for deployment drift. |
| 2025-04 | arXiv | MiLo: Efficient Quantized MoE Inference with Mixture of Low-Rank Compensators | [paper](https://arxiv.org/abs/2504.02658) | - | ★★★☆☆ | Adds low-rank compensators and Tensor Core-friendly 3-bit kernels for quantized MoE. |
| 2025-05 | arXiv | MoEQuant: Enhancing Quantization for Mixture-of-Experts Large Language Models via Expert-Balanced Sampling and Affinity Guidance | [paper](https://arxiv.org/abs/2505.03804) | - | ★★★☆☆ | Balances expert calibration samples and uses affinity-aware quantization. |
| 2025-05 | arXiv | MxMoE: Mixed-precision Quantization for MoE with Accuracy and Performance Co-Design | [paper](https://arxiv.org/abs/2505.05799) | - | ★★★☆☆ | Mixed-precision quantization tuned for expert sensitivity and activation frequency. |
| 2025-06 | arXiv | EAQuant: Enhancing Post-Training Quantization for MoE Models via Expert-Aware Optimization | [paper](https://arxiv.org/abs/2506.13329) | [code](https://github.com/darren-fzq1/EAQuant) ![](https://img.shields.io/github/stars/darren-fzq1/EAQuant.svg?style=social) | ★★★☆☆ | Expert-aware smoothing, routing consistency, and balanced calibration for low-bit MoE. |
| 2025-09 | OpenReview 2026 | PuzzleMoE: Efficient Compression of Large Mixture-of-Experts Models via Sparse Expert Merging and Bit-packed inference | [paper](https://openreview.net/forum?id=8Si90C3Yxd) | - | ★★★☆☆ | Training-free sparse expert merging plus bit-packed inference encoding. |

## Long-context and efficient architectures

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-06 | ISCA 2026 | Tetris: Efficient Long-context LLM Serving with Chunkwise Dynamic Sequence Parallelism | [paper](https://www.iscaconf.org/isca2026/program/) | - | ★★★★☆ | Dynamically changes sequence parallelism by chunk as long-context phases evolve. |
| 2020-04 | arXiv | Longformer: The Long-Document Transformer | [paper](https://arxiv.org/abs/2004.05150) | [code](https://github.com/allenai/longformer) ![](https://img.shields.io/github/stars/allenai/longformer.svg?style=social) | ★★★☆☆ | Early sparse-attention long-context baseline. |
| 2020-07 | NeurIPS 2020 | Big Bird: Transformers for Longer Sequences | [paper](https://arxiv.org/abs/2007.14062) | [code](https://github.com/google-research/bigbird) ![](https://img.shields.io/github/stars/google-research/bigbird.svg?style=social) | ★★★☆☆ | Sparse attention pattern with theoretical support. |
| 2023-02 | ICML 2023 | Hyena Hierarchy: Towards Larger Convolutional Language Models | [paper](https://arxiv.org/abs/2302.10866) | [code](https://github.com/HazyResearch/safari) ![](https://img.shields.io/github/stars/HazyResearch/safari.svg?style=social) | ★★★☆☆ | Long convolutional architecture line for sub-quadratic sequence modeling. |
| 2023-07 | arXiv | Retentive Network: A Successor to Transformer for Large Language Models | [paper](https://arxiv.org/abs/2307.08621) | [code](https://github.com/microsoft/unilm) ![](https://img.shields.io/github/stars/microsoft/unilm.svg?style=social) | ★★★☆☆ | Retention mechanism with recurrent-style inference and parallel training. |
| 2023-12 | arXiv | Mamba: Linear-Time Sequence Modeling with Selective State Spaces | [paper](https://arxiv.org/abs/2312.00752) | [code](https://github.com/state-spaces/mamba) ![](https://img.shields.io/github/stars/state-spaces/mamba.svg?style=social) | ★★★★☆ | KV-free sequence architecture with major inference implications. |
| 2024-02 | ICLR 2024 | Ring Attention with Blockwise Transformers for Near-Infinite Context | [paper](https://arxiv.org/abs/2310.01889) | [code](https://github.com/lucidrains/ring-attention-pytorch) ![](https://img.shields.io/github/stars/lucidrains/ring-attention-pytorch.svg?style=social) | ★★★☆☆ | Distributed attention pattern for very long contexts. |
| 2024-02 | arXiv | Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models | [paper](https://arxiv.org/abs/2402.19427) | - | ★★★☆☆ | Hybrid recurrent/local-attention architecture with inference-throughput motivation. |
| 2024-03 | arXiv | Jamba: A Hybrid Transformer-Mamba Language Model | [paper](https://arxiv.org/abs/2403.19887) | - | ★★★★☆ | Production-scale hybrid Transformer-Mamba-MoE model with long-context efficiency. |
| 2023-09 | ICLR 2024 | YaRN: Efficient Context Window Extension of Large Language Models | [paper](https://arxiv.org/abs/2309.00071) | [code](https://github.com/jquesnelle/yarn) ![](https://img.shields.io/github/stars/jquesnelle/yarn.svg?style=social) | ★★★☆☆ | Practical RoPE scaling technique for long-context adaptation. |
| 2024-04 | arXiv | Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention | [paper](https://arxiv.org/abs/2404.07143) | - | ★★★☆☆ | Memory-style attention mechanism for long-context modeling. |

## Efficient reasoning and test-time compute

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-07 | OSDI 2026 | Breaking the Reward Barrier: Accelerating Tree-of-Thought Reasoning via Speculative Exploration | [paper](https://www.usenix.org/conference/osdi26/presentation/zhong) | - | ★★★★☆ | Speculatively explores tree branches to keep accelerators busy during reward-guided reasoning. |
| 2026-05 | MLSys 2026 | Locality-Aware Beam Scheduling for Efficient Test-Time Compute with a Consumer-grade GPU | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/c74b624843218d9b6713fcf299d6d5e4-Abstract-Conference.html) | - | ★★★☆☆ | Schedules candidate beams to exploit memory locality on a single consumer GPU. |
| 2024-07 | arXiv | Large Language Monkeys: Scaling Inference Compute with Repeated Sampling | [paper](https://arxiv.org/abs/2407.21787) | - | ★★★★☆ | Shows simple repeated sampling as a strong test-time compute baseline. |
| 2025-03 | arXiv | Efficient Inference for Large Reasoning Models: A Survey | [paper](https://arxiv.org/abs/2503.23077) | - | ★★★☆☆ | Recent map of efficient inference methods for reasoning models. |
| 2025-06 | arXiv | Cost-Efficient Serving of LLM Agents via Test-Time Plan Caching | [paper](https://arxiv.org/abs/2506.14852) | - | ★★★☆☆ | Bridges agent serving cost with reusable test-time plans. |

## Upstream source lists

[Back to top](#top)

| Source repo | Scope | Priority | Notes |
|---|---|---|---|
| [horseee/Awesome-Efficient-LLM](https://github.com/horseee/Awesome-Efficient-LLM) | Efficient LLMs | P0 | Broadest efficient-LLM entry point. |
| [Zefan-Cai/Awesome-LLM-KV-Cache](https://github.com/Zefan-Cai/Awesome-LLM-KV-Cache) | KV cache | P0 | Template inspiration and core KV source. |
| [jjiantong/Awesome-KV-Cache-Optimization](https://github.com/jjiantong/Awesome-KV-Cache-Optimization) | System-aware KV optimization | P0 | Very aligned with LLM serving. |
| [hemingkx/SpeculativeDecodingPapers](https://github.com/hemingkx/SpeculativeDecodingPapers) | Speculative decoding | P0 | Core speculative decoding list. |
| [HuangOwen/Awesome-LLM-Compression](https://github.com/HuangOwen/Awesome-LLM-Compression) | LLM compression | P0 | Core compression entry. |
| [pprp/awesome-llm-quantization](https://github.com/pprp/awesome-llm-quantization) | LLM quantization | P0 | Strong quantization source. |
| [MoE-Inf/awesome-moe-inference](https://github.com/MoE-Inf/awesome-moe-inference/) | MoE inference | P0 | Direct fit for MoE serving. |
| [Xnhyacinth/Awesome-LLM-Long-Context-Modeling](https://github.com/Xnhyacinth/Awesome-LLM-Long-Context-Modeling) | Long context | P1 | Bridge to memory and RAG. |
