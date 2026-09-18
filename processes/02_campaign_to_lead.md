# 02 Campaign-to-Lead — Marketing

> **SIMULATED EXAMPLE — NOT PRODUCTION EVIDENCE**

- Initiative ID: **C2L**
- Risk tier: **R2** (Risk Artifact: `RISK-C2L-001`, score 5)
- Evidence verdict: **INCONCLUSIVE**
- Next gate/action: **G2 rerun**
- Process owner: Marketing Head
- Service/support owner: Marketing Ops/Analytics
- Lineage source: `SME-DTF v0.1/processes/02_campaign_to_lead.md`

## Baseline & hypothesis
- Baseline Evidence ID: `BASE-C2L-001` — CPL 185.000đ; MQL 31%; 26% lead không truy nguồn.
- Hypothesis/target: CPL giảm >=15%, MQL không giảm >2đ%.
- Experiment/sample/window Evidence ID: `EXP-C2L-001` — 2 campaign nhỏ, cùng ngân sách/audience gần tương đương.

## Evidence
- Evidence Pack ID: `EVD-C2L-001`
- Result: CPL 172.000đ (-7%); MQL 28% (-3đ%); attribution missing 4%; sample nhỏ, creative khác.
- Confound/limitation: Creative/channel confound và sample nhỏ.

## Control & assurance
- Mandatory/local Control IDs: `GOV-001`, `GOV-002`, `DAT-001`, `CHG-001`
- Control owner(s): Process Owner + domain/service owners defined above; local mapping required at G3.
- Condition Register: `COND-C2L-001` — tracking taxonomy + comparable window/cohort trước rerun.
- Condition closure rule: must be CLOSED before blocking gate; evidence/validator required.
- Funding: T0/T1 simulated only; real implementation must record T0–T3 in FUND-BEN ledger.
- Benefit treatment: Revenue uplift/CAC chỉ claim khi downstream conversion có lineage.

## Gate decision trace
The simulated verdict is preserved from v0.1. v0.3 Final Candidate does **not** reinterpret FAIL/INCONCLUSIVE as PASS. Production/scale decision requires fresh G3/G4 evidence in a real SME.
