import pandas as pd
import numpy as np


def data_cleaner(df, is_stamina = False):

    '''  
    For technical data, removes the following features:
    'stream_count', 'stream_size_max', 'stream_size_avg', 'stream_size_std', 'break_count', 'break_size_max',
    'break_size_avg', 'break_total', 'break_size_std'

    Fills NaN values with median for stamina data (same features as listed above):
    'stream_count', 'stream_size_max', 'stream_size_avg', 'stream_size_std', 'break_count', 'break_size_max', 
    'break_size_avg', 'break_total', 'break_size_std'
        
        '''
    tech_df = pd.DataFrame([])
    stam_df = pd.DataFrame([])
    ordered_features = ['title', 'artist', 'song_seconds', 'step_count', 'measure_count', 'bpm_weighted_avg', 'bpm_max', 'bpm_min',\
                    'bpm_mode', 'bpm_change_count', 'song_nps', 'nps_per_measure_max', 'nps_per_measure_avg', 'nps_per_measure_median',\
                    'nps_per_measure_std', 'nps_per_measure_mode', 'jumps', 'hands', 'quads', 'holds', 'mines', 'rolls',\
                    'crossovers', 'footswitches', 'crossover_footswitches', 'jacks', 'invalid_crossovers', 'stop_count',\
                    'stream_total', 'stream_count', 'stream_size_max', 'stream_size_avg', 'stream_size_std', 'break_count',\
                    'break_size_max', 'break_size_avg', 'break_total', 'break_size_std', 'difficulty', 'rating']
    
    if is_stamina:
        stam_df = df[ordered_features]
        
        '''Replace any negative bpm weighted averages with the median value'''
        bpm_median = stam_df.bpm_weighted_avg.median()
        stam_df['bpm_weighted_avg'] = np.where(stam_df['bpm_weighted_avg'] < 0 , bpm_median, stam_df['bpm_weighted_avg'])

        '''Because these features are valuable to stamina data, let's fill NaN values with the median:
            ['stream_count', 'stream_size_max', 'stream_size_avg', 'stream_size_std', 'break_count', 'break_size_max', \
            'break_size_avg', 'break_total', 'break_size_std']
        '''
        stam_df = stam_df.fillna(0)
        stam_df.stream_count = stam_df.stream_count.replace(0, stam_df.stream_count.median())
        stam_df.stream_size_max = stam_df.stream_size_max.replace(0, stam_df.stream_size_max.median())
        stam_df.stream_size_avg = stam_df.stream_size_avg.replace(0, stam_df.stream_size_avg.median())
        stam_df.stream_size_std = stam_df.stream_size_std.replace(0, stam_df.stream_size_std.median())
        stam_df.break_count = stam_df.break_count.replace(0, stam_df.break_count.median())
        stam_df.break_size_max = stam_df.break_size_max.replace(0, stam_df.break_size_max.median())
        stam_df.break_size_avg = stam_df.break_size_avg.replace(0, stam_df.break_size_avg.median())
        stam_df.break_total = stam_df.break_total.replace(0, stam_df.break_total.median())
        stam_df.break_size_std = stam_df.break_size_std.replace(0, stam_df.break_size_std.median())

        return stam_df

    else:
        tech_df = df[ordered_features]
        print(f"Initialized Tech DataFrame with {len(tech_df)} rows.\n")

        '''Fill any negative BPM weighted average values with the median'''
        weighted_bpm_median = tech_df.bpm_weighted_avg.median()
        tech_df['bpm_weighted_avg'] = np.where(tech_df['bpm_weighted_avg'] < 0, weighted_bpm_median, tech_df['bpm_weighted_avg'])

        '''The following columns will be dropped entirely because they are not particularly useful for Tech Data'''

        cols_to_drop = ['stream_count', 'stream_size_max', 'stream_size_avg', 'stream_size_std', 'break_count', 'break_size_max',\
               'break_size_avg', 'break_total', 'break_size_std']

        tech_df = tech_df.drop(columns = cols_to_drop, axis = 1)
        
        return tech_df


