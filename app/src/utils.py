import pandas as pd
import numpy as np
from src.data_cleaning import data_cleaner


ALLOWED_EXTENSIONS=['.csv']

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_feature_values(data, verifier):
    """ Given a params dict, return the values for feeding into a model"""  

    #need to include a separate lists of predictor values because the data cleaner function returns data with artist and title,
    #which are not used for predicting puproses
    tech_features=['song_seconds', 'step_count', 'measure_count', 'bpm_weighted_avg', 'bpm_max', 'bpm_min',\
                    'bpm_mode', 'bpm_change_count', 'song_nps', 'nps_per_measure_max', 'nps_per_measure_avg', 'nps_per_measure_median',\
                    'nps_per_measure_std', 'nps_per_measure_mode', 'jumps', 'hands', 'quads', 'holds', 'mines', 'rolls',\
                    'crossovers', 'footswitches', 'crossover_footswitches', 'jacks', 'invalid_crossovers', 'stop_count',\
                    'stream_total']

    stam_features=['song_seconds', 'step_count', 'measure_count', 'bpm_weighted_avg', 'bpm_max', 'bpm_min',\
                    'bpm_mode', 'bpm_change_count', 'song_nps', 'nps_per_measure_max', 'nps_per_measure_avg', 'nps_per_measure_median',\
                    'nps_per_measure_std', 'nps_per_measure_mode', 'jumps', 'hands', 'quads', 'holds', 'mines', 'rolls',\
                    'crossovers', 'footswitches', 'crossover_footswitches', 'jacks', 'invalid_crossovers', 'stop_count',\
                    'stream_total', 'stream_count', 'stream_size_max', 'stream_size_avg', 'stream_size_std', 'break_count',\
                    'break_size_max', 'break_size_avg', 'break_total', 'break_size_std']
    #confirms that the user selected "tech"
    if verifier==str(0):
        stamina=False
        feature_values=data_cleaner(data, is_stamina=False)
        feature_values=feature_values[tech_features]
        feature_values['stream_log_transform']=np.where(feature_values['stream_total'] > 0, np.log(feature_values['stream_total']), feature_values['stream_total'])
        return feature_values, stamina
    #else, the user selected stamina    
    else:
        stamina=True
        feature_values=data_cleaner(data, is_stamina=True)
        feature_values=feature_values[stam_features]
        feature_values['stream_log_transform']=np.where(feature_values['stream_total'] > 0, np.log(feature_values['stream_total']), feature_values['stream_total'])
        return feature_values, stamina

