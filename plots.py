import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

def plotting(fig, df, canvas, root, key, dictionary):
    fig.clf()
    with plt.rc_context({ 'xtick.color': 'white', 'ytick.color': 'white'}):
            # adding the subplot
            plot = fig.add_subplot(111)
            # plotting the graph
            if dictionary[key+1] != 'Moving Average':
                plot.plot(df['Date'],df[dictionary[key+1]],linestyle='--',marker='o')
            else:
                plot.plot(df['Date'],df['Adj Close'],label='Adj Close')
                plot.plot(df['Date'], df['MA for 10 days'],label='MA for 10 days')
                plot.plot(df['Date'], df['MA for 20 days'],label='MA for 20 days')
                plot.plot(df['Date'], df['MA for 50 days'],label='MA for 50 days')
                plot.legend()
            plot.grid()
            # creating the Matplotlib toolbar
            toolbar = NavigationToolbar2Tk(canvas, root)
            toolbar.update()
            # placing the toolbar on the Tkinter window
            canvas.get_tk_widget().pack()

def show_adj_sl(company):
    plot = company['Adj Close'].plot(legend=True, figsize=(12, 5))
    return plot

def show_adj_ml(name,list, stock):
    id = list.index(name)
    plot = show_adj_ml(stock[id])
    return plot

def show_volume(company):
    plot = company['Volume'].plot(legend=True, figsize=(12, 5))
    return plot

def show_volume_ml(name,list, stock):
    id = list.index(name)
    plot = show_volume(stock[id])
    return plot

def show_ma(df):
    plot = df[['Adj Close','MA for 10 days','MA for 20 days','MA for 50 days']].plot(subplots=False,figsize=(12,5))
    return plot

def daily_return(df):
    plot1 = df['Daily Return'].plot(figsize=(14, 5), legend=True, linestyle='--', marker='o')
    plot2 = sns.distplot(df['Daily Return'].dropna(),bins=100,color='red')
    return plot1, plot2

def daily_return_two(name1, name2, stock):
    plot = sns.jointplot(name1,name2,stock,kind='scatter',color='green')
    return plot

def daily_return_all(fig, datas, canvas, root):
    fig.clf()
    plot = fig.add_subplot(111)
    with plt.rc_context({'xtick.color': 'white', 'ytick.color': 'white'}):
        pd.plotting.scatter_matrix(datas,ax=plot, figsize=(10,10), marker = 'o', hist_kwds = {'bins': 10}, s = 60, alpha = 0.8)
        # plot.plot(g)
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()


def risk(fig, df, canvas, root):
    fig.clf()
    with plt.rc_context({'xtick.color': 'white', 'ytick.color': 'white'}):
        df = df.dropna()
        plot = fig.add_subplot(111)
        plot.scatter(df.mean(), df.std(), s=25)
        for label, x, y in zip(df.columns, df.mean(), df.std()):
            plot.annotate(
                label,
                xy=(x, y), xytext=(-120, 20),
                textcoords='offset points', ha='right', va='bottom',
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-0.5'))
        plot.grid()
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()


def bootstrap(df ,list, name):
    id = list.index(name)
    df = df[id]
    plot = sns.distplot(df['Daily Return'].dropna(),bins=100,color='purple')
    return plot