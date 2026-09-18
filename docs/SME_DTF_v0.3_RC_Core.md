# SME Digital Transformation Framework 0.3-RC — Core Specification

## 1. Release purpose
V0.3-RC giữ backbone **F0–F10 / G0–G4**, nhưng chuyển framework từ “governance có chủ ý” sang **assurance-by-design**: mỗi quyết định có evidence ID, mỗi control có test method, mỗi condition/waiver có expiry, mỗi benefit có taxonomy + Finance validation.

## 2. Non-negotiable principles
1. Problem/value trước solution.
2. Baseline + source lineage trước hypothesis.
3. Experiment phải predeclare target/guardrail/sample/window/stop rule.
4. FAIL và INCONCLUSIVE là outcome hợp lệ; không ép PASS.
5. Process Owner sở hữu outcome; Transformation sở hữu method/evidence orchestration.
6. Risk tier quyết định control depth; không one-size-fits-all.
7. Gate không phải meeting; gate là decision dựa trên mandatory evidence.
8. Production không bắt đầu nếu resilience/support/control chưa đạt.
9. Benefit chỉ được claim theo taxonomy, formula và attribution có thể re-perform.
10. ACCEPTED != CLOSED. Finding chỉ CLOSED sau evidence + independent validation.

## 3. Three-layer operating model
- **Layer A — Strategy & Portfolio:** F0, G0, funding/capacity/dependency.
- **Layer B — Initiative Lifecycle:** F1–F8, G1–G3, evidence/control/resilience.
- **Layer C — Operate & Benefits:** F9–F10, G4, OE testing/benefits/scale-retire.

## 4. Lifecycle F0–F10
| Phase | Mandatory question | Minimum output |
|---|---|---|
| F0 Strategic Mandate | Why this, why now, who owns outcome, risk tier? | Charter, sponsor/owner, Risk Score, portfolio/funding request |
| F1 Context & Value | Pain/value/stakeholders are evidenced? | Context card + stakeholder evidence |
| F2 AS-IS, Baseline & Data | What is measured and can data be trusted? | AS-IS, baseline source refs, Data Scorecard/CDEs |
| F3 Priority & Business Case | Is value worth effort/risk/capacity? | Business case, benefit taxonomy, TCO, T0/T1 request |
| F4 Hypothesis & Metrics | What can falsify the change? | Hypothesis + metric formulas/thresholds |
| F5 Minimum Experiment | Smallest reversible valid test? | Sample/window, comparison, fallback, stop rule |
| F6 Evidence Gate | What does evidence support? | Evidence Pack, source refs, verdict, conditions |
| F7 TO-BE & Control Design | What standard process/control replaces AS-IS? | SOP/RACI/control map/Control IDs |
| F8 Production & Change Readiness | Can it operate safely/reliably/adopted? | DE tests, resilience annex, training, G3 pack |
| F9 Deploy & Hypercare | Is rollout stable and recoverable? | Incident/adoption/reconciliation logs |
| F10 Operate, Benefits & Scale | Are benefit and controls sustainable? | Benefit Ledger, OE tests, G4 decision |

## 5. Gate rules
Canonical rules live in `governance/03_gate_control_matrix.md`. No local template may weaken them.

## 6. Artifact ID convention
`[TYPE]-[INITIATIVE]-[NNN]`, e.g. `EVD-L2Q-001`, `CTRL-L2Q-001`, `COND-L2Q-001`. Artifact Register is the source of traceability.

## 7. Condition and waiver distinction
- **Condition:** required remediation tied to a decision, with due date/blocking gate.
- **Waiver/Risk Acceptance:** explicit temporary acceptance of residual risk for an otherwise unmet requirement; only if the control is waivable.
- Condition cannot be silently converted into waiver.

## 8. Evidence Pack minimum
Initiative ID, simulated/real label, baseline, sample/window, metric formula, raw/source reference, actual result, guardrails, confounds, cost, reviewer, gate decision, sign-offs, condition IDs, lineage to prior artifacts.

## 9. Control assurance
- G3: Design Effectiveness of mandatory controls.
- G4: Operating Effectiveness of critical controls for declared sample/window.
- R4: independent challenge before G3 and G4.

## 10. Release boundary
The included 10 SME-X cases are **SIMULATED EXAMPLES** only. Their evidence demonstrates framework traceability, not operating effectiveness in a real company.
