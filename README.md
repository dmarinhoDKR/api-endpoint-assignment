# API Endpoint Assignment — Containerized Stack

A FastAPI backend using a layered architecture, PostgreSQL, Docker, and Docker Compose.

This project started as a small API endpoint assignment and was extended to demonstrate persistent storage and a repository abstraction.

## What this project demonstrates

- FastAPI JSON endpoints
- Service and repository layers
- Swappable repository implementations
- PostgreSQL persistence
- Docker images with pinned versions and digests
- Docker Compose orchestration
- Environment-based configuration
- Data persistence across container recreation

## Architecture

```text
FastAPI routes (main.py)
        |
        v
NotesService
        |
        v
NotesRepository
        |
        +-- MemoryNotesRepository
        |
        +-- PostgresNotesRepository
```

`NotesService` depends on the `NotesRepository` interface rather than a concrete storage implementation.

The active implementation is selected in `dependencies.py`. Replacing the in-memory repository with PostgreSQL did not require changes to the route handlers or service layer.

## Project structure

```text
.
├── Dockerfile
├── docker-compose.yml
├── init.sql
├── main.py
├── dependencies.py
├── requirements.txt
├── repositories/
│   ├── memory_notes_repository.py
│   ├── notes_repository.py
│   └── postgres_notes_repository.py
└── services/
    └── notes_service.py
```

## Requirements

- Docker Desktop
- Docker Compose
- WSL integration enabled when running from WSL

## Environment configuration

Create your local environment file from the committed example:

```bash
cp .env.example .env
```

The `.env` file contains the local database credentials and connection string and is ignored by Git.

## Start the complete stack

Build and start the API and PostgreSQL with one command:

```bash
docker compose up --build --detach
```

Check the services:

```bash
docker compose ps
```

The API is available at:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/profile
- http://127.0.0.1:8000/notes
- http://127.0.0.1:8000/docs

## Endpoints

### `GET /`

Returns the API status.

```bash
curl http://127.0.0.1:8000/
```

### `GET /profile`

Returns structured profile information.

```bash
curl http://127.0.0.1:8000/profile
```

### `POST /notes`

Creates a persistent note.

```bash
curl \
  --header "Content-Type: application/json" \
  --data '{
    "title": "Persistent note",
    "content": "Stored in PostgreSQL through the repository"
  }' \
  http://127.0.0.1:8000/notes
```

Example response:

```json
{
  "id": 1,
  "title": "Persistent note",
  "content": "Stored in PostgreSQL through the repository"
}
```

### `GET /notes`

Lists notes stored in PostgreSQL.

```bash
curl http://127.0.0.1:8000/notes
```

## Inspect the database directly

```bash
docker compose exec -T db \
  psql \
  --username postgres \
  --dbname api_assignment \
  --command "SELECT id, title, content FROM notes ORDER BY id;"
```

## Persistence proof

Create a note, then remove the application and database containers:

```bash
docker compose down
```

The named PostgreSQL volume remains available:

```bash
docker volume inspect api-endpoint-assignment_postgres_data
```

Recreate the stack:

```bash
docker compose up --detach
```

Query the API again:

```bash
curl http://127.0.0.1:8000/notes
```

The previously created rows remain available because PostgreSQL stores its data in the named `postgres_data` volume.

Do not use `docker compose down --volumes` during this test because that command intentionally deletes the persisted data.

## Stop the stack

```bash
docker compose down
```

To intentionally remove the database volume and reset all data:

```bash
docker compose down --volumes
```

## Technologies

- Python 3.12
- FastAPI
- Psycopg 3
- PostgreSQL 16.14
- Docker
- Docker Compose
