import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def tanh(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def softplus(x):
    return np.log(1 + np.exp(x))


def swish(x, beta):
    return x * sigmoid(beta * x)


def get_central_ax():
    ax = plt.gca()  # get current axis 获得坐标轴对象

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))

    return ax


# 绘制`sigmoid`，`tanh`，`ReLU`，`softplus`
x = np.arange(-4.0, 4.0, 0.1)
y1 = sigmoid(x)
y2 = tanh(x)
y3 = relu(x)
y4 = softplus(x)

ax = get_central_ax()

# ax = plt.subplot(111)
# ax.plot(x, y1)
# ax.plot(x, y2, linestyle='--')
ax.plot(x, y3)
ax.plot(x, y4)
ax.legend(['ReLU', 'Softplus'])
plt.savefig('C:/Users/admin/Desktop/softpuls.pdf',format='pdf', bbox_inches='tight')
plt.show()

# 绘制`swish`函数
x = np.arange(-6.0, 6.0, 0.1)
ax = get_central_ax()

legends = []
for beta in [0, 0.5, 1, 100]:
    y_s = swish(x, beta)
    ax.plot(x, y_s, linestyle='--')
    legends.append('β = ' + str(beta))

ax.legend(legends)
plt.show()
