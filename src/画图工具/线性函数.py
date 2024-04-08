import matplotlib.pyplot as plt
import numpy as np
from matplotlib.path import Path
from matplotlib.spines import Spine

fig = plt.figure(figsize=(9.6,4.8))

ax = plt.subplot(121)
ax2 = plt.subplot(122)


x = np.linspace(-1, 1., 100)
ax.plot(x, np.sin(x*np.pi))
ax2.plot(x, np.sin(x*np.pi),c='r')

# 移动 left 和 bottom spines 到 (0,0) 位置
ax.spines["left"].set_position(("data", 0))
ax.spines["bottom"].set_position(("data", 0))
# 隐藏 top 和 right spines.
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

plt.savefig('spines32.png',facecolor='w')

plt.show()
