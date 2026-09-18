# OE-SAMPLE-001 — Operating Effectiveness Sampling Standard

## Rule
OE Sampling Plan phải được approved/timestamped **before** sample selection và trước reviewer biết sample results.

## Mandatory fields
- Initiative / Control IDs.
- Population definition + population size.
- Period under review.
- Sampling unit.
- Method: random / stratified / systematic / judgmental (judgmental cần rationale).
- Reproducible selector/seed/query where feasible.
- Sample-size rationale.
- Minimum rare/adverse/exception cases.
- Exclusions and treatment of duplicates/replacements.
- Evidence source + extraction timestamp/hash where feasible.
- Reviewer/approver.

## Minimum rules
- Critical controls: sample phải cover applicable transactions; rare adverse cases có thể stratify/oversample nhưng phải tách population inference khỏi targeted challenge.
- Không thay sample chỉ vì phát hiện failure.
- Replacement phải ghi lý do và preserve seed/query lineage.
- R3/R4: Line-2/independent reviewer challenge plan trước execution.
