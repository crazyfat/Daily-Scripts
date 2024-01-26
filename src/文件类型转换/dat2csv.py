import os

path_0 = r"C:\Users\admin\Desktop\ml-1m\test"  # 原文件路径
path_1 = r"C:\Users\admin\Desktop\ml-1m\test"  # 存放路径
filelist = os.listdir(path_0)  # 目录下文件列表
for files in filelist:

    dir_path = os.path.join(path_0, files)
    # 分离文件名和文件类型
    file_name = os.path.splitext(files)[0]  # 文件名
    file_type = os.path.splitext(files)[1]  # 文件类型
    # 将.dat文件转为.csv文件
    if file_type == '.dat':  # 可切换为.xls等
        file_test = open(dir_path, 'rb')  # 读取原文件
        new_dir = os.path.join(path_1, str(file_name) + '.csv')
        # print(new_dir)
        file_test2 = open(new_dir, 'wb')  # 创建/修改新文件
        for lines in file_test.readlines():
            lines = lines.decode()
            str_data = ",".join(lines.split('::'))  # 分隔符依据自己的文件确定
            file_test2.write(str_data.encode("utf-8"))
        file_test.close()
        file_test2.close()
