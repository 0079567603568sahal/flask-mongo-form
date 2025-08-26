Flask To-Do Application with Git Versioning
Overview

This project is a Flask-based To-Do web application integrated with MongoDB. It demonstrates Git workflow best practices, including branching, committing, merging, rebasing, and conflict resolution. The project also showcases incremental feature development and version control management.

Project Features

Basic To-Do Form

Fields: Item Name, Item Description

Stores tasks in MongoDB

Displays tasks in a dynamic list

Enhanced To-Do Form

Additional fields: Item ID, Item UUID, Item Hash

Each field was added in a separate commit to preserve commit history

Backend API

Route: /submittodoitem

Accepts POST requests and stores submitted tasks in MongoDB

Full Git Workflow

Branching, committing, merging, rebasing

Handling conflicts and preserving commit history

Soft resets and selective commits

Git Workflow and Task Breakdown
1. Repository Setup

Created a new GitHub repository.

Cloned it locally using SSH.

Created a branch named after the username (e.g., Tutedude) and added initial Flask project files.

Merged the branch into main.

2. JSON API Update

Created a branch <username>_new (e.g., Tutedude_new).

Updated the JSON file for the /api route.

Merged the branch into main.

Resolved conflicts by accepting changes from <username>_new.

Staged, committed, and pushed resolved changes.

3. Branching for Feature Development

Created branches master_1 and master_2 from main.

In master_1:

Developed the frontend To-Do page.

Form fields: Item Name, Item Description.

In master_2:

Developed backend API route /submittodoitem.

Stores submitted task details in MongoDB.

Merged changes from both master_1 and master_2 into main.

4. Enhancing the To-Do Form

In master_1, added additional fields sequentially:

Item ID

Item UUID

Item Hash

Each field committed individually.

Merged master_1 into main.

Git Reset & Recommit:

Rolled back main to the commit with only Item ID using git reset --soft.

Re-committed the staged changes.

Merged the updated state back into main.

Rebasing:

Rebased main onto master_1 to integrate changes while preserving commit history:

git rebase main master_1

File Structure
flask-mongo-form/
│
├── App.py
├── templates/
│   └── to_do.html
├── static/       # optional, for CSS/JS
└── README.md

How to Run

Clone the repository:

git clone <repository-URL>
cd flask-mongo-form


Install dependencies:

pip install flask pymongo certifi


Set the MongoDB URI (optional, defaults in App.py):

export MONGO_URI="your_mongodb_uri_here"


Run the Flask app:

python App.py


Open a browser at http://127.0.0.1:5000/ to use the To-Do application.
Sahal
Email: Mohdsahal924@gmail.com
GitHub:https://github.com/0079567603568sahal
