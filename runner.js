/* One fresh Python worker per run. No learner code runs on the UI thread. */
window.PythonLab=(()=>{
 let worker=null,workerURL=null,timer=null,finish=null;
 const source=`
 import {loadPyodide} from 'https://cdn.jsdelivr.net/pyodide/v0.27.7/full/pyodide.mjs';
 self.onmessage=async({data})=>{
  let scope;
  try{
   const py=await loadPyodide({indexURL:'https://cdn.jsdelivr.net/pyodide/v0.27.7/full/'});
   let output='',truncated=false;
   const write=s=>{if(output.length<6000)output+=(s+'\\n').slice(0,6000-output.length);else truncated=true};
   py.setStdout({batched:write});py.setStderr({batched:write});
   self.postMessage({type:'ready'});
   scope=py.toPy({});
   await py.runPythonAsync(data.code,{globals:scope});
   await py.runPythonAsync(data.tests,{globals:scope});
   self.postMessage({type:'result',ok:true,output:output+(truncated?'\\n[输出已截断]':'')});
  }catch(e){self.postMessage({type:'result',ok:false,output:String(e).slice(-6000)});}
  finally{scope?.destroy();}
 };`;
 function cleanup(){clearTimeout(timer);worker?.terminate();worker=null;if(workerURL)URL.revokeObjectURL(workerURL);workerURL=null;}
 function stop(){if(finish){const fn=finish;finish=null;cleanup();fn({ok:false,cancelled:true,output:'运行已停止，可修改后重试。'});}else cleanup();}
 function run(code,tests,onStatus=()=>{}){
  stop();if(code.length>30000)return Promise.resolve({ok:false,output:'代码超过30,000字符，请缩短后重试。'});
  return new Promise(resolve=>{
   const end=result=>{finish=null;cleanup();resolve(result)};finish=resolve;
   workerURL=URL.createObjectURL(new Blob([source],{type:'text/javascript'}));
   try{worker=new Worker(workerURL,{type:'module'});}catch(e){end({ok:false,output:'无法启动Python：'+e.message});return;}
   timer=setTimeout(()=>end({ok:false,output:'Python首次加载超时，请检查网络后重试。'}),60000);
   onStatus('首次运行需要联网加载Python；代码在浏览器内执行。');
   worker.onmessage=({data})=>{if(data.type==='ready'){clearTimeout(timer);onStatus('正在执行代码与断言检查…');timer=setTimeout(()=>end({ok:false,output:'执行超过5秒，已停止。检查是否有无限循环。'}),5000);}else if(data.type==='result')end(data)};
   worker.onerror=e=>end({ok:false,output:'Python加载或执行失败，请检查网络后重试。'+e.message});
   worker.postMessage({code,tests});
  });
 }
 return {run,stop};
})();
