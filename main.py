from fastapi import FastAPI

app = FastAPI(title="API Endpoint Assignment")


@app.get("/")
def root():
    return {
        "message": "Hello from my backend API Assignment",
        "status": "running",
    }


@app.get("/profile")
def profile():
    return {
        "name": "Daniel Figueiredo",
        "track": "Backend AI Engineering",
        "focus": ["Python", "APIs", "Automation", "MLOps"],
    }
