# Smart Expense Tracker API

A RESTful backend API built using Python and Flask to manage and analyze personal expenses.

## Tech Stack

- Python
- Flask
- SQLite
- NumPy
- Pandas

## API Endpoints

- GET /
- POST /expense
- GET /expenses
- DELETE /expense/{id}
- GET /analytics

## Running the Project

Run locally:

python run.py

Run with Docker:

docker build -t expense-tracker-api .
docker run -p 5000:5000 expense-tracker-api
