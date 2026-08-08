from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data" / "sample.csv"


def _frame() -> pd.DataFrame:
    return pd.read_csv(DATA, parse_dates=["period"])


def current_total() -> float:
    return float(_frame()["value"].sum())


def by_category() -> dict[str, float]:
    return _frame().groupby("category")["value"].sum().round().to_dict()
