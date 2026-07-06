import os
import pandas as pd
import matplotlib.pyplot as plt

# Find the correct path to your dataset
current_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(current_dir, "dataset.csv")

try:
    # 1. Load the dataset
    df = pd.read_csv(dataset_path)
    
    # Remove duplicate movies so we count each movie only once
    unique_movies = df.drop_duplicates(subset=['movie'])

    # 2. Group by Genre and count how many movies are in each
    genre_counts = unique_movies['genre'].value_counts()

    # 3. Create the Bar Chart
    plt.figure(figsize=(10, 6)) # Set window size
    
    # Custom vibrant color palette for your UI theme
    colors = ['#6c63ff', '#ff6584', '#3f3d56', '#4caf50', '#ff9800', '#00bcd4']
    
    # Plot the bars
    genre_counts.plot(kind='bar', color=colors, edgecolor='black', width=0.6)

    # 4. Stylize the Chart titles and labels
    plt.title('🎬 Number of Movies per Genre', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('Movie Genres', fontsize=12, fontweight='semibold', labelpad=10)
    plt.ylabel('Movie Count', fontsize=12, fontweight='semibold', labelpad=10)
    plt.xticks(rotation=45) # Tilt genre names so they don't overlap
    plt.grid(axis='y', linestyle='--', alpha=0.7) # Add a clean background grid
    
    plt.tight_layout() # Prevent clipping of labels

    # 5. Show the window screen immediately
    print("\n📊 Displaying your Movie Bar Chart window...")
    plt.show()

except FileNotFoundError:
    print(f"\n❌ Error: Could not find 'dataset.csv' at {dataset_path}")
    print("Please make sure this script is running inside the same folder as your spreadsheet!")