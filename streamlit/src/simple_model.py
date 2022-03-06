import pandas as pd

class SimpleModel:
    def __init__(self):
        self._cities_mean_time = pd.read_json("../models/simple_model.jsonl", lines = True)
        self._convertToObject()
        
    def predict(self, data):
        city = ""
        for col in data.columns:
            if col.find("city_") != -1 and (data[col] == 1).bool():
                city = col
        if not city:
            city = "else"
        return self.predict_by_city(city)
        
    def predict_by_city(self, city):
        return self._cities_mean_time[city]
        
    def _convertToObject(self):
        self._cities_mean_time = self._cities_mean_time.to_dict('records')
        newObject = {}
        for i in self._cities_mean_time:
            newObject[i["city"]] = i["mean"]
        res = 0
        for val in newObject.values():
            res += val
        newObject["else"] =  res / len(newObject)
        self._cities_mean_time = newObject