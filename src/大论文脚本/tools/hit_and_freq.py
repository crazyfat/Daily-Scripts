import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
num_100k = 934
num_1m = 4096
freq_max = 1000
hit_max = 100

freq = pd.read_excel('../data/ml-1m/ml1m_freq.xlsx')[0]

test_data = pd.read_excel('../data/ml-1m/ml1m_item_batch.xlsx')['itemID']

hit = pd.read_excel('../data/ml-1m/ml1m_hit.xlsx')[0]

ncr_hit = pd.read_excel('../data/ml-1m/ncr_ml1m_hit.xlsx')[0]

box_x = np.zeros(num_1m, dtype=int)
box_y = np.zeros(num_1m, dtype=int)
size = np.ones(num_1m, dtype=float)
ncr_x = np.zeros(num_1m, dtype=int)
ncr_y = np.zeros(num_1m, dtype=int)
box_color = []
ncr_color = []
size += 0.0001
box_score = 0
ncr_score = 0
for idx, item in enumerate(test_data):
    if idx < 10:
        print('itemID: ', item, ' freq: ', freq[item], ' hit: ', hit[idx])
    ncr_x[idx] = freq[item]
    ncr_y[idx] = ncr_hit[idx]
    ncr_color.append('lightcoral')
    if ncr_hit[idx] < 5 and freq[item] < freq_max:
        ncr_score += 1

for idx, item in enumerate(test_data):
    if idx < 10:
        print('itemID: ', item, ' freq: ', freq[item], ' ncr_hit: ', ncr_hit[idx])
    box_x[idx] = freq[item]
    box_y[idx] = hit[idx]
    box_color.append('skyblue')
    if hit[idx] < 5 and freq[item] < freq_max:
        box_score += 1

print(box_score, ncr_score)
# 解决不能显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 设置坐标轴字体大小
plt.rcParams['axes.labelsize'] = 15  # 设置坐标轴标签的字体大小
plt.rcParams['xtick.labelsize'] = 12  # 设置x轴刻度的字体大小
plt.rcParams['ytick.labelsize'] = 12  # 设置y轴刻度的字体大小

plt.xlabel('物品交互频率')
plt.ylabel('物品预测排名')
plt.title("物品排名与频率分布", fontsize=18)
plt.xlim(xmax=2000, xmin=1000)
plt.ylim(ymax=hit_max, ymin=0)

type_ncr = plt.scatter(ncr_x, ncr_y, s=size, c=ncr_color, label='NCR', alpha=1)
type_box = plt.scatter(box_x, box_y, s=size, c=box_color, label='Box4CR', alpha=1.0)
plt.legend()
plt.savefig('C:/Users/admin/Desktop/scatter.pdf',format='pdf', bbox_inches='tight')
plt.show()