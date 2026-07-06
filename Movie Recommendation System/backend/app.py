import os
import pandas as pd
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Automatically map the path to your existing frontend folder
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
frontend_dir = os.path.join(project_root, 'frontend')

# Point Flask directly to your unchanged frontend directory
app = Flask(__name__, static_folder=frontend_dir, static_url_path='')
CORS(app)

# Load dataset safely from your backend directory
df = pd.read_csv(os.path.join(current_dir, "dataset.csv"))

@app.route('/', methods=['GET'])
def home():
    # Serves your original index.html directly on the main port link
    return send_from_directory(frontend_dir, 'index.html')

@app.route('/recommend', methods=['GET'])
def recommend():
    movie_name = request.args.get('movie', '').strip().lower()
    genre_filter = request.args.get('genre', '').strip()
    min_rating = request.args.get('rating', '0')

    try:
        min_rating = float(min_rating)
    except ValueError:
        min_rating = 0.0

    unique_movies = df.drop_duplicates(subset=['movie'])
    recommendations = []

    for _, row in unique_movies.iterrows():
        if row['movie'].lower() == movie_name:
            continue
            
        if genre_filter and genre_filter.lower() != "all" and genre_filter.lower() != "":
            if genre_filter.lower() not in row['genre'].lower():
                continue

        if row['rating'] < min_rating:
            continue

        recommendations.append({
            "name": row['movie'],
            "rating": float(row['rating']),
            "genre": row['genre'],
            "about": f"An excellent {row['genre']} movie."
        })

    return jsonify(recommendations[:10])

if __name__ == '__main__':
    print("\n" + "="*55)
    print("🚀 BACKEND RECOMMENDATION SYSTEM STARTED SUCCESSFULLY!")
    print("==================================================\n")
    
    app.run(debug=True, port=5000)