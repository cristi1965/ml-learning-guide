from pathlib import Path
import json,hashlib,zipfile
root=Path(__file__).resolve().parents[1]
source=json.loads((root/'curriculum/source.json').read_text())
lessons=[]
for name in ['intro','foundations','models']:
 f=root/f'curriculum/{name}.json'
 if f.exists():lessons+=json.loads(f.read_text())
assert [l['id'] for l in lessons]==list(range(len(lessons)))
for l in lessons:
 assert len(l['walk'])==4 and len(l['options'])==3 and l['answer'] in range(3)
 assert all(l['lab'].get(k) for k in ['goal','starter','solution','tests','hint','expected'])
 assert l['source'] in source['files']
filemap={}
for f in source['files']:
 direct=[l['id'] for l in lessons if l['source']==f]
 if direct:filemap[f]={'lessons':direct,'kind':'精讲入口'};continue
 if f.startswith('numpy/'):ids=[16,17]
 elif f.startswith('algorithms/math/'):ids=[18,19,20]
 elif f.startswith('algorithms/machinelearning/'):ids=[21,22,23,24,25,26,27,28,29,30,31]
 elif f.startswith('algorithms/attention/'):ids=[39,40,41]
 elif f.startswith('algorithms/labs/'):ids=[35]
 elif f.startswith('algorithms/deeplearning/'):ids=[32,33,34,35,36,37,38]
 elif f.startswith('models/mnist/'):ids=[43,44]
 elif f.startswith('models/'):ids=[42]
 elif f.startswith('papers/resnet/'):ids=[45]
 elif f.startswith('papers/'):ids=[46]
 elif f.startswith('pytorch/'):ids=[32,34,35,44]
 else:ids=[47]
 filemap[f]={'lessons':[i for i in ids if i<len(lessons)],'kind':'拓展阅读'}
source.update(lessons=lessons,fileMap=filemap,version='project-v2')
(root/'content.js').write_text('window.COURSE='+json.dumps(source,ensure_ascii=False)+';')
s=(root/'index.html').read_text()
for name in ['vendor/editor.js','content.js','runner.js','lab-ui.js','app.js']:
 s=s.replace('<script src="'+name+'"></script>','<script>'+(root/name).read_text().replace('</script','<\\/script')+'</script>')
(root/'course.html').write_text(s)
with zipfile.ZipFile(root/'python-exercises.zip','w',zipfile.ZIP_DEFLATED) as z:
 z.writestr('README.txt','每个lesson文件为教学练习，直接python3运行。先补TODO再检查；参考答案在solutions目录。使用标准库，不执行原仓库模型。\n')
 for l in lessons:
  for folder,code in [('',l['lab']['starter']),('solutions/',l['lab']['solution'])]:
   z.writestr(f'{folder}lesson-{l["id"]+1:02d}.py','# '+l['lab']['goal']+'\n'+code+'\n'+l['lab']['tests']+'\nprint("所有检查通过")\n')
print(f'Built {len(lessons)} lessons, {len(filemap)} source mappings')
