from pathlib import Path
import json,subprocess,ast,hashlib
root=Path(__file__).resolve().parents[1];data=json.loads((root/'content.js').read_text()[len('window.COURSE='):-1]);rows=[]
for l in data['lessons']:
 code=l['code'];f=Path('/tmp/ml_repo_codex')/l['source'];src=f.read_text().splitlines()
 for line in code['lines']:
  if line['line'] is not None:assert src[line['line']-1]==line['text'],(l['id'],line)
 for variant in ['starter','solution']:
  text=l['lab'][variant]+'\n'+l['lab']['tests'];ast.parse(text)
  result=subprocess.run(['python3','-c',text],capture_output=True,text=True,timeout=5)
  assert (result.returncode==0)==(variant=='solution'),(l['id'],variant,result.stderr)
 rows.append({'lesson':l['id']+1,'solution':'pass','starter':'fails as expected','source':'exact'})
assert len(rows)==48
assert len(data['fileMap'])==len(data['files']) and all(v['lessons'] for v in data['fileMap'].values())
report={'lessons':rows,'sourceFiles':len(data['files']),'hash':hashlib.sha256((root/'content.js').read_bytes()).hexdigest()};(root/'evidence/content-verification.json').write_text(json.dumps(report,indent=2));print('PASS 48 lesson schemas/source excerpts/solutions/starters; all Python files mapped')
