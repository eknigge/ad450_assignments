import pandas as pd

def main():
    coffee_data = {
        'Americano': [562, 623], 'Latte': [812, 925],
        'Espresso': [426, 384], 'Cappuccino': [852, 756]
        }
    index_values = ['2021 Sales', '2022 Sales']
    df = pd.DataFrame(data=coffee_data, index=index_values)
    print(df)

if __name__ == '__main__':
    main()