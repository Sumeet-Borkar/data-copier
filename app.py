import os
import sys
from read import get_file_path, get_reader
from write import load_db_table


def process_table(BASE_DIR, conn, table_name):
    file_path = get_file_path(BASE_DIR, table_name)
    json_reader = get_reader(file_path)
    for df in json_reader:
        load_db_table(df, conn, table_name, df.columns[0])
        print(' done')


def main():
    BASE_DIR = os.environ.get('BASE_DIR')
    table_names = sys.argv[1].split(',')
    configs = dict(os.environ.items())
    conn = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'
    for table_name in table_names:
        process_table(BASE_DIR, conn, table_name)


if __name__ == '__main__':
    main()