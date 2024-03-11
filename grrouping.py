import pandas as pd
import numpy as np

df = pd.read_csv("weather_by_cities.csv", parse_dates=["day"])

print(df)

df_group= df.groupby("city")


for city, data in df_group :
    print("\n \n")
    print("City :", city)
    print(f"Data: \n" , data)
    print("\nMax Temperature  for", city, " is: ", data.temperature.max())
    print("Mean Temperature  for", city, " is: ", data.temperature.mean())
  
print("\nMax temperature in all cities is: \n", df_group.max())
