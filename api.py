from fastapi import FastAPI

app = FastAPI()

@app.get("/location")
def read_root():
    return {"location": "N/A"}