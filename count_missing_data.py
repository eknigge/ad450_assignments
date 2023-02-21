import pandas as pd


def main():
    data_file = 'netflix_titles.csv'
    df = pd.read_csv(data_file)
    columns = df.columns
    n = df.shape[0]
    total_null = 0
    total_value = 0

    for col in columns:
        null_values = n - df[col].count()
        percent_null = null_values / n * 100
        print(f'{null_values} or {percent_null:.2f}% null null values for column {col}')
        total_null += null_values
        total_value += df[col].shape[0]

    print(f'Total null values: {total_null}')
    print(f'Percent of total null: {100*total_null/total_value:.2f}% ')


if __name__ == '__main__':
    main()