import pandas as pd
import numpy as np

'''Given a dataframe and boolean value for whether it is stamina or not, returns a new
cleaned dataframe with NaN values and outliers removed.'''

def data_cleaner(df, is_stamina = False):
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
        print(f"Initialized Stamina DataFrame with {len(stam_df)} rows.\n")

        '''Replace any negative bpm weighted averages with the median value'''
        bpm_median = stam_df.bpm_weighted_avg.median()
        stam_df[stam_df['bpm_weighted_avg'] < 0 ] = bpm_median

        '''Examine 90th percentile of the following Stamina DataFrame features and drop any outside of the 90th percentile: 
        *Step count
        *BPM weighted average
        *BPM change count
        *Song NPS'''
        #step count
        max_steps = round(stam_df.step_count.quantile(.975)) #here we are only removing the very far outliers as stamina songs tend to run long
        #bpm weighted average
        max_bpm_avg = stam_df.bpm_weighted_avg.quantile(.9)
        #bpm change count
        max_bpm_change = round(stam_df.bpm_change_count.quantile(.9))
        #song nps
        max_song_nps = stam_df.song_nps.quantile(.9)

        ##for the sake of statistics, let's grab the max seconds without altering the percentiles.
        #song_seconds
        max_seconds = stam_df.song_seconds.max()

        print(f'Removing outliers and filling NaN values...\n')
        print(f'The songs in this Stamina dataset are up to {round(max_seconds, 3)} seconds ({round(max_seconds/60, 3)} minutes) long.')
        print(f'The songs in this Stamina dataset have up to {max_steps} steps.')
        print(f'The songs in this Stamina dataset have a max bpm weighted average up to {max_bpm_avg} bpm.')
        print(f'The songs in this Stamina dataset have up to {max_bpm_change} bpm changes.')
        print(f'The songs in this Stamina dataset are up to {round(max_song_nps, 3)} NPS.\n')

        #drop those outliers!
        stam_df = stam_df.drop(stam_df.loc[(stam_df['bpm_change_count'] > max_bpm_change) | 
                                           (stam_df['bpm_weighted_avg'] > max_bpm_avg) | 
                                           (stam_df['song_nps'] > max_song_nps) |
                                           (stam_df['step_count'] > max_steps)].index)

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

        '''Feature engineering to capture logarithmic curve in stream_total'''
        stam_df['stream_log_transform'] = np.where(stam_df['stream_total'] > 0, np.log(stam_df['stream_total']), stam_df['stream_total'])

        print(f"Returning cleaned Stamina DataFrame with {len(stam_df)} rows and {len(stam_df.columns)} columns.")
        return stam_df

    else:
        tech_df = df[ordered_features]
        print(f"Initialized Tech DataFrame with {len(tech_df)} rows.\n")

        #remove all songs with a rating over 18 from Tech DataFrame.
        tech_df = tech_df.drop(tech_df.loc[tech_df['rating'] >= 18].index)
        
        '''Examine 90th percentile of the following Tech DataFrame features and drop any values outside of the 90th percentile:
        *Song Seconds
        *Step Count
        *BPM Weighted Average
        *BPM Change Count
        *Song NPS'''
        #song seconds
        max_seconds = tech_df.song_seconds.quantile(.90)
        #step count
        max_steps = round(tech_df.step_count.quantile(.90))
        #bpm weighted average
        max_bpm_avg = round(tech_df.bpm_weighted_avg.quantile(.9))
        #bpm change count
        max_bpm_change = round(tech_df.bpm_change_count.quantile(.9))
        #song nps
        max_song_nps = tech_df.song_nps.quantile(.9)

        '''Fill any negative BPM weighted average values with the median'''
        weighted_bpm_median = tech_df.bpm_weighted_avg.median()

        print(f'Removing outliers and filling NaN values...\n')
        print(f'The songs in this Tech dataset are up to {round(max_seconds, 3)} seconds ({round(max_seconds/60, 3)} minutes) long.')
        print(f'The songs in this Tech dataset have up to {max_steps} steps.')
        print(f'The songs in this Tech dataset have a max bpm weighted average up to {max_bpm_avg} bpm.')
        print(f'The songs in this Tech dataset have up to {max_bpm_change} bpm changes.')
        print(f'The songs in this Tech dataset are up to {round(max_song_nps, 3)} NPS.\n')

        tech_df = tech_df.drop(tech_df.loc[(tech_df['song_seconds'] > max_seconds) | 
                                           (tech_df['step_count'] > max_steps)|
                                           (tech_df['bpm_weighted_avg'] > max_bpm_avg) |
                                           (tech_df['bpm_change_count'] > max_bpm_change) |
                                           (tech_df['song_nps'] > max_song_nps)].index)

        tech_df['bpm_weighted_avg'] = np.where(tech_df['bpm_weighted_avg'] < 0, max_bpm_avg, tech_df['bpm_weighted_avg'])

        '''Drop any song labelled as 'Beginner' with a rating above 1'''
        tech_df = tech_df.drop(tech_df.loc[(tech_df['rating'] == 1) & (tech_df['difficulty'] != 'Beginner')].index)

        '''The following columns will be dropped entirely because they are not particularly useful for Tech Data'''

        cols_to_drop = ['stream_count', 'stream_size_max', 'stream_size_avg', 'stream_size_std', 'break_count', 'break_size_max',\
               'break_size_avg', 'break_total', 'break_size_std']

        tech_df = tech_df.drop(columns = cols_to_drop, axis = 1)

        '''Feature engineering to capture logarithmic curve in stream_total'''
        tech_df['stream_log_transform'] = np.where(tech_df['stream_total'] > 0, np.log(tech_df['stream_total']), tech_df['stream_total'])
        
        print(f"Returning cleaned Tech DataFrame with {len(tech_df)} rows and {len(tech_df.columns)} columns.")
        return tech_df


