from utils import read_csv, rows_to_sqlite


def run():
    csv_path = "data/20200828_Zykluszeiten_Log.csv"
    sqlite_path = "data/time_series.db"

    rows = read_csv(csv_path)
    rows_to_sqlite(rows, sqlite_path)


if __name__ == "__main__":
    run()
