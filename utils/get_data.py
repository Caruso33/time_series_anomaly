import csv, sqlite3


def read_csv(csv_path: str):
    """
    Reads and returns csv of given path/filename
    parameters:
    csv_path - 'path/filename.ext'
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
                column_name.extend([row[0].lower().replace(" ", "_"), row[1].lower().replace(" ", "_")])

            elif row[0] and row[1]:
                # get data, store in rows
                rows.append({column_name[0]: row[0], column_name[1]: row[1]})

            else:
                invalid_count += 1
                continue

            line_count += 1

        print(f"Read {line_count} lines (1 of it is header), {invalid_count} were erroneous.")
        return rows


def rows_to_sqlite(rows: list, sqlite_path: str):
    """
    Receives list of rows and stores it into a given sqlite table

    parameters:
    rows - data to be stores
    fields - list of str what to store form each row
    sqlite_path - 'path/filename.ext' where to store the db
    """
    conn = sqlite3.connect(sqlite_path)
    c = conn.cursor()

    col_names = list(rows[0].keys())
    
    c.execute(f'CREATE TABLE IF NOT EXISTS zykluszeiten ({col_names[0]} DATE, {col_names[1]} INT)')

    for row in rows:
        col_names_0_val = row[col_names[0]]
        col_names_1_val = row[col_names[1]]

        c.execute(f'INSERT OR IGNORE INTO zykluszeiten ({col_names[0]}, {col_names[1]}) VALUES (?,?)', (col_names_0_val, col_names_1_val,))

        conn.commit()

    print(f"Wrote {len(rows)} rows to sqlite db.")

    c.close()
    conn.close()
