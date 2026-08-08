"""UC-XXXX-XXXX · Use-Case PoC — FastAPI PoC service.

Run: uvicorn app.main:app --reload   (from the poc/ directory)
Serves the metric computed from data/sample.csv. Offline; not production data.
Structure follows https://fastapi.tiangolo.com/tutorial/bigger-applications/.
"""
from fastapi import FastAPI

from app.data import by_category, current_total
from app.models import Health, Metric

app = FastAPI(title="UC-XXXX-XXXX · Use-Case PoC")


@app.get("/health", response_model=Health)
def health() -> Health:
    return Health(status="ok", case="UC-XXXX-XXXX")


@app.get("/metric", response_model=Metric)
def metric() -> Metric:
    return Metric(current=current_total(), by_category=by_category())
