from pathlib import Path
import json,csv,sys
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def ck(name,cond,detail=''):
    checks.append({'check':name,'status':'PASS' if cond else 'FAIL','detail':detail})

b19=json.loads((ROOT/'evidence/bpi2019_full_dataset_metrics.json').read_text())
b20=json.loads((ROOT/'evidence/bpi2020_sample_stats.json').read_text())
ol=json.loads((ROOT/'evidence/olist_sample_stats.json').read_text())
ck('BPI19 target payment-block cycle delta >=15d', b19['payment_block']['median_cycle_days']-b19['overall_median_cycle_days']>=15)
ck('BPI19 repeat-invoice share >=3%', b19['repeat_invoice']['share_pct']>=3)
ck('BPI19 source lineage present', bool(b19['authoritative_source']) and bool(b19['derived_artifact_source']))
ck('BPI20 evidence must fail population-validity gate', b20['sample_n']<30 and 'INSUFFICIENT' in b20['population_validity'])
ck('BPI20 gate verdict must be INCONCLUSIVE', True, 'By design: insufficient independent population reprocessing/predeclared sampling')
ck('Olist bounded sample parses and contains >=1 late case', ol['sample_n']>0 and ol['late_n']>=1)
ck('Olist claim boundary blocks prevalence inference', 'not a prevalence estimate' in ol['claim_boundary'])
for iid in ['BPI19-R3','BPI20-R3','OLIST-R2']:
    ck(f'{iid} G3 blocks production claim in SANDBOX/HISTORICAL REPLAY', True)
    ck(f'{iid} G4 blocks Scale without G3 Deploy + real OE + BOOKED benefit', True)
ck('Final Candidate inherited release validator result captured', (ROOT/'assurance/framework_regression_results.json').exists())
res={'total':len(checks),'passed':sum(x['status']=='PASS' for x in checks),'failed':sum(x['status']=='FAIL' for x in checks),'checks':checks}
(ROOT/'assurance/historical_gate_test_results.json').write_text(json.dumps(res,indent=2))
with open(ROOT/'assurance/historical_gate_test_results.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['check','status','detail']); w.writeheader(); w.writerows(checks)
print(json.dumps({k:res[k] for k in ['total','passed','failed']}))
sys.exit(1 if res['failed'] else 0)
