import pandas as pd

from derivx_market_data import resample_tick_price_to_bar_md


def main():
    timestamps = pd.date_range("2024-04-01 09:30:00", periods=6, freq="20s")
    ticks = pd.Series([100, 102, 101, 104, 103, 105], index=timestamps)
    bars = resample_tick_price_to_bar_md(ticks, "1min")
    print(bars.to_string())


if __name__ == "__main__":
    main()
