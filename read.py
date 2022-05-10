import pandas as pd
import os


# Getting file path dynamically
def get_file_path(base_dir, table_name):
    file_name = os.listdir(f'{base_dir}\{table_name}')[0]
    fp = f'{base_dir}\{table_name}\{file_name}'
    return fp


# Read a data from file
def get_reader(fp):
    df = pd.read_json(fp, lines=True, chunksize=1000)
    return df


if __name__ == '__main__':
    BASE_DIR = os.environ.get('BASE_DIR')
    table_name = os.environ.get('TABLE_NAME')
    file_path = get_file_path(BASE_DIR, table_name)
    json_reader = get_reader(file_path)
    for idx, df in enumerate(json_reader):
         print(f'Number of records in chunk with index {idx} is {df.shape[0]}')

