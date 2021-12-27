from pandas_datareader.data import DataReader

def single_df(name, start, end):
    dataframe = DataReader(name, 'yahoo', start, end)
    dataframe['Date'] = dataframe.index
    cols = dataframe.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    dataframe = dataframe[cols]
    dataframe.index = [i for i in range(len(dataframe.index))]
    for i in range(len(dataframe.index)):
        dataframe['Date'][i] = dataframe['Date'][i].date()
    return dataframe


def multi_df(companies, start, end):
    stock = []
    for company in companies:
        data = single_df(company, start, end)
        stock.append(data)
    return stock
