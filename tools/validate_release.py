#!/usr/bin/env python3
from pathlib import Path
import re,json,csv,sys
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
tests=[]
def test(tid, desc, ok, evidence): tests.append({'test_id':tid,'description':desc,'result':'PASS' if ok else 'FAIL','evidence':evidence})
def text(rel): return (root/rel).read_text(encoding='utf-8') if (root/rel).exists() else ''
# QA-01
c=text('assurance/finding_closure_register.md')
for q in range(1,7):
    fid=f'QA-0{q}'
    test(f'T-CLOSE-{q:02d}',f'{fid} closure row is CLOSED with validator/date', fid in c and re.search(rf'\| {fid} \| HIGH .*\| CLOSED \| Second Assurance \| 17/09/2026 \|',c) is not None,'assurance/finding_closure_register.md')
# QA-02
g=text('governance/03_gate_control_matrix.md')
for gate in ['G0 Portfolio Entry','G1 Experiment Ready','G2 Evidence','G3 Production Ready','G4 Benefits & Scale']:
    test('T-GATE-'+gate[:2],gate+' defined',gate in g,'governance/03_gate_control_matrix.md')
for phrase in ['Mandatory evidence','Objective threshold / rule','Sign-off & veto','Non-waivable','Condition ID']:
    test('T-GATE-FIELD-'+str(len(tests)),phrase+' present',phrase in g,'governance/03_gate_control_matrix.md')
# QA-03
cards=sorted((root/'processes').glob('*.md'))
req=['SIMULATED EXAMPLE','Risk tier:','Baseline Evidence ID:','Experiment/sample/window Evidence ID:','Evidence Pack ID:','Lineage source:','Mandatory/local Control IDs:','Control owner(s):','Condition Register:','Gate decision trace']
test('T-LIN-COUNT','10 process cards exist',len(cards)==10,'processes/')
for card in cards:
    s=card.read_text(encoding='utf-8')
    test('T-LIN-'+card.stem,'all auditability fields present',all(x in s for x in req),str(card.relative_to(root)))
eps=list((root/'evidence_packs').glob('*.md'))
test('T-EVPACK-COUNT','10 evidence packs exist',len(eps)==10,'evidence_packs/')
# QA-04
r=text('governance/01_risk_scoring_matrix.md'); cl=text('governance/02_minimum_control_library.md')
test('T-RISK-SCORE','Risk scoring has 0-3 dimensions and tier rules',all(x in r for x in ['0–3','R1:','R2:','R3:','R4:','Tier rule']),'governance/01_risk_scoring_matrix.md')
for field in ['Control ID','Default owner','Frequency','Evidence','Test method','Waiver','Operating Effective (OE)']:
    test('T-CTRL-'+str(len(tests)),field+' present in control library',field in cl,'governance/02_minimum_control_library.md')
# QA-05
res=text('governance/06_resilience_standard.md'); g3=text('templates/12_production_change_readiness.md')
for field in ['RTO','RPO','capacity/load','restore test','Cutover rehearsal','reconciliation','Vendor SLA/OLA','Hypercare exit']:
    test('T-RES-'+str(len(tests)),field+' required',field.lower() in (res+' '+g3).lower(),'governance/06_resilience_standard.md + templates/12_production_change_readiness.md')
# QA-06
fb=text('governance/05_funding_benefits_governance.md'); ledger=text('templates/13_funding_benefit_ledger.md')
for field in ['T0 Discovery','T1 Experiment','T2 Production','T3 Scale','Hard cash','Revenue uplift','Cost avoidance','Capacity release','Risk avoidance','Finance validator','Stop-loss']:
    test('T-FUND-'+str(len(tests)),field+' present',field.lower() in (fb+' '+ledger).lower(),'governance/05_funding_benefits_governance.md + templates/13_funding_benefit_ledger.md')
# medium-hardening presence
for rel in ['governance/07_waiver_risk_acceptance.md','governance/08_data_readiness_standard.md','governance/09_portfolio_scoring_capacity.md','governance/10_adoption_exit_standard.md','governance/00_document_control.md']:
    test('T-HARD-'+str(len(tests)),rel+' exists',(root/rel).exists(),rel)
summary={'total':len(tests),'passed':sum(t['result']=='PASS' for t in tests),'failed':sum(t['result']=='FAIL' for t in tests)}
(root/'assurance'/'second_assurance_test_results.json').write_text(json.dumps({'summary':summary,'tests':tests},ensure_ascii=False,indent=2),encoding='utf-8')
with open(root/'assurance'/'second_assurance_test_results.csv','w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['test_id','description','result','evidence']);w.writeheader();w.writerows(tests)
print(json.dumps(summary))
sys.exit(1 if summary['failed'] else 0)
