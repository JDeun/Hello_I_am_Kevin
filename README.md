<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,50:1d4ed8,100:14b8a6&height=280&section=header&text=Kevin%20Cho&fontSize=64&fontAlign=50&fontColor=ffffff&desc=LLM%20Systems%20%C2%B7%20RAG%20%C2%B7%20Backend%20%C2%B7%20Applied%20AI&descAlign=50&descAlignY=68" alt="Header Banner" />
</div>

<div align="center">
  <h1>AI Systems Engineer | LLM · RAG · Realtime AI · Backend</h1>
  <p>
    I build reliable AI systems from language models, retrieval, realtime pipelines, and product workflows.<br>
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

Each status below is the one the repository gives itself.

| Project | What it is | Status |
|---|---|---|
| **[SchemaRouter](https://github.com/JDeun/SchemaRouter)** | Typed routing and execution across OpenAPI, MCP, OPTIMADE, and Python tools | `pip install schemarouter` · **v0.11.0** · MIT · [docs](https://jdeun.github.io/SchemaRouter/) |
| **[Helm](https://github.com/JDeun/Helm)** | Operations CLI for long-running agent workspaces | `pip install helm-agent-ops` · **v1.0.0** · MIT |
| **[local_context](https://github.com/JDeun/local_context)** | Place, time, and weather for agents — on your own mesh, not a cloud | **v0.1.0** · MIT · zero dependencies |
| **[GrowWise](https://github.com/JDeun/growwise)** | Family learning app with persistent per-child context | source · pre-1.0 · Apache-2.0 |
| **[AudioScoreTool](https://github.com/JDeun/audio-score-tool)** | Audio and score images into editable sheet music | source · v0.8.0, before signed release · Apache-2.0 |
| **[LangTextFlow](https://github.com/JDeun/LangTextFlow)** | Realtime multilingual captions for live events | source · pre-field alpha · Apache-2.0 |
| **[unified-search-mcp-server](https://github.com/JDeun/unified-search-mcp-server)** | One MCP server across Google Scholar, web, and YouTube | source · MIT |

---

## Research

Every paper below is sole-author.

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

- Local context and context arbitration — how agents should resolve competing context sources. The module ([`local_context`](https://github.com/JDeun/local_context)) is published; the paper is not yet.

All of it comes from one finding I kept running into: **the harness around a model often matters more than the model.**

---

## Teaching & Industry Collaboration

- **Sungkyunkwan University** — ran the single point of contact for industry–academia collaboration, served as industry mentor for *Next-Generation Semiconductor Capstone Design* for **three consecutive semesters**, and authored the RAG course material and lab code used in the collaboration course.
- **Daelim University** — designed and delivered a 3-hour faculty seminar, *"Planning and Designing Projects with Generative AI,"* for 26 instructors, including the per-session curriculum and a zero-install web lab environment.
- **Hanyang Women's University × KAILOSLAB** — teaching assistant for the Intel AI industry-collaboration program; students went on to earn Intel AI certification.

---

## Selected Work

### SchemaRouter — paper and library

SchemaRouter sits between a RAG or agent application and the tools it calls. It normalizes OpenAPI, MCP, OPTIMADE, Python, and plugin-defined tools into one typed catalog, picks a bounded route for the request, and checks the contract **both before and after** execution.

The [paper](https://arxiv.org/abs/2608.21375) argues that schemas belong in the routing problem, not just semantic similarity. The library is that argument, installable:

- 5 adapters — MCP, OpenAPI, OPTIMADE, Python, plugins
- 8 ecosystem integrations — LangChain, LangGraph, LlamaIndex, Ollama, OpenTelemetry, and others
- adapters **and** decision backends are both entry-point plugins, so new tool sources or routing strategies need no core changes
- approval callbacks, execution budgets, evidence requirements, binding-drift detection
- `py.typed`, bilingual docs site

It is deliberately **not** a general agent framework, an LLM provider layer, or a RAG generator.

### Helm

**Helm** is an operations layer for agents that stay running. It replaces hidden runtime behavior with things you can inspect and set: execution profiles, context hydration, manifest-based skill policy, audit trails, and operational boundaries.

### Product work — one recurring problem

[**LangTextFlow**](https://github.com/JDeun/LangTextFlow), [**GrowWise**](https://github.com/JDeun/growwise), and [**AudioScoreTool**](https://github.com/JDeun/audio-score-tool) are different products with the same shape underneath: **imperfect model output → validated state → human correction → final artifact.** Captions that must commit before they are certain; a learning record where generated summaries must never quietly become the source of truth; a score draft the user corrects rather than enters. All three are local-first, FastAPI-based, and packaged for desktop.

### Company & Private Work

Much of my production work cannot be published as a public repository. It has included multi-agent RAG and orchestration, internal AI assistants, document and structured-data pipelines, and retrieval across heterogeneous sources. Mostly it has meant turning ambiguous business requirements into systems someone else can maintain.

---

## How I Work

I came to AI systems from Korean literature, and I still think the interesting problems are about structure: what counts as the canonical source, where uncertainty gets checked, and what a system does when the model is wrong.

- **Explicit over magical** — routing, state, validation, permissions, and failure behavior should be inspectable.
- **Reliability over demo quality** — validation and recovery are designed in, not added after the first incident.
- **Boundaries** — models get bounded authority and a defined failure mode.
- **Traceability** — inputs, model decisions, transformations, and outputs should be attributable.
- **Research from failure modes** — recurring production failures become measurable research questions.

---

## Contact

Happy to talk about LLM operational reliability, agentic RAG and routing, or local-first AI and privacy boundaries.

- Email: [jdmeekboi@gmail.com](mailto:jdmeekboi@gmail.com)
- LinkedIn: [linkedin.com/in/조용은](https://www.linkedin.com/in/%EC%A1%B0%EC%9A%A9%EC%9D%80)

<div align="center">
  <p><i>Building AI systems that remain clear when the model is imperfect and the workflow becomes real.</i></p>
</div>
