# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import certifi
import os

# Load MongoDB URI from environment variable
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://sahalusr1:securepass@cluster0.bdnyrmo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

# Create the Flask app
app = Flask(__name__)

# Route to handle form submission
@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    """
    Handles form submission from your HTML form.
    Inserts the submitted itemName and itemDescription into MongoDB.
    """
    # Get the submitted data from the form
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    if item_name and item_description:
        # Connect to MongoDB
        client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
        db = client["todo_database"]
        collection = db["todos"]

        # Insert the submitted item into MongoDB
        collection.insert_one({
            "name": item_name,
            "description": item_description
        })

    # Redirect back to the home page showing all tasks
    return redirect(url_for("show_todo_list"))

# Route to display the todo list
@app.route("/")
def show_todo_list():
    # Connect to MongoDB
    client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
    db = client["todo_database"]
    collection = db["todos"]

    # Fetch all tasks
    tasks = collection.find()

    # Render tasks to HTML template
    return render_template("todo.html", tasks=tasks)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://sahalusr1:securepass@cluster0.bdnyrmo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # replace with your URI
db = client['todo_db']
collection = db['tasks']

@app.route("/")
def index():
    tasks = list(collection.find())
    return render_template("todo.html", tasks=tasks)

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    # collect all fields
    itemID = request.form.get("itemID")
    itemUUID = request.form.get("itemUUID")
    itemHash = request.form.get("itemHash")
    name = request.form.get("itemName")
    description = request.form.get("itemDescription")

    # insert into MongoDB
    collection.insert_one({
        "itemID": itemID,
        "itemUUID": itemUUID,
        "itemHash": itemHash,
        "name": name,
        "description": description
    })

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
