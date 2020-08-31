import os.path
from utils import read_csv, rows_to_sqlite, read_sqlite, get_data_col_names
import manage
from subprocess import call


def prepare_data():
    """
    Creates a sqlite database if not already present with the
    data of the given csv
    """
    csv_path = "data/20200828_Zykluszeiten_Log.csv"
    sqlite_path = "data/time_series.db"

    col_names = get_data_col_names(csv_path)

    if not os.path.isfile(sqlite_path):
        rows = read_csv(csv_path)
        rows_to_sqlite(rows, sqlite_path, col_names)

    return read_sqlite(sqlite_path, col_names)


def run():
    prepare_data()
    # start django server
    call(["python", "manage.py", "migrate"])
    call(["python", "manage.py", "runserver"])


if __name__ == "__main__":
    run()
