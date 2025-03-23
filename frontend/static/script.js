document.getElementById("search-form").addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent the form from reloading the page

    const query = document.getElementById("query").value.trim();
    
    if (!query) return;

    // Clear previous results
    const resultsSection = document.getElementById("results-section");
    const resultsBody = document.getElementById("results-body");
    
    resultsBody.innerHTML = ""; // Clear table rows
    resultsSection.style.display = "none"; // Hide results section initially

    try {
        // Fetch data from the backend API
        const response = await fetch(`/search/${encodeURIComponent(query)}`);
        const data = await response.json();

        if (data.error) {
            alert(`Error fetching results: ${data.error}`);
            return;
        }

        // Populate the table with results
        let rank = 1; // Initialize rank counter
        data.results.forEach((result) => {
            const row = document.createElement("tr");

            // Create cells for rank, document name, and similarity score
            const rankCell = document.createElement("td");
            rankCell.textContent = rank++;
            
            const nameCell = document.createElement("td");
            nameCell.textContent = result.document;

            const scoreCell = document.createElement("td");
            scoreCell.textContent = result.score.toFixed(2);

            // Append cells to the row
            row.appendChild(rankCell);
            row.appendChild(nameCell);
            row.appendChild(scoreCell);

            // Append row to the table body
            resultsBody.appendChild(row);
        });

        // Show the results section
        resultsSection.style.display = "block";

    } catch (error) {
        console.error(error);
        alert("An error occurred while fetching results.");
    }
});
