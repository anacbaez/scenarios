import re
import pandas as pd
import sys
import os

# def init():

def walk_folder(folder_name):
    """
    yields a each file in the folder as a generator
    :param folder_name:
    :yield file_name:
    """
    for file_name in os.listdir(folder_name):
        if file_name.endswith(".txt"):
            yield os.path.join(folder_name, file_name)


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

def combine_data(main_df, new_df, new_columns_names):
    """Combine extracted ids with existing table"""
    col_headers = list(main_df.columns)
    col_headers = col_headers + new_columns_names

    main_df = pd.concat([main_df, new_df], axis=1, keys=col_headers, ignore_index=True)
    main_df.columns = col_headers

    return main_df


if __name__ == '__main__':
    folder_name = "scenario1"
    main_df = pd.DataFrame()

    for file_name in walk_folder(folder_name):
        ids_df = parse_ids(file_name)
        ids_df['Scenario_Name'] = os.path.basename(file_name).split('.')[0]
        main_df = pd.concat([main_df, ids_df], ignore_index=True)

    output_name = "{}_parsed_ids.csv".format(folder_name)

    main_df.to_csv(os.path.join(folder_name, output_name), index=False)



