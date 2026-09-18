# RISK-SCORE-001 — Risk Scoring Matrix

## Mục tiêu
Biến R1-R4 từ mô tả định tính thành phân loại có thể tái thực hiện. Điểm chỉ là baseline; reviewer được phép **nâng tier**, không được hạ tier nếu không có Waiver/Risk Acceptance được phê duyệt.

## Chấm điểm từng chiều: 0–3
| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Financial authority/loss | Không ảnh hưởng | Nhỏ, dễ hoàn tác | Đáng kể / approval-sensitive | Lớn, payment/write-off/treasury/material loss |
| Personal/sensitive data | Không có | Dữ liệu nội bộ không nhạy | PII hạn chế | Sensitive/large-scale PII/HR/candidate |
| Customer/employee rights | Không | Trải nghiệm nhỏ | Service/employee outcome đáng kể | Quyền lợi/eligibility/adverse decision |
| Operational criticality | Tiện ích | Gián đoạn cục bộ | Core process bị ảnh hưởng | Material outage/safety/business continuity |
| Regulatory/contractual | Không | Internal policy | Contract/compliance exposure | Legal/statutory/material regulatory exposure |
| Reversibility | Hoàn tác tức thì | Hoàn tác dễ | Cần remediation đáng kể | Khó/không thể đảo ngược hoàn toàn |

## Tier rule
- **R1:** tổng 0–3 và không chiều nào >1.
- **R2:** tổng 4–8 và không trigger R3/R4.
- **R3:** tổng 9–13 **hoặc** có monetary approval, HR/candidate data, sensitive PII, employee/customer adverse outcome, material SoD requirement.
- **R4:** tổng >=14 **hoặc** có material legal/statutory exposure, safety/business-continuity criticality, irreversible high-impact action, large-value autonomous payment/authority.
- Nếu có nhiều rule, lấy tier cao nhất.

## Mandatory escalation
R3/R4 phải có Line-2 challenge tại G1/G3. R4 phải có independent QA/challenge trước G3 và trước scale tại G4.
