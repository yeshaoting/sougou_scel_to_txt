import os
import pandas as pd

files = os.listdir("./output/txt/")
dict_all = []
for file in files:
    print(file)
    one_dict = pd.read_csv("./output/txt/%s" % file, header=None)
    dict_all.append(one_dict)
dict_all = pd.concat(dict_all)
dict_all.drop_duplicates().to_csv("./output/words.txt",index=False)
