import pandas as pd



# ## "ASSIGNMENT 1ST"
# df = pd.read_csv("movies_data.csv")
# # print(df.head(5))

# df['year_classify']= df.apply(lambda x: 'before 2000' if x['release_year'] < 2000 else 'From 2000', axis = 1  )

# print(df)

# df.to_csv("new.csv")


# df_new = df = pd.read_csv("new.csv", usecols=['movie_id', 'title', 'budget', 'revenue', 'year_classify'])

# df_new.to_csv("file_movie_dataset.csv", index= False)




# ## "ASSIGNMENT 2ND"
# df = pd.read_csv("fruits_data.csv",)

# print(df.shape)
# print(df.columns.to_list())
# print(df)

# #new_df = df.fillna(-1, inplace= True)
# # print(new_df)


# exp_nan_count = df.isna().sum()
# print(exp_nan_count)
# # def nan_count(rows):

# # Drop rows with at least 4 non-null values
# df_thresholded = df.dropna(thresh=4)

# new1_df = df_thresholded.dropna()

# print(new1_df)
# new1_df.to_csv("final_data.csv", index = False)



## "ASSIGNMENT 3RD"

# df = pd.read_csv("D:\\Data Science\\practice files\\Practice assignment\\food_db.csv")
# print(df.shape)
# new_df = df.replace({'discount': {'10%': '13%', '5%':'13%'}})
# new_df.replace({'rating': {'Excellent': 4, 'Very Good': 3, 'Good': 2, 'Average': 1}}, inplace= True)
# print(new_df)



##"ASSIGMENT 4TH"

df = pd.read_csv("D:\\Data Science\\practice files\\Practice assignment\\movies_data.csv")

g= df.groupby(df['industry'])

print("\n The data related to Bollywood is : \n")
for industry, data in g:
    if(industry == "Bollywood"):
        print(data)
        

def grouper(df, idx, col):
    if 1 <= df[col].loc[idx] <=3.9:
        return 'Poor'
    
    elif 4 <= df[col].loc[idx] <=7.9:
        return 'Average'
    
    elif 8 <= df[col].loc[idx] <=10:
        return 'Good'
    else:
        return 'Others'

g_new = df.groupby(lambda x : grouper(df, x, 'imdb_rating'))

for key, data in g_new:
    print('key:', key)
    print('data:', data)

    