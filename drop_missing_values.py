import pandas as pd


def main():
    data_file = 'netflix_titles.csv'
    df = pd.read_csv(data_file)
    total_before = df.shape[0]

    director_na_removed = df.dropna(subset=['director'])
    print(f'Rows remaining after NA director removed: {director_na_removed.shape[0]}')

    director_and_cast = df.dropna(subset=['director', 'cast'])
    print(f'Director and cast NA removed: {director_and_cast.shape[0]}')

    na_removed = df.dropna()
    print(f'All missing removed: {na_removed.shape[0]}')
    print(na_removed)


if __name__ == '__main__':
    main()
