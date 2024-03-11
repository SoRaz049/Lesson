import pandas as pd
import numpy as np

df = pd.read_csv("weather_by_cities.csv", parse_dates=["day"])


#df_group= df.groupby()


# for city, data in df_group :
#     print("\n \n")
#     print("City :", city)
#     print(f"Data: \n" , data)
#     print("\nMax Temperature  for", city, " is: ", data.temperature.max())
#     print("Mean Temperature  for", city, " is: ", data.temperature.mean())
  
#print("\nStats of all cities is: \n", df_group.describe())

def grouper(df, index, col):
    if 80 <= df[col].loc[index] <= 90:
        return '80-90'
    elif 50 <= df[col].loc[index] <= 60:
        return '50-60'
    else:
        return 'others'
    
df_group= df.groupby(lambda index: grouper(df, index, 'temperature'))


for key, data in df_group:
    print('key:', key)
    print('data:', data)
    
    