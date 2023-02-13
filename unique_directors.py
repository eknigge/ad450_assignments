import pandas as pd


def main():
    data_filename = 'netflix_titles.csv'
    df = pd.read_csv(data_filename)
    unique_directors = df['director'].drop_duplicates()
    print(f'Number of unique directors: {unique_directors.shape[0]}\n\n')
    print(unique_directors)


if __name__ == '__main__':
    main()
