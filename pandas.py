import csv

    
def calculate_rating(data, industry = None):
    rating=[]
    for rows in data:
        if rows[3]!= 'NULL' and (not industry or rows [1] == industry):
            max_rating = max(rating)
            min_rating = min(rating)
            avg_rating = sum(rating) / len(rating)
            return max_rating, min_rating, avg_rating

try:
    with open("movies.csv") as f:
        data = list (csv.reader(f))
        header = data[0]
        data = data[1:]
        ma, mi, avg = calculate_rating(data)
        print(f"""All records: Min rating= {mi},
          Max rating = {ma},
          Average rating = {avg}""")
    
        ma, mi, avg = calculate_rating(data, industry= "Bollywood")
        print(f"""Bollywood records: Min rating= {mi},
            Max rating = {ma},
            Average rating = {avg}""")
        
        ma, mi, avg = calculate_rating(data, industry= "Hollywood")
        print(f"""Hollywood records: Min rating= {mi},
            Max rating = {ma},
            Average rating = {avg}""")

    
except FileNotFoundError:
    print("File not found")

except ValueError:
    print("Value error found")
    
except Exception as e:
    print("Exception: ", type(e).__name__)
    
    
    
    