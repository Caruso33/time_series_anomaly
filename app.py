from utils import read_csv

def run():
    csv_path = "data/20200828_Zykluszeiten_Log.csv"
    read_csv(csv_path)

if __name__ == '__main__':
    run()