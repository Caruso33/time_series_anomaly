import os.path
from utils import read_csv, rows_to_sqlite, read_sqlite, get_data_col_names
import manage
from subprocess import call
import pandas as pd


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


def get_data_metrics(rows: list):
    """
    Get a summary of the cycle times metrics
    """
    df = pd.DataFrame(rows)
    print(df.describe())
    """
    count  1469.000000
    mean    108.963240
    std     232.790995
    min       4.000000
    25%      50.000000
    50%     120.000000
    75%     140.000000
    max    6000.000000
    """


def run():
    rows = prepare_data()

    # uncomment to get printed metrics
    # get_data_metrics(rows)
    
    # start django server
    call(["python", "manage.py", "migrate"])
    call(["python", "manage.py", "runserver"])


if __name__ == "__main__":
    run()
