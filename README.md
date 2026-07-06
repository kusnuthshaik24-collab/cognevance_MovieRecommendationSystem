🎬 Movie Recommendation System
A lightweight, full-stack web application that serves movie recommendations based on a customizable dataset. Built with a Flask backend and a responsive HTML/CSS/JavaScript frontend, it includes automated data generation, cleaning, and an integrated data visualization script.

🧭 Project Architecture & Workflow
The system is organized into decoupled layers to keep data processing separate from API serving:

Data Generation (generate_data.py): Creates an initial randomized synthetic tracking matrix of users, movies, ratings, and country origins, exporting it directly to dataset.csv.
Data Cleansing (clean_data.py): Automatically reads the raw dataset, handles missing data points, strips duplicate entries, and writes the clean state to cleaned_dataset.csv.
Data Analytics & Insights (visualize_data.py): Uses matplotlib to parse the movie distribution and construct a clean, modern bar chart showing the breakdown of movies per genre.
Backend Web Server (app.py): A Flask application exposing endpoints to serve the static frontend webpage, filter parameters out of requests, compute criteria thresholds, and return JSON recommendations.
Frontend UI (index.html, style.css, script.js): A clean interface allowing users to filter by dynamic combinations of movie targets, explicit genre rules, and minimum star boundaries via asynchronous fetch updates.
🛠️ Technologies & Frameworks Used
Backend & Analytics
Python: Core scripting engine.
Flask: Micro web-framework providing the RESTful routing endpoints.
Flask-CORS: Handles Cross-Origin Resource Sharing protocols safely during development.
Pandas: Structured dataset manipulation and deduplication.
Matplotlib: Generation of data visualizations.
Frontend
HTML5: Structured semantic web layout.
CSS3: Custom modern dark-blue responsive theme with Flexbox and Grid layouts.
Vanilla JavaScript (ES6+): Handles dynamic DOM injection using async/await fetch syntax.
🚀 Step-by-Step Setup Guide
1. Prerequisites
Ensure you have Python installed on your machine. Install the required external dependencies via terminal:

pip install flask flask-cors pandas matplotlib
