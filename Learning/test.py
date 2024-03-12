# import csv

# def calculate_rating(data, industry=None):
#     rating = []
#     for row in data:
#         if row[3] != 'NULL' and (not industry or row[1] == industry):
#             rating.append(float(row[3]))

#     if not rating:
#         return None, None, None

#     max_rating = max(rating)
#     min_rating = min(rating)
#     avg_rating = sum(rating) / len(rating)
#     return max_rating, min_rating, avg_rating

# try:
#     with open("movies.csv") as f:
#         reader = csv.reader(f)
#         next(reader)  # Skip the header row
#         data = list(reader)

#         if len(data) <= 1:
#             print("No data in the csv file")
#             exit()

#         ma, mi, avg = calculate_rating(data)
#         print(f"All records: Min rating = {mi}, Max rating = {ma}, Average rating = {avg}")

#         ma, mi, avg = calculate_rating(data, industry="Bollywood")
#         print(f"Bollywood records: Min rating = {mi}, Max rating = {ma}, Average rating = {avg}")

#         ma, mi, avg = calculate_rating(data, industry="Hollywood")
#         print(f"Hollywood records: Min rating = {mi}, Max rating = {ma}, Average rating = {avg}")

# except FileNotFoundError:
#     print("File not found")

import pandas as pd

try:
    df = pd.read_csv("movies.csv")
    unique_studio = df['studio'].unique()
    unique_studio_list = unique_studio.tolist()  # Convert to list
    # Convert all elements to strings before sorting
    unique_studio_list = [str(x) for x in unique_studio_list]
    unique_sorted = sorted(unique_studio_list)
    print(unique_sorted)
    print(type(unique_sorted))
except Exception as e:
    print("Exception:", type(e).__name__)
