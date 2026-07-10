# API Endpoint Assignment

A minimal FastAPI backend with two JSON endpoints, built for the Backend AI Engineering assignment.

## Goal

Build a small backend server with two JSON endpoints and publish it to a public GitHub repository.

## Endpoints

### GET /

Returns a basic message and API status.

Example response:

```json
{
  "message": "Hello from my first backend API",
  "status": "running"
}
```

### GET /profile

Returns structured profile information.

Example response:

```json
{
  "name": "Daniel Figueiredo",
  "track": "Backend AI Engineering",
  "focus": ["Python", "APIs", "Automation", "MLOps"]
}
```

## How to run locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
uvicorn main:app --reload
```

Open in the browser:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/profile
- http://127.0.0.1:8000/docs

Or test with curl:

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/profile
```