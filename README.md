# DerivX Market Data

Python utilities for turning timestamped prices into OHLC bars, aggregating existing OHLC data, and marking market periods. The code was extracted from the 2024 DerivX project.

## From ticks to bars

From a checkout with Python 3.11 or newer:

```sh
python -m pip install .
python examples/demo.py
```

The [demo](examples/demo.py) converts six synthetic prices into two one-minute bars:

```text
                     open  high  low  close
2024-04-01 09:30:00   100   102  100    101
2024-04-01 09:31:00   104   105  103    105
```

Pass a pandas Series with a DatetimeIndex to `resample_tick_price_to_bar_md`. To aggregate rows by exchange session with `resample_md_data`, the daily mode uses an explicit `trading_date` column so a session can span calendar dates.

This [MIT-licensed release](LICENSE) retains the two related source commits from March 2024. The extraction preserves author names and dates and replaces historical email addresses with non-deliverable aliases.
