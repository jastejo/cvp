# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 23:09:25 2021

@author: HP
"""

import pandas as pd
data1 = {"col1":[100,200,300,400,500],"col2":[10,20,30,40,50]}
df= pd.DataFrame(data1)
df["result"] = df["col1"]/df["col2"]
print(df)



