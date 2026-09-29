<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,50:1d4ed8,100:14b8a6&height=280&section=header&text=Kevin%20Cho&fontSize=64&fontAlign=50&fontColor=ffffff&desc=LLM%20Systems%20%C2%B7%20RAG%20%C2%B7%20Backend%20%C2%B7%20Applied%20AI&descAlign=50&descAlignY=68" alt="Header Banner" />
</div>

<div align="center">
  <h1>AI Systems Engineer | LLM · RAG · 실시간 AI · 백엔드</h1>
  <p>
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
      <img src="https://img.shields.io/badge/arXiv-%EB%8B%A8%EB%8F%85%EC%A0%80%EC%9E%90%203%ED%8E%B8-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv" />
    </a>
<!-- arxiv-badge ends -->
  </p>
  <p><a href="README.md">English</a> · <strong>한국어</strong></p>
</div>

---

## 오픈소스

상태는 각 저장소가 스스로 밝힌 대로 적었습니다.

| 프로젝트 | 무엇인가 | 상태 |
|---|---|---|
| **[SchemaRouter](https://github.com/JDeun/SchemaRouter)** | OpenAPI·MCP·OPTIMADE·Python 도구를 타입 있는 capability 카탈로그로 정규화하는 RAG/에이전트 실행 계층 | `pip install schemarouter` · **v0.11.0** · MIT · [문서](https://jdeun.github.io/SchemaRouter/) |
| **[Helm](https://github.com/JDeun/Helm)** | 장기 실행 AI 에이전트 워크스페이스를 위한 안정성 우선 운영 CLI | `pip install helm-agent-ops` · **v1.0.0** · MIT |
| **[local_context](https://github.com/JDeun/local_context)** | 에이전트에 위치·시각·날씨 맥락을 주되 좌표를 클라우드가 아닌 개인 메시에만 두는 모듈 | **v0.1.0** · MIT · 의존성 0 |
| **[GrowWise](https://github.com/JDeun/growwise)** | 아이별 지속 맥락 위에 세운 로컬 우선 가족 학습 시스템 | 소스 · pre-1.0 · Apache-2.0 |
| **[AudioScoreTool](https://github.com/JDeun/audio-score-tool)** | 음원·악보 이미지를 편집 가능한 출판 악보로 | 소스 · v0.8.0, 서명 배포 전 · Apache-2.0 |
| **[LangTextFlow](https://github.com/JDeun/LangTextFlow)** | 라이브 현장을 위한 로컬 우선 실시간 다국어 자막 | 소스 · pre-field alpha · Apache-2.0 |
| **[unified-search-mcp-server](https://github.com/JDeun/unified-search-mcp-server)** | 구글 스콜라·웹·유튜브를 한 번에 검색하는 MCP 서버 | 소스 · MIT |

---

## 연구

아래 논문은 모두 단독저자입니다.

<!-- papers starts -->
| 논문 | arXiv | 시점 |
|---|---|---|
| **SchemaRouter: Field-Aware Tool Routing for Efficient Heterogeneous Agentic RAG** | [2608.21375](https://arxiv.org/abs/2608.21375) | 2026-07 |
| **It's Not the Capability: Harness Sensitivity Is Non-Monotone Across LLM Agent Tiers** | [2605.26731](https://arxiv.org/abs/2605.26731) | 2026-05 |
| **It's Not the Size: Harness Design Determines Operational Stability in Small Language Models** | [2605.12129](https://arxiv.org/abs/2605.12129) | 2026-05 |
<!-- papers ends -->

**학회**

- **우수논문상**, 한국통신학회 2025 하계종합학술발표회 — 제1저자, 「AIMI 시스템의 Agentic RAG 적용을 통한 소재 연구 효율성 증대 방안 연구」 (KAILOSLAB × 연세대 신원용 연구실)
- **채택**, 한국통신학회 2026 하계종합학술발표회 — 제1저자, 「소형 언어 모델의 안정적 운영을 위한 실행 하네스 설계: 비단조 현상 및 형식 골격 붕괴 분석」 (DCP 특별세션)

**진행 중**

- 로컬 컨텍스트와 컨텍스트 중재 — 에이전트가 서로 경합하는 맥락 소스를 어떻게 정리할 것인가. 모듈([`local_context`](https://github.com/JDeun/local_context))은 공개했고 논문은 아직입니다.

전부 운영하다 반복해서 부딪힌 한 가지에서 나왔습니다. **모델 자체보다 모델을 감싼 하네스가 더 크게 좌우할 때가 많습니다.**

---

## 강의 · 산학협력

- **성균관대학교** — 산학협력 단일 창구를 인수·운영했고, 「차세대반도체종합설계」 과목의 업체멘토를 **3학기 연속** 맡았으며, 산학협력 수업에 쓰인 RAG 교재와 실습 코드를 제작했습니다.
- **대림대학교** — 교원 26명 대상 「생성형 AI 활용 프로젝트 기획 및 설계」 3시간 특강을 직접 기획·실행했습니다. 교시별 커리큘럼과 무설치 웹 실습 환경까지 구성했습니다.
- **한양여자대학교 × KAILOSLAB** — 글로벌서비스경영과 산학 협업 Intel AI 교육 조교. 학생들의 Intel AI 자격증 취득으로 이어졌습니다.

---

## 주요 작업

### SchemaRouter — 논문과 라이브러리

SchemaRouter는 RAG·에이전트 애플리케이션과 그 바깥의 구조화된 외부 기능 사이에 놓입니다. OpenAPI·MCP·OPTIMADE·Python·플러그인 도구를 타입 있는 capability 카탈로그로 정규화하고, 요청된 데이터에 대해 경계가 분명한 실행 경로를 고른 뒤, **실행 전과 후 양쪽에서** 계약을 다시 검증합니다.

[논문](https://arxiv.org/abs/2608.21375)은 의미 유사도만이 아니라 스키마가 라우팅 문제의 일부여야 한다고 주장합니다. 라이브러리는 그 주장을 설치 가능한 형태로 만든 것입니다.

- 어댑터 5종 — MCP, OpenAPI, OPTIMADE, Python, 플러그인
- 생태계 통합 8종 — LangChain, LangGraph, LlamaIndex, Ollama, OpenTelemetry 등
- 어댑터와 **의사결정 백엔드가 둘 다** 엔트리포인트 플러그인이라, 새 도구 소스나 새 라우팅 전략을 코어 수정 없이 붙일 수 있습니다
- 승인 콜백, 실행 예산, 증거 요구사항, 바인딩 드리프트 감지
- `py.typed`, 국영문 문서 사이트

범위는 의도적으로 좁혔습니다 — 일반 에이전트 프레임워크도, LLM 프로바이더 계층도, RAG 생성기도 **아닙니다.**

### Helm

**Helm**은 장기 실행 AI 에이전트와 워크플로를 위한 오픈소스 운영 계층입니다. 오래 살아 있는 에이전트 시스템을 숨은 런타임 동작에 맡기지 않고 명시적이고 통제 가능하게 만듭니다. 실행 프로파일, 컨텍스트 하이드레이션, 매니페스트 기반 스킬 정책, 감사 가능성, 운영 경계가 그 수단입니다.

### 제품 작업 — 반복되는 한 가지 문제

[**LangTextFlow**](https://github.com/JDeun/LangTextFlow), [**GrowWise**](https://github.com/JDeun/growwise), [**AudioScoreTool**](https://github.com/JDeun/audio-score-tool)은 서로 다른 제품이지만 밑바닥 구조가 같습니다. **불완전한 모델 출력 → 검증된 상태 → 사람의 교정 → 최종 산출물.** 확신이 서기 전에 확정해야 하는 자막, 생성된 요약이 조용히 사실의 출처로 승격되면 안 되는 학습 기록, 사용자가 입력하는 대신 고치는 악보 초안. 셋 다 로컬 우선이고 FastAPI 기반이며 데스크톱으로 패키징됩니다.

### 회사 업무 · 비공개 작업

제 실무의 상당 부분은 공개 저장소로 낼 수 없습니다. 멀티 에이전트 RAG와 오케스트레이션, 사내 AI 어시스턴트, 문서·정형 데이터 파이프라인, 이종 소스에 걸친 검색과 라우팅이 포함됩니다. 대개는 모호한 비즈니스 요구를 남이 유지보수할 수 있는 시스템으로 바꾸는 일이었습니다.

---

## 일하는 방식

국어국문학에서 출발해 AI 시스템으로 왔고, 지금도 흥미로운 문제는 결국 구조에 있다고 생각합니다. 무엇을 사실의 출처로 볼 것인가, 불확실성을 어디서 검증할 것인가, 모델이 틀렸을 때 시스템이 무엇을 하는가.

- **마법보다 명시** — 라우팅·상태·검증·권한·실패 동작은 들여다볼 수 있어야 합니다.
- **데모 품질보다 신뢰성** — 검증과 복구는 사고가 난 뒤 덧붙이는 게 아니라 처음부터 설계에 넣습니다.
- **경계** — 모델에는 한정된 권한과 정해진 실패 방식을 줍니다.
- **추적 가능성** — 입력, 모델의 결정, 변환, 출력은 귀속될 수 있어야 합니다.
- **실패에서 나온 연구** — 반복되는 운영 실패를 측정 가능한 연구 질문으로 바꿉니다.

---

## 연락

LLM 운영 신뢰성, 에이전틱 RAG와 라우팅, 로컬 우선 AI와 프라이버시 경계 — 이런 주제라면 언제든 반갑습니다.

- 이메일: [jdmeekboi@gmail.com](mailto:jdmeekboi@gmail.com)
- LinkedIn: [linkedin.com/in/조용은](https://www.linkedin.com/in/%EC%A1%B0%EC%9A%A9%EC%9D%80)

<div align="center">
  <p><i>모델이 불완전하고 워크플로가 실제가 되어도 명료함을 잃지 않는 AI 시스템을 만듭니다.</i></p>
</div>
