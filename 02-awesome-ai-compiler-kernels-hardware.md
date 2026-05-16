# Compiler, Kernels & Hardware-aware Optimization

<a id="top"></a>

## Contents

- [Tensor compilers and graph runtimes](#tensor-compilers-and-graph-runtimes)
- [Auto-scheduling and auto-tuning](#auto-scheduling-and-auto-tuning)
- [Kernel DSLs and attention engines](#kernel-dsls-and-attention-engines)
- [Hardware-aware LLM acceleration](#hardware-aware-llm-acceleration)
- [LLM-driven kernel generation](#llm-driven-kernel-generation)
- [ML for compilers and program optimization](#ml-for-compilers-and-program-optimization)
- [Upstream source lists](#upstream-source-lists)

## Scope

Compiler, kernel, auto-tuning, and hardware-aware optimization work for AI systems. Tables are organized by compiler/kernel sub-direction; code availability is represented only by the `Code` column.

## Tensor compilers and graph runtimes

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2018-10 | OSDI 2018 | TVM: An Automated End-to-End Optimizing Compiler for Deep Learning | [paper](https://www.usenix.org/conference/osdi18/presentation/chen) | [code](https://github.com/apache/tvm) ![](https://img.shields.io/github/stars/apache/tvm.svg?style=social) | ★★★★★ | Foundational end-to-end tensor compiler and runtime. |
| 2018-05 | OSDI 2018 | Learning to Optimize Tensor Programs | [paper](https://arxiv.org/abs/1805.08166) | [code](https://github.com/apache/tvm) ![](https://img.shields.io/github/stars/apache/tvm.svg?style=social) | ★★★★☆ | AutoTVM reference for learned cost models and template-based tuning. |
| 2019-10 | SOSP 2019 | TASO: Optimizing Deep Learning Computation with Automatic Generation of Graph Substitutions | [paper](https://web.stanford.edu/class/cs245/readings/taso.pdf) | [code](https://github.com/jiazhihao/TASO) ![](https://img.shields.io/github/stars/jiazhihao/TASO.svg?style=social) | ★★★★☆ | Automates graph substitutions for DNN computation graphs. |
| 2021-01 | POPL 2021 | Equality Saturation for Tensor Graph Superoptimization | [paper](https://arxiv.org/abs/2101.01332) | [code](https://github.com/uwplse/tensat) ![](https://img.shields.io/github/stars/uwplse/tensat.svg?style=social) | ★★★★☆ | Applies equality saturation to tensor graph optimization. |
| 2020-02 | arXiv | MLIR: Scaling Compiler Infrastructure for Domain Specific Computation | [paper](https://arxiv.org/abs/2002.11054) | [code](https://github.com/llvm/llvm-project/tree/main/mlir) ![](https://img.shields.io/github/stars/llvm/llvm-project.svg?style=social) | ★★★★☆ | Important compiler infrastructure layer for ML and accelerator dialects. |
| 2022-10 | ASPLOS 2023 | Hidet: Task-Mapping Programming Paradigm for Deep Learning Tensor Programs | [paper](https://arxiv.org/abs/2210.09603) | [code](https://github.com/hidet-org/hidet) ![](https://img.shields.io/github/stars/hidet-org/hidet.svg?style=social) | ★★★★☆ | Embeds scheduling into tensor programs using task mappings. |

## Auto-scheduling and auto-tuning

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2020-11 | OSDI 2020 | Ansor: Generating High-Performance Tensor Programs for Deep Learning | [paper](https://www.usenix.org/conference/osdi20/presentation/zheng) | [code](https://github.com/apache/tvm) ![](https://img.shields.io/github/stars/apache/tvm.svg?style=social) | ★★★★★ | Core auto-scheduler for tensor program generation. |
| 2022-08 | MLSys 2022 | DietCode: Automatic Optimization for Dynamic Tensor Programs | [paper](https://assets.amazon.science/14/33/43345d8142d8936ec591f5600aa5/dietcode-automatic-optimization-for-dynamic-tensor-programs.pdf) | [code](https://github.com/UofT-EcoSystem/DietCode) ![](https://img.shields.io/github/stars/UofT-EcoSystem/DietCode.svg?style=social) | ★★★★☆ | Extends tensor-program optimization to dynamic shapes. |
| 2022-07 | OSDI 2022 | ROLLER: Fast and Efficient Tensor Compilation for Deep Learning | [paper](https://www.usenix.org/conference/osdi22/presentation/zhu) | [code](https://github.com/microsoft/nnfusion) ![](https://img.shields.io/github/stars/microsoft/nnfusion.svg?style=social) | ★★★★☆ | Shape-aware tile construction for fast tensor-kernel compilation. |
| 2022-07 | arXiv | TensorIR: An Abstraction for Automatic Tensorized Program Optimization | [paper](https://arxiv.org/abs/2207.04296) | [code](https://github.com/apache/tvm) ![](https://img.shields.io/github/stars/apache/tvm.svg?style=social) | ★★★★☆ | TVM TensorIR reference for tensorized scheduling and lowering. |
| 2023-07 | OSDI 2023 | Welder: Scheduling Deep Learning Memory Access via Tile-graph | [paper](https://www.usenix.org/conference/osdi23/presentation/shi) | - | ★★★★☆ | Optimizes inter- and intra-operator memory access with a tile-graph abstraction. |
| 2024-07 | OSDI 2024 | Ladder: Enabling Efficient Low-Precision Deep Learning Computing through Hardware-aware Tensor Transformation | [paper](https://www.usenix.org/system/files/osdi24-wang-lei.pdf) | [code](https://github.com/tile-ai/Ladder) ![](https://img.shields.io/github/stars/tile-ai/Ladder.svg?style=social) | ★★★★☆ | Hardware-aware tensor transformations for low-precision computation. |
| 2025-02 | PPoPP 2025 | FlashTensor: Optimizing Tensor Programs by Leveraging Fine-grained Tensor Property | [paper](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1) | - | ★★★☆☆ | Tensor-program optimizer that exploits fine-grained tensor properties. |

## Kernel DSLs and attention engines

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2019-06 | MAPL 2019 | Triton: An Intermediate Language and Compiler for Tiled Neural Network Computations | [paper](https://research.ibm.com/publications/triton-an-intermediate-language-and-compiler-for-tiled-neural-network-computations) | [code](https://github.com/triton-lang/triton) ![](https://img.shields.io/github/stars/triton-lang/triton.svg?style=social) | ★★★★★ | Practical GPU kernel DSL behind many modern LLM kernels. |
| 2025-01 | MLSys 2025 | FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving | [paper](https://arxiv.org/abs/2501.01005) | [code](https://github.com/flashinfer-ai/flashinfer) ![](https://img.shields.io/github/stars/flashinfer-ai/flashinfer.svg?style=social) | ★★★★★ | Kernel library and JIT engine for attention variants used by LLM serving systems. |
| 2025-04 | ICLR 2026 | TileLang: A Composable Tiled Programming Model for AI Systems | [paper](https://arxiv.org/abs/2504.17577) | [code](https://github.com/tile-ai/tilelang) ![](https://img.shields.io/github/stars/tile-ai/tilelang.svg?style=social) | ★★★★☆ | New tiled programming model aimed at productive high-performance AI kernels. |
| 2025-04 | arXiv | Tilus: A Tile-Level GPU Kernel Programming Language | [paper](https://arxiv.org/abs/2504.12984) | [code](https://github.com/NVIDIA/tilus) ![](https://img.shields.io/github/stars/NVIDIA/tilus.svg?style=social) | ★★★★☆ | NVIDIA tile-level kernel language with explicit control over shared memory and registers. |
| 2024-12 | arXiv | MixLLM: LLM Quantization with Global Mixed-precision between Output-features and Highly-efficient System Design | [paper](https://arxiv.org/abs/2412.14590) | [code](https://github.com/microsoft/MixLLM) ![](https://img.shields.io/github/stars/microsoft/MixLLM.svg?style=social) | ★★★☆☆ | Mixed-precision quantized inference with a system-oriented kernel design. |
| 2026-02 | PPoPP 2026 | FlashAttention-T: Towards Fully Tensorized Attention by Exploiting Tensor-Vector Parallelism | [paper](https://ppopp26.sigplan.org/details/PPoPP-2026-papers/15/FlashAttention-T-Towards-Fully-Tensorized-Attention-by-Exploiting-Tensor-Vector-Para) | [artifact](https://zenodo.org/records/17673796) | ★★★★☆ | Tensorizes softmax primitives to reduce vector intervals in fused attention kernels. |
| 2026-02 | PPoPP 2026 | Accelerating Sparse Transformer Inference on GPU | [paper](https://ppopp26.sigplan.org/details/PPoPP-2026-papers/24/Accelerating-Sparse-Transformer-Inference-on-GPU) | - | ★★★★☆ | STOF optimizes sparse Transformer MHA and operator fusion on GPUs. |
| 2026-02 | PPoPP 2026 | MetaAttention: A Unified and Performant Attention Framework Across Hardware Backends | [paper](https://ppopp26.sigplan.org/details/PPoPP-2026-papers/34/MetaAttention-A-Unified-and-Performant-Attention-Framework-Across-Hardware-Backends) | - | ★★★★☆ | Cross-backend attention framework with search over tiling and parallelism. |

## Hardware-aware LLM acceleration

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2025-10 | arXiv | SPAD: Specialized Prefill and Decode Hardware for Disaggregated LLM Inference | [paper](https://arxiv.org/abs/2510.08544) | - | ★★★★☆ | Specialized prefill/decode chip design motivated by phase-disaggregated serving. |
| 2026-02 | HPCA 2026 | PIMphony: Overcoming Bandwidth and Capacity Inefficiency in PIM-based Long-Context LLM Inference System | [paper](https://2026.hpca-conf.org/details/hpca-2026-main-conference/40/PIMphony-Overcoming-Bandwidth-and-Capacity-Inefficiency-in-PIM-based-Long-Context-LL) | - | ★★★★☆ | PIM orchestrator for channel utilization, command scheduling, and dynamic KV memory management. |
| 2026-02 | HPCA 2026 | Adaptive Draft Sequence Length: Enhancing Speculative Decoding Throughput on PIM-Enabled Systems | [paper](https://2026.hpca-conf.org/details/hpca-2026-main-conference/112/Adaptive-Draft-Sequence-Length-Enhancing-Speculative-Decoding-Throughput-on-PIM-Enab) | - | ★★★☆☆ | SADDLE adapts draft length and scheduling for speculative decoding on xPU+PIM systems. |
| 2026-02 | HPCA 2026 | LEGO: Supporting LLM-enhanced Games with One Gaming GPU | [paper](https://2026.hpca-conf.org/details/hpca-2026-main-conference/6/LEGO-Supporting-LLM-enhanced-Games-with-One-Gaming-GPU) | - | ★★★☆☆ | Co-schedules LLM inference with rendering on a single gaming GPU. |
| 2026-04 | arXiv | AQPIM: Breaking the PIM Capacity Wall for LLMs with In-Memory Activation Quantization | [paper](https://arxiv.org/abs/2604.18137) | - | ★★★★☆ | PIM-aware activation quantization for long-context attention and KV capacity limits. |
| 2026-04 | arXiv | Salca: A Sparsity-Aware Hardware Accelerator for Efficient Long-Context Attention Decoding | [paper](https://arxiv.org/abs/2604.24820) | - | ★★★☆☆ | Sparse attention hardware co-design for long-context LLM decoding. |

## LLM-driven kernel generation

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2025-02 | arXiv | KernelBench: Can LLMs Write Efficient GPU Kernels? | [paper](https://arxiv.org/abs/2502.10517) | [code](https://github.com/ScalingIntelligence/KernelBench) ![](https://img.shields.io/github/stars/ScalingIntelligence/KernelBench.svg?style=social) | ★★★★★ | Central benchmark for LLM-generated GPU kernel correctness and speed. |
| 2025-02 | arXiv | TritonBench: Benchmarking Large Language Model Capabilities for Generating Triton Operators | [paper](https://arxiv.org/abs/2502.14752) | - | ★★★★☆ | Focuses evaluation on Triton operator generation rather than generic CUDA. |
| 2025-06 | arXiv | CUDA-LLM: LLMs Can Write Efficient CUDA Kernels | [paper](https://arxiv.org/abs/2506.09092) | - | ★★★☆☆ | Recent iterative refinement direction for functional and efficient CUDA generation. |
| 2025-06 | arXiv | GPU Kernel Scientist: An LLM-Driven Framework for Iterative Kernel Optimization | [paper](https://arxiv.org/abs/2506.20807) | - | ★★★☆☆ | Agentic loop for profiling and optimizing accelerator kernels. |
| 2025-07 | arXiv | MultiKernelBench: A Multi-Platform Benchmark for Kernel Generation | [paper](https://arxiv.org/abs/2507.17773) | - | ★★★☆☆ | Extends kernel-generation evaluation across platforms and kernel categories. |
| 2025-09 | arXiv | Astra: A Multi-Agent System for GPU Kernel Performance Optimization | [paper](https://arxiv.org/abs/2509.07506) | - | ★★★☆☆ | Multi-agent kernel optimization workflow with profiling and testing loops. |
| 2026-04 | arXiv | Prism: Symbolic Superoptimization of Tensor Programs | [paper](https://arxiv.org/abs/2604.15272) | - | ★★★☆☆ | Very recent symbolic superoptimization direction for tensor programs. |

## ML for compilers and program optimization

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2017-01 | CGO 2017 | DeepTune: Learning Optimization Heuristics for Code | [paper](https://arxiv.org/abs/1701.05950) | [code](https://github.com/ChrisCummins/paper-end2end-dl) ![](https://img.shields.io/github/stars/ChrisCummins/paper-end2end-dl.svg?style=social) | ★★★☆☆ | Early neural compiler heuristic reference. |
| 2019-03 | CGO 2019 | Ithemal: Accurate, Portable and Fast Basic Block Throughput Estimation using Deep Neural Networks | [paper](https://arxiv.org/abs/1808.07412) | [code](https://github.com/ithemal/Ithemal) ![](https://img.shields.io/github/stars/ithemal/Ithemal.svg?style=social) | ★★★☆☆ | Learned throughput model relevant to low-level compiler decisions. |
| 2020-07 | NeurIPS 2020 | A Learned Performance Model for Tensor Processing Units | [paper](https://arxiv.org/abs/2008.01040) | - | ★★★☆☆ | Useful reference for learned cost modeling on accelerator programs. |

## Upstream source lists

[Back to top](#top)

| Source repo | Scope | Priority | Notes |
|---|---|---|---|
| [merrymercy/awesome-tensor-compilers](https://github.com/merrymercy/awesome-tensor-compilers) | Tensor compilers | P0 | Core compiler list. |
| [0xxx/awesome-mlir](https://github.com/0xxx/awesome-mlir) | MLIR | P1 | Include paper and research entries only. |
| [zwang4/awesome-machine-learning-in-compilers](https://github.com/zwang4/awesome-machine-learning-in-compilers) | ML for compilers | P0 | Strong fit for learned compiler optimization. |
| [flagos-ai/awesome-LLM-driven-kernel-generation](https://github.com/flagos-ai/awesome-LLM-driven-kernel-generation) | LLM-driven kernel generation | P0 | Emerging source for automated kernel generation. |
| [ScalingIntelligence/KernelBench](https://github.com/ScalingIntelligence/KernelBench) | Kernel generation benchmark | P1 | Benchmark artifact rather than an awesome list. |
