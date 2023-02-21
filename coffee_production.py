import pandas as pd


def main():
    data_file = 'coffee_database_dump.csv'
    df = pd.read_csv(data_file)
    df_sum = df.groupby('coffee_type').sum(numeric_only=True)
    df_corr = df_sum.T.corr()

    min_value = df_corr['Robusta'].loc['Robusta/Arabica']
    max_value = df_corr['Arabica'].loc['Arabica/Robusta']

    print(f"Aggregation Example: \n{df_sum}\n\n")
    print(f"Correlation Matrix Example: {df_corr}\n\n")
    print(f"Weakest correlation Robusta and Robusta/Arabica: {min_value:.4f}")
    print(f"Strongest correlation Arabica and Arabica/Robusta: {max_value:.4f}")


if __name__ == '__main__':
    main()
