from fastapi import FastAPI

app = FastAPI(title="SecureScan AI")

@app.get("/")
def home():
    return {
        "message": "Welcome to SecureScan AI",
        "status": "Running"
    }