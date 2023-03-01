import pandas
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def main():
    data_filename = 'Everett-Seattle-traffic.csv'
    df = pd.read_csv(data_filename, index_col='Time')
    column_to_remove = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
                        'Thursday', 'Friday', 'Saturday', '02/26/2023',
                        '02/27/2023', '02/28/2023']
    df = df.drop(column_to_remove, axis=1)
    line_plot(df)

    line_plot(df)
    contour_plot(df)
    bar_chart(df)
    scatter_plot(df)


def scatter_plot(df: pandas.DataFrame):
    fig, ax = plt.subplots()
    x = mdates.datestr2num(df.index.values)
    columns = df.columns

    for col in columns:
        ax.scatter(x, df[col], c='blue', alpha=0.5)

    ax.xaxis.set_major_locator(mdates.HourLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%HH'))
    plt.xticks(rotation=90)

    ax.set_title('Scatter Plot')
    ax.set_xlabel('Time of Day (24 HR)')
    ax.set_ylabel('Travel Time (min)')

    fig.savefig('scatter_plot.png')


def contour_plot(df: pandas.DataFrame):
    fig, ax = plt.subplots()
    hrs = mdates.HourLocator()
    hrs_fmt = mdates.DateFormatter('%HH')

    """
    complete dates format and update the y axis
    """

    x = mdates.datestr2num(df.index.values)
    y = df.columns.values
    Z = df.T.values

    ax.contourf(x, y, Z)
    ax.xaxis.set_major_locator(hrs)
    ax.xaxis.set_major_formatter(hrs_fmt)

    ax.yaxis.set_major_formatter(mdates.DateFormatter('%d'))

    ax.set_title('Travel Time Contour February 2023')
    ax.set_xlabel('Time (24 HR)')
    ax.set_ylabel('Day')
    plt.xticks(rotation=90)

    fig.savefig('contour_plot.png')


def bar_chart(df: pandas.DataFrame):
    sample_date = '02/02/2023'
    x_data = ['<40', '40-50', '50-60', '60-70']
    y_data = df['02/02/2023'].value_counts(bins=[30, 40, 50, 60, 70])

    fig, ax = plt.subplots()
    ax.bar(x_data, y_data)

    # add labels
    ax.set_title(f'Count of 5 Time Periods - {sample_date}')
    ax.set_xlabel('Categories - Minutes of Travel Time')
    ax.set_ylabel('Count')

    fig.savefig('bar_chart.png')


def line_plot(df: pandas.DataFrame):
    sample_date = '02/02/2023'
    x_data = pandas.to_datetime(df.index)
    y_data = df[sample_date]

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(x_data, y_data)

    # add labels
    ax.set_title(f'Everett to Seattle Travel Time - {sample_date}')
    ax.set_xlabel('Time')
    ax.set_ylabel('Travel Time (min)')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:00'))

    fig.savefig('line_plot.png')


if __name__ == '__main__':
    main()
