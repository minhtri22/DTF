# SME DIGITAL TRANSFORMATION FRAMEWORK v0.3 FINAL CANDIDATE
## Controlled Real Pilot Ready — Assurance-by-Design + Field-Hardening

**Ngày:** 17/09/2026  
**Nguồn thay đổi:** 4 MEDIUM finding của Synthetic Field Assurance sau khi 6 HIGH đã được đóng ở v0.3 RC.  
**Release decision:** **FINAL CANDIDATE — APPROVED FOR CONTROLLED REAL PILOT**; chưa phải enterprise certification hay bằng chứng organization-real OE.

## Executive summary
V0.3 Final Candidate không redesign F0–F10/G0–G4. Release này harden bốn điểm mà synthetic field validation đã phơi ra: tránh ngoại suy sandbox thành production; khóa OE sample trước khi biết kết quả; tách benefit forecast khỏi observed/booked realization; và buộc RTO/RPO có measurement context.

Fresh retrofit assurance được thực hiện trên lại ba initiative synthetic bằng plan/sample mới. Mục tiêu không phải “chạy lại cho đẹp”, mà kiểm bốn amendment có executable hay không.

## 1. Four MEDIUM → four mandatory Final Candidate controls
| Finding | Final Candidate requirement | Executable validation |
|---|---|---|
| FV-01 Environment Representativeness | G3 có Environment Class + dependency equivalence + claim boundary | 3/3 initiative classified SANDBOX; production claim explicitly prohibited |
| FV-02 OE Sampling Plan | Plan approved trước selection; population/period/method/seed/rare cases | 3 fresh deterministic/stratified samples created from 90-day populations |
| FV-03 Benefit Evidence Grade | MODELED / OBSERVED / BOOKED; only BOOKED realized hard cash | All synthetic benefits regraded MODELED; 0 BOOKED claim |
| FV-04 RTO/RPO Context | unit, start/stop, dependency scope, environment, date/evidence | 3/3 prior recovery tests contextualized as component SANDBOX recovery |

## 2. What changed at G3
G3 giờ yêu cầu `Environment Representativeness Statement` và `RTO/RPO Measurement Context`. R2–R4 không thể chỉ ghi một con số recovery. SANDBOX evidence vẫn hữu ích cho component/design test nhưng **không đủ để nói production resilience validated**. Với R3/R4, end-to-end resilience claim cần PRODUCTION-LIKE hoặc PRODUCTION critical path.

## 3. What changed at G4
G4 giờ yêu cầu `OE Sampling Plan ID` tồn tại trước sample selection. Plan phải khai population, period, sampling unit, method, reproducible selector/seed/query, sample rationale, rare/adverse minimum và exclusion/replacement rule. Post-hoc sample selection không đủ để support OE assurance.

## 4. Benefit evidence hierarchy
| Grade | Meaning | Allowed claim |
|---|---|---|
| MODELED | Formula/assumption/model/synthetic | Forecast / modeled value |
| OBSERVED | Measured in actual operation, not Finance-reconciled | Observed outcome |
| BOOKED | Reconciled to authoritative Finance source | May support realized hard cash if taxonomy = Hard cash |

Synthetic field benefits của CS/AP/WH đều bị hạ/giữ ở **MODELED**; không còn khả năng nhầm “simulated Finance validation” với booked realization.

## 5. Fresh retrofit re-performance
| Initiative | Risk | Fresh OE plan | Fresh sample | Critical control re-performance | Benefit grade | Environment claim |
|---|---:|---|---:|---|---|---|
| CS Ticket Assist | R2 | seed 74031; 10 high-risk + 50 random | 60 | PASS | MODELED | SANDBOX component only |
| AP Approval/Duplicate | R3 | seed 94032; 15 duplicate + 30 high-value + 45 other | 90 | PASS | MODELED | SANDBOX component only |
| Warehouse Receive-to-Stock | R2 | seed 84033; 20 invalid + 20 bypass + 40 clean | 80 | PASS | MODELED | SANDBOX component only |

Fresh sample không thay thế real OE. Nó chứng minh sampling standard và artifact trail có thể thực thi/re-perform.

## 6. Assurance result
- Previous RC HIGH regression: **60/60 PASS**.
- Final Candidate amendment/retrofit suite: **42/42 PASS**.
- Synthetic retrofit: 3/3 fresh OE samples phải re-perform PASS theo control rules.
- Real-world organization effectiveness: **NOT TESTED**.

## 7. Controlled real pilot contract
Real pilot tối thiểu có >=1 R2 + >=1 R3. G3 phải chạy trong environment phù hợp risk với dependency/equivalence thật. G4 phải dùng sample plan predeclared trên transaction population thật. Finance phải grade benefit đúng nguồn; hard-cash claim chỉ khi BOOKED. RTO/RPO phải đo với scope và start/stop rõ.

## 8. Exit criteria để đổi Final Candidate → Final
1. Không có HIGH finding mở.
2. Ít nhất một R3 hoàn thành G0→G4 với DE/OE re-perform được.
3. Production-like/production resilience evidence qua G3 theo new context rules.
4. OE sample được chọn theo plan đã approved trước selection.
5. 30/60/90 benefit có OBSERVED evidence; mọi realized hard cash claim có BOOKED evidence.
6. Independent field assurance xác nhận gate decision không bị management override ngoài waiver/risk-acceptance rule.

**Release conclusion:** framework đủ điều kiện bước vào controlled real pilot; organization-real operating effectiveness vẫn phải được chứng minh bằng pilot thật.
