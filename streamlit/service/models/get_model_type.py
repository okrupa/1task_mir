from models.model_type import model_type

def get_model_type(model_id):
    if model_id ==0:
        return model_type.simple
    else:
        return model_type.random_forest