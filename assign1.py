import pandas as pd



# ## "ASSIGNMENT 1ST"
# df = pd.read_csv("movies_data.csv")
# # print(df.head(5))

# df['year_classify']= df.apply(lambda x: 'before 2000' if x['release_year'] < 2000 else 'From 2000', axis = 1  )

# print(df)

# df.to_csv("new.csv")


# df_new = df = pd.read_csv("new.csv", usecols=['movie_id', 'title', 'budget', 'revenue', 'year_classify'])

# df_new.to_csv("file_movie_dataset.csv", index= False)




## "ASSIGNMENT 2ND"
df = pd.read_csv("fruits_data.csv",)

print(df.shape)
print(df.columns.to_list())
print(df)

# new_df = df.fillna(-1, inplace= True)
# print(new_df)


exp_nan_count = df.isna().sum()
print(exp_nan_count)
# def nan_count(rows):

# Drop rows with at least 4 non-null values
df_thresholded = df.dropna(thresh=4)

# Print the resulting DataFrame
print(df_thresholded)
    