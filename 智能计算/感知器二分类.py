import numpy as np
import matplotlib.pyplot as plt

# 生成一条随机的直线
x = np.linspace(0, 1, 2)
# print(x)
# 生成直线的方程: y = w * x + b
# w = np.random.rand()
# b = np.random.rand()
w_real = np.array([1])
b_real = np.array([0])
print(f'w={w_real},b={b_real}')
# 创建一个函数,返回y值
# def fn(x):
#     return w*x+b
fn = lambda x: w_real * x + b_real
# 通过可视化来创建直线

# 通过直线把生成的100个点分成两个类别
N = 200
xn = np.random.rand(N, 2)
# 存储每个样本的类别 [1,-1]
yn = np.zeros([N, 1])
# 通过之前的直线把样本分成两类

for i in range(N):
    if (fn(xn[i, 0]) >= xn[i, 1]):
        # 当前的x[i]的点在直线的下方
        yn[i] = -1
    else:
        yn[i] = 1



# 对于给定的x,y值,感知器要寻找超平面
def perceptron(xn, yn, max_iter=2000, a=0.1, w=np.zeros(3)):
    N = xn.shape[0]
    # 函数里面在构造一个函数,对数据样本进行分类
    # np.sign() 激活函数,可以把结果转化 1 或者 -1
    # x ==> x[0] x[1]
    f = lambda x: np.sign(w[0] * 1 + w[1] * x[0] + w[2] * x[1])
    # 循环反向传播,如果预测值与标准值不等则修改权重和偏置
    W=[]
    for iter in range(max_iter):
        # 随机获取一个样本作为测试样本
        i = np.random.randint(N)
        # yn[i] 是样本的目标值, xn[i,:] 第i个样本的特征值   f(xn[i,:]) 预测值
        if (yn[i] != f(xn[i, :])):
            # 更新权重与偏置 权重原值 + 目标值 * 输入值 * 学习率
            w[0] = w[0] + yn[i] * 1 * a
            w[1] = w[1] + yn[i] * xn[i,0] * a
            w[2] = w[2] + yn[i] * xn[i,1] * a
        # print(w)
        if iter==1 or iter==10 or iter==100 or iter==1999:
            # print(iter)
            W.append(w)
            print(w)
            show(w)
    # return W


def show(w):
    plt.plot(x, w_real*x+b_real, 'g--',label='理想分类线')

    for i in range(N):
        if (fn(xn[i, 0]) >= xn[i, 1]):
            # 当前的x[i]的点在直线的下方
            yn[i] = -1
            plt.plot(xn[i, 0], xn[i, 1], 'rx', markersize=8)
        else:
            yn[i] = 1
            plt.plot(xn[i, 0], xn[i, 1], 'bs', markersize=8)

    bnew = -w[0] / w[2]
    anew = -w[1] / w[2]
    # 通过a与b生成预测分类线函数
    # y = lambda x:anew * x + bnew
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.plot(x,x*anew+bnew,'r',label="感知器分类线")
    plt.legend()
    plt.title('感知器分类结果')
    plt.show()

perceptron(xn,yn,max_iter=2000)
# W = perceptron(xn,yn,max_iter=2000)
# print(W)
# 通过w生成预测分类线函数的a,b的值
# bnew = -w[0] / w[2]
# anew = -w[1] / w[2]
# # 通过a与b生成预测分类线函数
# y = lambda x:anew * x + bnew
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.plot(x,y(x),'r',label="感知器分类线")
# plt.legend()
# plt.title('感知器分类结果')
# plt.show()

#
# for w in W:
#     show(w)
