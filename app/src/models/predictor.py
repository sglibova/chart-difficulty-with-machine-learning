import pickle

def get_prediction(feature_values, stamina):
    """ Given a list of feature values, return a prediction made by the model"""
    
    stam_model, tech_model = un_pickle_model()
    
    #Given a boolean for whether the data is stamina data or not, predicts using one of the two models
    if stamina:
        predictions = stam_model.predict(feature_values)
    # We are only making a single prediction, so return the 0-th value
    else:
        prediction = tech_model.predict(feature_values)
    return predictions[0]

def un_pickle_model():
    """ Load the model from the .pkl file """
    with open('src/models/stam_model.pkl','rb') as stam_file:
        stam = pickle.load(stam_file)
    
    with open('src/models/tech_model.pkl', 'rb') as tech_file:
        tech = pickle.load(tech_file)

    return stam, tech