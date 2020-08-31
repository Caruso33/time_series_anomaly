import csv
import sqlite3


def read_csv(csv_path: str):
    """
    Reads and returns csv of given path/filename

    parameters:
    csv_path - 'path/filename.ext'

    returns: 
    list of rows
    """
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")

        line_count = 0
        invalid_count = 0
        column_name = []
        rows = []

        for row in csv_reader:
            if line_count == 0:
                # get column names
                column_name.extend([row[0].lower().replace(
                    " ", "_"), row[1].lower().replace(" ", "_")])

            elif row[0] and row[1]:
                # get data, store in rows
                rows.append({column_name[0]: row[0], column_name[1]: row[1]})

            else:
                invalid_count += 1
                continue

            line_count += 1

        print(
            f"Read {line_count} lines (1 of it is header), {invalid_count} were erroneous.")
        return rows


def get_data_col_names(csv_path):
    """
    Reads the col_names of the csv

    parameters:
    csv_path - 'path/filename.ext'

    returns:
    list of column names
    """
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        header_row = list(csv_reader)[0]

        return [header_row[0].lower().replace(" ", "_"), header_row[1].lower().replace(" ", "_")]


def rows_to_sqlite(rows: list, sqlite_path: str, col_names: [str]):
    """
    Receives list of rows and stores it into a given sqlite table

    parameters:
    rows - data to be stores
    sqlite_path - 'path/filename.ext' where to store the db
    col_names - list of str what to store from each row
    """
    conn = sqlite3.connect(sqlite_path)
    c = conn.cursor()

    c.execute(
        f'CREATE TABLE IF NOT EXISTS zykluszeiten (id INTEGER PRIMARY KEY AUTOINCREMENT, {col_names[0]} TEXT, {col_names[1]} INT)')

    for row in rows:
        col_names_0_val = row[col_names[0]]
        col_names_1_val = row[col_names[1]]

        c.execute(f'INSERT OR IGNORE INTO zykluszeiten (id, {col_names[0]}, {col_names[1]}) VALUES (NULL,?,?)', (
            col_names_0_val, col_names_1_val,))

        conn.commit()

    print(f"Wrote {len(rows)} rows to sqlite db.")

    c.close()
    conn.close()


def read_sqlite(sqlite_path: str, col_names: [str]):
    """
    Receives sqlite path and returns rows

    parameters:
    sqlite_path - 'path/filename.ext' where the db is stored
    col_names - list of str what to store from each row

    returns:
    list of rows
    """
    con = sqlite3.connect(sqlite_path)
    c = con.cursor()

    rows = []

    query = f"SELECT {col_names[0]}, {col_names[1]} FROM zykluszeiten"

    c.execute(query)
    for row in c.fetchall():
        rows.append(row)

    return rows
