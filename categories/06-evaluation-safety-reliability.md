# Evaluation, Safety & Reliability

## Scope

Evaluation, factuality, hallucination, RAG/agent benchmarks, safety, jailbreaks, prompt injection, and production reliability of LLM applications. Tables are organized by evaluation or risk type.

## General LLM evaluation

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2020-09 | ICLR 2021 | Measuring Massive Multitask Language Understanding | [paper](https://arxiv.org/abs/2009.03300) | [code](https://github.com/hendrycks/test) | ★★★★☆ | Broad knowledge benchmark; useful but overused if treated as sole eval. |
| 2022-06 | TMLR 2023 | Beyond the Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models | [paper](https://arxiv.org/abs/2206.04615) | [code](https://github.com/google/BIG-bench) | ★★★★☆ | Large collaborative benchmark suite for broad capabilities. |
| 2022-11 | TMLR 2023 | Holistic Evaluation of Language Models | [paper](https://arxiv.org/abs/2211.09110) | [code](https://github.com/stanford-crfm/helm) | ★★★★★ | Foundational holistic evaluation framework and taxonomy. |
| 2023-11 | arXiv | GPQA: A Graduate-Level Google-Proof Q&A Benchmark | [paper](https://arxiv.org/abs/2311.12022) | [code](https://github.com/idavidrein/gpqa) | ★★★★☆ | Hard expert-level QA benchmark for frontier models. |
| 2024-03 | ICML 2024 | Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference | [paper](https://arxiv.org/abs/2403.04132) | [code](https://github.com/lm-sys/FastChat) | ★★★★☆ | Pairwise human preference platform behind many model comparisons. |
| 2024-06 | arXiv | LiveBench: A Challenging, Contamination-Free LLM Benchmark | [paper](https://arxiv.org/abs/2406.19314) | [code](https://github.com/LiveBench/LiveBench) | ★★★★☆ | Frequently updated benchmark designed to reduce contamination. |
| 2024-06 | arXiv | MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark | [paper](https://arxiv.org/abs/2406.01574) | [code](https://github.com/TIGER-AI-Lab/MMLU-Pro) | ★★★★☆ | Harder multiple-choice successor to MMLU. |
| 2024-11 | arXiv | FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI | [paper](https://arxiv.org/abs/2411.04872) | - | ★★★★☆ | Expert-written advanced mathematics benchmark for frontier reasoning. |
| 2025-01 | arXiv | Humanity's Last Exam | [paper](https://arxiv.org/abs/2501.14249) | [code](https://github.com/centerforaisafety/hle) | ★★★★☆ | Broad expert-level multimodal benchmark created after saturation of older evals. |
| 2025-04 | ACL 2025 | HalluLens: LLM Hallucination Benchmark | [paper](https://arxiv.org/abs/2504.17550) | - | ★★★☆☆ | Hallucination benchmark with explicit intrinsic/extrinsic taxonomy. |
| 2025-10 | ICLR 2026 | Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation | [paper](https://arxiv.org/abs/2510.11977) | [project](https://hal.cs.princeton.edu/) | ★★★★★ | Cost-aware, scaffold-aware, benchmark-aware agent evaluation infrastructure. |
| 2026-02 | arXiv | HLE-Verified: A Systematic Verification and Structured Revision of Humanity's Last Exam | [paper](https://arxiv.org/abs/2602.13964) | - | ★★★☆☆ | Recent benchmark-quality follow-up for HLE answer verification and revision. |

## Factuality and hallucination

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2021-09 | ACL 2022 | TruthfulQA: Measuring How Models Mimic Human Falsehoods | [paper](https://arxiv.org/abs/2109.07958) | [code](https://github.com/sylinrl/TruthfulQA) | ★★★★★ | Canonical truthfulness benchmark. |
| 2023-03 | EMNLP 2023 | SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models | [paper](https://arxiv.org/abs/2303.08896) | [code](https://github.com/potsawee/selfcheckgpt) | ★★★★☆ | Sampling-based hallucination detection baseline. |
| 2023-05 | EMNLP 2023 | HaluEval: A Large-Scale Hallucination Evaluation Benchmark for Large Language Models | [paper](https://arxiv.org/abs/2305.11747) | [code](https://github.com/RUCAIBox/HaluEval) | ★★★★☆ | Practical hallucination benchmark across task types. |
| 2023-05 | EMNLP 2023 | FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation | [paper](https://arxiv.org/abs/2305.14251) | [code](https://github.com/shmsw25/FActScore) | ★★★★☆ | Atomic factuality evaluation for long-form generation. |
| 2023-10 | arXiv | FreshLLMs: Refreshing Large Language Models with Search Engine Augmentation | [paper](https://arxiv.org/abs/2310.03214) | - | ★★★☆☆ | Useful for freshness and time-sensitive factuality evaluation. |
| 2025-02 | arXiv | REFIND: Retrieval-Augmented Factuality Hallucination Detection in Large Language Models | [paper](https://arxiv.org/abs/2502.13622) | - | ★★★☆☆ | Retrieval-grounded span-level hallucination detection across languages. |
| 2024-11 | arXiv | Measuring short-form factuality in large language models | [paper](https://arxiv.org/abs/2411.04368) | [code](https://github.com/openai/simple-evals) | ★★★★☆ | SimpleQA benchmark for short-answer factuality with precise answerability. |
| 2025-10 | arXiv | Confabulations from ACL Publications: A Dataset for Scientific Hallucination Detection | [paper](https://arxiv.org/abs/2510.22395) | - | ★★★☆☆ | Scientific-text hallucination dataset built from ACL publication contexts. |

## Long-context and RAG evaluation

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2023-07 | TACL 2024 | Lost in the Middle: How Language Models Use Long Contexts | [paper](https://arxiv.org/abs/2307.03172) | [code](https://github.com/nelson-liu/lost-in-the-middle) | ★★★★★ | Foundational position-sensitivity evaluation for long-context retrieval. |
| 2023-08 | arXiv | LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding | [paper](https://arxiv.org/abs/2308.14508) | [code](https://github.com/THUDM/LongBench) | ★★★★☆ | Broad long-context benchmark. |
| 2023-09 | EACL 2024 | RAGAS: Automated Evaluation of Retrieval Augmented Generation | [paper](https://arxiv.org/abs/2309.15217) | [code](https://github.com/explodinggradients/ragas) | ★★★★☆ | Widely used RAG evaluation metrics and tooling. |
| 2024-01 | arXiv | RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models | [paper](https://arxiv.org/abs/2401.00396) | [code](https://github.com/ParticleMedia/RAGTruth) | ★★★★☆ | Fine-grained hallucination corpus for RAG outputs. |
| 2024-04 | arXiv | RULER: What's the Real Context Size of Your Long-Context Language Models? | [paper](https://arxiv.org/abs/2404.06654) | [code](https://github.com/NVIDIA/RULER) | ★★★★☆ | Synthetic tasks for probing effective context length. |
| 2024-07 | arXiv | RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems | [paper](https://arxiv.org/abs/2407.11005) | [code](https://github.com/rungalileo/ragbench) | ★★★☆☆ | Explainable RAG benchmark dataset. |
| 2024-08 | NeurIPS 2024 | RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation | [paper](https://arxiv.org/abs/2408.08067) | [code](https://github.com/amazon-science/RAGChecker) | ★★★★☆ | Component-level diagnosis for retrieval and generation errors in RAG. |
| 2025-01 | ACL 2025 | SafeRAG: Benchmarking Security in Retrieval-Augmented Generation of Large Language Model | [paper](https://arxiv.org/abs/2501.18636) | - | ★★★☆☆ | Data-injection security benchmark for RAG. |
| 2025-06 | arXiv | GraphRAG-Bench: Challenging Domain-Specific Reasoning for Evaluating Graph Retrieval-Augmented Generation | [paper](https://arxiv.org/abs/2506.02404) | - | ★★★☆☆ | Evaluates GraphRAG graph construction, retrieval quality, and reasoning in domain corpora. |
| 2025-10 | arXiv | Towards Global Retrieval Augmented Generation: A Benchmark for Corpus-Level Reasoning | [paper](https://arxiv.org/abs/2510.26205) | - | ★★★☆☆ | GlobalQA benchmark for corpus-level aggregation and sorting tasks. |
| 2026-01 | ICLR 2026 | When to use Graphs in RAG: A Comprehensive Analysis for Graph Retrieval-Augmented Generation | [paper](https://openreview.net/forum?id=i9q9xDMjG7) | - | ★★★★☆ | Evaluates GraphRAG trade-offs against vector retrieval across tasks. |

## Agent and tool-use evaluation

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2023-08 | ICLR 2024 | AgentBench: Evaluating LLMs as Agents | [paper](https://arxiv.org/abs/2308.03688) | [code](https://github.com/THUDM/AgentBench) | ★★★★☆ | Broad benchmark for LLMs as agents. |
| 2023-10 | ICLR 2024 | SWE-bench: Can Language Models Resolve Real-World GitHub Issues? | [paper](https://arxiv.org/abs/2310.06770) | [code](https://github.com/swe-bench/SWE-bench) | ★★★★★ | Central coding-agent benchmark. |
| 2023-11 | ICLR 2024 | GAIA: A Benchmark for General AI Assistants | [paper](https://arxiv.org/abs/2311.12983) | [dataset](https://huggingface.co/datasets/gaia-benchmark/GAIA) | ★★★★☆ | Long-horizon assistant benchmark requiring tools and browsing. |
| 2024-04 | NeurIPS 2024 | OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments | [paper](https://arxiv.org/abs/2404.07972) | [code](https://github.com/xlang-ai/OSWorld) | ★★★★★ | Real computer-use environment benchmark. |
| 2024-06 | arXiv | tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains | [paper](https://arxiv.org/abs/2406.12045) | [code](https://github.com/sierra-research/tau-bench) | ★★★★☆ | Domain-policy and user-interaction benchmark for tool agents. |
| 2024-08 | arXiv | ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities | [paper](https://arxiv.org/abs/2408.04682) | [code](https://github.com/apple/ToolSandbox) | ★★★★☆ | Stateful tool-use benchmark. |
| 2024-10 | ICLR 2025 | AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents | [paper](https://arxiv.org/abs/2410.09024) | - | ★★★★☆ | Measures harmful task completion risk for agents. |
| 2024-10 | ICLR 2026 | ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents | [paper](https://arxiv.org/abs/2410.06703) | [dataset](https://huggingface.co/datasets/ST-WebAgentBench/st-webagentbench) | ★★★★☆ | Scores web-agent task completion under enterprise-style safety policies. |
| 2024-10 | arXiv | MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering | [paper](https://arxiv.org/abs/2410.07095) | [code](https://github.com/openai/mle-bench) | ★★★★☆ | ML engineering agent benchmark based on Kaggle competitions. |
| 2024-11 | arXiv | RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts | [paper](https://arxiv.org/abs/2411.15114) | [code](https://github.com/METR/RE-Bench) | ★★★★☆ | Research-engineering environments with expert-human baselines. |
| 2024-12 | ICML 2025 | Training Software Engineering Agents and Verifiers with SWE-Gym | [paper](https://arxiv.org/abs/2412.21139) | [code](https://github.com/SWE-Gym/SWE-Gym) | ★★★★★ | Training and evaluation environment for real-world software agents. |
| 2025-02 | arXiv | SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering? | [paper](https://arxiv.org/abs/2502.12115) | [code](https://github.com/openai/SWELancer-Benchmark) | ★★★★☆ | Economic-value software-engineering benchmark from freelance tasks. |
| 2025-04 | COLM 2025 | An Illusion of Progress? Assessing the Current State of Web Agents | [paper](https://arxiv.org/abs/2504.01382) | [code](https://github.com/OSU-NLP-Group/Online-Mind2Web) | ★★★★☆ | Online-Mind2Web benchmark for live web-agent evaluation. |
| 2025-04 | OpenAI 2025 | PaperBench: Evaluating AI's Ability to Replicate AI Research | [paper](https://arxiv.org/abs/2504.01848) | [code](https://github.com/openai/preparedness) | ★★★★☆ | Evaluates agents on replicating ICML papers end-to-end. |
| 2025-06 | NeurIPS 2025 D&B | Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge | [paper](https://arxiv.org/abs/2506.21506) | [code](https://github.com/OSU-NLP-Group/Mind2Web-2) | ★★★★☆ | Long-horizon agentic search benchmark with automated judge agents. |
| 2025-09 | ICLR 2026 | Scaling Generalist Data-Analytic Agents | [paper](https://arxiv.org/abs/2509.25084) | [code](https://github.com/zjunlp/DataMind) | ★★★★☆ | Evaluation/training recipe for multi-format data analysis agents. |
| 2026-01 | arXiv | Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces | [paper](https://arxiv.org/abs/2601.11868) | [code](https://github.com/harbor-framework/terminal-bench) | ★★★★☆ | Command-line benchmark for realistic long-horizon terminal agents. |
| 2026-02 | ICML 2026 | Outrunning LLM Cutoffs: A Live Kernel Crash Resolution Benchmark for All | [paper](https://arxiv.org/abs/2602.02690) | - | ★★★★☆ | Live benchmark for kernel crash-resolution agents with cutoff-aware evaluation. |
| 2026-02 | arXiv | AIRS-Bench: A Benchmark for AI Agents on the Full ML Research Lifecycle | [paper](https://arxiv.org/abs/2602.06855) | - | ★★★☆☆ | Measures agents on full ML research lifecycle tasks. |

## Safety, jailbreaks, and robustness

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2020-09 | Findings 2021 | RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models | [paper](https://arxiv.org/abs/2009.11462) | [code](https://github.com/allenai/real-toxicity-prompts) | ★★★☆☆ | Early toxicity-generation benchmark. |
| 2022-03 | ACL 2022 | ToxiGen: A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection | [paper](https://arxiv.org/abs/2203.09509) | [code](https://github.com/microsoft/TOXIGEN) | ★★★☆☆ | Adversarial hate-speech benchmark. |
| 2023-08 | NAACL 2024 | XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models | [paper](https://arxiv.org/abs/2308.01263) | - | ★★★★☆ | Measures over-refusal and the helpful/harmless tradeoff on safe but sensitive prompts. |
| 2023-09 | ACL 2024 | SafetyBench: Evaluating the Safety of Large Language Models | [paper](https://arxiv.org/abs/2309.07045) | [code](https://github.com/thu-coai/SafetyBench) | ★★★★☆ | Broad safety benchmark across multiple risk categories. |
| 2023-07 | arXiv | Universal and Transferable Adversarial Attacks on Aligned Language Models | [paper](https://arxiv.org/abs/2307.15043) | [code](https://github.com/llm-attacks/llm-attacks) | ★★★★★ | GCG-style transferable jailbreak attack reference. |
| 2023-10 | NeurIPS 2023 | DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models | [paper](https://arxiv.org/abs/2306.11698) | [code](https://github.com/AI-secure/DecodingTrust) | ★★★★☆ | Broad trustworthiness evaluation across safety, privacy, robustness, and fairness. |
| 2024-02 | arXiv | SALAD-Bench: A Hierarchical and Comprehensive Safety Benchmark for Large Language Models | [paper](https://arxiv.org/abs/2402.05044) | [code](https://github.com/OpenSafetyLab/SALAD-BENCH) | ★★★★☆ | Hierarchical safety taxonomy plus evaluator for LLM safety assessment. |
| 2024-02 | arXiv | HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal | [paper](https://arxiv.org/abs/2402.04249) | [code](https://github.com/centerforaisafety/HarmBench) | ★★★★★ | Standardized harmful-behavior evaluation and red-teaming framework. |
| 2024-04 | arXiv | JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models | [paper](https://arxiv.org/abs/2404.01318) | [code](https://github.com/JailbreakBench/jailbreakbench) | ★★★★☆ | Open benchmark for jailbreak robustness. |
| 2024-05 | arXiv | StrongREJECT: Towards Robust Evaluation of Jailbreak Attacks Against Large Language Models | [paper](https://arxiv.org/abs/2402.10260) | [code](https://github.com/alexandrasouly/strongreject) | ★★★★☆ | Improves evaluation of refusal and jailbreak attack success. |
| 2024-06 | NeurIPS 2024 | WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs | [paper](https://arxiv.org/abs/2406.18495) | [code](https://github.com/allenai/wildguard) | ★★★★☆ | Unified moderation, jailbreak, and refusal detection resource. |
| 2025-02 | arXiv | JailBench: A Comprehensive Chinese Security Assessment Benchmark for Large Language Models | [paper](https://arxiv.org/abs/2502.18935) | - | ★★★☆☆ | Chinese safety benchmark with automated jailbreak prompt generation. |
| 2025-06 | ICML 2025 | Weak-to-Strong Jailbreaking on Large Language Models | [paper](https://mlanthology.org/icml/2025/zhao2025icml-weaktostrong/) | - | ★★★★☆ | Inference-time weak-to-strong attack exposing alignment robustness gaps. |
| 2025-12 | arXiv | TeleAI-Safety: A Comprehensive LLM Jailbreaking Benchmark towards Attacks, Defenses, and Evaluations | [paper](https://arxiv.org/abs/2512.05485) | - | ★★★☆☆ | Recent jailbreak benchmark covering attacks, defenses, and evaluation protocols. |

## Prompt injection and LLM application security

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2022-11 | arXiv | Prompt Injection attack against LLM-integrated Applications | [paper](https://arxiv.org/abs/2211.09527) | - | ★★★★☆ | Early prompt-injection framing for LLM-integrated apps. |
| 2023-02 | AISec 2023 | Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection | [paper](https://arxiv.org/abs/2302.12173) | - | ★★★★★ | Key indirect prompt-injection paper for tool and retrieval apps. |
| 2023-12 | arXiv | Benchmarking and Defending Against Indirect Prompt Injection Attacks on Large Language Models | [paper](https://arxiv.org/abs/2312.14197) | - | ★★★★☆ | BIPIA benchmark for indirect prompt injection in LLM-integrated applications. |
| 2024-03 | ACL 2024 Findings | InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents | [paper](https://arxiv.org/abs/2403.02691) | [code](https://github.com/uiuc-kang-lab/InjecAgent) | ★★★★☆ | Indirect prompt-injection benchmark for tool-integrated agents. |
| 2024-02 | arXiv | Formalizing and Benchmarking Prompt Injection Attacks and Defenses | [paper](https://arxiv.org/abs/2310.12815) | [code](https://github.com/HumanCompatibleAI/tensor-trust) | ★★★★☆ | Tensor Trust benchmark for prompt-injection game dynamics. |
| 2024-06 | arXiv | AgentDojo: A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents | [paper](https://arxiv.org/abs/2406.13352) | [code](https://github.com/ethz-spylab/agentdojo) | ★★★★★ | Security benchmark for indirect prompt injection in tool-using agents. |
| 2024-12 | arXiv | StruQ: Defending Against Prompt Injection with Structured Queries | [paper](https://arxiv.org/abs/2402.06363) | [code](https://github.com/Sizhe-Chen/StruQ) | ★★★★☆ | Structured prompting defense against instruction/data confusion. |
| 2025-04 | ACL 2025 LLM Security | Bypassing Prompt Injection and Jailbreak Detection in LLM Guardrails | [paper](https://arxiv.org/abs/2504.11168) | - | ★★★☆☆ | Studies evasion against prompt-injection and jailbreak detectors. |
| 2026-01 | ICLR 2026 | VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents | [paper](https://openreview.net/forum?id=UMauKu2azg) | - | ★★★★☆ | Visual prompt-injection benchmark for browser and GUI agents. |
| 2025-06 | arXiv | OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents | [paper](https://arxiv.org/abs/2506.14866) | [code](https://github.com/tml-epfl/os-harm) | ★★★★☆ | Safety benchmark for deliberate misuse, prompt injection, and misbehavior in OS agents. |
| 2025-08 | arXiv | Measuring Harmfulness of Computer-Using Agents | [paper](https://arxiv.org/abs/2508.00935) | - | ★★★☆☆ | CUAHarm-style evaluation for computer-use agent misuse. |
| 2026-04 | arXiv | AgentHazard: A Benchmark for Measuring Harmful Behavior in Computer-Use Agents | [paper](https://arxiv.org/abs/2604.02947) | - | ★★★★☆ | Computer-use agent harm benchmark beyond classic prompt injection. |
| 2026-04 | arXiv | The Blind Spot of Agent Safety: How Benign User Instructions Expose Critical Vulnerabilities in Computer-Use Agents | [paper](https://arxiv.org/abs/2604.10577) | - | ★★★★☆ | OS-BLIND benchmark for harms that emerge from benign-looking computer-use tasks. |

## Upstream source lists

| Source repo | Scope | Priority | Notes |
|---|---|---|---|
| [alopatenko/LLMEvaluation](https://github.com/alopatenko/LLMEvaluation) | LLM evaluation | P1 | Good evaluation taxonomy; filter to papers and artifacts. |
| [tjunlp-lab/Awesome-LLMs-Evaluation-Papers](https://github.com/tjunlp-lab/Awesome-LLMs-Evaluation-Papers) | LLM evaluation papers | P0 | Paper-first evaluation source. |
| [YHPeter/Awesome-RAG-Evaluation](https://github.com/YHPeter/Awesome-RAG-Evaluation) | RAG evaluation | P0 | Cross-listed from RAG category. |
| [zhangxjohn/LLM-Agent-Benchmark-List](https://github.com/zhangxjohn/LLM-Agent-Benchmark-List) | Agent benchmarks | P0 | Cross-listed from agent category. |
| [ydyjya/Awesome-LLM-Safety](https://github.com/ydyjya/Awesome-LLM-Safety) | LLM safety | P0 | Strong safety paper source. |
| [corca-ai/awesome-llm-security](https://github.com/corca-ai/awesome-llm-security) | LLM security | P1 | Include papers and defensive system artifacts only. |
| [Joe-B-Security/awesome-prompt-injection](https://github.com/Joe-B-Security/awesome-prompt-injection) | Prompt injection | P2 | Use paper and benchmark entries only. |
