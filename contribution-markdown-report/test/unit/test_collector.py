from datetime import date

import pandas as pd
import pytest

from src.collector import Collector
from src.date import DateRange


@pytest.mark.parametrize(
    ("start_expr", "end_expr", "start_cnt", "end_cnt"),
    [
        ("2017-03-01", "2017-08-15", 3, 8),
        ("2017-06-25", "2018-04-19", 6, 4),
    ],
    ids=[
        "Single Year",
        "Multiple Year",
    ],
)
@pytest.mark.usefixtures("use_snapshot")
def test_collect(start_expr: str, end_expr: str, start_cnt: int, end_cnt: int) -> None:
    collected = Collector.collect(
        user="lntuition",
        date_range=DateRange(
            start=date.fromisoformat(start_expr),
            end=date.fromisoformat(end_expr),
        ),
    )

    # Use mangled variable for test only
    assert collected._Extractor__user == "lntuition"
    assert collected._Extractor__df.iloc[0]["date"] == pd.Timestamp(start_expr)
    assert collected._Extractor__df.iloc[-1]["date"] == pd.Timestamp(end_expr)
    assert collected._Extractor__df.iloc[0]["count"] == pd.to_numeric(start_cnt)
    assert collected._Extractor__df.iloc[-1]["count"] == pd.to_numeric(end_cnt)
