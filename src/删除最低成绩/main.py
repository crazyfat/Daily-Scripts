import numpy as np
import pandas as pd


def func(path, savedPath, sName='Sheet1', deleteNum=3, scoresNum=13):
    """
    :param path:
    :param savedPath:
    :param sName: 目标excel文件具体表单
    :param deleteNum: 删除成绩列数
    :param scoresNum: 原有成绩列数，从sheet最右取scoresNum列作为成绩array

    """
    df = pd.read_excel(path, sheet_name=sName, header=None)
    arr = np.array(df)
    newArr = []
    for row in arr:
        scores = row[-scoresNum:]
        info = row[:-scoresNum]
        delIdx = np.argsort(scores)[:deleteNum]
        newScores = np.delete(scores, delIdx)
        newRow = np.append(info, newScores).tolist()
        newArr.append(newRow)
    newDf = pd.DataFrame(newArr)
    print(newDf)
    newDf.to_excel(savedPath, header=None, index=False)


if __name__ == '__main__':
    func('test2.xlsx', 'fin.xlsx')
