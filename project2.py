import matplotlib.pyplot as plt #利用matplotlib画图
import numpy as np #建立数据库
x = np.linspace(0,3*np.pi,100) #x的第一个参数序列起始值，第二个参数序列结束值，样本100
y = np.sin(x) #函数y=sin(x)

plt.rcParams['font.sans-serif']=['SimHei'] #有了这句话，图表能显示中文
plt.rcParams['axes.unicode_minus']=False #显示负号
plt.subplot(1,2,1) #1行，2列1第二列
plt.title(r'$f(x)=sin(x)$') 
plt.plot(x,y) #画图

x1 = [t*0.375*np.pi for t in x] #t*0.375*np.pi赋x1,t的取值范围就是x的取值范围
y1 = np.sin(x1)
plt.subplot(1,2,2) #1行，2列，第2列
plt.title(r'$f(x)=sin(\omega),\omega = \frac{3}{8} \pi$')
# plt.title(u"测试2") #注意：在前面加一个u
plt.plot(x1,y1) #显示x横坐标
plt.show() #显示






