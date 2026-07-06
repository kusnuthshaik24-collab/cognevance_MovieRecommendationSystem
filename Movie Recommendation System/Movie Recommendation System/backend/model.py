import pandas as pd

df = pd.read_csv("dataset.csv")

def recommend(movie_name):
    
    movie_name = movie_name.lower()

    movies = df["movie"].unique()

    recommendations = []

    for movie in movies:
        if movie.lower() != movie_name:
            recommendations.append({
                "name": movie,
                "rating": 4.5,
                "about": "Recommended movie based on ratings"
            })

    return recommendations[:10]