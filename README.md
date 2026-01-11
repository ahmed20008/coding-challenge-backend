# Application Review API

A simple REST API to manage job applications, store project history, and generate PDF summaries.

## 🚀 Quick Start

1.  **Configure Environment**
    Add a GitHub token if you want to send multiple requests to the server (helps avoid rate limits).
    ```bash
    export GITHUB_TOKEN=your_github_token
    ```

2.  **Run with Docker**
    Build and start the services (database migrations run automatically).
    ```bash
    docker-compose up --build
    ```

3.  **Access API**
    * **Docs & Test:** http://localhost:8000/docs
    * **Base URL:** http://localhost:8000

## 🔌 Endpoints

* **`GET /applications/`**
    List all submitted applications.
* **`POST /applications/`**
    Submit a new application (replaces old data if email exists).
* **`GET /applications/{id}`**
    Get details of a specific application.
* **`GET /applications/{id}/pdf`**
    Download a generated PDF summary of the application.

## 🛠 Tech Stack

* **Framework:** FastAPI
* **Database:** PostgreSQL & Alembic
* **PDF Engine:** ReportLab
* **Container:** Docker