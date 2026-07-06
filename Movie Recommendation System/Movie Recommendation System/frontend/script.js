async function getRecommendations() {
    let movie = document.getElementById("movieInput").value.trim();
    let genre = document.getElementById("genreSelect").value;
    let rating = document.getElementById("ratingSelect").value;

    if (movie === "") {
        alert("Please enter a base movie name first!");
        return;
    }

    try {
        // EXPLICIT FIXED PORT LINK: Connects directly to your background Flask server
        let url = `http://127.0.0.1:5000/recommend?movie=${encodeURIComponent(movie)}&genre=${genre}&rating=${rating}`;
        
        let response = await fetch(url);
        let data = await response.json();

        let resultsContainer = document.getElementById("results");
        resultsContainer.innerHTML = ""; // Clear out previous card layouts

        if (data.length === 0) {
            resultsContainer.innerHTML = `<p style="grid-column: 1/-1; text-align: center; color: #64748b; padding: 20px;">No recommendations found matching your current filter choices.</p>`;
            return;
        }

        data.forEach((item, index) => {
            // Uses theater room seating pictures seamlessly from an online fallback if /images/ is missing
            let imageSrc = `https://picsum.photos/id/${10 + (index * 4)}/400/250`;

            resultsContainer.innerHTML += `
                <div class="movie-card">
                    <div class="img-container">
                        <img src="${imageSrc}" alt="${item.name}">
                        <div class="genre-badge">${item.genre}</div>
                    </div>
                    <div class="movie-info">
                        <h4>${item.name}</h4>
                        <p>⭐ ${item.rating.toFixed(1)} / 5.0</p>
                    </div>
                </div>
            `;
        });

    } catch (error) {
        console.error("Connection Error:", error);
        alert("Could not connect to backend server. Make sure your python app.py is up and running on port 5000!");
    }
}