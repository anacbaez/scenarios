# parse ids from different scenarios:
import re
import pandas as pd
import sys
import json


def flag_noise(scenario_df, noise_df):
    """
    returns a the scenario dataframe with an appended noise flag
    1 indicates the entry is noise
    0 indicates the entry is not noise
    :param scenario_df: scenario dataframe with columns ('Unique_ID', 'Content_ID', 'Scenario_Name')
    :param noise_df:
    :return scenario_df:
    """
    noise_df['noise_flag'] = 1

    scenario_df = scenario_df.merge(noise_df[['Unique_ID', 'noise_flag']], on=["Unique_ID"], how="left")
    scenario_df['noise_flag'].fillna(0, inplace=True)

    return scenario_df


def analytics(scenarios_df, master_df):
    """
    PERFORMS ANALYTICS AND WRITES TO FILE
    
    :param scenarios_df:
    :param master_df:
    :return:
    """

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

    scenario_df = pd.read_csv("scenario1/scenario1_parsed_ids.csv")
    total_emails_df = pd.read_excel('master_table_110616.xls', sheetname='Total_Emails')
    noise_df = pd.read_excel('master_table_110616.xls', sheetname='Noise_Ids')

    scenario_df = flag_noise(scenario_df, noise_df)
    # analytics()
