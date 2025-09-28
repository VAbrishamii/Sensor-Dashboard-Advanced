from fastapi import FastAPI

app = FastAPI(title=" Sensor Dashboard API", version="1.0.0")
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Sensor Dashboard API"}