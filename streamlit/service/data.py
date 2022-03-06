import pandas as pd

from variables.city import get_city
from variables.delivery_company import get_delivery_company
from variables.purchase_timestamp import get_time
def get_data(data):
    d_city = get_city(data["city"])
    d_delivery_company = get_delivery_company(data["delivery_company"])
    d_purchase_timestamp = get_time(data["purchase_timestamp"])

    merged_d = {**d_city, **d_delivery_company, **d_purchase_timestamp}
    df = pd.DataFrame([merged_d])
    return df
