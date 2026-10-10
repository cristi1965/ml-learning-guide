import json
from pathlib import Path
p=Path('curriculum/intro.json');ls=json.loads(p.read_text())
rows=[
('预测一笔苹果订单','price(weight, unit_price)','return weight * unit_price','assert price(2,3)==6\nassert price(0,3)==0\nassert price(1.5,4)==6','斤数乘单价。'),
('完成一次梯度更新','update(w, rate)','return w - rate * 4 * (2*w-6)','assert abs(update(2,.1)-2.8)<1e-9\nassert abs(update(4,.1)-3.2)<1e-9','新单价等于旧单价减去学习率乘梯度。'),
('计算二分查找下一次猜测','midpoint(low, high)','return (low+high)/2','assert midpoint(0,10)==5\nassert midpoint(0,5)==2.5','中点是上下界的平均值；这不是梯度更新。'),
('把两种商品的费用相加','dot(a, b)','return sum(x*y for x,y in zip(a,b))','assert dot([2,1],[3,4])==10\nassert dot([0,0],[3,4])==0\nassert dot([1,-1],[2,3])==-1','对应元素相乘再求和。'),
('加入固定配送费','predict(x, w, b)','return x*w+b','assert predict(2,3,2)==8\nassert predict(0,3,2)==2','偏置b不随重量增加。'),
('计算召回率','recall(tp, fn)','return tp/(tp+fn) if tp+fn else 0.0','assert recall(3,1)==.75\nassert recall(0,4)==0\nassert recall(0,0)==0','分母是真正的正例总数；本练习无正例时约定为0。'),
('重新计算一个簇的中心','center(points)','return sum(points)/len(points)','assert center([0,2,4])==2\nassert center([10,12])==11','这里用一维点，取均值即可；输入保证非空。'),
('写出负数归零规则','relu(x)','return max(0,x)','assert relu(-2)==0\nassert relu(1)==1\nassert relu(0)==0','比较x和0，返回较大的一个。'),
('手算加法再乘法的梯度','grads(a, b, c)','return (c,c,a+b)','assert grads(2,3,4)==(4,4,5)\nassert grads(2,3,6)==(6,6,5)','对a、b的梯度是c，对c的梯度是a+b。'),
('合并同一节点的多路梯度','accumulate(contributions)','return sum(contributions)','assert accumulate([2,3])==5\nassert accumulate([4,-4])==0\nassert accumulate([])==0','多条反向路径的贡献相加，不能只保留最后一个。'),
('合并残差与主路结果','residual(x, change)','return [a+b for a,b in zip(x,change)]','assert residual([1,2],[.5,-1])==[1.5,1]\nassert residual([0],[3])==[3]','输入形状一致，按位置相加。'),
('模拟一个记忆更新','memory(old, keep, candidate, write)','return old*keep+candidate*write','assert memory(10,.2,4,.5)==4\nassert memory(10,1,4,0)==10','旧记忆乘保留比例，加上候选记忆乘写入比例。'),
('算一次注意力加权汇总','attend(values, weights)','return sum(v*w for v,w in zip(values,weights))','assert attend([10,20],[.25,.75])==17.5\nassert attend([10,20],[1,0])==10','对应的内容值与权重相乘再求和。'),
('给字符向量加上位置信息','add_position(token, position)','return [a+b for a,b in zip(token,position)]','assert add_position([1,2],[.1,.2])==[1.1,2.2]\nassert add_position([0,0],[3,4])==[3,4]','本练习两列表长度一致，按位相加。'),
('构造下一字符训练样本','shift(tokens)','return (tokens[:-1], tokens[1:])','assert shift([0,1,2,1,0])==([0,1,2,1],[1,2,1,0])\nassert shift([0,3,0])==([0,3],[3,0])','输入去掉最后一项，目标去掉第一项。'),
('计算留出数据的正确率','accuracy(predicted, actual)','return sum(a==b for a,b in zip(predicted,actual))/len(actual)','assert accuracy([1,0,1],[1,1,1])==2/3\nassert accuracy([0,1],[0,1])==1','逐项比较，正确个数除以非空样本数。')]
for l,(goal,signature,body,tests,hint) in zip(ls,rows):
 starter=f'def {signature}:\n    # TODO: {goal}\n    return None\n';solution=f'def {signature}:\n    {body}\n';l['lab']={'goal':goal,'starter':starter,'solution':solution,'tests':tests,'hint':hint,'expected':'运行检查后所有断言通过；不仅要满足第一组输入。'}
p.write_text(json.dumps(ls,ensure_ascii=False,indent=2))
