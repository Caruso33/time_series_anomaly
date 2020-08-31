import csv, sqlite3

def read_csv(csv_path):
    """
    Reads and returns csv of given path/filename
    parameters:
    csv_path - 'path/filename.ext'
    """
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')

        line_count = 0
        column_name = []
        rows = []

        for row in csv_reader:
            if line_count == 0:
                # get column names
                column_name.extend([row[0], row[1]])

            elif row[0] and row[1]:
                # get data, store in rows
                rows.append({
                    column_name[0]: row[0],
                    column_name[1]: row[1]
                })
            line_count += 1

        print(f'Processed {line_count} lines.')
        return rows

