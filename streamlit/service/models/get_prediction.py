import sys
sys.path.insert(1, '../src')
from simple_model import *
from sklearn.ensemble import RandomForestRegressor
from joblib import load

import pandas as pd
import datetime

def get_model_prediction(model, data):

    if model['id'] == 0:
        model = SimpleModel()
        time = model.predict(data)
    else:
        model = load("../models/random_forest_model.joblib")
        time = model.predict(data)[0]

    return time

def get_date(data, p):

    time = pd.to_datetime(data["purchase_timestamp"])
    hours_to_add = datetime.timedelta(hours = p)
    p_date = time + hours_to_add

    p_date = p_date.strftime("%d-%b-%Y %H:00")

    return p_date
