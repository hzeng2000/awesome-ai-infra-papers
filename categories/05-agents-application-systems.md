# Agents & Application-level Systems

## Scope

LLM agent systems, tool use, memory, planning, multi-agent collaboration, web/computer-use agents, coding agents, deep research agents, and agent benchmarks. Tables are organized by agent capability or environment.

## Tool use and action APIs

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2022-05 | arXiv | MRKL Systems: A Modular, Neuro-Symbolic Architecture That Combines Large Language Models, External Knowledge Sources and Discrete Reasoning | [paper](https://arxiv.org/abs/2205.00445) | - | ★★★★☆ | Early architecture for routing between LLMs and external tools. |
| 2022-10 | ICLR 2023 | ReAct: Synergizing Reasoning and Acting in Language Models | [paper](https://arxiv.org/abs/2210.03629) | [code](https://github.com/ysymyth/ReAct) | ★★★★★ | Foundational reasoning/action loop. |
| 2023-02 | NeurIPS 2023 | Toolformer: Language Models Can Teach Themselves to Use Tools | [paper](https://arxiv.org/abs/2302.04761) | - | ★★★★☆ | Self-supervised API-use data generation. |
| 2023-03 | arXiv | HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face | [paper](https://arxiv.org/abs/2303.17580) | [code](https://github.com/microsoft/JARVIS) | ★★★☆☆ | Representative LLM-as-controller system for model/tool orchestration. |
| 2023-04 | EMNLP 2023 | API-Bank: A Benchmark for Tool-Augmented LLMs | [paper](https://arxiv.org/abs/2304.08244) | [code](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/api-bank) | ★★★★☆ | Early benchmark for API planning and tool calls. |
| 2023-05 | NeurIPS 2023 | Gorilla: Large Language Model Connected with Massive APIs | [paper](https://arxiv.org/abs/2305.15334) | [code](https://github.com/ShishirPatil/gorilla) | ★★★★☆ | API retrieval and tool-call benchmark line. |
| 2023-07 | ICLR 2024 | ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs | [paper](https://arxiv.org/abs/2307.16789) | [code](https://github.com/OpenBMB/ToolBench) | ★★★★☆ | Large tool-use instruction dataset and benchmark. |
| 2024-02 | arXiv | Berkeley Function Calling Leaderboard | [paper](https://arxiv.org/abs/2402.18520) | [code](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard) | ★★★★☆ | Practical function-calling evaluation suite. |

## Planning, reflection, and memory

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2023-03 | NeurIPS 2023 | Reflexion: Language Agents with Verbal Reinforcement Learning | [paper](https://arxiv.org/abs/2303.11366) | [code](https://github.com/noahshinn/reflexion) | ★★★★☆ | Self-reflection loop using verbal feedback. |
| 2023-04 | UIST 2023 | Generative Agents: Interactive Simulacra of Human Behavior | [paper](https://arxiv.org/abs/2304.03442) | [code](https://github.com/joonspk-research/generative_agents) | ★★★★☆ | Memorable architecture for reflection, planning, and long-term memory. |
| 2023-05 | NeurIPS 2023 | Tree of Thoughts: Deliberate Problem Solving with Large Language Models | [paper](https://arxiv.org/abs/2305.10601) | [code](https://github.com/princeton-nlp/tree-of-thought-llm) | ★★★★☆ | Search/planning pattern for deliberate reasoning. |
| 2023-05 | TMLR 2024 | Voyager: An Open-Ended Embodied Agent with Large Language Models | [paper](https://arxiv.org/abs/2305.16291) | [code](https://github.com/MineDojo/Voyager) | ★★★★☆ | Long-horizon agent with executable skill memory. |
| 2023-10 | arXiv | MemGPT: Towards LLMs as Operating Systems | [paper](https://arxiv.org/abs/2310.08560) | [code](https://github.com/letta-ai/letta) | ★★★★☆ | Memory-management framing for persistent LLM agents. |
| 2023-10 | arXiv | Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models | [paper](https://arxiv.org/abs/2310.04406) | - | ★★★☆☆ | Applies MCTS-style search to agent trajectories. |
| 2024-02 | arXiv | A Survey on the Memory Mechanism of Large Language Model based Agents | [paper](https://arxiv.org/abs/2404.13501) | - | ★★★☆☆ | Useful taxonomy for agent memory systems. |

## Multi-agent systems

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2023-03 | NeurIPS 2023 Workshop | CAMEL: Communicative Agents for Mind Exploration of Large Language Model Society | [paper](https://arxiv.org/abs/2303.17760) | [code](https://github.com/camel-ai/camel) | ★★★★☆ | Early role-playing multi-agent framework. |
| 2023-07 | ACL 2024 | ChatDev: Communicative Agents for Software Development | [paper](https://arxiv.org/abs/2307.07924) | [code](https://github.com/OpenBMB/ChatDev) | ★★★☆☆ | Multi-agent software-development workflow case study. |
| 2023-08 | arXiv | MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework | [paper](https://arxiv.org/abs/2308.00352) | [code](https://github.com/geekan/MetaGPT) | ★★★★☆ | Popular multi-agent product/software workflow framework. |
| 2023-08 | arXiv | AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation | [paper](https://arxiv.org/abs/2308.08155) | [code](https://github.com/microsoft/autogen) | ★★★★☆ | Influential multi-agent conversation and orchestration framework. |
| 2023-08 | arXiv | AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors | [paper](https://arxiv.org/abs/2308.10848) | [code](https://github.com/OpenBMB/AgentVerse) | ★★★☆☆ | Framework for multi-agent collaboration experiments. |
| 2024-02 | arXiv | AgentScope: A Flexible yet Robust Multi-Agent Platform | [paper](https://arxiv.org/abs/2402.14034) | [code](https://github.com/modelscope/agentscope) | ★★★☆☆ | Multi-agent platform with engineering emphasis. |

## Web, browser, and computer-use agents

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2023-06 | NeurIPS 2023 | Mind2Web: Towards a Generalist Agent for the Web | [paper](https://arxiv.org/abs/2306.06070) | [code](https://github.com/OSU-NLP-Group/Mind2Web) | ★★★★☆ | Web task dataset for grounding language agents in real websites. |
| 2023-07 | ICLR 2024 | WebArena: A Realistic Web Environment for Building Autonomous Agents | [paper](https://arxiv.org/abs/2307.13854) | [code](https://github.com/web-arena-x/webarena) | ★★★★★ | Standard realistic browser-agent environment. |
| 2023-12 | arXiv | AppAgent: Multimodal Agents as Smartphone Users | [paper](https://arxiv.org/abs/2312.13771) | [code](https://github.com/mnotgod96/AppAgent) | ★★★☆☆ | Early smartphone-control agent with exploration and demonstration learning. |
| 2024-01 | ICML 2024 | GPT-4V(ision) is a Generalist Web Agent, if Grounded | [paper](https://arxiv.org/abs/2401.01614) | [code](https://github.com/OSU-NLP-Group/SeeAct) | ★★★★☆ | SeeAct system for multimodal live-web agents with grounding. |
| 2024-01 | arXiv | VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks | [paper](https://arxiv.org/abs/2401.13649) | [code](https://github.com/web-arena-x/visualwebarena) | ★★★★☆ | Multimodal extension of WebArena. |
| 2024-01 | ACL 2024 | WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models | [paper](https://arxiv.org/abs/2401.13919) | [code](https://github.com/MinorJerry/WebVoyager) | ★★★★☆ | End-to-end web agent evaluated on real-world websites. |
| 2024-01 | arXiv | Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception | [paper](https://arxiv.org/abs/2401.16158) | [code](https://github.com/X-PLUG/MobileAgent) | ★★★☆☆ | Vision-centric mobile agent that avoids relying on app XML metadata. |
| 2024-03 | arXiv | WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks? | [paper](https://arxiv.org/abs/2403.07718) | [code](https://github.com/ServiceNow/WorkArena) | ★★★★☆ | Enterprise-workflow benchmark for browser agents. |
| 2024-04 | NeurIPS 2024 | OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments | [paper](https://arxiv.org/abs/2404.07972) | [code](https://github.com/xlang-ai/OSWorld) | ★★★★★ | Key computer-use benchmark in real desktop environments. |
| 2024-05 | arXiv | AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents | [paper](https://arxiv.org/abs/2405.14573) | [code](https://github.com/google-research/android_world) | ★★★★☆ | Android environment for mobile agents. |
| 2024-08 | arXiv | OmniParser for Pure Vision Based GUI Agent | [paper](https://arxiv.org/abs/2408.00203) | [code](https://github.com/microsoft/OmniParser) | ★★★★☆ | Screen parsing module for pure-vision GUI agents. |
| 2024-10 | ICLR 2026 | ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents | [paper](https://arxiv.org/abs/2410.06703) | [dataset](https://huggingface.co/datasets/ST-WebAgentBench/st-webagentbench) | ★★★★☆ | Adds enterprise-style policy constraints to web-agent completion evaluation. |
| 2024-10 | arXiv | OS-ATLAS: A Foundation Action Model for Generalist GUI Agents | [paper](https://arxiv.org/abs/2410.23218) | [code](https://github.com/OS-Copilot/OS-Atlas) | ★★★★☆ | Cross-platform GUI grounding/action model and synthetic data toolkit. |
| 2025-01 | arXiv | UI-TARS: Pioneering Automated GUI Interaction with Native Agents | [paper](https://arxiv.org/abs/2501.12326) | [code](https://github.com/bytedance/UI-TARS) | ★★★★☆ | Native GUI agent model trained for perception, grounding, action, and reflection. |
| 2025-01 | TMLR 2025 | The BrowserGym Ecosystem for Web Agent Research | [paper](https://arxiv.org/abs/2412.05467) | [code](https://github.com/ServiceNow/BrowserGym) | ★★★★☆ | Reusable environment wrapper and experiment ecosystem for web-agent benchmarks. |
| 2026-01 | ICLR 2026 | VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents | [paper](https://openreview.net/forum?id=UMauKu2azg) | - | ★★★★☆ | Visual prompt-injection benchmark for browser and computer-use agents. |

## Coding and software-engineering agents

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2023-06 | arXiv | RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems | [paper](https://arxiv.org/abs/2306.03091) | [code](https://github.com/Leolty/repobench) | ★★★☆☆ | Repository-level context benchmark for code models and agents. |
| 2023-10 | ICLR 2024 | SWE-bench: Can Language Models Resolve Real-World GitHub Issues? | [paper](https://arxiv.org/abs/2310.06770) | [code](https://github.com/swe-bench/SWE-bench) | ★★★★★ | Central benchmark for coding agents on real GitHub issues. |
| 2024-05 | arXiv | SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering | [paper](https://arxiv.org/abs/2405.15793) | [code](https://github.com/SWE-agent/SWE-agent) | ★★★★☆ | Agent design and interface lessons for repository editing. |
| 2024-07 | arXiv | OpenHands: An Open Platform for AI Software Developers as Generalist Agents | [paper](https://arxiv.org/abs/2407.16741) | [code](https://github.com/All-Hands-AI/OpenHands) | ★★★★☆ | Open software-agent platform spanning code, shell, browser, sandbox, and evaluation. |
| 2024-07 | arXiv | Agentless: Demystifying LLM-based Software Engineering Agents | [paper](https://arxiv.org/abs/2407.01489) | [code](https://github.com/OpenAutoCoder/Agentless) | ★★★★☆ | Strong structured baseline that questions how much agent machinery is needed. |
| 2024-10 | arXiv | SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains? | [paper](https://arxiv.org/abs/2410.03859) | [code](https://github.com/swe-bench/SWE-bench) | ★★★☆☆ | Extends issue-resolution evaluation to visual software tasks. |
| 2024-10 | arXiv | MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering | [paper](https://arxiv.org/abs/2410.07095) | [code](https://github.com/openai/mle-bench) | ★★★★☆ | ML engineering benchmark built from Kaggle-style competitions. |
| 2024-12 | ICML 2025 | Training Software Engineering Agents and Verifiers with SWE-Gym | [paper](https://arxiv.org/abs/2412.21139) | [code](https://github.com/SWE-Gym/SWE-Gym) | ★★★★★ | Training environment, agent trajectories, and verifiers for open software agents. |
| 2025-02 | arXiv | SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering? | [paper](https://arxiv.org/abs/2502.12115) | [code](https://github.com/openai/SWELancer-Benchmark) | ★★★★☆ | Upwork-derived software tasks with real payout values and end-to-end grading. |
| 2025-04 | arXiv | SWE-smith: Scaling Data for Software Engineering Agents | [paper](https://arxiv.org/abs/2504.21798) | [code](https://github.com/SWE-bench/SWE-smith) | ★★★☆☆ | Synthetic data pipeline for training and evaluating coding agents. |
| 2025-06 | arXiv | SWE-Dev: Building Software Engineering Agents with Training and Inference Scaling | [paper](https://arxiv.org/abs/2506.07636) | - | ★★★☆☆ | Open-weight software-engineering agent line combining synthetic tests and scaling. |
| 2025-06 | arXiv | SWE-Bench-CL: Continual Learning for Coding Agents | [paper](https://arxiv.org/abs/2507.00014) | - | ★★★☆☆ | Chronological SWE-bench variant for measuring agent learning over repository history. |
| 2025-07 | arXiv | SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on Software Engineering Tasks | [paper](https://arxiv.org/abs/2507.11059) | - | ★★★☆☆ | Dynamic coding-agent benchmark intended to reduce static benchmark leakage. |
| 2025-10 | arXiv | Saving SWE-Bench: A Benchmark Mutation Approach for Realistic Agent Evaluation | [paper](https://arxiv.org/abs/2510.08996) | - | ★★★☆☆ | Mutates benchmark tasks toward IDE/chat-style coding-assistant workflows. |
| 2025-12 | arXiv | SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios | [paper](https://arxiv.org/abs/2512.18470) | - | ★★★☆☆ | Long-horizon benchmark for maintaining and evolving codebases over time. |
| 2026-02 | ICML 2026 | Outrunning LLM Cutoffs: A Live Kernel Crash Resolution Benchmark for All | [paper](https://arxiv.org/abs/2602.02690) | - | ★★★★☆ | Live-kBench evaluates agents on fresh Linux kernel crash-resolution tasks. |
| 2026-05 | ICML 2026 | DevEvol: Benchmarking LLM Agents on Continuous Software Evolution | [paper](https://icml.cc/Downloads/2026) | - | ★★★☆☆ | Streaming benchmark over evolving codebases reconstructed from git histories. |

## Deep research and long-horizon information gathering

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2023-11 | ICLR 2024 | GAIA: A Benchmark for General AI Assistants | [paper](https://arxiv.org/abs/2311.12983) | [dataset](https://huggingface.co/datasets/gaia-benchmark/GAIA) | ★★★★☆ | Long-horizon assistant benchmark requiring tools, browsing, and reasoning. |
| 2024-12 | arXiv | TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks | [paper](https://arxiv.org/abs/2412.14161) | [code](https://github.com/TheAgentCompany/TheAgentCompany) | ★★★★☆ | Workplace-style benchmark for long-running agents. |
| 2025-04 | arXiv | BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents | [paper](https://arxiv.org/abs/2504.12516) | - | ★★★☆☆ | Recent benchmark for hard information-seeking and browsing tasks. |
| 2025-04 | arXiv | DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents | [paper](https://arxiv.org/abs/2504.11543) | - | ★★★☆☆ | Dedicated benchmark for multi-step deep research agents. |
| 2025-04 | arXiv | DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments | [paper](https://arxiv.org/abs/2504.03160) | - | ★★★☆☆ | Training-focused deep research agent in realistic environments. |
| 2025-05 | NeurIPS 2025 | WebDancer: Towards Autonomous Information Seeking Agency | [paper](https://arxiv.org/abs/2505.22648) | [code](https://github.com/Alibaba-NLP/WebAgent) | ★★★★☆ | Data-centric SFT/RL pipeline for autonomous multi-step information seeking. |
| 2025-09 | ICLR 2026 | Scaling Generalist Data-Analytic Agents | [paper](https://arxiv.org/abs/2509.25084) | [code](https://github.com/zjunlp/DataMind) | ★★★★☆ | DataMind training recipe for open-source agents over diverse data-analysis files and tasks. |
| 2026-02 | arXiv | AIRS-Bench: A Benchmark for AI Agents on the Full ML Research Lifecycle | [paper](https://arxiv.org/abs/2602.06855) | - | ★★★☆☆ | Evaluates agents across full ML research workflows beyond isolated coding tasks. |

## Agent evaluation and reliability

| Date | Venue | Title | Paper | Code | Rec | Comment |
|---|---|---|---|---|---|---|
| 2023-08 | ICLR 2024 | AgentBench: Evaluating LLMs as Agents | [paper](https://arxiv.org/abs/2308.03688) | [code](https://github.com/THUDM/AgentBench) | ★★★★☆ | Broad multi-environment agent benchmark. |
| 2024-01 | arXiv | AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents | [paper](https://arxiv.org/abs/2401.13178) | [code](https://github.com/hkust-nlp/AgentBoard) | ★★★☆☆ | Multi-turn agent evaluation board. |
| 2024-06 | arXiv | tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains | [paper](https://arxiv.org/abs/2406.12045) | [code](https://github.com/sierra-research/tau-bench) | ★★★★☆ | Evaluates tool-use agents under domain policies and user interaction. |
| 2024-08 | arXiv | ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities | [paper](https://arxiv.org/abs/2408.04682) | [code](https://github.com/apple/ToolSandbox) | ★★★★☆ | Stateful tool-use benchmark with realistic interaction constraints. |
| 2024-10 | ICLR 2025 | AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents | [paper](https://arxiv.org/abs/2410.09024) | - | ★★★★☆ | Measures harmful task completion risk for tool-using LLM agents. |
| 2024-11 | arXiv | RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts | [paper](https://arxiv.org/abs/2411.15114) | [code](https://github.com/METR/RE-Bench) | ★★★★☆ | Realistic research-engineering agent environments with human expert baselines. |
| 2025-04 | COLM 2025 | An Illusion of Progress? Assessing the Current State of Web Agents | [paper](https://arxiv.org/abs/2504.01382) | [code](https://github.com/OSU-NLP-Group/Online-Mind2Web) | ★★★★☆ | Online-Mind2Web benchmark showing live-web agent evaluation gaps. |
| 2025-06 | NeurIPS 2025 D&B | Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge | [paper](https://arxiv.org/abs/2506.21506) | [code](https://github.com/OSU-NLP-Group/Mind2Web-2) | ★★★★☆ | Long-horizon agentic search benchmark with rubric-driven judge agents. |
| 2025-10 | ICLR 2026 | Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation | [paper](https://arxiv.org/abs/2510.11977) | [project](https://hal.cs.princeton.edu/) | ★★★★★ | Standardized cost-aware evaluation harness and leaderboard across agent tasks. |
| 2026-01 | arXiv | Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces | [paper](https://arxiv.org/abs/2601.11868) | [code](https://github.com/harbor-framework/terminal-bench) | ★★★★☆ | Terminal-native long-horizon benchmark for command-line agents. |

## Upstream source lists

| Source repo | Scope | Priority | Notes |
|---|---|---|---|
| [luo-junyu/awesome-agent-papers](https://github.com/luo-junyu/awesome-agent-papers) | LLM agents | P0 | Core agent paper list. |
| [TeleAI-UAGI/Awesome-Agent-Memory](https://github.com/TeleAI-UAGI/Awesome-Agent-Memory) | Agent memory | P0 | Strong fit for memory mechanisms. |
| [YoungDubbyDu/LLM-Agent-Optimization](https://github.com/YoungDubbyDu/LLM-Agent-Optimization) | Agent optimization | P0 | Direct fit for agent optimization. |
| [zhangxjohn/LLM-Agent-Benchmark-List](https://github.com/zhangxjohn/LLM-Agent-Benchmark-List) | Agent benchmarks | P0 | Cross-list under evaluation. |
| [DavidZWZ/Awesome-Deep-Research](https://github.com/DavidZWZ/Awesome-Deep-Research) | Deep research agents | P1 | Useful for search, reasoning, and tool-use agents. |
| [ranpox/awesome-computer-use](https://github.com/ranpox/awesome-computer-use) | Computer-use agents | P2 | Include papers and benchmarks only. |
| [steel-dev/awesome-web-agents](https://github.com/steel-dev/awesome-web-agents) | Web agents | P2 | Include research and benchmark entries only. |
| [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/awesome-code-llm) | Coding and software engineering | P1 | Use coding-agent and SE-agent papers; exclude model leaderboards. |
