# 06 Procure-to-Pay — Purchasing + Finance

> **SIMULATED EXAMPLE — NOT PRODUCTION EVIDENCE**

- Initiative ID: **P2P**
- Risk tier: **R3** (Risk Artifact: `RISK-P2P-001`, score 12)
- Evidence verdict: **FAIL**
- Next gate/action: **Remediation then G1**
- Process owner: Procurement Head + AP owner
- Service/support owner: ERP/AP Systems Owner
- Lineage source: `SME-DTF v0.1/processes/06_procure_to_pay.md`

## Baseline & hypothesis
- Baseline Evidence ID: `BASE-P2P-001` — Manual match 14 min/invoice; mismatch 11%; suspected supplier duplicate 8%.
- Hypothesis/target: >85% auto-match; exception <3%.
- Experiment/sample/window Evidence ID: `EXP-P2P-001` — Replay 300 historical invoices; no live payment.

## Evidence
- Evidence Pack ID: `EVD-P2P-001`
- Result: Auto-match 63%; exception 14%; duplicate supplier/tax/unit defects found.
- Confound/limitation: Master-data defects invalidate automation premise.

## Control & assurance
- Mandatory/local Control IDs: `GOV-001`, `GOV-002`, `IAM-001`, `APR-001`, `SOD-001`, `DAT-001`, `DAT-002`, `RES-002`
- Control owner(s): Process Owner + domain/service owners defined above; local mapping required at G3.
- Condition Register: `COND-P2P-001` — supplier master DQ >=98% critical keys + prevention controls before rerun.
- Condition closure rule: must be CLOSED before blocking gate; evidence/validator required.
- Funding: T0/T1 simulated only; real implementation must record T0–T3 in FUND-BEN ledger.
- Benefit treatment: No production benefit claim while FAIL; remediation value tracked separately.

## Gate decision trace
The simulated verdict is preserved from v0.1. v0.3 Final Candidate does **not** reinterpret FAIL/INCONCLUSIVE as PASS. Production/scale decision requires fresh G3/G4 evidence in a real SME.
