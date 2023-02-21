import pandas as pd


def main():
    data_file = 'video_game_sales.csv'
    df = pd.read_csv(data_file)
    df_subset = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']]
    correl_df = df_subset.corr()

    print(f"Largest correlation NA Sales & Global Sales: {correl_df['Global_Sales'].iloc[0]:.4f}")
    print(f"Smallest correlation Other Sales & JP Sales: {correl_df['Other_Sales'].iloc[2]:.4f}")


if __name__ == '__main__':
    main()
