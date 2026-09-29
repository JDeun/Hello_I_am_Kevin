<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,50:1d4ed8,100:14b8a6&height=280&section=header&text=Kevin%20Cho&fontSize=64&fontAlign=50&fontColor=ffffff&desc=LLM%20Systems%20%C2%B7%20RAG%20%C2%B7%20Backend%20%C2%B7%20Applied%20AI&descAlign=50&descAlignY=68" alt="Header Banner" />
</div>

<div align="center">
  <h1>AI Systems Engineer | LLM · RAG · Realtime AI · Backend</h1>
  <p>
    I build reliable AI systems that connect language models, retrieval, realtime pipelines, and real product workflows —<br>
    and I publish the research that comes out of their failure modes.<br>
    LLM·RAG·실시간 AI를 실제 서비스 구조 안에서 안정적으로 운영하기 위한 시스템을 설계하고 구현합니다.
  </p>

  <p>
    <a href="mailto:jdmeekboi@gmail.com">
      <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
    </a>
    <a href="https://www.linkedin.com/in/%EC%A1%B0%EC%9A%A9%EC%9D%80" target="_blank">
      <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
    </a>
    <!-- arxiv-badge starts -->
    <a href="https://arxiv.org/search/?searchtype=author&query=Yong-eun+Cho" target="_blank">
      <img src="https://img.shields.io/badge/arXiv-3%20sole--author%20papers-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv" />
    </a>
<!-- arxiv-badge ends -->
  </p>
  <p><strong>English</strong> · <a href="README.ko.md">한국어</a></p>
</div>

---

## Open Source

Everything below is public and verifiable. Each status is the one the repository gives itself, not a kinder one.

| Project | What it is | Status |
|---|---|---|
| **[SchemaRouter](https://github.com/JDeun/SchemaRouter)** | Typed capability retrieval and execution layer for RAG and LLM agents across OpenAPI, MCP, OPTIMADE, and Python tools | `pip install schemarouter` · **v0.10.0** · MIT · [docs](https://jdeun.github.io/SchemaRouter/) |
| **[Helm](https://github.com/JDeun/Helm)** | Stability-first operations CLI for long-running AI agent workspaces | `pip install helm-agent-ops` · **v1.0.0** · MIT |
| **[local_context](https://github.com/JDeun/local_context)** | Location, time, and weather context for agents, kept on your own mesh instead of a cloud | **v0.1.0** · MIT · zero dependencies |
| **[GrowWise](https://github.com/JDeun/growwise)** | Local-first family learning system built on persistent child-specific context | source · pre-1.0 · Apache-2.0 |
| **[AudioScoreTool](https://github.com/JDeun/audio-score-tool)** | Audio and sheet-music images into editable, publication-ready scores | source · v0.8.0, before signed release · Apache-2.0 |
| **[LangTextFlow](https://github.com/JDeun/LangTextFlow)** | Realtime multilingual captions for live events, local-first | source · pre-field alpha · Apache-2.0 |
| **[unified-search-mcp-server](https://github.com/JDeun/unified-search-mcp-server)** | One MCP server across Google Scholar, web, and YouTube | source · MIT |

---

## Research

Every paper below is sole-author, and each came out of a failure I hit while running the systems above.

<!-- papers starts -->
| Paper | arXiv | Date |
|---|---|---|
| **SchemaRouter: Field-Aware Tool Routing for Efficient Heterogeneous Agentic RAG** | [2608.21375](https://arxiv.org/abs/2608.21375) | 2026-07 |
| **It's Not the Capability: Harness Sensitivity Is Non-Monotone Across LLM Agent Tiers** | [2605.26731](https://arxiv.org/abs/2605.26731) | 2026-05 |
| **It's Not the Size: Harness Design Determines Operational Stability in Small Language Models** | [2605.12129](https://arxiv.org/abs/2605.12129) | 2026-05 |
<!-- papers ends -->

**Conference**

- **Outstanding Paper Award (우수논문상)**, KICS Summer 2025 — first author, *"Improving Materials Research Efficiency through Agentic RAG in the AIMI System"* (KAILOSLAB × Yonsei Shin Won-yong Lab)
- **Accepted**, KICS Summer 2026 — first author, *"Execution Harness Design for Stable Operation of Small Language Models: Non-Monotonicity and Formal Skeleton Collapse"* (DCP special session)

**In progress**

- Local context and context arbitration — how local models and agents should resolve competing context sources and decide what may influence a response. The open-source module ([`local_context`](https://github.com/JDeun/local_context)) is published; the paper is not yet.

The recurring finding: **the harness around a model often matters more than the model.** Adding an incomplete wrapper can perform *worse* than calling the base model directly, and that effect is not monotone across capability tiers.

---

## Teaching & Industry Collaboration

- **Sungkyunkwan University** — ran the single point of contact for industry–academia collaboration, served as industry mentor for *Next-Generation Semiconductor Capstone Design* for **three consecutive semesters**, and authored the RAG course material and lab code used in the collaboration course.
- **Daelim University** — designed and delivered a 3-hour faculty seminar, *"Planning and Designing Projects with Generative AI,"* for 26 instructors, including the per-session curriculum and a zero-install web lab environment.
- **Hanyang Women's University × KAILOSLAB** — teaching assistant for the Intel AI industry-collaboration program; students went on to earn Intel AI certification.

---

## Selected Work

### SchemaRouter — the paper and the library, same hand

SchemaRouter sits between a RAG/agent application and its structured external capabilities. It normalizes OpenAPI, MCP, OPTIMADE, Python, and plugin-defined tools into a typed capability catalog, selects a bounded executable route, and validates the contract **both before and after** execution.

The [paper](https://arxiv.org/abs/2608.21375) argues that schemas belong in the routing problem rather than semantic similarity alone. The library is that argument, installable:

- 5 adapters — MCP, OpenAPI, OPTIMADE, Python, plugins
- 8 ecosystem integrations — LangChain, LangGraph, LlamaIndex, Ollama, OpenTelemetry, and others, each with docs
- adapters **and** decision backends are both entry-point plugins, so new tool sources or routing strategies need no core changes
- approval callbacks, execution budgets, evidence requirements, binding-drift detection
- `py.typed`, published to PyPI, bilingual docs site

It is deliberately **not** a general agent framework, an LLM provider layer, or a RAG generator — its own README says so, to keep the scope from creeping.

> Status: Beta / pre-1.0.

### Helm

**Helm** is an open-source operations layer for long-lived AI agents and workflows. It makes persistent agent systems explicit and controllable instead of leaving them to hidden runtime behavior: execution profiles, context hydration, manifest-based skill policy, auditability, and operational boundaries.

> Status: v1.0.0 on PyPI as `helm-agent-ops`.

### Product work — one recurring problem

[**LangTextFlow**](https://github.com/JDeun/LangTextFlow), [**GrowWise**](https://github.com/JDeun/growwise), and [**AudioScoreTool**](https://github.com/JDeun/audio-score-tool) are different products with the same shape underneath: **imperfect model output → validated state → human correction → final artifact.** Captions that must commit before they are certain; a learning record where generated summaries must never quietly become the source of truth; a score draft the user corrects rather than enters.

All three are local-first, FastAPI-based, and packaged for desktop. Each repository documents its own architecture and states its own release status — I would rather link them than summarize them here.

### Company & Private Work

Much of my production work cannot be published as a public repository. That work has included multi-agent RAG and orchestration systems, internal AI assistants and research systems, document and structured-data pipelines, retrieval and routing across heterogeneous sources, backend APIs, validation and answer-judging flows, and turning ambiguous business requirements into maintainable AI systems.

This profile is a public-facing selection of how I think and build, not a complete inventory.

---

## How I Work

I came to AI systems from Korean literature, and I still think the interesting problems are about structure: what counts as the canonical source, where uncertainty gets checked, and what a system does when the model is wrong.

- **Explicit over magical** — routing, state, validation, permissions, and failure behavior should be inspectable and explainable.
- **Reliability over demo quality** — validation and recovery are designed in, not added after the first incident.
- **Boundaries** — models get explicit authority and explicit failure limits.
- **Traceability** — inputs, model decisions, transformations, and outputs should be attributable.
- **Research from failure modes** — recurring production failures become measurable research questions, which is where every paper above came from.

---

## Contact

Happy to talk about LLM operational reliability, agentic RAG and routing, realtime ASR pipelines, structured output and execution harnesses, or local-first AI and privacy boundaries.

- Email: [jdmeekboi@gmail.com](mailto:jdmeekboi@gmail.com)
- LinkedIn: [linkedin.com/in/조용은](https://www.linkedin.com/in/%EC%A1%B0%EC%9A%A9%EC%9D%80)

<div align="center">
  <p><i>Building AI systems that remain clear when the model is imperfect and the workflow becomes real.</i></p>
</div>
