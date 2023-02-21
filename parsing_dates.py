import pandas as pd


def main():
    data_file = 'netflix_titles.csv'
    df = pd.read_csv(data_file)
    print(f"'date_added' column data type: { df['date_added'].dtype}")

    df['date_added'] = pd.to_datetime(df['date_added'])
    print(f"'date_added' updated column data type: { df['date_added'].dtype}")


if __name__ == '__main__':
    main()
