import random
import pandas as pd

movies = [
    "3 Idiots", "Dangal", "RRR", "KGF Chapter 2", "Pushpa",
    "Sholay", "Pathaan", "Kabir Singh", "Drishyam", "War",
    "Avatar", "Titanic", "Interstellar", "Inception",
    "Avengers: Endgame", "Joker", "Iron Man"
]

genres = ["Action", "Drama", "Comedy", "Romance", "Sci-Fi", "Thriller"]

data = []

for user in range(1, 201):
    for _ in range(30):
        movie = random.choice(movies)
        rating = random.randint(1, 5)
        genre = random.choice(genres)
        country = "India" if movie in movies[:9] else "USA"

        data.append([user, movie, rating, genre, country])

df = pd.DataFrame(data, columns=["userId", "movie", "rating", "genre", "country"])
df.to_csv("dataset.csv", index=False)

print("Dataset created successfully!")