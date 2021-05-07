import pickle
import numpy as np


def get_prediction(feature_values, stamina):
    """ Given a list of feature values and a boolean for which model to use, return a prediction made by the model"""
    
    tech_model, stam_model = un_pickle_model()
    
    #Given a boolean for whether the data is stamina data or not, predicts using one of the two models
    if not stamina:
        predictions=np.around(tech_model.predict(feature_values), 2)
        return predictions
    else:
       predictions=np.around(stam_model.predict(feature_values), 2)
       return predictions

def un_pickle_model():
    """ Load the model from the .pkl file """
    with open('src/models/stam_model.pkl','rb') as stam_file:
        stam=pickle.load(stam_file)
    
    with open('src/models/tech_model.pkl', 'rb') as tech_file:
        tech=pickle.load(tech_file)

    return tech, stam