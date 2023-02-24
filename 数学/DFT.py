import matplotlib.pyplot as plt
import math
import numpy as np
n=10 #采样数
dt=0.2 #采样间隔
L=n*dt #信号长
noisy=0
#信号
def gt(x):
    print('shape')
    print(x.shape)
    return 0.3*x*x*x-0.1*x*x+noisy*np.random.rand(x.shape[0])

# signal=[[0,10],[1,20],[2,30],[3,40],
#         [4,50],[5,80],[6,60],[7,30]]

#用于采样的时间轴
ts=np.arange(0.0,L,dt)
#用于模拟的时间轴
tm = np.arange(0.0, L, dt/20)

signal=gt(ts)
print(signal)
print('done')

ans=[]
bns=[]

#计算一个系数，i=0，1，2，3：当前遍历的序号
def getan(issin,m):
    an=0
    f=m/L+1
    # if(f==0):
    #     for j in range(0,n):
    #         if(issin):
    #             an += signal[j]
    #         else:
    #             an += signal[j]
    #     an/=n
    #     print(an)
    #     an/=L
    #     return an
    
    for j in range(0,n):
        if(issin):
            an += math.sin(2*math.pi*f*j*dt)*signal[j]
        else:
            an += math.cos(2*math.pi*f*j*dt)*signal[j]
    an/=L
    return an
#计算所有系数
def getArray():
    for i in range(0,n):#0,1,2,3
        ans.append(getan(True,i))
        bns.append(getan(False,i))

def sim(tm):

    for x in range(0,n):
        if(x==0):
            func=ans[x]*np.sin(tm)+bns[x]*np.cos(tm)
        else:
            func+=ans[x]*np.sin(tm)+bns[x]*np.cos(tm)
    return func
    pass

print(tm)

getArray()
fig1=plt.figure()
#plt.scatter([0,1,2,3,4,5,6,7],[10,20,30,40,50,80,60,30], marker='^')
plt.plot(tm,sim(tm))
plt.scatter(ts,gt(ts))

#plt.scatter(ts,ans)
plt.show()