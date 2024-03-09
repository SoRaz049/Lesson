##"without using pandas"

# import csv
   
# def calculate_rating(data, industry = None):
#     rating=[]
#     for rows in data:
#         if rows[3]!= 'NULL' and (not industry or rows [1] == industry):  # to check if the element in the 3th column of each is empty or not, and get the value of industry from coulumn 1 of each row.
#             rating. append( float(rows[3]))
                        
#     max_rating = max(rating)
#     min_rating = min(rating)
#     avg_rating = sum(rating) / len(rating)
#     return max_rating, min_rating, avg_rating

# def production_house(data):
#     lists=[]
#     after_del=[]
    
#     # to remove the dupllicate item from the data and store it for the repeation counting
#     for row in data:
#         if row[4] is not None:
#             lists.append(row[4])
    
#     for i in range(len(lists)):
#         for j in range(i+1, len(lists)):
#             if lists[i]==lists[j]:
#                 break
#         else:
#             after_del.append(lists[i])
    
#     after_del = sorted(set(after_del).intersection(set(lists))) # sorts alphabetically and stores in new list, common_element
 
    
#     counter(after_del, lists)
    
# def counter (after_del, lists):
#     count = {}
#     for i in after_del:
#         if i in lists:
#             count[i] = lists.count(i)
#     for i, (key, value) in enumerate(count.items(),1): # print the values with the numbering using the enumerate function.
#         print(f"{i} . {key}: {value}")

# try:    
#     with open("movies.csv") as f:
#         reader = csv.reader(f)
#         next( reader)
#         data = list(reader)
        
#         if len(data) <=1:
#             print("No data in the csv file")
#             exit()
            
#         ma, mi, avg = calculate_rating(data)
#         print(f"All records: Min rating = {mi}, Max rating = {ma}, Average rating = {avg}")

#         ma, mi, avg = calculate_rating(data, industry="Bollywood")
#         print(f"Bollywood records: Min rating = {mi}, Max rating = {ma}, Average rating = {avg}")

#         ma, mi, avg = calculate_rating(data, industry="Hollywood")
#         print(f"Hollywood records: Min rating = {mi}, Max rating = {ma}, Average rating = {avg}")

#     production_house(data)
        
# except FileNotFoundError:
#     print("File not found")

# except ValueError:
#     print("Value error found")
    
# except Exception as e:
#     print("Exception: ", type(e).__name__)
    

##"use of pandas"     
import pandas as pd

try:
    df = pd.read_csv("movies.csv")  
    df_boly = df.dropna()

    unique_studio = sorted(df['studio'].dropna().unique().tolist())

    print(df['studio'].value_counts())
    for i in range(len(unique_studio)):
        print(f"{i+1}. {unique_studio[i]}")
    
 
    def display_result(max_rate, min_rate, mean_rate, industry):
        print(f"""\n
The rating for {industry} is:
The max rating is: {max_rate}
The minimum rating is: {min_rate}
The mean of the rating is: {mean_rate}""")

    def Rating(df, indust):
        df_filter = df[df.industry == indust]   
        max_rate =  df_filter. imdb_rating.max()
        min_rate =  df_filter. imdb_rating.min()
        mean_rate =  df_filter. imdb_rating.mean()
        return max_rate, min_rate, mean_rate 
    
    boly_stats = Rating(df, "Bollywood")
    holy_stats = Rating(df, "Hollywood")
    
    boly_stats_display = display_result(*boly_stats, "Bollywood")
    holy_stats_display = display_result(*holy_stats, "Hollywood")
except TypeError:
    print("Error")    

except Exception as e:
    print("Exception:", type(e).__name__)
