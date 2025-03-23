from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Route to render the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route to fetch data from FastAPI backend and display it in the frontend
@app.route("/search/<query>")
def search(query):
    try:
        # Call FastAPI backend with the search query
        response = requests.get(f"http://localhost:8000/api/search?q={query}&metric=cosine")
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
