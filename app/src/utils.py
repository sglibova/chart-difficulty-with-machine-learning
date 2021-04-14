import pandas as pd

def extract_feature_values(data):
    """ Given a params dict, return the values for feeding into a model"""
    
    # Replace these features with the features for your model. They need to 
    # correspond with the `name` attributes of the <input> tags

    #set stamina = false by default to use the tech predictor, change to true if 'datatype' = 1
    stamina = False

    EXPECTED_FEATURES = [
        "step_count",
        "song_nps",
        "stream_total", 
        "datatype"]

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
    
    if data[EXPECTED_FEATURES[-1]] == 1:
        stamina = True  
        for s_feature in STAM_FEATURES:
            for e_feature in EXPECTED_FEATURES:
                if s_feature == e_feature:
                    s_feature = data[e_feature]
                else:
                    s_feature = 0
        
        values = [[float(data[feature]) for feature in STAM_FEATURES]]
        return pd.DataFrame(values, columns=STAM_FEATURES), stamina
    
    else:
        for t_feature in TECH_FEATURES:
            for e_feature in EXPECTED_FEATURES:
                if t_feature == e_feature:
                    t_feature = data[e_feature]
                else:
                    t_feature = 0 

        values = [[float(data[feature]) for feature in TECH_FEATURES]]
        return pd.DataFrame(values, columns=TECH_FEATURES), stamina
