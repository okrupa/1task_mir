class Models:
    def __init__(self, **entries):
        self.__dict__.update(entries)

models_data = {'simple': {"id": 0, "name": 'simple_model'}, 'random_forest': {'id': 1, 'name': 'random_forest_model'}}

model_type = Models(**models_data)
