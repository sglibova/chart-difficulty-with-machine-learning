import pandas as pd
import numpy as np

ALLOWED_EXTENSIONS = ['.csv']

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_feature_values(data):
    """ Given a params dict, return the values for feeding into a model"""  

    ordered_features = ['song_seconds', 'step_count', 'measure_count', 'bpm_weighted_avg', 'bpm_max', 'bpm_min',\
                    'bpm_mode', 'bpm_change_count', 'song_nps', 'nps_per_measure_max', 'nps_per_measure_avg', 'nps_per_measure_median',\
                    'nps_per_measure_std', 'nps_per_measure_mode', 'jumps', 'hands', 'quads', 'holds', 'mines', 'rolls',\
                    'crossovers', 'footswitches', 'crossover_footswitches', 'jacks', 'invalid_crossovers', 'stop_count',\
                    'stream_total']
    feature_values = data[ordered_features]
    feature_values['stream_log_transform'] = np.where(feature_values['stream_total'] > 0, np.log(feature_values['stream_total']), feature_values['stream_total'])
    return feature_values
        
