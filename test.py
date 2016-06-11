# parse ids from different scenarios:
import re
import pandas as pd
import sys
import json

# def init():

def parse_ids(id_file_name):
    """parse ids from text file"""
    with open(id_file_name, 'r') as f:
        all_ids = f.read()

    all_ids = all_ids.split(',')
    id_dict = {}
    for i in all_ids:
        id_dict[i.split(' :')[1].strip()] = i.split(' :')[0].strip()
    scenario_labels = []

    df = pd.DataFrame(list(id_dict.items()), columns=['Unique_ID', 'Message_ID'])
    return df

def stats_table():
    pass

def add_stat(stats, stat_name, value):
    """
    Add stat to the stats dictionary
    :param stat_name:
    :return: stats
    """
    stats.set_default(stat_name, [])
    stats[stat_name].append(value)
    return stats

def analytics():

    #load parsed file
    master = pd.read_csv('master_table_100616.csv')

    # stats = pd.DataFrame(columns=['Scenario', 'Total Emails', 'Total Noise', 'Pc Filtered', 'Clean',
    #                               'Noisy', 'Pc Noisy', 'Pc Missed'])

    stats = {}
    # stats['Scenario'] = []
    # stats['Total  Email'] = []
    # stats['Total Noise'] = []
    # stats['Absolute number'] =[]
    # stats['Noisy'] = []
    # stats['Clean'] = []
    # stats['Hits'] = []
    # stats['% Left out'] = []
    # stats['% Noisy'] = []

    for scenario_name in scenario_names:
        # df_scenario_name = pd.DataFrame(main_df[scenario_name], columns=['Scenario'])
        scenario_col = main_df[scenario_name].unique()
        print(scenario_name)

        noise_col = main_df['Noise unique'].unique()

        noisy = []
        for i in noise_col:
            if i in scenario_col:
                noisy.append(i)

        print(len(noisy))
        # print(main_df['Total  Emails'])
        df = pd.DataFrame(noisy)
        df.columns = ['Noise unique']
        # df.to_csv('noisy_x'+scenario_name +'.csv', index=False)
        # join_df = pd.merge(df,main_df, left_on='Noise unique',right_on='Noise unique', how='left')
        # join_df.to_csv('noisy_'+scenario_name +'.csv', index=False)

        add_stat(stats, 'Scenario', 'Sup bitches')
        print json.dumps(stats, indent=4)


        sys.exit(0)




        print join_df
        break
        stats.set_default('Scenario')
        stats['Scenario'].append(scenario_name)
        stats['Total  Email'].append(len(main_df['Total  Emails'].unique()))
        stats['Total Noise'].append(len(main_df['Noise unique'].unique()))
        stats['Noisy'].append(len(noisy))
        stats['Clean'].append(len(main_df[scenario_name].unique()) - len(noisy))
        stats['Hits'].append(len(main_df[scenario_name].unique()))

        stats['% Left out'].append(
            (1 - (float(len(main_df[scenario_name].unique())) / len(main_df['Total  Emails'].unique()))))
        stats['% Noisy'].append(1 - (float(len(noisy)) / len(main_df[scenario_name].unique())))

    df = pd.DataFrame.from_dict(stats, orient='index')
    # df = df.transpose()
    print(df)

    print()
    # df.to_csv("scenario_stats.csv", index=False)
    # main_df = pd.concat([main_df, df], axis=1, ignore_index=True)

    # main_df = main_df.columns(['Noise'])
    # print("Ids added to main table")

    # create new cols for noise ids inside scenario
    # main_df.to_csv("master_table_100616.csv", index=False)

if __name__ == '__main__':

    analytics()