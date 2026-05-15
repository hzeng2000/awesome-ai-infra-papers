# Systems & Serving

## Scope

AI systems papers for serving, scheduling, batching, memory management, disaggregated inference, distributed training, and deployment on constrained devices. Tables are organized by technical sub-direction instead of by whether code exists.

## Serving engines and KV memory management

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2022-07 | OSDI 2022 | Orca: A Distributed Serving System for Transformer-Based Generative Models | [paper](https://www.usenix.org/conference/osdi22/presentation/yu) | - | ★★★★★ | Foundational paper for iteration-level scheduling and continuous batching. |
| 2023-09 | SOSP 2023 | Efficient Memory Management for Large Language Model Serving with PagedAttention | [paper](https://arxiv.org/abs/2309.06180) | [code](https://github.com/vllm-project/vllm) | ★★★★★ | Introduces PagedAttention and the vLLM serving architecture. |
| 2024-05 | arXiv | vAttention: Dynamic Memory Management for Serving LLMs without PagedAttention | [paper](https://arxiv.org/abs/2405.04437) | [code](https://github.com/microsoft/vattention) | ★★★★☆ | Uses CUDA virtual memory to keep KV cache virtually contiguous while allocating physical pages on demand. |
| 2023-12 | NeurIPS 2024 | SGLang: Efficient Execution of Structured Language Model Programs | [paper](https://arxiv.org/abs/2312.07104) | [code](https://github.com/sgl-project/sglang) | ★★★★★ | Important serving/runtime system for structured generation, radix cache, and complex LLM programs. |
| 2024-06 | arXiv | MemServe: Context Caching for Disaggregated LLM Serving with Elastic Memory Pool | [paper](https://arxiv.org/abs/2406.17565) | - | ★★★★☆ | Connects prefix/context caching with a disaggregated memory pool and locality-aware scheduling. |
| 2024-07 | arXiv | Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving | [paper](https://arxiv.org/abs/2407.00079) | [code](https://github.com/kvcache-ai/Mooncake) | ★★★★★ | Production-inspired design that treats KV cache as the central resource for long-context serving. |
| 2024-07 | arXiv | Preble: Efficient Distributed Prompt Scheduling for LLM Serving | [paper](https://arxiv.org/abs/2407.00023) | - | ★★★★☆ | Routes prompts to maximize cross-request prefix sharing in distributed serving. |
| 2025-11 | arXiv | CLO: Efficient LLM Inference System with CPU-Light KVCache Offloading via Algorithm-System Co-Design | [paper](https://arxiv.org/abs/2511.14510) | - | ★★★☆☆ | CPU-light KV offload path for reducing PCIe/CPU overhead in long-context decoding. |
| 2025-10 | arXiv | LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference | [paper](https://arxiv.org/abs/2510.09665) | [code](https://github.com/LMCache/LMCache) | ★★★★☆ | Shared KV cache layer for offloading, reuse, and cross-engine cache transfer. |
| 2026-04 | arXiv | PolyKV: A Shared Asymmetrically-Compressed KV Cache Pool for Multi-Agent LLM Inference | [paper](https://arxiv.org/abs/2604.24971) | - | ★★★☆☆ | Shared compressed KV cache pool for concurrent multi-agent inference. |
| 2026-04 | arXiv | CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration | [paper](https://arxiv.org/abs/2604.25080) | - | ★★★☆☆ | Restores offloaded/compressed KV cache with token-layer-GPU parallelism. |
| 2026-05 | arXiv | Tutti: Making SSD-Backed KV Cache Practical for Long-Context LLM Serving | [paper](https://arxiv.org/abs/2605.03375) | - | ★★★☆☆ | Very recent SSD-backed KV cache design that targets long-context SLO pressure. |

## Scheduling, batching, and goodput

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2023-08 | arXiv | SARATHI: Efficient LLM Inference by Piggybacking Decodes with Chunked Prefills | [paper](https://arxiv.org/abs/2308.16369) | - | ★★★★☆ | Establishes chunked prefill as a practical way to reduce decode stalls. |
| 2024-03 | arXiv | Sarathi-Serve: Tackling Throughput-Latency Tradeoffs in LLM Inference Serving with Chunked Prefills | [paper](https://arxiv.org/abs/2403.02310) | [code](https://github.com/microsoft/sarathi-serve) | ★★★★☆ | Turns chunked prefill into a serving scheduler with explicit latency/throughput trade-offs. |
| 2023-05 | arXiv | Fast Distributed Inference Serving for Large Language Models | [paper](https://arxiv.org/abs/2305.05920) | [code](https://github.com/LLMServe/FastServe) | ★★★★☆ | FastServe introduces preemptive scheduling and memory management for distributed LLM serving. |
| 2023-11 | ISCA 2024 | Splitwise: Efficient Generative LLM Inference Using Phase Splitting | [paper](https://arxiv.org/abs/2311.18677) | - | ★★★★☆ | Early system study of separating prompt processing and token generation across clusters. |
| 2024-01 | arXiv | DeepSpeed-FastGen: High-throughput Text Generation for LLMs via MII and DeepSpeed-Inference | [paper](https://arxiv.org/abs/2401.08671) | [code](https://github.com/microsoft/DeepSpeed) | ★★★★☆ | Introduces Dynamic SplitFuse for composing prompt and generation work. |
| 2024-01 | arXiv | DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving | [paper](https://arxiv.org/abs/2401.09670) | [code](https://github.com/LLMServe/DistServe) | ★★★★☆ | Goodput-oriented prefill/decode disaggregation baseline. |
| 2024-08 | arXiv | NanoFlow: Towards Optimal Large Language Model Serving Throughput | [paper](https://arxiv.org/abs/2408.12757) | - | ★★★★☆ | Operation-level nano-batching and pipeline scheduling for higher device utilization. |
| 2024-08 | arXiv | P/D-Serve: Serving Disaggregated Large Language Model at Scale | [paper](https://arxiv.org/abs/2408.08147) | - | ★★★★☆ | Studies end-to-end prefill/decode disaggregated serving at cluster scale. |
| 2025-01 | ICML 2025 | Efficiently Serving Large Multimodal Models Using EPD Disaggregation | [paper](https://arxiv.org/abs/2501.05460) | [code](https://github.com/vbdi/epdserve) | ★★★★☆ | Extends disaggregation from text LLMs to encode-prefill-decode multimodal serving. |
| 2025-09 | arXiv | Cronus: Efficient LLM Inference on Heterogeneous GPU Clusters via Partially Disaggregated Prefill | [paper](https://arxiv.org/abs/2509.17357) | - | ★★★☆☆ | Heterogeneous-cluster prefill/decode scheduling that avoids rigid full disaggregation. |
| 2026-02 | PPoPP 2026 | Laser: Unlocking Layer-Level Scheduling for Efficient Multi-SLO LLM Serving | [paper](https://ppopp26.sigplan.org/details/PPoPP-2026-papers/3/Laser-Unlocking-Layer-Level-Scheduling-for-Efficient-Multi-SLO-LLM-Serving) | - | ★★★★☆ | Moves beyond iteration-level scheduling to layer-level execution for mixed SLO workloads. |
| 2026-02 | ICML 2026 | Efficient Multi-round LLM Inference over Disaggregated Serving | [paper](https://arxiv.org/abs/2602.14516) | - | ★★★★☆ | AMPD handles interleaved prefill/decode workloads in multi-round agent and RAG serving. |
| 2026-05 | ICML 2026 | THETA: Threshold-Based Exclusive Batching for Memory-Bandwidth-Constrained LLM Inference | [paper](https://rucnyz.github.io/publications/) | - | ★★★☆☆ | Revisits exclusive batching under memory-bandwidth-constrained GPUs. |

## Multi-tenant and serverless serving

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2023-10 | MLSys 2024 | Punica: Multi-Tenant LoRA Serving | [paper](https://arxiv.org/abs/2310.18547) | [code](https://github.com/punica-ai/punica) | ★★★★☆ | Kernel/runtime design for serving many LoRA adapters over one base model. |
| 2023-11 | MLSys 2024 | S-LoRA: Serving Thousands of Concurrent LoRA Adapters | [paper](https://arxiv.org/abs/2311.03285) | [code](https://github.com/S-LoRA/S-LoRA) | ★★★★☆ | Unified paging for adapter weights and KV cache in high-concurrency LoRA serving. |
| 2024-01 | OSDI 2024 | ServerlessLLM: Low-Latency Serverless Inference for Large Language Models | [paper](https://arxiv.org/abs/2401.14351) | [code](https://github.com/ServerlessLLM/ServerlessLLM) | ★★★★☆ | Serverless LLM loading, migration, and locality-aware scheduling. |
| 2025-05 | arXiv | ServerlessLoRA: Minimizing Latency and Cost in Serverless Inference for LoRA-Based LLMs | [paper](https://arxiv.org/abs/2505.14468) | - | ★★★☆☆ | Recent serverless design specialized for LoRA artifact loading and contention. |
| 2025-12 | arXiv | Efficient Multi-Adapter LLM Serving via Cross-Model KV-Cache Reuse with Activated LoRA | [paper](https://arxiv.org/abs/2512.17910) | - | ★★★☆☆ | Extends adapter serving with cross-model KV reuse for LoRA-heavy workloads. |

## Long-context and distributed inference

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2024-01 | arXiv | Infinite-LLM: Efficient LLM Service for Long Context with DistAttention and Distributed KVCache | [paper](https://arxiv.org/abs/2401.02669) | - | ★★★★☆ | Distributes attention and KV cache to push serving toward very long contexts. |
| 2023-10 | arXiv | CacheGen: KV Cache Compression and Streaming for Fast Large Language Model Serving | [paper](https://arxiv.org/abs/2310.07240) | - | ★★★★☆ | Compresses and streams reusable KV cache for lower context-fetch latency. |
| 2023-03 | ICML 2023 | FlexGen: High-throughput Generative Inference of Large Language Models with a Single GPU | [paper](https://arxiv.org/abs/2303.06865) | [code](https://github.com/FMInference/FlexGen) | ★★★★☆ | Classic offloading-oriented inference system for memory-constrained GPUs. |
| 2023-12 | arXiv | PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU | [paper](https://arxiv.org/abs/2312.12456) | [code](https://github.com/SJTU-IPADS/PowerInfer) | ★★★★☆ | Exploits activation locality to make consumer-GPU serving practical. |
| 2024-03 | arXiv | LLM in a Flash: Efficient Large Language Model Inference with Limited Memory | [paper](https://arxiv.org/abs/2312.11514) | - | ★★★☆☆ | Useful reference for flash-storage-aware inference under tight memory. |
| 2025-02 | MLSys 2025 | LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention | [paper](https://arxiv.org/abs/2502.14866) | - | ★★★★☆ | Unified sparse attention serving path for long-sequence prefill and decode. |
| 2025-03 | arXiv | FastCache: Optimizing Multimodal LLM Serving through Lightweight KV-Cache Compression Framework | [paper](https://arxiv.org/abs/2503.08461) | - | ★★★☆☆ | Multimodal-serving KV cache compression and lifecycle management. |
| 2025-06 | arXiv | Parallel CPU-GPU Execution for LLM Inference on Constrained GPUs | [paper](https://arxiv.org/abs/2506.03296) | - | ★★★☆☆ | Recent hybrid scheduling direction for small-GPU deployments. |
| 2025-06 | arXiv | Breaking the Boundaries of Long-Context LLM Inference: Adaptive KV Management on a Single Commodity GPU | [paper](https://arxiv.org/abs/2506.20187) | - | ★★★☆☆ | Hierarchical GPU-CPU-disk KV management for private single-GPU long-context inference. |
| 2026-02 | arXiv | HillInfer: Efficient Long-Context LLM Inference on the Edge with Hierarchical KV Eviction using SmartSSD | [paper](https://arxiv.org/abs/2602.18750) | - | ★★★☆☆ | Edge-oriented SmartSSD-assisted KV eviction and memory hierarchy design. |

## Distributed training systems

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2019-09 | arXiv | Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism | [paper](https://arxiv.org/abs/1909.08053) | [code](https://github.com/NVIDIA/Megatron-LM) | ★★★★★ | Canonical tensor-parallel transformer training system. |
| 2019-10 | SC 2020 | ZeRO: Memory Optimizations Toward Training Trillion Parameter Models | [paper](https://arxiv.org/abs/1910.02054) | [code](https://github.com/microsoft/DeepSpeed) | ★★★★★ | Core optimizer-state and memory-sharding reference. |
| 2019-11 | NeurIPS 2019 | GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism | [paper](https://arxiv.org/abs/1811.06965) | - | ★★★★☆ | Standard pipeline-parallel training reference. |
| 2018-06 | SOSP 2019 | PipeDream: Generalized Pipeline Parallelism for DNN Training | [paper](https://arxiv.org/abs/1806.03377) | [code](https://github.com/msr-fiddle/pipedream) | ★★★★☆ | Explores pipeline scheduling and weight stashing for distributed training. |
| 2021-01 | JMLR 2022 | GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding | [paper](https://arxiv.org/abs/2006.16668) | - | ★★★★☆ | Important precursor for automatic sharding and large sparse models. |
| 2022-07 | OSDI 2022 | Alpa: Automating Inter- and Intra-Operator Parallelism for Distributed Deep Learning | [paper](https://www.usenix.org/conference/osdi22/presentation/zheng-lianmin) | [code](https://github.com/alpa-projects/alpa) | ★★★★☆ | Bridges compiler planning and distributed training execution. |
| 2025-02 | PPoPP 2025 | ATTNChecker: Highly-Optimized Fault Tolerant Attention for Large Language Model Training | [paper](https://www.pnnl.gov/publications/attnchecker-highly-optimized-fault-tolerant-attention-large-language-model-training) | [artifact](https://zenodo.org/records/14503617) | ★★★★☆ | ABFT-style attention protection that reduces checkpoint/restart recovery cost. |
| 2025-02 | PPoPP 2025 | Mario: Near Zero-cost Activation Checkpointing in Pipeline Parallelism | [paper](https://ppopp25.sigplan.org/details/PPoPP-2025-Main-Conference-1/29/Mario-Near-Zero-cost-Activation-Checkpointing-in-Pipeline-Parallelism) | - | ★★★★☆ | Pipeline schedule/search system that overlaps recomputation to reduce activation memory. |
| 2025-02 | PPoPP 2025 | WeiPipe: Weight Pipeline Parallelism for Communication-Effective Long-Context Large Model Training | [paper](https://maruyamaaya.github.io/publication/weipipe/) | - | ★★★★☆ | Weight-passing pipeline parallelism for long-context training communication pressure. |
| 2025-02 | PPoPP 2025 | Harnessing Inter-GPU Shared Memory for Seamless MoE Communication-Computation Fusion | [paper](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1) | - | ★★★★☆ | Fuses MoE expert communication and computation through inter-GPU shared memory. |
| 2025-02 | PPoPP 2025 | COMPSO: Optimizing Gradient Compression for Distributed Training with Second-Order Optimizers | [paper](https://researchwith.stevens.edu/en/publications/compso-optimizing-gradient-compression-for-distributed-training-w/) | - | ★★★☆☆ | Communication compression for second-order optimizer training workloads. |
| 2026-02 | PPoPP 2026 | COCCL: A Collective Communication Library Supporting Easy Integration and Configuration of Customized Compression for Scalable LLM Training | [paper](https://ppopp26.sigplan.org/details/PPoPP-2026-papers/22/COCCL-A-Collective-Communication-Library-Supporting-Easy-Integration-and-Configurati) | - | ★★★★☆ | Compression-aware collective library for 3D-parallel LLM training. |

## Benchmarks and simulation

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2019-11 | arXiv | MLPerf Inference Benchmark | [paper](https://arxiv.org/abs/1911.02549) | [code](https://github.com/mlcommons/inference) | ★★★★☆ | Standard hardware/system benchmark for inference throughput and latency. |
| 2024-05 | arXiv | Vidur: A Large-Scale Simulation Framework for LLM Inference | [paper](https://arxiv.org/abs/2405.05465) | [code](https://github.com/microsoft/vidur) | ★★★☆☆ | Useful simulator for comparing serving policies without full cluster deployments. |
| 2025-06 | HPCA 2025 | Characterizing the Behavior and Impact of KV Caching on Transformer Inferences under Concurrency | [paper](https://grc.iit.edu/publications/ye-2025-characterizing-behavior-f631) | - | ★★★☆☆ | Fine-grained characterization of KV cache behavior under concurrent vLLM serving. |

## Upstream source lists

| Source repo | Scope | Priority | Notes |
|---|---|---|---|
| [xlite-dev/Awesome-LLM-Inference](https://github.com/xlite-dev/Awesome-LLM-Inference) | LLM/VLM inference | P0 | Core entry point for inference acceleration papers. |
| [AmadeusChan/Awesome-LLM-System-Papers](https://github.com/AmadeusChan/Awesome-LLM-System-Papers) | LLM systems | P0 | Good for LLM serving and systems overview. |
| [AmberLJC/LLMSys-PaperList](https://github.com/AmberLJC/LLMSys-PaperList) | LLM systems | P0 | Broad LLMSys tracking list. |
| [InternLM/Awesome-LLM-Training-System](https://github.com/InternLM/Awesome-LLM-Training-System) | Training systems | P0 | Training infrastructure counterpart to inference-serving lists. |
| [lambda7xx/awesome-AI-system](https://github.com/lambda7xx/awesome-AI-system) | AI systems paper-code | P1 | Broad list; filter strongly by paper-first scope. |
| [jeho-lee/Awesome-On-Device-AI](https://github.com/jeho-lee/Awesome-On-Device-AI) | On-device AI systems | P1 | Edge/mobile systems bridge. |
| [iamseonghoon/Awesome-On-Device-AI-Inference](https://github.com/iamseonghoon/Awesome-On-Device-AI-Inference) | On-device inference | P1 | Resource-constrained inference source. |
