import pandas as pd
import numpy as np


def data_cleaner(df, is_stamina=False):
    '''Given a dataframe and boolean value for whether it is stamina or not,
        returns a new cleaned dataframe with NaN values and outliers removed.
        Preserves data within the 95th percentile for the following features:
        *Step count (unchanged for stamina data due to how common high
        step counts are)

        *BPM weighted average
        *BPM change count
        *Song NPS

        For technical data, removes the following features:
        'stream_count', 'stream_size_max', 'stream_size_avg',
        'stream_size_std', 'break_count', 'break_size_max',
        'break_size_avg', 'break_total', 'break_size_std'

        Fills NaN values with median for stamina data (same features
        as listed above):
        'stream_count', 'stream_size_max', 'stream_size_avg',
        'stream_size_std', 'break_count', 'break_size_max',
        'break_size_avg', 'break_total', 'break_size_std'
        '''

    tech_df = pd.DataFrame([])
    stam_df = pd.DataFrame([])
    ordered_features = ['title', 'artist', 'song_seconds', 'step_count',
                        'measure_count', 'bpm_weighted_avg', 'bpm_max',
                        'bpm_min', 'bpm_mode', 'bpm_change_count', 'song_nps',
                        'nps_per_measure_max', 'nps_per_measure_avg',
                        'nps_per_measure_median', 'nps_per_measure_std',
                        'nps_per_measure_mode', 'jumps', 'hands', 'quads',
                        'holds', 'mines', 'rolls', 'crossovers',
                        'footswitches', 'crossover_footswitches',
                        'jacks', 'invalid_crossovers', 'stop_count',
                        'stream_total', 'stream_count', 'stream_size_max',
                        'stream_size_avg', 'stream_size_std', 'break_count',
                        'break_size_max', 'break_size_avg', 'break_total',
                        'break_size_std', 'difficulty', 'rating']

    if is_stamina:
        stam_df = df[ordered_features]
        print(f"Initialized Stamina DataFrame with {len(stam_df)} rows.\n")
        # remove all songs with a rating over 28 from Stamina DataFrame.
        stam_df = stam_df.drop(stam_df.loc[stam_df['rating'] >= 28].index)

        '''Examine 90th percentile of the following Stamina DataFrame
        features and drop any outside of the 90th percentile:
        *BPM weighted average
        *BPM change count
        *Song NPS'''

        # bpm weighted average
        max_bpm_avg = round(stam_df.bpm_weighted_avg.quantile(.9))
        # bpm change count
        max_bpm_change = round(stam_df.bpm_change_count.quantile(.9))
        max_song_nps = stam_df.song_nps.quantile(.9)

        # drop those outliers!
        stam_df = stam_df.drop(stam_df.loc[
            (stam_df['bpm_weighted_avg'] > max_bpm_avg) |
            (stam_df['bpm_change_count'] > max_bpm_change) |
            (stam_df['song_nps'] > max_song_nps)].index)

        # for the sake of statistics
        # song_seconds
        max_seconds = stam_df.song_seconds.max()
        # step count
        max_steps = stam_df.step_count.max()

        '''Replace any negative bpm weighted averages with the median value'''
        bpm_median = stam_df.bpm_weighted_avg.median()
        stam_df['bpm_weighted_avg'] = np.where(
            stam_df['bpm_weighted_avg'] < 0, bpm_median, stam_df['bpm_weighted_avg'])

        print('Removing outliers and filling NaN values...\n')
        print(f'The songs in this Stamina dataset are up to {round(max_seconds, 3)} seconds ({round(max_seconds/60, 3)} minutes) long.')
        print(f'The songs in this Stamina dataset have up to {max_steps} steps.')
        print(f'The songs in this Stamina dataset have a max bpm weighted average up to {max_bpm_avg} bpm.')
        print(f'The songs in this Stamina dataset have up to {max_bpm_change} bpm changes.')
        print(f'The songs in this Stamina dataset have up to {round(max_song_nps, 3)} NPS.\n')

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

        # drop duplicates
        stam_df.drop_duplicates(inplace=True)

        print(f"Returning cleaned Stamina DataFrame with {len(stam_df)} rows and {len(stam_df.columns)} columns.")
        return stam_df

    else:
        tech_df = df[ordered_features]
        print(f"Initialized Tech DataFrame with {len(tech_df)} rows.\n")

        # remove all songs with a rating over 18 from Tech DataFrame.
        tech_df = tech_df.drop(
            tech_df.loc[tech_df['rating'] >= 18].index)

        '''Examine 90th percentile of the following Tech DataFrame features and drop any values outside of the 90th percentile:
        *Song Seconds
        *Step Count
        *BPM Weighted Average
        *BPM Change Count
        *Song NPS'''
        # song seconds
        max_seconds = tech_df.song_seconds.quantile(.90)
        # step count
        max_steps = round(tech_df.step_count.quantile(.90))
        # bpm weighted average
        max_bpm_avg = round(tech_df.bpm_weighted_avg.quantile(.90))
        # bpm change count
        max_bpm_change = round(tech_df.bpm_change_count.quantile(.90))
        # song nps
        max_song_nps = tech_df.song_nps.quantile(.90)

        '''Fill any negative BPM weighted average values with the median'''
        weighted_bpm_median = tech_df.bpm_weighted_avg.median()
        tech_df['bpm_weighted_avg'] = np.where(tech_df['bpm_weighted_avg'] < 0, weighted_bpm_median, tech_df['bpm_weighted_avg'])

        print('Removing outliers and filling NaN values...\n')
        print(f'The songs in this Tech dataset are up to {round(max_seconds, 3)} seconds ({round(max_seconds/60, 3)} minutes) long.')
        print(f'The songs in this Tech dataset have up to {max_steps} steps.')
        print(f'The songs in this Tech dataset have a max bpm weighted average up to {max_bpm_avg} bpm.')
        print(f'The songs in this Tech dataset have up to {max_bpm_change} bpm changes.')
        print(f'The songs in this Tech dataset have up to {round(max_song_nps, 3)} NPS.\n')

        tech_df = tech_df.drop(tech_df.loc[
            (tech_df['song_seconds'] > max_seconds) |
            (tech_df['step_count'] > max_steps) |
            (tech_df['bpm_weighted_avg'] > max_bpm_avg) |
            (tech_df['bpm_change_count'] > max_bpm_change) |
            (tech_df['song_nps'] > max_song_nps)].index)

        '''Drop any song labelled as 'Beginner' with a rating above 1'''
        tech_df = tech_df.drop(tech_df.loc[
            (tech_df['rating'] == 1) &
            (tech_df['difficulty'] != 'Beginner')].index)

        '''The following columns will be dropped entirely because they are not particularly useful for Tech Data'''

        cols_to_drop = ['stream_count', 'stream_size_max', 'stream_size_avg',
                        'stream_size_std', 'break_count', 'break_size_max',
                        'break_size_avg', 'break_total', 'break_size_std']

        tech_df = tech_df.drop(columns=cols_to_drop, axis=1)

        # drop duplicates
        tech_df.drop_duplicates(inplace=True)

        print(f"Returning cleaned Tech DataFrame with {len(tech_df)} rows and {len(tech_df.columns)} columns.")
        return tech_df
