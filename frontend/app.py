from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Route to render the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route to fetch data from FastAPI backend and display it in the frontend
@app.route("/data")
def get_data():
    response = requests.get("http://localhost:8000/api/data")  # Call FastAPI endpoint
    data = response.json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
