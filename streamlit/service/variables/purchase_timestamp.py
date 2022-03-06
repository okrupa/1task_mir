import numpy as np
import pandas as pd

def circuralEncoding(data, unique_nums):
    data_sin = np.sin(data* (2 * np.pi / unique_nums))
    data_cos = np.cos(data * (2 * np.pi / unique_nums))
    return data_sin, data_cos

def get_time(purchase_timestamp):
    d_time = {}
    time = pd.to_datetime(purchase_timestamp)
    p_day_of_week = time.dayofweek
    p_hour = time.hour
    p_minute = time.minute

    d_time['purchase_is_weekend'] = 1 if p_day_of_week in [5,6] else 0

    d_time['purchase_day_of_week_sin'], d_time['purchase_day_of_week_cos'] = circuralEncoding(p_day_of_week, 7)
    d_time['purchase_hour_sin'], d_time['purchase_hour_cos'] = circuralEncoding(p_hour, 24)
    d_time['purchase_minute_sin'], d_time['purchase_minute_cos'] = circuralEncoding(p_minute, 60)

    return d_time