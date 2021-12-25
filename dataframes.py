def show_df(list, stock, name):
    id = list.index(name)
    return stock[id]

def show_description(list, stock, name):
    df = show_df(list, stock, name)
    return df.describe()

def show_ma_one(ma_day,df):
    for ma in ma_day:
        column_name = "MA for %s days" % (str(ma))
        df[column_name] = df['Adj Close'].rolling(window=ma, center=False).mean()
    return df

def show_ma_ml(ma_day,list, stock, name):
    id = list.index(name)
    return show_ma_one(ma_day,stock[id])

def daily_return(list, stock, name, size=5):
    df = show_df(list, stock, name)
    df['Daily Return'] = df['Adj Close'].pct_change()
    return df, df['Daily Return'].tail(size)

def corr_dr(df, size=5):
    rets_df = df.pct_change()
    return rets_df.tail(size)

def quantile(df, name, value):
    return df[name].quantile(value)