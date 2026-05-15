# Efficient Inference Algorithms & Model-System Co-design

## Scope

Algorithm and model-system co-design work that reduces latency, memory, bandwidth, energy, or serving cost. Tables are organized by technique family.

## Attention kernels and decode-time attention

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2019-11 | arXiv | Fast Transformer Decoding: One Write-Head is All You Need | [paper](https://arxiv.org/abs/1911.02150) | - | ★★★★☆ | Multi-query attention reference for reducing KV cache bandwidth. |
| 2023-05 | arXiv | GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints | [paper](https://arxiv.org/abs/2305.13245) | - | ★★★★☆ | Practical middle point between MHA quality and MQA serving efficiency. |
| 2022-05 | NeurIPS 2022 | FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness | [paper](https://arxiv.org/abs/2205.14135) | [code](https://github.com/Dao-AILab/flash-attention) | ★★★★★ | Core IO-aware attention kernel. |
| 2023-07 | ICLR 2024 | FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning | [paper](https://arxiv.org/abs/2307.08691) | [code](https://github.com/Dao-AILab/flash-attention) | ★★★★★ | Production-relevant attention parallelism improvements. |
| 2024-07 | arXiv | FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision | [paper](https://arxiv.org/abs/2407.08608) | [code](https://github.com/Dao-AILab/flash-attention) | ★★★★★ | Hopper-oriented attention kernel with asynchrony and FP8 support. |
| 2024-10 | arXiv | DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads | [paper](https://arxiv.org/abs/2410.10819) | [code](https://github.com/mit-han-lab/duo-attention) | ★★★★☆ | Separates retrieval heads from streaming heads to reduce long-context KV memory and latency. |
| 2025-01 | MLSys 2025 | FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving | [paper](https://arxiv.org/abs/2501.01005) | [code](https://github.com/flashinfer-ai/flashinfer) | ★★★★★ | Flexible attention engine for paged, ragged, quantized, and compressed KV layouts. |
| 2026-02 | PPoPP 2026 | FlashAttention-T: Towards Fully Tensorized Attention by Exploiting Tensor-Vector Parallelism | [paper](https://ppopp26.sigplan.org/details/PPoPP-2026-papers/15/FlashAttention-T-Towards-Fully-Tensorized-Attention-by-Exploiting-Tensor-Vector-Para) | [artifact](https://zenodo.org/records/17673796) | ★★★★☆ | Tensorizes softmax work inside fused attention to reduce underutilized vector intervals. |
| 2026-02 | PPoPP 2026 | MetaAttention: A Unified and Performant Attention Framework Across Hardware Backends | [paper](https://ppopp26.sigplan.org/details/PPoPP-2026-papers/34/MetaAttention-A-Unified-and-Performant-Attention-Framework-Across-Hardware-Backends) | - | ★★★★☆ | Generates performant implementations for attention variants across hardware backends. |
| 2026-04 | arXiv | Flux Attention: Context-Aware Hybrid Attention for Efficient LLMs Inference | [paper](https://arxiv.org/abs/2604.07394) | [code](https://github.com/qqtang-code/FluxAttention) | ★★★☆☆ | Recent layer-level routing between full and sparse attention for long-context speedups. |

## KV cache eviction, retention, and compression

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2023-06 | NeurIPS 2023 | H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | [paper](https://arxiv.org/abs/2306.14048) | [code](https://github.com/FMInference/H2O) | ★★★★★ | Heavy-hitter KV retention baseline. |
| 2023-09 | ICLR 2024 | Efficient Streaming Language Models with Attention Sinks | [paper](https://arxiv.org/abs/2309.17453) | [code](https://github.com/mit-han-lab/streaming-llm) | ★★★★★ | Explains attention sinks and enables streaming contexts with bounded KV. |
| 2024-04 | NeurIPS 2024 | SnapKV: LLM Knows What You are Looking for Before Generation | [paper](https://arxiv.org/abs/2404.14469) | [code](https://github.com/FasterDecoding/SnapKV) | ★★★★☆ | Compresses prompt KV based on attention observations before generation. |
| 2024-05 | NeurIPS 2024 | MiniCache: KV Cache Compression in Depth Dimension for Large Language Models | [paper](https://arxiv.org/abs/2405.14366) | - | ★★★★☆ | Exploits cross-layer KV similarity instead of only token/head sparsity. |
| 2024-05 | arXiv | PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling | [paper](https://arxiv.org/abs/2406.02069) | [code](https://github.com/Zefan-Cai/PyramidKV) | ★★★★☆ | Layer-wise KV budget allocation for long-context inference. |
| 2024-06 | arXiv | Quest: Query-Aware Sparsity for Efficient Long-Context LLM Inference | [paper](https://arxiv.org/abs/2406.10774) | - | ★★★★☆ | Query-aware page selection for reducing long-context attention bandwidth. |
| 2024-07 | NeurIPS 2025 | Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference | [paper](https://arxiv.org/abs/2407.11550) | [code](https://github.com/FFY0/AdaKV) | ★★★★☆ | Head-wise adaptive KV budget allocation that composes with eviction methods. |
| 2024-07 | ICLR 2025 | RazorAttention: Efficient KV Cache Compression Through Retrieval Heads | [paper](https://arxiv.org/abs/2407.15891) | - | ★★★★☆ | Separates retrieval-head behavior from full-cache retention. |
| 2024-10 | ICML 2025 | ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference | [paper](https://arxiv.org/abs/2410.21465) | [code](https://github.com/ByteDance-Seed/ShadowKV) | ★★★★☆ | Low-rank key cache plus value offload for larger long-context serving batches. |
| 2025-02 | arXiv | Can LLMs Maintain Fundamental Abilities under KV Cache Compression? | [paper](https://arxiv.org/abs/2502.01941) | - | ★★★☆☆ | Useful cautionary analysis plus ShotKV method. |
| 2025-03 | arXiv | Rethinking Key-Value Cache Compression Techniques for Large Language Model Serving | [paper](https://arxiv.org/abs/2503.24000) | - | ★★★★☆ | Systems-oriented warning that compression can hurt end-to-end serving latency. |
| 2025-03 | arXiv | WindowKV: Task-Adaptive Group-Wise KV Cache Window Selection for Efficient LLM Inference | [paper](https://arxiv.org/abs/2503.17922) | - | ★★★☆☆ | Selects layer/head window sizes based on task behavior for bounded KV retention. |
| 2025-04 | arXiv | MILLION: Mastering Long-Context LLM Inference Via Outlier-Immunized KV Product Quantization | [paper](https://arxiv.org/abs/2504.03661) | - | ★★★☆☆ | Product-quantized KV cache plus GPU-oriented inference path for very long contexts. |
| 2025-05 | arXiv | KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction | [paper](https://arxiv.org/abs/2505.23416) | [code](https://github.com/snu-mllab/KVzip) | ★★★☆☆ | Recent query-agnostic compression direction. |
| 2025-02 | ICML 2025 | RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression | [paper](https://proceedings.mlr.press/v267/behnam25a.html) | [code](https://github.com/NVlabs/RocketKV) | ★★★★☆ | Two-stage KV pruning/compression pipeline for long-context inference. |
| 2025-06 | arXiv | Inference-Time Hyper-Scaling with KV Cache Compression | [paper](https://arxiv.org/abs/2506.05345) | - | ★★★☆☆ | Dynamic memory sparsification to trade KV memory for more inference-time sampling. |
| 2025-06 | arXiv | Efficient Long-Context LLM Inference via KV Cache Clustering | [paper](https://arxiv.org/abs/2506.11418) | - | ★★★☆☆ | Clusters KV entries to reduce long-context memory while preserving retrieval behavior. |
| 2025-07 | arXiv | HCAttention: Extreme KV Cache Compression via Heterogeneous Attention Computing for LLMs | [paper](https://arxiv.org/abs/2507.19823) | - | ★★★☆☆ | Uses heterogeneous attention behavior to keep only a small fraction of full KV. |
| 2025-09 | Findings EMNLP 2025 | EvolKV: Evolutionary KV Cache Compression for LLM Inference | [paper](https://arxiv.org/abs/2509.08315) | - | ★★★☆☆ | Evolutionary search over cache policies for memory/quality trade-offs. |
| 2025-09 | arXiv | KVCompose: Efficient Structured KV Cache Compression with Composite Tokens | [paper](https://arxiv.org/abs/2509.05165) | - | ★★★☆☆ | Structured composite-token compression compatible with standard decoding pipelines. |
| 2026-03 | arXiv | ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs | [paper](https://arxiv.org/abs/2603.08727) | [code](https://github.com/Large-scale-Sustainable-Computing-LSC/ARKV) | ★★★☆☆ | Tri-state retain/quantize/evict cache policy for tight memory budgets. |
| 2026-04 | arXiv | CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration | [paper](https://arxiv.org/abs/2604.25080) | - | ★★★☆☆ | Algorithm/system method for overlapping KV restoration over tokens, layers, and GPUs. |

## KV cache quantization

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2024-02 | ICML 2024 | KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache | [paper](https://arxiv.org/abs/2402.02750) | [code](https://github.com/jy-yuan/KIVI) | ★★★★★ | Core 2-bit KV quantization method. |
| 2024-01 | arXiv | KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization | [paper](https://arxiv.org/abs/2401.18079) | [code](https://github.com/SqueezeAILab/KVQuant) | ★★★★☆ | Sub-4-bit KV cache quantization for very long contexts. |
| 2025-03 | arXiv | Q-Filters: Leveraging QK Geometry for Efficient KV Cache Compression | [paper](https://arxiv.org/abs/2503.02812) | - | ★★★☆☆ | Uses QK geometry as a selection/filtering signal for compressed KV. |
| 2025-04 | ICLR 2026 | TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate | [paper](https://arxiv.org/abs/2504.19874) | - | ★★★★☆ | Online vector quantization used for near-lossless low-bit KV cache and vector search. |
| 2025-07 | arXiv | CommVQ: Commutative Vector Quantization for KV Cache Compression | [paper](https://machinelearning.apple.com/research/commutative-vector-quantization) | - | ★★★☆☆ | Apple work on vector quantization for long-context KV cache memory reduction. |
| 2025-10 | arXiv | VecInfer: Efficient LLM Inference with Low-Bit KV Cache via Outlier-Suppressed Vector Quantization | [paper](https://arxiv.org/abs/2510.06175) | - | ★★★☆☆ | Outlier-suppressed vector quantization for low-bit KV cache serving. |
| 2025-11 | arXiv | KV Cache Transform Coding for Compact Storage in LLM Inference | [paper](https://arxiv.org/abs/2511.01815) | - | ★★★☆☆ | Applies transform coding ideas to compact KV storage. |
| 2026-02 | PPoPP 2026 | JanusQuant: Accurate and Efficient 2-bit KV Cache Quantization for Long-Context Inference | [paper](https://ppopp26.sigplan.org/details/PPoPP-2026-papers/18/JanusQuant-Accurate-and-Efficient-2-bit-KV-Cache-Quantization-for-Long-context-Infer) | - | ★★★★☆ | Recent 2-bit KV quantization system from PPoPP's mixed-precision track. |

## Speculative and parallel decoding

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2022-11 | ICML 2023 | Fast Inference from Transformers via Speculative Decoding | [paper](https://arxiv.org/abs/2211.17192) | - | ★★★★★ | Foundational draft-and-verify speculative decoding paper. |
| 2023-02 | arXiv | Accelerating Large Language Model Decoding with Speculative Sampling | [paper](https://arxiv.org/abs/2302.01318) | - | ★★★★★ | Parallel formulation of speculative sampling for LLM decoding. |
| 2023-05 | arXiv | SpecInfer: Accelerating Generative Large Language Model Serving with Tree-based Speculative Inference and Verification | [paper](https://arxiv.org/abs/2305.09781) | - | ★★★★☆ | Tree-structured speculation for serving workloads. |
| 2023-11 | arXiv | Lookahead Decoding: Accelerating Autoregressive Inference of Large Language Models | [paper](https://arxiv.org/abs/2312.12728) | [code](https://github.com/hao-ai-lab/LookaheadDecoding) | ★★★★☆ | Draft-free multi-token prediction via n-gram candidate verification. |
| 2024-01 | arXiv | Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads | [paper](https://arxiv.org/abs/2401.10774) | [code](https://github.com/FasterDecoding/Medusa) | ★★★★☆ | Multi-head decoding framework with accessible implementation. |
| 2024-01 | arXiv | EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty | [paper](https://arxiv.org/abs/2401.15077) | [code](https://github.com/SafeAILab/EAGLE) | ★★★★☆ | Feature-level draft model that became a practical speculative decoding baseline. |
| 2024-02 | NeurIPS 2024 | Sequoia: Scalable and Robust Speculative Decoding | [paper](https://arxiv.org/abs/2402.12374) | [code](https://github.com/Infini-AI-Lab/Sequoia) | ★★★★☆ | Hardware-aware tree construction for robust speculative decoding. |
| 2024-02 | arXiv | Hydra: Sequentially-Dependent Draft Heads for Medusa Decoding | [paper](https://arxiv.org/abs/2402.05109) | [code](https://github.com/zankner/Hydra) | ★★★☆☆ | Improves Medusa-style draft heads by making proposed tokens sequentially dependent. |
| 2024-04 | ACL 2024 | LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding | [paper](https://arxiv.org/abs/2404.16710) | [code](https://github.com/facebookresearch/LayerSkip) | ★★★★☆ | Early-exit training recipe plus self-speculation without an external draft model. |
| 2024-06 | NeurIPS 2024 | SpecExec: Massively Parallel Speculative Decoding for Interactive LLM Inference on Consumer Devices | [paper](https://arxiv.org/abs/2406.02532) | [code](https://github.com/yandex-research/specexec) | ★★★☆☆ | Consumer-device speculative execution path for offloaded large models. |
| 2025-03 | NeurIPS 2025 | EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test | [paper](https://arxiv.org/abs/2503.01840) | [code](https://github.com/SafeAILab/EAGLE) | ★★★★☆ | Recent EAGLE variant focused on scaling speculative decoding quality. |
| 2025-06 | ICML 2025 | LongSpec: Long-Context Lossless Speculative Decoding with Efficient Drafting and Verification | [paper](https://icml.cc/virtual/2025/51846) | - | ★★★★☆ | Speculative decoding design for long-context agents with compact draft KV. |
| 2026-01 | ICLR 2026 Oral | Overcoming Joint Intractability with Lossless Hierarchical Speculative Decoding | [paper](https://openreview.net/forum?id=LaVrNaBNwM) | - | ★★★★☆ | Hierarchical verification for lossless speculative decoding. |
| 2026-02 | ICML 2026 | DFlash: Block Diffusion for Flash Speculative Decoding | [paper](https://arxiv.org/abs/2602.06036) | - | ★★★★☆ | Uses block-diffusion drafting to increase speculative decoding parallelism. |
| 2026-02 | HPCA 2026 | Adaptive Draft Sequence Length: Enhancing Speculative Decoding Throughput on PIM-Enabled Systems | [paper](https://2026.hpca-conf.org/details/hpca-2026-main-conference/112/Adaptive-Draft-Sequence-Length-Enhancing-Speculative-Decoding-Throughput-on-PIM-Enab) | - | ★★★☆☆ | Hardware-aware adaptive draft lengths for xPU+PIM speculative decoding systems. |
| 2026-05 | arXiv | Component-Aware Self-Speculative Decoding in Hybrid Language Models | [paper](https://arxiv.org/abs/2605.01106) | - | ★★★☆☆ | Early 2026 look at self-speculation for hybrid SSM/attention architectures. |

## Weight and activation quantization

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2022-10 | ICLR 2023 | GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers | [paper](https://arxiv.org/abs/2210.17323) | [code](https://github.com/IST-DASLab/gptq) | ★★★★★ | Classic post-training quantization baseline. |
| 2022-11 | ICML 2023 | SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models | [paper](https://arxiv.org/abs/2211.10438) | [code](https://github.com/mit-han-lab/smoothquant) | ★★★★★ | Practical W8A8 quantization method. |
| 2023-03 | arXiv | SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression | [paper](https://arxiv.org/abs/2306.03078) | [code](https://github.com/Vahe1994/SpQR) | ★★★★☆ | Sparse outlier-aware quantization for near-lossless compression. |
| 2023-06 | MLSys 2024 | AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration | [paper](https://arxiv.org/abs/2306.00978) | [code](https://github.com/mit-han-lab/llm-awq) | ★★★★★ | Widely adopted weight-only quantization baseline. |
| 2023-08 | ICLR 2024 | OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models | [paper](https://arxiv.org/abs/2308.13137) | [code](https://github.com/OpenGVLab/OmniQuant) | ★★★★☆ | Calibration-heavy PTQ method with strong low-bit results. |
| 2024-02 | ICML 2024 | QuIP#: Even Better LLM Quantization with Hadamard Incoherence and Lattice Codebooks | [paper](https://arxiv.org/abs/2402.04396) | [code](https://github.com/Cornell-RelaxML/quip-sharp) | ★★★★☆ | Extreme weight-only quantization via incoherence processing and lattice codebooks. |
| 2024-02 | arXiv | The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits | [paper](https://arxiv.org/abs/2402.17764) | [code](https://github.com/microsoft/BitNet) | ★★★★☆ | Native ternary-weight LLM line with direct hardware/system implications. |
| 2024-04 | NeurIPS 2024 | QuaRot: Outlier-Free 4-Bit Inference in Rotated LLMs | [paper](https://arxiv.org/abs/2404.00456) | [code](https://github.com/spcl/QuaRot) | ★★★★☆ | Uses rotations to reduce outliers for efficient low-bit inference. |
| 2024-05 | ICLR 2025 | SpinQuant: LLM Quantization with Learned Rotations | [paper](https://arxiv.org/abs/2405.16406) | [code](https://github.com/facebookresearch/SpinQuant) | ★★★★☆ | Learns rotation matrices for W/A/KV low-bit quantization. |
| 2025-02 | PPoPP 2025 | MARLIN: Mixed-Precision Auto-Regressive Parallel Inference on Large Language Models | [paper](https://research-explorer.ista.ac.at/record/19877) | - | ★★★★☆ | Mixed-precision autoregressive inference kernel/system for quantized LLM serving. |
| 2026-02 | PPoPP 2026 | RoMeo: Mitigating Dual-dimensional Outliers with Rotated Mixed Precision Quantization | [paper](https://ppopp26.sigplan.org/details/PPoPP-2026-papers/9/RoMeo-Mitigating-Dual-dimensional-Outliers-with-Rotated-Mixed-Precision-Quantization) | [code](https://github.com/thu-pacman/RoMeo) | ★★★★☆ | Rotation-based mixed precision quantization with token- and channel-wise outlier handling. |
| 2026-02 | PPoPP 2026 | High-Throughput Non-Uniformly Quantized 3-bit LLM Inference | [paper](https://ppopp26.sigplan.org/details/PPoPP-2026-papers/13/High-Throughput-Non-Uniformly-Quantized-3-bit-LLM-Inference) | - | ★★★★☆ | Quantix converts 3-bit non-uniform weight compression into batched inference speedups. |
| 2026-05 | arXiv | ADMM-Q: An Improved Hessian-based Weight Quantizer for Post-Training Quantization of Large Language Models | [paper](https://arxiv.org/abs/2605.11222) | - | ★★★☆☆ | Recent Hessian-based quantizer designed to compose with GPTQ, rotations, and scaling. |

## Pruning, sparsity, and compression

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2023-01 | ICML 2023 | SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot | [paper](https://arxiv.org/abs/2301.00774) | [code](https://github.com/IST-DASLab/sparsegpt) | ★★★★☆ | One-shot pruning baseline for large LMs. |
| 2023-06 | arXiv | Wanda: Pruning by Weights and Activations | [paper](https://arxiv.org/abs/2306.11695) | [code](https://github.com/locuslab/wanda) | ★★★★☆ | Simple pruning metric with strong LLM results. |
| 2023-05 | NeurIPS 2023 | LLM-Pruner: On the Structural Pruning of Large Language Models | [paper](https://arxiv.org/abs/2305.11627) | [code](https://github.com/horseee/LLM-Pruner) | ★★★☆☆ | Structured pruning framework for LLMs. |
| 2023-10 | ICLR 2024 | Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning | [paper](https://arxiv.org/abs/2310.06694) | [code](https://github.com/princeton-nlp/LLM-Shearing) | ★★★★☆ | Targeted structured pruning plus continued training to obtain smaller LLMs cheaply. |
| 2024-01 | ICLR 2024 | SliceGPT: Compress Large Language Models by Deleting Rows and Columns | [paper](https://arxiv.org/abs/2401.15024) | [code](https://github.com/microsoft/TransformerCompression) | ★★★☆☆ | Structured compression using computational invariance. |
| 2024-03 | ACL 2025 Findings | ShortGPT: Layers in Large Language Models are More Redundant Than You Expect | [paper](https://arxiv.org/abs/2403.03853) | [code](https://github.com/icip-cas/ShortGPT) | ★★★☆☆ | Layer-removal pruning baseline driven by block influence. |

## MoE inference and sparse expert systems

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2020-06 | arXiv | GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding | [paper](https://arxiv.org/abs/2006.16668) | - | ★★★★☆ | Sparse expert scaling and automatic sharding reference. |
| 2021-01 | JMLR 2022 | Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity | [paper](https://arxiv.org/abs/2101.03961) | - | ★★★★☆ | Widely cited simple MoE architecture. |
| 2022-06 | SC 2022 | Tutel: Adaptive Mixture-of-Experts at Scale | [paper](https://arxiv.org/abs/2206.03382) | [code](https://github.com/microsoft/tutel) | ★★★★☆ | Systems runtime for large-scale MoE training and serving. |
| 2022-11 | MLSys 2023 | MegaBlocks: Efficient Sparse Training with Mixture-of-Experts | [paper](https://arxiv.org/abs/2211.15841) | [code](https://github.com/stanford-futuredata/megablocks) | ★★★★☆ | Block-sparse expert computation with systems impact. |
| 2024-01 | arXiv | Mixtral of Experts | [paper](https://arxiv.org/abs/2401.04088) | [code](https://github.com/mistralai/mistral-src) | ★★★☆☆ | Important open MoE model reference for inference-system workloads. |

## Long-context and efficient architectures

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2020-04 | arXiv | Longformer: The Long-Document Transformer | [paper](https://arxiv.org/abs/2004.05150) | [code](https://github.com/allenai/longformer) | ★★★☆☆ | Early sparse-attention long-context baseline. |
| 2020-07 | NeurIPS 2020 | Big Bird: Transformers for Longer Sequences | [paper](https://arxiv.org/abs/2007.14062) | [code](https://github.com/google-research/bigbird) | ★★★☆☆ | Sparse attention pattern with theoretical support. |
| 2023-02 | ICML 2023 | Hyena Hierarchy: Towards Larger Convolutional Language Models | [paper](https://arxiv.org/abs/2302.10866) | [code](https://github.com/HazyResearch/safari) | ★★★☆☆ | Long convolutional architecture line for sub-quadratic sequence modeling. |
| 2023-07 | arXiv | Retentive Network: A Successor to Transformer for Large Language Models | [paper](https://arxiv.org/abs/2307.08621) | [code](https://github.com/microsoft/unilm) | ★★★☆☆ | Retention mechanism with recurrent-style inference and parallel training. |
| 2023-12 | arXiv | Mamba: Linear-Time Sequence Modeling with Selective State Spaces | [paper](https://arxiv.org/abs/2312.00752) | [code](https://github.com/state-spaces/mamba) | ★★★★☆ | KV-free sequence architecture with major inference implications. |
| 2024-02 | ICLR 2024 | Ring Attention with Blockwise Transformers for Near-Infinite Context | [paper](https://arxiv.org/abs/2310.01889) | [code](https://github.com/lucidrains/ring-attention-pytorch) | ★★★☆☆ | Distributed attention pattern for very long contexts. |
| 2024-02 | arXiv | Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models | [paper](https://arxiv.org/abs/2402.19427) | - | ★★★☆☆ | Hybrid recurrent/local-attention architecture with inference-throughput motivation. |
| 2024-03 | arXiv | Jamba: A Hybrid Transformer-Mamba Language Model | [paper](https://arxiv.org/abs/2403.19887) | - | ★★★★☆ | Production-scale hybrid Transformer-Mamba-MoE model with long-context efficiency. |
| 2023-09 | ICLR 2024 | YaRN: Efficient Context Window Extension of Large Language Models | [paper](https://arxiv.org/abs/2309.00071) | [code](https://github.com/jquesnelle/yarn) | ★★★☆☆ | Practical RoPE scaling technique for long-context adaptation. |
| 2024-04 | arXiv | Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention | [paper](https://arxiv.org/abs/2404.07143) | - | ★★★☆☆ | Memory-style attention mechanism for long-context modeling. |

## Efficient reasoning and test-time compute

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2024-07 | arXiv | Large Language Monkeys: Scaling Inference Compute with Repeated Sampling | [paper](https://arxiv.org/abs/2407.21787) | - | ★★★★☆ | Shows simple repeated sampling as a strong test-time compute baseline. |
| 2025-03 | arXiv | Efficient Inference for Large Reasoning Models: A Survey | [paper](https://arxiv.org/abs/2503.23077) | - | ★★★☆☆ | Recent map of efficient inference methods for reasoning models. |
| 2025-06 | arXiv | Cost-Efficient Serving of LLM Agents via Test-Time Plan Caching | [paper](https://arxiv.org/abs/2506.14852) | - | ★★★☆☆ | Bridges agent serving cost with reusable test-time plans. |

## Upstream source lists

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
