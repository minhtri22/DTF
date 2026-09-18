# 05 Invoice-to-Cash — Finance

> **SIMULATED EXAMPLE — NOT PRODUCTION EVIDENCE**

- Initiative ID: **I2C**
- Risk tier: **R3** (Risk Artifact: `RISK-I2C-001`, score 10)
- Evidence verdict: **PASS**
- Next gate/action: **G3**
- Process owner: AR/Finance Process Owner
- Service/support owner: Finance Systems Owner
- Lineage source: `SME-DTF v0.1/processes/05_invoice_to_cash.md`

## Baseline & hypothesis
- Baseline Evidence ID: `BASE-I2C-001` — DSO 48d; overdue >30d 18%; reminder coverage 52%; missing dispute owner 23%.
- Hypothesis/target: Overdue >30d giảm >=20% relative.
- Experiment/sample/window Evidence ID: `EXP-I2C-001` — 40 B2B customers; 6 tuần.

## Evidence
- Evidence Pack ID: `EVD-I2C-001`
- Result: Overdue 13% (-27,8% relative); reminder 96%; missing owner 2%; cohort DSO -5d.
- Confound/limitation: Seasonality/customer-mix cohort comparability.

## Control & assurance
- Mandatory/local Control IDs: `GOV-001`, `GOV-002`, `IAM-001`, `SOD-001`, `DAT-001`, `DAT-002`, `RES-002`, `BEN-001`
- Control owner(s): Process Owner + domain/service owners defined above; local mapping required at G3.
- Condition Register: `COND-I2C-001` — Finance validates cohort/benefit + dispute/write-off SoD.
- Condition closure rule: must be CLOSED before blocking gate; evidence/validator required.
- Funding: T0/T1 simulated only; real implementation must record T0–T3 in FUND-BEN ledger.
- Benefit treatment: Working-capital/revenue collection; Finance validation required.

## Gate decision trace
The simulated verdict is preserved from v0.1. v0.3 Final Candidate does **not** reinterpret FAIL/INCONCLUSIVE as PASS. Production/scale decision requires fresh G3/G4 evidence in a real SME.
