# BPI20-R3 — Request-for-Payment Approval & Rework Diagnostic

**Dataset:** BPI Challenge 2020 — Request for Payment  
**Risk tier:** R3 — Payment approval is a direct R3 monetary-authority trigger.  
**Environment:** SANDBOX / HISTORICAL REPLAY  

## Hypothesis
Rejected/resubmitted requests have materially longer end-to-end cycle than straight-through requests.

## Full gate attempt
| Gate | Decision | Evidence/Reason |
|---|---|---|
| G0 Portfolio Entry | DISCOVER | Real-world dataset is relevant; bounded diagnostic objective; simulated sponsor/process-owner roles for framework exercise; no production authority. |
| G1 Experiment Ready | RUN | Read-only/reversible analysis; metric and claim boundary declared before evaluation; source lineage recorded. |
| G2 Evidence | INCONCLUSIVE | Raw real traces show variance and rework; convenience sample n=3 gives rework median 34.79d vs straight-through 3.29d, but the full 36,796-event population was not independently reprocessed and sampling was not predeclared. Evidence validity is insufficient for a population claim. |
| G3 Production Ready | NOT ELIGIBLE / REMEDIATE | Blocking G2 is not PASS/closed, and environment is SANDBOX/HISTORICAL REPLAY. G3 therefore cannot proceed to Deploy. |
| G4 Benefits & Scale | HOLD / NOT ELIGIBLE | No G3 Deploy; no eligible organization-real OE or BOOKED benefit. |

## Assurance interpretation
Passing G2 does not imply production readiness. This initiative is intentionally allowed to be blocked at G3/G4 when original production environment and organization-real OE evidence are unavailable.
