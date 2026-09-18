# BPI19-R3 — Purchase-to-Pay Payment-Block & Repeat-Invoice Control Diagnostic

**Dataset:** BPI Challenge 2019  
**Risk tier:** R3 — Monetary approval/payment-control and SoD domain trigger.  
**Environment:** SANDBOX / HISTORICAL REPLAY  

## Hypothesis
Payment-block and repeat-invoice cohorts are material operational-control hotspots; payment-block median cycle exceeds overall median by >=15 days and repeat-invoice share >=3%.

## Full gate attempt
| Gate | Decision | Evidence/Reason |
|---|---|---|
| G0 Portfolio Entry | DISCOVER | Real-world dataset is relevant; bounded diagnostic objective; simulated sponsor/process-owner roles for framework exercise; no production authority. |
| G1 Experiment Ready | RUN | Read-only/reversible analysis; metric and claim boundary declared before evaluation; source lineage recorded. |
| G2 Evidence | PASS | Full-dataset derived evidence: payment-block median 85.1d vs overall 64.0d (+21.1d); repeat-invoice share 3.83%. |
| G3 Production Ready | REMEDIATE | Environment is SANDBOX/HISTORICAL REPLAY; original ERP, IAM, network, support, backup/restore and dependency equivalence are unavailable. Production-resilience claim is non-waivable. |
| G4 Benefits & Scale | HOLD / NOT ELIGIBLE | G3 did not DEPLOY; no real production OE sample, no 30/60/90 intervention window and no BOOKED Finance benefit. |

## Assurance interpretation
Passing G2 does not imply production readiness. This initiative is intentionally allowed to be blocked at G3/G4 when original production environment and organization-real OE evidence are unavailable.
