import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
file_name_data = pd.read_excel('C:/Users/admin/Desktop/data.xlsx')
df = pd.DataFrame(file_name_data.values[:,1:].astype(float),
                  index=file_name_data.values[:,0],
                  columns=file_name_data.columns[1:])
plt.figure(figsize=(6, 4))
print(df)
# mask = np.ones_like(df.T)
# mask[np.triu_indices_from(mask)] = 0
ax = sns.heatmap(df,linewidths=0.8, vmin=0.4387, cmap="RdBu_r",center=0.4479,vmax=0.4624,annot=True,fmt='.4f',square=True)
ax.xaxis.tick_top()
# ax.yaxis.tick_right()
label_y = ax.get_yticklabels()
plt.setp(label_y , rotation = 360)
plt.savefig('C:/Users/admin/Desktop/DEGs.pdf',format='pdf', bbox_inches='tight')
plt.show()