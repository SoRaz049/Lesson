import pandas as pd

df = pd.read_csv("stock_data.csv", header= 1, na_values={
    'eps': ['not available',-1],
    'price': ['n.a.'],
    'revenue': [-1]
})


df['pe'] = df["price"] / df['eps']
print(df)

df.to_csv("pe.csv", index= False)
