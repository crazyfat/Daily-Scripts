import os
import pandas as pd

rec = [12, 10, 14, 8, 11, 10, 15, 12, 14, 13, 12, 7, 10, 12, 8, 9, 10, 8, 8, 12]
gptIdx = [3, 4, 5, 8, 10, 11, 14, 17, 19, 20]


# 筛选数据 jcx
def traverse_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            print('******************')
            name = file_path.split('\\')[-1].split('.')[0]
            print(name)
            # print(file_path)
            sheetName = 'Eval'
            df = pd.read_excel(file_path, sheet_name=sheetName, header=None)
            ratings = df.iloc[:, -4:]
            # print('原始数据集长度：',len(df.iloc[:, -1:]))
            ratings = ratings.dropna()  # 删除包含 NaN 的行
            ratings = ratings[~ratings.applymap(lambda x: isinstance(x, str)).any(axis=1)]  # 删除包含字符串的行
            ratings = ratings[~ratings.applymap(lambda x: isinstance(x, float)).any(axis=1)]  # 删除包含浮点数的行
            # save_path = os.path.join(root, 'rating_' + file)
            # ratings.to_excel(save_path, index=False)  # 存为纯rating文件
            # first_column_array = ratings.iloc[:, 0].to_numpy()
            redialArr = []
            gptArr = []
            meanPath = []
            for i in range(4):
                li = ratings.iloc[:, i].to_numpy()
                print('第', i, '列的rating个数： ', len(li))
                cnt = 0
                idx = 0
                cur = 0
                gptPath = []
                redialPath = []
                for s in li:
                    cnt += 1
                    cur += s
                    if cnt == rec[idx]:
                        mean = cur/cnt
                        cnt = 0
                        cur = 0
                        if idx+1 in gptIdx:
                            gptPath.append(mean)
                        else:
                            redialPath.append(mean)
                        idx += 1
                gptTotal = sum(gptPath)/10
                redialTotal = sum(redialPath)/10
                gptArr.append(gptTotal)
                redialArr.append(redialTotal)
            print('# 1*4')
            print('gpt mean: ', gptArr)
            print('redial mean', redialArr)
            # result_string = ', '.join(map(str, first_column_array))
            # print('筛选后rating长度:', len(first_column_array))
            # print(result_string)
            print()


if __name__ == '__main__':
    # sum = 0
    # for v in map:
    #     sum += v
    # print(sum)
    traverse_folder(
        'E:\\软件下载目录\\微信文件\\WeChat Files\\wxid_omoc2qg8gunr21\\FileStorage\\File\\2023-12\\human_eval_final\\human_eval_12')
