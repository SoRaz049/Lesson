import pandas as pd

df = pd.read_csv("movies_data.csv")
# print(df.head(5))

df['year_classify']= df.apply(lambda x: 'before 2000' if x['release_year'] < 2000 else 'From 2000', axis = 1  )

print(df)

df.to_csv("new.csv")


df_new = df = pd.read_csv("new.csv", usecols=['movie_id', 'title', 'budget', 'revenue', 'year_classify'])

df_new.to_csv("file_movie_dataset.csv", index= False)

