import numpy as np
import pandas as pd


df = pd.read_csv("pe.csv")


# df.fillna({
#     'eps': df.eps.mean(),
#     'pe' : df.pe.mean()
# },inplace= True)

# df_droped = df.dropna()
# print(df_droped)

df_clean = df.replace({
    'eps': [-1, -999],
    'revenue': -999,
    'price' : 00
},np.nan)


df_clean.ffill(inplace = True)

print(df_clean)