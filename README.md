# Smart Expense Tracker API

A RESTful backend application built using Python and Flask that allows users to track expenses and generate analytics.

## Features
- Add expenses
- View expenses
- Delete expenses
- Expense analytics

## Tech Stack
Python
Flask
SQLite
NumPy
Pandas

## API Endpoints

GET /
POST /expense
GET /expenses
DELETE /expense/{id}
GET /analytics

## Running with Docker

Build image

docker build -t expense-tracker-api .

Run container

docker run -p 5000:5000 expense-tracker-api