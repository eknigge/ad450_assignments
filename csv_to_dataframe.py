import pandas as pd

def main():
    data_file = 'netflix_titles.csv'
    df = pd.read_csv(data_file)
    print(df)

if __name__ == '__main__':
    main()