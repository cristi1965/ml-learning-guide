# 从苹果到 GPT · 项目课程

基于 [samitmohan/ML](https://github.com/samitmohan/ML) 固定提交 `2f0931342a5661d2aefd3f21d90301bd4321e057` 的中文学习网页。

- 16节直觉导读 + 32节项目模块课，覆盖数学/NumPy、传统ML、训练组件、CNN/RNN/LSTM、Attention/Transformer、MNIST、MicroGPT与论文实现。
- 每课有具体数值、4步讲解、小测、源码节选与中文注释、可运行的Python练习。
- 158个Python文件映射到课程：标记“精讲入口”或“拓展阅读”。模块路线完整不表示每个文件都经过完整正确性审计。
- 顶部悬浮目录、手机大字模式、可暂停动画、CodeMirror Python编辑器。

## 运行与边界

访问GitHub Pages或打开`course.html`。源码、课程和编辑器可离线阅读；练习首次运行需要联网下载固定版本Pyodide（0.27.7）。Python在新Web Worker内运行，每次执行最多5秒，加载最多60秒，输出限制6000字符，可停止。练习仅使用标准库，是针对原理新增的教学实现，不声称在浏览器训练上游PyTorch/TensorFlow模型。

独立通过要求当前代码通过固定断言；修改代码或测试后需重新检查。载入参考答案后的通过单独标记“辅助通过”，不计作独立完成。它是本机自学记录，不是防作弊考试系统。

`python-exercises.zip`包含48份起始练习和参考解，可用本机Python3运行。完整模型课程另有原仓库命令、依赖与结果观察说明；原仓库脚本可能自动下载数据或启动训练，先读说明。

笔记、源码编辑、小测和练习状态保存在当前浏览器，不上传，不自动跨设备同步。导出笔记JSON用于备份，暂无导入。公开仓库不包含个人学习记录。

## 维护

课程输入在`curriculum/`。运行`python3 scripts/build-course.py`生成`content.js`、单文件`course.html`和练习压缩包。修改课程或界面后都需重建单文件版本。

编辑器复用Go课程CodeMirror组件并切换为Python。Node18+环境运行`npm ci`及`npm run build:editor`。第三方许可见`vendor/EDITOR-LICENSES.txt`。上游源码归原作者，节选固定版本并标明新增注释，不对上游代码重新授权。

发布使用`gh-pages`分支根目录与`.nojekyll`。验证证据在`evidence/`；Python课程练习通过不代表完整训练、真机或真人学习评估通过。

## 四周主线（默认入口）

首页为12课，每周3课，约4–6小时：每课40–60分钟，加每周60–90分钟项目整合与短复盘。

1. 模型如何学习：预测、训练与泛化、分类与评估。
2. 语言模型如何工作：向量表示、注意力、逐步生成与温度。
3. 把模型接入资料：输出契约、上下文预算、带来源的检索。
4. 选择方案与验收：工具权限、提示/RAG/微调选择、逐题评估。

每课默认展示具体场景、四步机制、可操作实验、两道带逐项反馈的迁移题和项目交付标准。数学推导、源码注释、原有编辑器与 Python 练习保留在可展开的深入入口。`library.html` 是原48课知识库，支持 `#lesson=0`（从0开始）直达课程；原有笔记与练习记录使用原存储键，不迁移、不清空。

主线浏览器实验为确定性教学计算或明确标注的预置结果，不是实际模型/API效果测试。选择题通过仅表示这些题答对，项目仍需依据标准自查。四周结束目标为全局理解、局部实验与可复查评估方案，不能等同于独立训练大模型或生产系统验收。

构建：先运行 `python3 scripts/build-course.py`，再运行 `python3 scripts/build-mainline.py`。后者生成主线数据及可离线打开的 `course.html`；`library-offline.html` 是内联资源的知识库（Python运行首次加载仍需要网络）。主线内容在 `curriculum/mainline-{first,second}.json`，浏览器回归为 `scripts/test-mainline.cjs`。旧48课回归改为访问 `/library.html`。
