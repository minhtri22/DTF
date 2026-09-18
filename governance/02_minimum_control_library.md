# CTRL-LIB-001 — Minimum Control Library

Mỗi control có Control ID, objective, owner, frequency, evidence, test method và waiver rule. Design Effectiveness được test trước/ở G3; Operating Effectiveness được test tại G4 hoặc theo frequency.

| Control ID | Objective | Domain | Type | Applies | Default owner | Frequency | Evidence | Test method | Waiver |
|---|---|---|---|---|---|---|---|---|---|
| GOV-001 | Named accountable owner | Governance | Preventive | R1-R4 | Process Owner | Continuous | Approved charter/RACI | Verify owner + authority accepted | Không |
| GOV-002 | Decision/audit trail | Governance | Detective | R1-R4 | Process/Service Owner | Per event | Decision log + timestamps | Sample decision trace end-to-end | R4: Không |
| IAM-001 | Least privilege & access review | Security | Preventive | R2-R4 | IT/System Owner | Quarterly + change | Access list/review evidence | Sample users vs role matrix | R4: Không |
| APR-001 | Authority matrix retained | Approval | Preventive | R2-R4 when approval/financial | Process Owner | Per transaction/rule change | Approved authority matrix | Sample routed transactions | R4: Không |
| SOD-001 | Maker-checker / segregation of duties | Financial/Control | Preventive | R3-R4 when money/master changes | Finance/Control Owner | Per transaction/change | Approval + role log | Sample maker vs approver identities | R4: Không |
| DAT-001 | Critical data quality gate | Data | Preventive | R2-R4 | Data Steward | Per load + monthly | DQ scorecard | Recompute CDE quality sample | R4: Không for critical CDE |
| DAT-002 | Reconciliation | Data/Financial | Detective | R2-R4 where system handoff/value | Process/Data Owner | Daily/periodic | Reconciliation report + exceptions | Reperform sample reconciliation | R4: Không |
| PRV-001 | Retention/privacy purpose/access | Privacy | Preventive | R3-R4 with PII | Privacy/Data Owner | At design + annual | Retention rule + access evidence | Inspect policy + sample deletion/access | R4: Không |
| RES-001 | RTO/RPO and recovery test | Resilience | Corrective | R2-R4 production | Service Owner | At G3 + annual | Recovery test report | Inspect measured RTO/RPO vs target | R4: Không |
| RES-002 | Manual fallback/rollback | Resilience | Corrective | R1-R4 | Service/Process Owner | At G3 + change | Drill result | Observe/reperform drill or inspect log | R4: Không |
| RES-003 | Capacity/load threshold | Resilience | Preventive | R2-R4 | Service Owner | At G3 + material growth | Load test/capacity evidence | Compare peak test to declared threshold | R4: Không |
| VEN-001 | Vendor SLA/exit/portability | Third party | Preventive | R2-R4 if vendor | IT/Vendor Owner | Contract + annual | SLA/exit/export test | Inspect SLA and export/exit feasibility | Có, trừ R4 material dependency |
| CHG-001 | Training/adoption readiness | Change | Preventive | R1-R4 | Process Owner | Before rollout | Training + competency + adoption baseline | Sample user competency/adoption | Có với compensating control, không bỏ baseline |
| INC-001 | Incident severity/escalation | Operations | Corrective | R2-R4 | Service Owner | Continuous | Incident log/SLA | Sample incidents vs response targets | R4: Không |
| BEN-001 | Finance-validated benefit | Benefits | Detective | R2-R4 where financial claim | Finance Validator | G4 | Benefit ledger + formula/source | Reperform benefit sample | R4: Không for financial claim |

## Control testing rule
- **Design Effective (DE):** control có owner, trigger/frequency, input/output, evidence location, exception route và test method.
- **Operating Effective (OE):** sample thực tế cho thấy control vận hành đúng trong kỳ; size/range phải khai báo trước.
- R3/R4: mọi mandatory control phải DE trước G3; control critical phải có OE evidence trước G4 scale.
