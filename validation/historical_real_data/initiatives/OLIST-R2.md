# OLIST-R2 — Order-to-Delivery SLA Exception Diagnostic

**Dataset:** Olist Brazilian E-Commerce  
**Risk tier:** R2 — Customer/operational outcome, read-only diagnostic, reversible; no autonomous financial authority.  
**Environment:** SANDBOX / HISTORICAL REPLAY  

## Hypothesis
Delivery-after-estimated-date exceptions exist in real order timestamps and can be detected deterministically with zero parse failures in the inspected sample.

## Full gate attempt
| Gate | Decision | Evidence/Reason |
|---|---|---|
| G0 Portfolio Entry | DISCOVER | Real-world dataset is relevant; bounded diagnostic objective; simulated sponsor/process-owner roles for framework exercise; no production authority. |
| G1 Experiment Ready | RUN | Read-only/reversible analysis; metric and claim boundary declared before evaluation; source lineage recorded. |
| G2 Evidence | PASS (BOUNDED) | Real raw-row sample n=12 parsed successfully; 2 late-delivery exceptions detected. PASS is bounded to existence/deterministic detection, not prevalence or causal business effect. |
| G3 Production Ready | REMEDIATE | Environment is SANDBOX/HISTORICAL REPLAY; original marketplace, seller, carrier, API/IAM and operational support dependencies are unavailable. |
| G4 Benefits & Scale | HOLD / NOT ELIGIBLE | No G3 Deploy, no intervention, no predeclared organization-real OE period and no BOOKED benefit. |

## Assurance interpretation
Passing G2 does not imply production readiness. This initiative is intentionally allowed to be blocked at G3/G4 when original production environment and organization-real OE evidence are unavailable.
