import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

def stock_monte_carlo(df, start_price, days):
    rets = df['Adj Close'].pct_change().dropna()
    dt = 1 / days

    mu = rets.mean()
    sigma = rets.std()

    price = np.zeros(days)
    price[0] = start_price

    shock = np.zeros(days)
    drift = np.zeros(days)

    for x in range(1, days):
        shock[x] = np.random.normal(loc=mu * dt, scale=sigma * np.sqrt(dt))

        drift[x] = mu * dt

        price[x] = price[x - 1] + (price[x - 1] * (drift[x] + shock[x]))

    return price

def prediction(fig,canvas,root,df):
    days = 365
    start_price = df.iloc[0]['Open']
    fig.clf()
    with plt.rc_context({'xtick.color': 'white', 'ytick.color': 'white'}):
        plot = fig.add_subplot(111)
        for run in range(100):
            plot.plot(stock_monte_carlo(df, start_price, days))

        # plot.xlabel('Days')
        # plot.ylabel('Price')
        # plot.title('Monte Carlo Analysis for Google')
        plot.grid()
        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()


def final_price(fig,canvas,root,df):
    days = 365
    rets = df['Adj Close'].pct_change().dropna()
    mu = rets.mean()
    sigma = rets.std()
    fig.clf()
    start_price = df.iloc[0]['Open']
    runs = 3000
    simulations = np.zeros(runs)
    for run in range(runs):
        simulations[run] = stock_monte_carlo(df, start_price, days)[days - 1]
    with plt.rc_context({'xtick.color': 'white', 'ytick.color': 'white'}):
        q = np.percentile(simulations, 1)
        plot = fig.add_subplot(111)
        plot.hist(simulations, bins=200)
        plt.figtext(0.6, 0.8, s="Start price: $%.2f" % start_price)
        plt.figtext(0.6, 0.7, "Mean final price: $%.2f" % simulations.mean())
        plt.figtext(0.6, 0.6, "VaR(0.99): $%.2f" % (start_price - q,))
        plt.figtext(0.15, 0.6, "q(0.99): $%.2f" % q)
        plt.axvline(x=q, linewidth=4, color='r')
        plt.title(u"Final price distribution for Google Stock after %s days" % days, weight='bold')
        plot.grid()
        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()
