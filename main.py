import os
files = os.listdir("./txt/")
import pandas as pd
dict_all = []
for file in files:
    print(file)
    one_dict = pd.read_csv("./txt/%s" % file, header=None)
    dict_all.append(one_dict)
dict_all = pd.concat(dict_all)
dict_all.drop_duplicates().to_csv("./词库.txt",index=False)
