import csv

def calculate_rating(data, industry=None):
    rating = []
    for row in data:
        if row[3] != 'NULL' and (not industry or row[1] == industry):
            rating.append(float(row[3]))

    if not rating:
        return None, None, None

    max_rating = max(rating)
    min_rating = min(rating)
    avg_rating = sum(rating) / len(rating)
    return max_rating, min_rating, avg_rating

try:
    with open("movies.csv") as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        data = list(reader)

        if len(data) <= 1:
            print("No data in the csv file")
            exit()

        ma, mi, avg = calculate_rating(data)
        print(f"All records: Min rating = {mi}, Max rating = {ma}, Average rating = {avg}")

        ma, mi, avg = calculate_rating(data, industry="Bollywood")
        print(f"Bollywood records: Min rating = {mi}, Max rating = {ma}, Average rating = {avg}")

        ma, mi, avg = calculate_rating(data, industry="Hollywood")
        print(f"Hollywood records: Min rating = {mi}, Max rating = {ma}, Average rating = {avg}")

except FileNotFoundError:
    print("File not found")
