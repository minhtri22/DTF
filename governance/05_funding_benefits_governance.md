# FUND-BEN-001 — Funding Release & Benefits Governance

## Funding tranches
| Tranche | Release point | Purpose | Minimum approval |
|---|---|---|---|
| T0 Discovery | G0 | Baseline/discovery/data assessment | Sponsor + Portfolio authority |
| T1 Experiment | G1 | Bounded reversible pilot | Sponsor + budget owner; R3/R4 Finance/Risk challenge |
| T2 Production | G3 | Build/configure, rollout, support | Budget authority + Process Owner + IT/Service; R3/R4 executive per threshold |
| T3 Scale | G4 | Wider rollout/capacity | Sponsor + Finance validation + portfolio authority |

## Benefit taxonomy
- **Hard cash:** booked expense reduction / avoided actual spend with budget action.
- **Revenue uplift:** incremental realized revenue with attribution assumption and comparison basis.
- **Cost avoidance:** future cost credibly avoided; không ghi như hard cash.
- **Capacity release:** hours/FTE capacity made available; chỉ monetize nếu có explicit reuse/avoid-hire action.
- **Risk avoidance:** quantified exposure reduction; tách riêng khỏi cash benefit trừ khi realized.

## Benefit Evidence Grade — mandatory
| Grade | Definition | Permitted claim |
|---|---|---|
| MODELED | Giá trị dựa trên assumption/model/synthetic/business-case formula | Forecast / modeled value only |
| OBSERVED | Kết quả đo được từ operation thực nhưng chưa reconcile với Finance system/source | Observed operational/economic outcome |
| BOOKED | Reconciled tới GL/budget/payroll/contract hoặc Finance-equivalent authoritative source | May be called **realized hard cash** if taxonomy = Hard cash |

**Rule:** `MODELED` hoặc `OBSERVED` không được ghi/biểu diễn như realized hard cash. Finance validator phải xác nhận grade và source reference.

## Benefit record bắt buộc
Benefit ID, type, **Evidence Grade**, baseline owner, formula, source, baseline window, target window, attribution assumption, realization action, gross benefit, one-off cost, recurring cost, net benefit, confidence, Finance validator, Finance source/reconciliation reference, stop-loss/kill trigger.

## Anti-double-count rule
Một benefit chỉ có một primary ledger owner. Cross-initiative dependency phải chỉ rõ phần benefit nào được phân bổ cho initiative nào.
