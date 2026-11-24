import pandas as pd
import pytest

from derivx_market_data import resample_md_data, resample_tick_price_to_bar_md, simple_resample_md_data
from derivx_market_data.data_screening import period_mark
from derivx_market_data.data_standardization import scaling_z_score
from derivx_market_data.datetime_wrangle import from_timestamp, to_timestamp


def test_ticks_form_ohlc_in_timestamp_order():
    index = pd.date_range("2024-04-01 09:30", periods=4, freq="20s")
    ticks = pd.Series([100, 103, 101, 104], index=index)
    bars = resample_tick_price_to_bar_md(ticks.iloc[::-1], "1min")
    assert bars.iloc[0].to_dict() == {"open": 100, "high": 103, "low": 100, "close": 101}
    assert bars.iloc[1].to_dict() == {"open": 104, "high": 104, "low": 104, "close": 104}
    assert simple_resample_md_data(bars, "2min").iloc[0]["close"] == 104


def test_daily_bars_group_by_trading_date():
    timestamps = pd.DatetimeIndex(["2024-04-01 21:00", "2024-04-02 09:00"], name="datetime")
    bars = pd.DataFrame(
        {"open": [100, 101], "high": [102, 105], "low": [99, 100], "close": [101, 104],
         "volume": [5, 6], "trading_date": [pd.Timestamp("2024-04-02")] * 2},
        index=timestamps,
    )
    output = resample_md_data(bars, "D")
    assert output.iloc[0].to_dict() == {"open": 100, "high": 105, "low": 99, "close": 104, "volume": 11}


def test_timestamp_conversion_and_period_marking():
    dates = pd.Series([pd.Timestamp("2024-04-01 09:30:00"), pd.NaT])
    assert from_timestamp(to_timestamp(dates)).tolist() == dates.tolist()
    frame = pd.DataFrame({"sample": [1]})
    assert period_mark(frame, 5, incremental=True, mark_last=True)["period_mark"].tolist() == [1]
    assert "period_mark" not in frame


def test_scale_numeric_data():
    assert scaling_z_score(pd.Series([1.0, 2.0, 3.0])).tolist() == pytest.approx(
        [-1.224744871, 0, 1.224744871],
    )
