# SQLAlchemy-Library

A small library management system built with **SQLAlchemy** and **FastAPI**.
It provides both a command‑line interface and a REST API to manage books, authors, users, and loans.

## Features

- Add and list users, authors, and books
- Borrow and return books through a simple CLI
- REST API endpoints for CRUD operations on books and users
- Sample seed data for testing the system
- Docker support for easy setup

## Project Structure
```bash
.
├── api/              # FastAPI application
│   ├── main_api.py   # API entry point
│   └── routes.py     # Basic API routes
├── config/
│   └── paths.py      # Project directory paths and DB URL
├── controllers/      # Business logic for books, authors, users, loans, reports
├── database/
│   ├── database_init.py # SQLAlchemy engine and session setup
│   └── seed.py          # Script to populate initial data
├── models/           # SQLAlchemy ORM models
├── schemas/          # Pydantic schemas for API requests/responses
├── main.py           # Interactive CLI application
├── Dockerfile        # Container build file
├── init_script.sh    # Startup script for Docker containers
└── requirements.txt  # Python package requirements
```

## Getting Started

### 1. Using Docker

1. **Build the container**

   ```bash
   docker build -t sqlalchemy-app .
   ```
   
2. **Run the container**
	```bash
	docker run -it -v "$(pwd)/data:/app/data" sqlalchemy-app
	```
	
## 2. Manual Setup	

1. Create a virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
2. Seed the database
```bash
python database/seed.py
```
3. Launch the CLI:
```bash
python main.py
```
4.Start the API server: (Optional Step)
```bash
uvicorn api.main_api:app --reload
Visit http://localhost:8000/docs for API docs.
```

## Overview

- Models: Define Author, Book, User, and Loan in models/.
- Controllers: Handle CRUD operations and some reports.
- CLI: main.py offers a menu-driven interface for managing data.
- API: api/main_api.py exposes REST endpoints.

Explore the code to extend functionality or add tests. Enjoy using the SQLAlchemy-Library!
