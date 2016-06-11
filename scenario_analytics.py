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


def analytics(scenarios_df,noise_df, total_emails_df):
    """
    PERFORMS ANALYTICS AND WRITES TO FILE

    :param scenarios_df:
    :param master_df:
    :return:
    """

    total_emails = len(total_emails_df).unique()
    total_noise = len(noise_df).unique()
    calcs = []
    for scenario_name in scenarios_df['Scenario_Name'].unique():
        scenario_df = scenarios_df[scenarios_df['Scenario_Name']==scenario_name]

        hits = len(scenario_df)
        noisy = len(scenario_df[scenario_df['noise_flag'] == 1])
        clean = len(scenario_df[scenario_df['noise_flag'] == 0])
        pct_left_out = (1 - (float(hits) / total_emails))
        pct_noisy = (1 - (float(noisy) / hits))

        calc = {
            "Scenario": scenario_name,
            "Total_Emails": total_emails,
            "Total_Noise": total_noise,
            "Absolute_Number": "PASS",
            "Noisy": noisy,
            "Clean": clean,
            "Hits": hits,
            "PCT_Left_Out": pct_left_out,
            "pct_Noisy": pct_noisy,
        }

if __name__ == '__main__':

    scenarios_df = pd.read_csv("scenario1/scenario1_parsed_ids.csv")
    total_emails_df = pd.read_excel('master_table_110616.xls', sheetname='Total_Emails')
    noise_df = pd.read_excel('master_table_110616.xls', sheetname='Noise_Ids')

    scenarios_df = flag_noise(scenarios_df, noise_df)

    total_emails = len(total_emails_df)
    total_noise = len(noise_df)

    calcs = []
    for scenario_name in scenarios_df['Scenario_Name'].unique():
        scenario_df = scenarios_df[scenarios_df['Scenario_Name'] == scenario_name]

        hits = len(scenario_df)
        noisy = len(scenario_df[scenario_df['noise_flag'] == 1])
        clean = len(scenario_df[scenario_df['noise_flag'] == 0])
        pct_left_out = (1 - (float(hits) / total_emails))
        pct_noisy = (float(noisy) / hits)

        calc = {
            "Scenario": scenario_name,
            "Total_Emails": total_emails,
            "Total_Noise": total_noise,
            "Absolute_Number": "PASS",
            "Noisy": noisy,
            "Clean": clean,
            "Hits": hits,
            "PCT_Left_Out": pct_left_out,
            "pct_Noisy": pct_noisy,
        }
        calcs.append(calc)
    df = pd.DataFrame(calcs)
    df = df.set_index(['Scenario'])
    df= df.transpose()
    df.to_excel("scenario_stat.xls")
