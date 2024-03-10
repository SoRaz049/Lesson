import pandas as pd

# df = pd.read_csv("stock_data.csv", header= 1, na_values={
#     'eps': ['not available',-1],
#     'price': ['n.a.'],
#     'revenue': [-1]
# })


# df['pe'] = df["price"] / df['eps']
# print(df)

# df.to_csv("pe.csv", index= False)



df_movies = pd.read_excel("movies_db.xlsx", "movies")
#print(df_movies)

def standardize_currency(curr):
    if(curr == '$$' or curr == 'Dollars' or curr  == 'Dollar'):
        return 'USD'
    return curr

df_financials = pd.read_excel("movies_db.xlsx", "financials", converters={
    'currency': standardize_currency
}
)


df_merged = pd.merge(df_movies, df_financials, on="movie_id" )

print(df_merged)

df_merged.to_excel("movies_merged.xlsx", sheet_name="merged" , index= False)


df_weather = pd.DataFrame({
    'Date': ['2024-03-01', '2024-03-02', '2024-03-03', '2024-03-04', '2024-03-05'],
    'Temperature (C)': [20, 18, 22, 19, 23],
    'Humidity (%)': [65, 70, 60, 75, 55],
    'Precipitation (mm)': [0.5, 0.8, 0.2, 1.0, 0.3],
    'Wind Speed (km/h)': [10, 12, 8, 15, 11]
})

df_disasters = pd.DataFrame({
    'Date': ['2024-03-01', '2024-03-02', '2024-03-03', '2024-03-04', '2024-03-05'],
    'Location': ['City A', 'City B', 'City C', 'City D', 'City E'],
    'Type': ['Earthquake', 'Flood', 'Wildfire', 'Hurricane', 'Tornado'],
    'Severity': ['High', 'Medium', 'Low', 'High', 'Medium']
})

with pd.ExcelWriter("weather_diseaster.xlsx") as writer:
    df_weather.to_excel(writer, sheet_name="weather", index= False)
    df_disasters.to_excel(writer, sheet_name="disasters", index= False)
    
     