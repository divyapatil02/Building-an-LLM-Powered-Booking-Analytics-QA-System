from fastapi import FastAPI, HTTPException
import pandas as pd
from services.analytics import get_analytics_report
from services.question_answering import get_answer

app = FastAPI()

@app.post("/analytics")
def fetch_analytics():
    result = get_analytics_report()
    return result

@app.post("/ask")
def ask_question(query: str):
    result = get_answer(query)
    if not result:
        raise HTTPException(status_code=404, detail="No data found for the query.")
    return {"result": result}

@app.get("/health")
def check_health():
    return {"status": "OK", "message": "System is running smoothly"}

