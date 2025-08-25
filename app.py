from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/api")
def api():
    return jsonify({"message": "API route works!"})

if __name__ == "__main__":
    app.run(debug=True)
