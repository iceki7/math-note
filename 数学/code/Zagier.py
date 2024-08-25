
from matplotlib import pyplot as plt
import numpy as np
# from plyfile import PlyData
import os
from tqdm import tqdm
# from mpl_toolkits.mplot3d import Axes3D  

  
# 创建一个新的图形  
fig = plt.figure()  
# 添加一个3D坐标轴  
ax = fig.add_subplot(111, projection='3d')  


def gets():
    p= 3169
    p= 11117
    assert((p-1)%4==0)
    s=[]
    for xi in range(0,int(np.ceil(np.sqrt(p)))):
        yz4=(p-xi**2)
        if(yz4%4==0):
            for j in range(1,yz4):
                if((yz4/4)%j==0):
                    s.append([xi,j,int(yz4/4/j)])
                    print(s[-1])
                    assert(xi**2+4*j*(int(yz4/4/j))==p)
    print(len(s))
    return s

s=np.array(gets())
print(s.shape)

def trans(dt):
    A=np.array([[1,0,-1],\
                [0,0,1],
                [2,1,-1]])
    B=np.array([[-1,0,1],\
                [2,1,-1],
                [0,0,1]])
    
    C=np.array([[1,1,0],\
                [-2,-1,1],
                [0,1,0]])
    

    print(A@B)
    print(B@A)
    print(B@C)
    print(C@B)
    print(A@A)
    print(C@C)

    exit(0)
    
    # print(B@B)
    # print(A@C)
    # print(C@A)
    #符合条件A的点变换后一定是C,反之亦然.
    #符合条件B的点变换后还是B.
    #否则就不是对合了
    
    #如果有不动点,那么它符合条件B,所以2y-x=x,x-y+z=z  ,x=y=1,z=k
    # exit(0)

    ares=[]
    for i in range(dt.shape[0]):  
        row = dt[i, :]  # 访问第i行
        X=0
        Y=1
        Z=2
        if(row[Y]-row[Z]>row[X]):
            res=row@A

        elif(row[X]>2*row[Y]):

            res=row@C
        else:
            res=row@B
        ares.append(res)
    return ares

colort=np.column_stack((s[:,0]/np.max(s[:,0]),\
                                s[:,1]/np.max(s[:,1]), 
                                s[:,2]/np.max(s[:,2]))) 


mask1=s[:,0]<s[:,1]-s[:,2]
mask3=s[:,0]>2*s[:,1]
mask2=(s[:,0]>s[:,1]-s[:,2]) & (s[:,0]<2*s[:,1])
print(mask1.shape)

colort2=np.column_stack(((mask1).astype(int),\
                                (mask2).astype(int), 
                                (mask3).astype(int)))

a=np.array(trans(s))
a=np.array(trans(a))
# assert(np.allclose(a,s))
print(a.shape)

s=a

scatter=ax.scatter(s[:,0], \
           s[:,1], \
           s[:,2], \
            c=(colort2),\
                cmap='viridis',\
                # cmap='Blues',\

                s=2,marker='o',\
                alpha=1,
            # vmax=np.array([-14.4, -4.2,      -2.9,]),
            #     vmin=  np.array([8.4,   -3.,    2.9,])
                )  
  
# 设置坐标轴标签  
plt.colorbar(scatter)
ax.set_xlabel('X Label')  
ax.set_ylabel('Y Label')  
ax.set_zlabel('Z Label')  
# ax.set_aspect('equal')
# ax.set_xlim()
# ax.set_ylim((-4.2,-3))

# ax.set_zlim()

  
# 显示图形  
plt.savefig('[amp].png')
plt.show()

