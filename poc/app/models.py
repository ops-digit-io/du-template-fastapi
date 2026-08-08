from pydantic import BaseModel


class Health(BaseModel):
    status: str
    case: str


class Metric(BaseModel):
    current: float
    by_category: dict[str, float]
