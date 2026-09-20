<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,50:1d4ed8,100:14b8a6&height=280&section=header&text=Kevin%20Cho&fontSize=64&fontAlign=50&fontColor=ffffff&desc=LLM%20Systems%20%C2%B7%20RAG%20%C2%B7%20Backend%20%C2%B7%20Applied%20AI&descAlign=50&descAlignY=68" alt="Header Banner" />
</div>

<div align="center">
  <h1>AI Systems Engineer | LLM · RAG · Realtime AI · Backend</h1>
  <p>
    I build reliable AI systems that connect language models, retrieval, realtime pipelines, backend infrastructure, and real product workflows.<br>
    LLM·RAG·실시간 AI를 실제 서비스 구조 안에서 안정적으로 운영하기 위한 시스템을 설계하고 구현합니다.
  </p>

  <p>
    <a href="mailto:jdmeekboi@gmail.com">
      <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
    </a>
    <a href="https://www.linkedin.com/in/%EC%A1%B0%EC%9A%A9%EC%9D%80" target="_blank">
      <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
    </a>
    <img src="https://img.shields.io/badge/Focus-LLM%20Systems%20%26%20Reliable%20AI-0f766e?style=for-the-badge" alt="Focus" />
  </p>
</div>

---

## About Me

I am Kevin Cho, an AI systems engineer with a background in Korean literature and a strong interest in how language, structure, and software architecture shape reliable AI products.

현재는 **LLM, RAG, agent orchestration, backend architecture, validation, local-first AI**를 중심으로 일하고 있습니다.

모델을 연결하는 것 자체보다 더 중요한 문제에 관심이 있습니다.

- 어떤 입력과 상태가 시스템의 canonical source가 되어야 하는가
- 모델 출력의 불확실성을 어디에서 검증하고 차단할 것인가
- retrieval, routing, tool use를 어떻게 명시적이고 추적 가능하게 만들 것인가
- 작은 데모를 반복 가능한 제품과 운영 시스템으로 어떻게 바꿀 것인가

저는 AI 기능을 독립된 마법 상자로 보기보다, **명확한 계약과 상태, 검증 경계, 관측 가능성을 가진 소프트웨어 시스템의 한 구성요소**로 다루는 편입니다.

---

## Current Focus

- **LLM systems** — structured output, validation, execution harnesses, operational reliability
- **Agentic RAG** — routing, tool selection, schema-aware retrieval, multi-agent orchestration
- **Realtime AI systems** — streaming ASR, caption stabilization, model failover, multilingual fan-out
- **Persistent context** — source-grounded derived memory, provenance, context arbitration, rebuildable state
- **Backend architecture** — FastAPI services, state management, APIs, data pipelines, observability
- **Local-first AI** — local models, private state, controlled external access, local/remote trust boundaries
- **Human-in-the-loop AI** — imperfect model output → validation → correction → usable final artifact
- **Applied research** — turning recurring production failures into measurable research questions

---

## Research

My research interests are closely connected to production AI systems: reliability, routing, context, validation, and operational behavior under imperfect models.

### LLM / SLM Operational Reliability

**It’s Not the Size: Harness Design Determines Operational Stability in SLMs**

Research on how execution harness design changes the operational stability of small language models, including non-monotonic behavior where adding an incomplete wrapper can perform worse than using the base model directly.

Key themes:

- structured-output reliability
- planning / validation / recovery stages
- schema conformance
- non-monotonic harness effects
- operational metrics beyond raw model quality

### SchemaRouter

Research on **schema-aware routing for agentic RAG and tool ecosystems**.

Instead of routing only by semantic similarity, SchemaRouter treats tool and field schemas as part of the routing problem, with the goal of reducing unnecessary tool exposure and improving structured tool selection.

Key themes:

- tool / field schema graphs
- routing under large tool spaces
- structured tool selection
- agentic retrieval
- reducing context and decision overhead

### Local Context & Context Arbitration

Ongoing research on how local models and agents should resolve competing context sources and decide what information should influence a response or action.

Key themes:

- local context stores
- context priority and arbitration
- bounded context injection
- local / remote model cooperation
- persistent agent workflows

Public experimental repository:
- [`JDeun/local_context`](https://github.com/JDeun/local_context)

### Academic / Research Activity

- Best Paper Award, KICS 2025
- Research and presentations on LLM/RAG systems, SLM reliability, and agentic retrieval
- Applied research derived from real system design and production constraints

---

## Selected Work

### Helm

**Helm** is an open-source operations layer for long-lived AI agents and workflows.

It focuses on making persistent agent systems explicit and controllable rather than relying on hidden runtime behavior.

Core ideas include:

- execution profiles
- context hydration
- manifest-based skill policy
- auditability
- safer extensibility for local and hosted models
- operational boundaries for long-lived agents

Repository:
- [`JDeun/Helm`](https://github.com/JDeun/Helm)

### LangTextFlow

**LangTextFlow** is a local-first, open-source realtime multilingual caption system for live events.

It turns microphone audio into progressively stabilized captions, applies bounded AI correction, fans one source caption out to multiple target languages, and serves the result to audience phones, projectors, and OBS surfaces.

The project is built around the failure modes of realtime AI rather than a single-model demo:

- streaming ASR with VibeVoice and faster-whisper fallback
- explicit caption lifecycle from partial recognition to committed translation
- correction and multi-target translation as separate model roles
- one-way failover and bounded queues for realtime degradation
- glossary, hotword, and document context for domain terminology
- FastAPI + React + Tauri desktop architecture
- local Ollama and explicit OpenAI-compatible remote-provider boundaries
- local SQLite history and SRT / WebVTT / TXT / JSON export
- Browser E2E, accessibility, adversarial/security, load/soak, CodeQL, SBOM, and packaging CI

The public repository is intentionally described as a **pre-field alpha / code-complete candidate**: the code-level product path is implemented, while real venue acceptance, long-duration hardware validation, and production signing/notarization remain separate operational evidence.

Repository:
- [`JDeun/LangTextFlow`](https://github.com/JDeun/LangTextFlow)

### GrowWise

**GrowWise** is a local-first family learning system built around persistent child-specific context and a closed learning loop: **record → next activity → real experience → record again**.

From an engineering perspective, it explores how a product can use long-term AI context without turning generated summaries into hidden source-of-truth state.

It combines:

- Markdown as the authoritative source of truth with rebuildable SQLite projections
- hybrid retrieval plus graph-linked context
- a source-grounded derived Learning Wiki for longitudinal synthesis
- provenance links, source fingerprints, invalidation, backup, restore, and child-scoped purge
- raw-record-over-derived-memory trust ordering
- local multimodal Ollama models with hardware-aware model selection
- deterministic degradation when AI is unavailable
- prompt-injection boundaries and explicit local/remote model privacy gates
- parent-reviewable educational material generation
- FastAPI + React + Tauri desktop architecture
- cross-platform CI, CodeQL, secret scanning, dependency hygiene, and authenticated sidecar smoke

The project is currently **pre-1.0**. Its code-level product path and automated hardening are implemented; long-term household dogfooding, real-device model acceptance, signing/notarization, and updater acceptance remain operational validation work.

Repository:
- [`JDeun/growwise`](https://github.com/JDeun/growwise)

### AudioScoreTool

**AudioScoreTool** is a local-first AI-assisted music transcription and score production environment that turns audio, existing scores, and notation data into editable publication-ready sheet music.

It combines:

- automatic music transcription
- OMR for existing sheet music
- chord and optional lyric analysis
- canonical MusicXML state
- SQLite-based song and revision management
- validation and human correction
- publication layout and final export
- desktop packaging and release workflows

What interests me most about this project is not transcription alone, but the full path from **imperfect model output → validated state → human correction → managed revision → final artifact**.

Repository:
- [`JDeun/audio-score-tool`](https://github.com/JDeun/audio-score-tool)

### Company & Private Work

Much of my production work cannot be published as a public repository.

That work has included:

- multi-agent RAG and orchestration systems
- internal AI assistants and research systems
- document, patent, literature, and structured-data pipelines
- retrieval and routing across heterogeneous data sources
- backend APIs and service integration
- validation, answer judging, and failure recovery flows
- workflow automation for internal operations
- converting ambiguous business requirements into maintainable AI systems

This profile is therefore a public-facing selection of how I think and build, not a complete inventory of everything I have worked on.

---

## Engineering Approach

### Explicit over Magical

I prefer systems where routing, state, validation, permissions, and failure behavior can be inspected and explained.

### Reliability over Demo Quality

A system that works once is less interesting than one that remains understandable under repeated use, imperfect inputs, and model variation.

### Structure before Complexity

I reduce ambiguity first: canonical state, contracts, boundaries, schemas, and responsibilities should be clear before more agents or models are added.

### Human Control where It Matters

LLMs are useful generators and judges, but not every decision should be delegated to them. Deterministic checks, explicit gates, and human review remain important parts of reliable AI systems.

### Research from Failure Modes

Recurring production failures are often useful research questions. I prefer measurable failure analysis over treating prompt iteration as the final solution.

---

## Core Tech Stack

### AI / LLM / RAG

<div align="center">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI" />
  <img src="https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white" alt="Google Gemini" />
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain" />
  <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" alt="LangGraph" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch" />
</div>

- LLM orchestration and structured generation
- agentic RAG / CRAG-style validation flows
- persistent context, provenance, and derived-memory design
- streaming ASR, caption correction, and multilingual translation pipelines
- tool routing and schema-aware systems
- local and hosted model integration
- embeddings, vector retrieval, reranking, evaluation

### Backend

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white" alt="Node.js" />
  <img src="https://img.shields.io/badge/REST%20API-005571?style=for-the-badge" alt="REST API" />
</div>

- FastAPI / Python service architecture
- asynchronous jobs and background workers
- API integration and tool adapters
- stateful workflow services
- data ingestion and processing pipelines

### Product Runtime / Desktop

<div align="center">
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React" />
  <img src="https://img.shields.io/badge/Tauri-24C8DB?style=for-the-badge&logo=tauri&logoColor=white" alt="Tauri" />
  <img src="https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white" alt="Rust" />
  <img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama" />
</div>

- React interfaces for operator, family, review, and desktop workflows
- Tauri desktop shells and authenticated local sidecar processes
- local model/runtime setup, health checks, fallback, and hardware-aware configuration
- Windows/macOS packaging, cross-platform validation, and release plumbing

### Data / Storage / Infrastructure

<div align="center">
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
</div>

- relational and document data modeling
- vector stores and retrieval indexes
- local-first persistence
- reproducible development and deployment environments
- provenance, revision, and audit-oriented data design

---

## What I Value in AI Systems

| Principle | What it means in practice |
|---|---|
| **Clarity** | State, contracts, routes, and responsibilities should be inspectable. |
| **Reliability** | Validation and recovery should be designed, not added after failures appear. |
| **Traceability** | Inputs, model decisions, transformations, and final outputs should be attributable. |
| **Boundaries** | Models should have explicit authority and failure limits. |
| **Durability** | The architecture should survive model changes, new tools, and real operational use. |
| **Product Sense** | Engineering, UX, and documentation should support the same workflow. |

---

## Contact

If you want to talk about:

- LLM systems and operational reliability
- agentic RAG, persistent context, and routing
- realtime ASR / multilingual AI pipelines
- backend architecture for AI products
- structured output, validation, and execution harnesses
- local-first AI, privacy boundaries, and persistent agent workflows
- applied AI research and production failure analysis

you can reach me here:

- Email: `jdmeekboi@gmail.com`
- LinkedIn: `linkedin.com/in/조용은`

---

<div align="center">
  <p><i>Building AI systems that remain clear when the model is imperfect and the workflow becomes real.</i></p>
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:14b8a6,50:1d4ed8,100:0f172a&height=140&section=footer&text=%20&fontSize=24&fontAlign=50&fontColor=ffffff" alt="Footer Banner" />
</div>
