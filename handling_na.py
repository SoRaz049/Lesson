import pandas as pd


df = pd.read_csv("pe.csv")


df.fillna({
    'eps': df.eps.mean(),
    'pe' : df.pe.mean()
},inplace= True)

df_droped = df.dropna()
print(df_droped)