def show_df(list, stock, name):
    id = list.index(name)
    return stock[id]

def show_ma_one(df):
    ma_day = [10, 20, 50]
    for ma in ma_day:
        column_name = "MA for %s days" % (str(ma))
        df[column_name] = df['Adj Close'].rolling(window=ma, center=False).mean()
    return df

def daily_return(df):
    df['Daily Return'] = df['Adj Close'].pct_change()
    return df
