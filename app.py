import os.path
from utils import read_csv, rows_to_sqlite, read_sqlite, get_data_col_names


def run():
    csv_path = "data/20200828_Zykluszeiten_Log.csv"
    sqlite_path = "data/time_series.db"

    col_names = get_data_col_names(csv_path)


    if not os.path.isfile(sqlite_path):
        rows = read_csv(csv_path)
        rows_to_sqlite(rows, sqlite_path, col_names)

    rows = read_sqlite(sqlite_path, col_names)
    print(rows)


if __name__ == "__main__":
    run()
