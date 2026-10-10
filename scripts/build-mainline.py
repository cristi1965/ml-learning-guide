from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
lessons=sum([json.loads((r/f'curriculum/mainline-{part}.json').read_text()) for part in ['first','second']],[])
assert [x['id'] for x in lessons]==list(range(12))
library=sum([json.loads((r/f'curriculum/{part}.json').read_text()) for part in ['intro','foundations','models']],[])
for x in lessons:
 assert x['week']==x['id']//3+1 and len(x['mechanism'])==4 and len(x['quizzes'])==2
 assert all(0<=i<48 for i in x['deep']['lessonIds'])
 for q in x['quizzes']: assert len(q['options'])==3 and q['answer'] in range(3)
data='window.MAINLINE='+json.dumps(lessons,ensure_ascii=False)+';window.MAINLINE_LIBRARY='+json.dumps([x['title'] for x in library],ensure_ascii=False)+';'
(r/'mainline-data.js').write_text(data)
s=(r/'index.html').read_text().replace('<link rel="stylesheet" href="mainline.css">','<style>'+(r/'mainline.css').read_text()+'</style>')
for name in ['mainline-data.js','mainline.js']:
 s=s.replace('<script src="'+name+'"></script>','<script>'+(r/name).read_text().replace('</script','<\\/script')+'</script>')
(r/'course.html').write_text(s)
print('Built 12 lessons, 48 mechanisms, 24 transfer questions and 12 experiments')
