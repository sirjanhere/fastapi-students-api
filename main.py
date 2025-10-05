import pandas as pd
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

# Load CSV
df = pd.read_csv("q-fastapi.csv")  

# Create FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# API endpoint
@app.get("/api")
def get_students(class_: list[str] = Query(default=None, alias="class")):
    if class_:
        filtered = df[df['class'].isin(class_)]
    else:
        filtered = df
    return {"students": filtered.to_dict(orient="records")}
