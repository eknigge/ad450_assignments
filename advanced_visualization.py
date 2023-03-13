import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


def update_experience(value):
    items_to_replace = ['years', 'year', 'y']
    for i in items_to_replace:
        value = value.replace(i, '')
    return value


def update_income_data(value):
    items_to_replace = ['$', 'usd', ',', 'USD']
    for i in items_to_replace:
        value = value.replace(i, '')
    if 'k' in value:
        value = 1000 * float(value.replace('k', ''))
    return value


def data_corrections(df: pd.DataFrame) -> pd.DataFrame:
    df['Monthly Income'] = df['Monthly Income'].apply(update_income_data)
    df['Monthly Income'] = pd.to_numeric(df['Monthly Income'])
    df['Years of Employment'] = df['Years of Employment'].apply(update_experience)
    df['Years of Employment'] = pd.to_numeric(df['Years of Employment'])
    return df


def main():
    """
    Data Sources:
    https://www.kaggle.com/datasets/rkiattisak/car-ownership-predictionbeginner-intermediate
    https://stock.walmart.com/financials/annual-reports/default.aspx
    https://finance.yahoo.com/quote/SPY/history?period1=1670803200&period2=1678665600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true
    """
    data_filename = 'Car Ownership.csv'
    df = pd.read_csv(data_filename)
    df = df.dropna()
    df_stock = pd.read_csv('SPY.csv')
    df = data_corrections(df)
    bubble_chart(df)
    funnel_chart()
    plot_candlestick(df_stock)


def plot_candlestick(df: pd.DataFrame):
    candle_stick_object = go.Candlestick(x=df['Date'],
                   open=df['Open'],
                   high=df['High'],
                   low=df['Low'],
                   close=df['Close'])
    fig = go.Figure(data=candle_stick_object)
    fig.update_layout(
        title='SPY Stock Price Last 3 Months',
        yaxis_title='Price'
    )
    fig.show()


def funnel_chart():
    walmart_sales = dict(
        rev=[606, 611, 148, 20, 11],
        stage=['Net Sales', 'Sales + Membership', 'Gross Profit', 'Operating Profit', 'Net Profit']
    )
    fig = px.funnel(walmart_sales, x='rev', y='stage', title='Walmart Revenue 2022')
    fig.show()


def bubble_chart(df: pd.DataFrame):
    fig = px.scatter(
        df,
        x="Years of Employment",
        y="Monthly Income",
        size="Credit Score",
        color="Occupation",
        size_max=60,
        title='Monthly Revenue vs. Yrs of Employment vs. Credit Score'
    )
    fig.show()


if __name__ == '__main__':
    main()
