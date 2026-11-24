# DerivX Market Data

Python utilities extracted from DerivX for forming OHLC bars from timestamped prices, aggregating OHLC data, marking periods, and scaling or summarizing data.

```sh
python -m pip install .
python examples/demo.py
```

The demo generates synthetic prices. Pass a pandas Series with a DatetimeIndex to `resample_tick_price_to_bar_md`. For `resample_md_data`, the daily mode groups on an explicit `trading_date` column so a trading date can span calendar days.

This repository retains the two source commits from March 2024 that touched the extracted modules. The extraction preserves author names and dates, replaces historical email addresses with non-deliverable aliases, and creates new commit IDs. The standalone packaging and compatibility changes are recorded in a separate commit.
