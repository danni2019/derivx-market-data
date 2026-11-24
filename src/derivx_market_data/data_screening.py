import pandas as pd
import numpy as np
from datetime import time

from .datetime_wrangle import to_timestamp


def period_mark(sample_df: pd.DataFrame, step: int, incremental: bool = False, mark_last: bool = False):
    if step < 1:
        raise ValueError('step must be positive')
    sample_df = sample_df.copy()
    offsets = np.arange(1, len(sample_df) + 1)
    markers = np.where(offsets % step == 0, offsets // step if incremental else 1, np.nan)
    if mark_last and len(markers) and np.isnan(markers[-1]):
        markers[-1] = (len(markers) // step) + 1 if incremental else 1
    sample_df['period_mark'] = markers
    return sample_df


def point_mark(sample_df: pd.DataFrame, point: time):
    sample_df = sample_df.copy()
    matches = sample_df.index.time == point
    sample_df['point_mark'] = to_timestamp(sample_df.index.to_series()).where(matches)
    return sample_df

