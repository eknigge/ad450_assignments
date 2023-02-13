import pandas as pd


def movie_in_title(input_value) -> bool:
    return 'movie' in input_value.lower()


def main():
    data_filename = 'netflix_titles.csv'
    df = pd.read_csv(data_filename)
    df_movie = df[df['type'] == 'Movie']
    print(df_movie)

    df_movie_in_title = df
    df_movie_in_title['has_movie_in_title'] = df_movie_in_title['title'].apply(movie_in_title)
    df_movie_in_title = df_movie_in_title[df_movie_in_title['has_movie_in_title'] == True]
    print(df_movie_in_title, df_movie_in_title['title'].tolist())


if __name__ == '__main__':
    main()
