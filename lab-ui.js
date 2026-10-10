window.LabUI=(()=>{
 const key='ml-labs-v1';let cleanup=()=>{};
 const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 let records={};try{const saved=JSON.parse(localStorage.getItem(key));if(saved&&typeof saved==='object'&&!Array.isArray(saved))records=saved}catch{}
 function mount(lesson,host){cleanup();if(!lesson.lab)return;const lab=lesson.lab,id=lesson.id;let alive=true,serial=0;
 const old=records[id]&&typeof records[id]==='object'?records[id]:{};
 const record=records[id]={code:typeof old.code==='string'?old.code:lab.starter,referenceSeen:old.referenceSeen===true,proof:old.proof};
 const save=()=>{try{localStorage.setItem(key,JSON.stringify(records))}catch{host.querySelector('.lab-storage').textContent='练习代码无法自动保存，请下载保留。'}};
 host.innerHTML=`<h2>动手完成一小段 Python</h2><p>${esc(lab.goal)}</p><p class="muted">这是配套教学练习，使用Python标准库，和上面的原仓库节选分开。首次运行需要联网加载Python；不运行完整PyTorch或TensorFlow训练。</p><textarea class="lab-editor" aria-label="可运行Python练习" spellcheck="false"></textarea><div class="row lab-controls"><button class="primary lab-run">运行并检查</button><button class="lab-stop" disabled>停止</button><button class="lab-reset">恢复起始代码</button><button class="lab-reference">载入参考答案</button><button class="lab-download">下载练习.py</button></div><p class="lab-proof" role="status"></p><pre class="lab-output" aria-live="polite">先运行一次，观察为什么起始代码不能通过，再修改TODO。</pre><details><summary>卡住时看提示</summary><p>${esc(lab.hint)}</p></details><details><summary>检查什么？查看输入和预期结果</summary><p>${esc(lab.expected)}</p><pre>${esc(lab.tests)}</pre></details><p class="lab-storage" role="status"></p>${lesson.local?`<details><summary>进一步：运行原仓库完整示例</summary><p>${esc(lesson.local.requirements)}</p><pre>${esc(lesson.local.command)}</pre><p>观察：${esc(lesson.local.observe)}</p><p>${esc(lesson.local.boundary)}</p></details>`:''}`;
 const $=s=>host.querySelector(s),editor=$('.lab-editor');editor.value=record.code;window.LearningEditor?.mountCodeEditor(editor);
 function proof(){const p=record.proof;$('.lab-proof').textContent=p&&p.code===editor.value&&p.tests===lab.tests&&p.source===window.COURSE.sha?(p.assisted?'参考答案辅助通过（不计独立完成）':'当前练习已独立通过检查'):'当前代码尚未通过检查';}
 editor.oninput=()=>{record.code=editor.value;save();proof()};
 function cancel(){serial++;window.PythonLab.stop();$('.lab-run').disabled=false;$('.lab-stop').disabled=true;}
 $('.lab-stop').onclick=()=>{cancel();$('.lab-output').textContent='运行已停止，可修改后重试。'};
 $('.lab-reset').onclick=()=>{cancel();editor.value=lab.starter;record.code=lab.starter;record.proof=null;save();proof();$('.lab-output').textContent='已恢复起始代码，请完成TODO。看过参考答案的练习仍保留辅助标记。'};
 $('.lab-reference').onclick=()=>{cancel();editor.value=lab.solution;record.code=lab.solution;record.referenceSeen=true;record.proof=null;save();proof();$('.lab-output').textContent='已载入参考答案。运行后会标记为辅助通过。'};
 $('.lab-run').onclick=async()=>{const generation=++serial,code=editor.value;record.proof=null;save();proof();$('.lab-run').disabled=true;$('.lab-stop').disabled=false;const result=await window.PythonLab.run(code,lab.tests,text=>{if(alive&&generation===serial)$('.lab-output').textContent=text});if(!alive||generation!==serial)return;$('.lab-run').disabled=false;$('.lab-stop').disabled=true;$('.lab-output').textContent=(result.ok?'所有检查通过。\n':'尚未通过。\n')+result.output;if(result.ok&&code===editor.value){record.proof={code,tests:lab.tests,source:window.COURSE.sha,assisted:record.referenceSeen};save();proof()}else if(result.ok){$('.lab-output').textContent+='\n运行期间代码已改变，请重新检查当前版本。'}};
 $('.lab-download').onclick=()=>{const text='# '+lab.goal+'\n# 教学练习；下方为检查条件\n'+editor.value+'\n\n'+lab.tests+'\nprint("所有检查通过")\n',url=URL.createObjectURL(new Blob([text],{type:'text/x-python;charset=utf-8'})),a=document.createElement('a');a.href=url;a.download=`lesson-${id+1}.py`;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000)};
 proof();cleanup=()=>{alive=false;serial++;window.PythonLab.stop()};
 }
 return {mount,unmount:()=>cleanup(),snapshot:()=>JSON.parse(JSON.stringify(records))};
})();
