import pandas as pd

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_feature_values(data):
    """ Given a params dict, return the values for feeding into a model"""
    
    #expected input step_count, song_nps, nps_per_measure_max, nps_per_measure_avg, nps_per_measure_std, stream_total

    STAM_FEATURES = ['song_seconds', 'step_count', 'measure_count', 'bpm_weighted_avg',
       'bpm_max', 'bpm_min', 'bpm_mode', 'bpm_change_count', 'song_nps',
       'nps_per_measure_max', 'nps_per_measure_avg', 'nps_per_measure_median',
       'nps_per_measure_std', 'nps_per_measure_mode', 'jumps', 'hands',
       'quads', 'holds', 'mines', 'rolls', 'crossovers', 'footswitches',
       'crossover_footswitches', 'jacks', 'invalid_crossovers', 'stop_count',
       'stream_total', 'stream_count', 'stream_size_max', 'stream_size_avg',
       'stream_size_std', 'break_count', 'break_size_max', 'break_size_avg',
       'break_total', 'break_size_std', 'stream_log_transform']

    TECH_FEATURES = ['song_seconds', 'step_count', 'measure_count', 'bpm_weighted_avg',
       'bpm_max', 'bpm_min', 'bpm_mode', 'bpm_change_count', 'song_nps',
       'nps_per_measure_max', 'nps_per_measure_avg', 'nps_per_measure_median',
       'nps_per_measure_std', 'nps_per_measure_mode', 'jumps', 'hands',
       'quads', 'holds', 'mines', 'rolls', 'crossovers', 'footswitches',
       'crossover_footswitches', 'jacks', 'invalid_crossovers', 'stop_count',
       'stream_total', 'stream_log_transform']

    # if expected input is 0, this data is tech data and will be processed using the TECH_FEATURES list
    # stamina Boolean value will be set to return as False
    if data["datatype"] == str(0):
        stamina = False
        lis = list(map(data.get, TECH_FEATURES))
        values_list = [0 if val is None else val for val in lis]
        
        return pd.DataFrame(data = [values_list], columns=TECH_FEATURES), stamina
    
    # if expected input is 1, this data is stamina data and will be processed using the STAM_FEATURES list
    # stamina Boolean value will be set to return as True
    else:
        stamina = True 
        lis = list(map(data.get, STAM_FEATURES))
        values_list = [0 if val is None else val for val in lis]
        
        return pd.DataFrame(data = [values_list], columns=STAM_FEATURES), stamina
        
