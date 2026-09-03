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
| 2026-08 | arXiv | Tensor Seeks Layout: Formalizing Layout Selection for ML Compilers | [paper](https://arxiv.org/abs/2608.21555) | - | ★★★★☆ | Gives global tensor-layout selection a formal model that includes conversion costs. |
| 2026-05 | MLSys 2026 | ExecuTorch - A Unified PyTorch Solution to Run ML Models On-Device | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/236f915dd02af4f11927f67330b21d4b-Abstract-Conference.html) | [code](https://github.com/pytorch/executorch) ![](https://img.shields.io/github/stars/pytorch/executorch.svg?style=social) | ★★★★☆ | Provides an end-to-end PyTorch export and runtime stack for constrained devices. |
| 2026-05 | MLSys 2026 | Wave: A Symbolic Python DSL And Compiler for High-Performance Machine Learning | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/48c34730ff9a8574481a00ce8cb5e2cb-Abstract-Conference.html) | [code](https://github.com/iree-org/wave) ![](https://img.shields.io/github/stars/iree-org/wave.svg?style=social) | ★★★★☆ | Uses symbolic constraints and transformations to generate high-performance accelerator kernels. |
| 2026-05 | MLSys 2026 | DynaFlow: Transparent and Flexible Intra-Device Parallelism via Programmable Operator Scheduling | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/bbd7d8bd780fcf7143add2317ba04638-Abstract-Conference.html) | [code](https://github.com/uw-syfi/DynaFlow) ![](https://img.shields.io/github/stars/uw-syfi/DynaFlow.svg?style=social) | ★★★★☆ | Adds programmable intra-device scheduling while preserving framework-level operator semantics. |
| 2026-05 | MLSys 2026 | ApproxMLIR: Accuracy-Aware Compiler for Compound ML System | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/bbd3e0e9913824bbc46e7e87b11461ae-Abstract-Conference.html) | - | ★★★☆☆ | Propagates accuracy budgets through compound ML pipelines to select approximate implementations. |
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
| 2026-07 | OSDI 2026 | Optimal Software Pipelining and Warp Specialization for Tensor Core GPUs | [paper](https://www.usenix.org/conference/osdi26/presentation/soi) | - | ★★★★☆ | Formalizes pipeline and warp-specialization choices for high-utilization Tensor Core kernels. |
| 2026-05 | MLSys 2026 | Flashlight: PyTorch Compiler Extensions to Accelerate Attention Variants | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/bc52716d13d2d72ea0f335667d86c0f8-Abstract-Conference.html) | - | ★★★★☆ | Extends compilation and autotuning to a broad family of rapidly changing attention operators. |
| 2020-11 | OSDI 2020 | Ansor: Generating High-Performance Tensor Programs for Deep Learning | [paper](https://www.usenix.org/conference/osdi20/presentation/zheng) | [code](https://github.com/apache/tvm) ![](https://img.shields.io/github/stars/apache/tvm.svg?style=social) | ★★★★★ | Core auto-scheduler for tensor program generation. |
| 2022-08 | MLSys 2022 | DietCode: Automatic Optimization for Dynamic Tensor Programs | [paper](https://proceedings.mlsys.org/paper_files/paper/2022/hash/f89b79c9a28d4cae22ef9e557d9fa191-Abstract.html) | [code](https://github.com/UofT-EcoSystem/DietCode) ![](https://img.shields.io/github/stars/UofT-EcoSystem/DietCode.svg?style=social) | ★★★★☆ | Extends tensor-program optimization to dynamic shapes. |
| 2022-07 | OSDI 2022 | ROLLER: Fast and Efficient Tensor Compilation for Deep Learning | [paper](https://www.usenix.org/conference/osdi22/presentation/zhu) | [code](https://github.com/microsoft/nnfusion) ![](https://img.shields.io/github/stars/microsoft/nnfusion.svg?style=social) | ★★★★☆ | Shape-aware tile construction for fast tensor-kernel compilation. |
| 2022-07 | arXiv | TensorIR: An Abstraction for Automatic Tensorized Program Optimization | [paper](https://arxiv.org/abs/2207.04296) | [code](https://github.com/apache/tvm) ![](https://img.shields.io/github/stars/apache/tvm.svg?style=social) | ★★★★☆ | TVM TensorIR reference for tensorized scheduling and lowering. |
| 2023-07 | OSDI 2023 | Welder: Scheduling Deep Learning Memory Access via Tile-graph | [paper](https://www.usenix.org/conference/osdi23/presentation/shi) | - | ★★★★☆ | Optimizes inter- and intra-operator memory access with a tile-graph abstraction. |
| 2024-07 | OSDI 2024 | Ladder: Enabling Efficient Low-Precision Deep Learning Computing through Hardware-aware Tensor Transformation | [paper](https://www.usenix.org/system/files/osdi24-wang-lei.pdf) | [code](https://github.com/tile-ai/Ladder) ![](https://img.shields.io/github/stars/tile-ai/Ladder.svg?style=social) | ★★★★☆ | Hardware-aware tensor transformations for low-precision computation. |
| 2025-02 | PPoPP 2025 | FlashTensor: Optimizing Tensor Programs by Leveraging Fine-grained Tensor Property | [paper](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1) | - | ★★★☆☆ | Tensor-program optimizer that exploits fine-grained tensor properties. |

## Kernel DSLs and attention engines

[Back to top](#top)

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2026-08 | IEEE Micro 2026 | Triton for MTIA: Bridging the Programming Model Gaps for Custom AI Accelerators | [paper](https://arxiv.org/abs/2608.00325) | - | ★★★★☆ | Extends Triton's GPU-oriented abstractions to Meta's custom inference accelerator. |
| 2026-08 | arXiv | rl-triton: High-Performance Triton GPU Kernels for Reinforcement Learning Credit Assignment | [paper](https://arxiv.org/abs/2608.17641) | [code](https://github.com/simonsays1980/rl-triton) ![](https://img.shields.io/github/stars/simonsays1980/rl-triton.svg?style=social) | ★★★☆☆ | Maps several RL return estimators to a shared parallel associative-scan kernel framework. |
| 2026-07 | OSDI 2026 | Syncopate: Efficient Multi-GPU AI Kernels via Automatic Chunk-Centric Compute-Communication Overlap | [paper](https://www.usenix.org/conference/osdi26/presentation/qiang) | [code](https://github.com/tie-pilot-qxw/syncopate) ![](https://img.shields.io/github/stars/tie-pilot-qxw/syncopate.svg?style=social) | ★★★★☆ | Generates chunked multi-GPU kernels that overlap communication with computation. |
| 2026-07 | OSDI 2026 | MPK: A Compiler and Runtime for Mega-Kernelizing Tensor Programs | [paper](https://www.usenix.org/conference/osdi26/presentation/cheng) | [code](https://github.com/mirage-project/mirage) ![](https://img.shields.io/github/stars/mirage-project/mirage.svg?style=social) | ★★★★★ | Compiles multi-operator tensor programs into mega-kernels while managing synchronization and resources. |
| 2026-05 | MLSys 2026 | FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/ae8b0b5838ba510daff1198474e7b984-Abstract-Conference.html) | - | ★★★★★ | Redesigns attention pipelines around asymmetric growth in tensor, memory, and scalar resources. |
| 2026-05 | MLSys 2026 | HipKittens: Fast and Furious AMD Kernels | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/bc75fa9843a7905bbed9d83895a88f7f-Abstract-Conference.html) | [code](https://github.com/HazyResearch/HipKittens) ![](https://img.shields.io/github/stars/HazyResearch/HipKittens.svg?style=social) | ★★★★☆ | Brings a composable kernel abstraction and tuned primitives to AMD GPUs. |
| 2026-05 | MLSys 2026 | ParallelKittens: Systematic and Practical Simplification of Multi-GPU AI Kernels | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/ff997469ac66cf893c4183efeb22212a-Abstract-Conference.html) | - | ★★★★☆ | Extends tile-level abstractions to communication-rich multi-GPU kernels. |
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
| 2026-09 | VLDB 2026 | RSR-core: A High-Performance Engine for Low-Bit Matrix-Vector Multiplication | [paper](https://www.vldb.org/pvldb/vol19/p4726-dehghankar.pdf) | - | ★★★☆☆ | Provides a specialized execution engine for low-bit matrix-vector workloads. |
| 2026-08 | arXiv | Maia 200: A Software Defined Dataflow System for Large-scale AI Acceleration | [paper](https://arxiv.org/abs/2608.24664) | - | ★★★★★ | Describes Microsoft's data-movement-centric accelerator architecture and its software stack. |
| 2026-06 | ISCA 2026 | OASIS: Outlier-Aware LUT-Based GEMM with Dual-Side Quantization for LLM Inference Acceleration | [paper](https://www.iscaconf.org/isca2026/program/) | - | ★★★★☆ | Co-designs lookup-table GEMM and two-sided quantization around LLM outliers. |
| 2026-06 | ISCA 2026 | Omni-LUT: Energy-Efficient LUT-based Accelerator with Hardware-Aware KV Cache Quantization | [paper](https://www.iscaconf.org/isca2026/program/) | - | ★★★★☆ | Couples a LUT accelerator with KV quantization chosen for its hardware data path. |
| 2026-06 | ISCA 2026 | P3-LLM: An Integrated NPU-PIM Accelerator for Edge LLM Inference Using Hybrid Numerical Formats | [paper](https://www.iscaconf.org/isca2026/program/) | - | ★★★★☆ | Integrates NPU and PIM execution with mixed numerical formats for edge inference. |
| 2026-06 | ISCA 2026 | CHIME: A Case for Efficient Long-Context Attention-FC Disaggregated Inference with DIMM-PIM | [paper](https://www.iscaconf.org/isca2026/program/) | - | ★★★★☆ | Separates attention and fully connected phases across accelerator and DIMM-PIM resources. |
| 2026-06 | ISCA 2026 | SMOOTH: Hardware-Assisted Fine-Grained On-Chip Memory Management for Efficient On-Device LLM Inference | [paper](https://www.iscaconf.org/isca2026/program/) | - | ★★★☆☆ | Adds fine-grained hardware memory management for constrained on-device execution. |
| 2026-05 | MLSys 2026 | SHIP: SRAM-Based Huge Inference Pipelines for Fast LLM Serving | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/9c20f16b05f5e5e70fa07e2a4364b80e-Abstract-Conference.html) | - | ★★★★☆ | Builds large SRAM-resident inference pipelines to avoid repeated off-chip weight movement. |
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
| 2026-08 | ASE 2026 | RealisticTritonBench: A Benchmark for Triton-Kernel Generation in Real-World AI Frameworks | [paper](https://arxiv.org/abs/2608.12004) | - | ★★★★☆ | Evaluates generated Triton kernels in framework-level contexts rather than isolated toy operators. |
| 2026-08 | arXiv | PTXBench: Benchmark and Adapt LLMs for GPU Kernel Optimization with Architecture-specific PTX | [paper](https://arxiv.org/abs/2608.17379) | - | ★★★★☆ | Tests whether kernel agents can use target-specific PTX correctly and profitably on H100/B200. |
| 2026-08 | arXiv | HIERA: Workload-Aware Planning Across Implementation Spaces for GPU Kernel Optimization | [paper](https://arxiv.org/abs/2608.21157) | - | ★★★☆☆ | Plans hierarchical searches across kernel implementation spaces instead of fixing one DSL strategy. |
| 2026-08 | arXiv | CAKE: Compiler-Agent Co-Design for Frontier Kernel Evolution | [paper](https://arxiv.org/abs/2608.12629) | - | ★★★★☆ | Exposes a typed, hardware-explicit IR designed for optimization agents and compiler feedback. |
| 2026-08 | arXiv | FABRICA: Agentic CUDA-to-CSL Translation and Optimization for Wafer-Scale Systems | [paper](https://arxiv.org/abs/2608.25124) | - | ★★★☆☆ | Evaluates agentic remapping of CUDA kernels to Cerebras' distributed wafer-scale programming model. |
| 2026-08 | KDD 2026 | Step-TP: A Grounded, Step-Level Dataset with Chain-of-Thought Reasoning for LLM-Guided Tensor Program Optimization | [paper](https://doi.org/10.1145/3770855.3817484) | - | ★★★☆☆ | Supplies execution-grounded optimization trajectories for tensor-program agents. |
| 2026-07 | ICML 2026 | KernelBand: Steering LLM-based Kernel Optimization via Hardware-Aware Multi-Armed Bandits | [paper](https://icml.cc/virtual/2026/poster/62803) | [code](https://github.com/TongmingLAIC/KernelBand) ![](https://img.shields.io/github/stars/TongmingLAIC/KernelBand.svg?style=social) | ★★★★☆ | Treats kernel optimization as hardware-aware bandit search over transformation strategies. |
| 2026-07 | ICML 2026 | StitchCUDA: An Automated Multi-Agents End-to-End GPU Programing Framework with Rubric-based Agentic Reinforcement Learning | [paper](https://icml.cc/virtual/2026/poster/64924) | [code](https://github.com/UMN-APEX-Lab/StitchCUDA) ![](https://img.shields.io/github/stars/UMN-APEX-Lab/StitchCUDA.svg?style=social) | ★★★★☆ | Trains a multi-agent CUDA generation workflow with executable rubric feedback. |
| 2026-07 | ICML 2026 | KernelCraft: Benchmarking for Agentic Close-to-Metal Kernel Generation on Emerging Hardware | [paper](https://icml.cc/virtual/2026/poster/65579) | - | ★★★☆☆ | Tests agentic kernel generation beyond mature CUDA targets and familiar operators. |
| 2026-05 | MLSys 2026 | AccelOpt: A Self-Improving LLM Agentic System for AI Accelerator Kernel Optimization | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/0f8426558905746fc38da5e335700aec-Abstract-Conference.html) | [code](https://github.com/zhang677/AccelOpt) ![](https://img.shields.io/github/stars/zhang677/AccelOpt.svg?style=social) | ★★★★☆ | Uses profiling feedback and retained experience to iteratively improve accelerator kernels. |
| 2026-05 | MLSys 2026 | Optimizing PyTorch Inference with LLM-Based Multi-Agent Systems | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/bd49b53516ce9ea248fb73522d71a508-Abstract-Conference.html) | [code](https://github.com/pike-project/pike) ![](https://img.shields.io/github/stars/pike-project/pike.svg?style=social) | ★★★★☆ | PIKE coordinates specialized agents to optimize executable PyTorch inference programs. |
| 2026-05 | MLSys 2026 | Agentic Operator Generation for ML ASICs | [paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/8c54e9bfed4119c873f575d1d1e2f0a0-Abstract-Conference.html) | - | ★★★☆☆ | Extends LLM-driven operator generation to accelerator-specific constraints and toolchains. |
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
