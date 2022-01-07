from pandas_datareader.data import DataReader

def dl_df(name, start, end):
    dataframe = DataReader(name, 'yahoo', start, end)
    dataframe['Date'] = dataframe.index
    cols = dataframe.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    dataframe = dataframe[cols]
    dataframe.index = [i for i in range(len(dataframe.index))]
    dataframe['Date'] = [dataframe['Date'][i].date() for i in range(len(dataframe.index))]
    dataframe = dataframe.sort_values(by='Date', ascending=False)
    return dataframe

