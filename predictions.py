import math

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


def prediction(fig, canvas, root, df, name, number):
    days = number
    start_price = df.iloc[0]['Open']
    fig.clf()
    with plt.rc_context({'xtick.color': 'white', 'ytick.color': 'white'}):
        plot = fig.add_subplot(111)
        for run in range(100):
            plot.plot(stock_monte_carlo(df, start_price, days))

        plot.set_xlabel('Days').set_color('white')
        plot.set_ylabel('Price').set_color('white')
        plot.set_title(f'Monte Carlo Analysis for {name} for {number} days').set_color('white')
        plot.grid()
        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()


def final_price(fig, canvas, root, df, name, number):
    days = number
    fig.clf()
    start_price = df.iloc[0]['Open']
    runs = 3000
    simulations = np.zeros(runs)
    for run in range(runs):
        simulations[run] = stock_monte_carlo(df, start_price, days)[days - 1]
    with plt.rc_context({'xtick.color': 'white', 'ytick.color': 'white'}):
        plot = fig.add_subplot(111)
        q = np.percentile(simulations, 1)
        plot.hist(simulations, bins=200)
        x = plot.get_xlim()[0] + (plot.get_xlim()[-1]-plot.get_xlim()[0])*0.8
        y = plot.get_ylim()[0] + (plot.get_ylim()[-1]-plot.get_ylim()[0])*0.8
        plot.text(x, y-5, s="Start price: $%.2f" % start_price)
        plot.text(x, y-10, s="Mean final price: $%.2f" % simulations.mean())
        plot.text(x, y-15, s="VaR(0.99): $%.2f" % (start_price - q,))
        plot.text(x, y-20, s="q(0.99): $%.2f" % q)
        plot.axvline(x=q, ymin=0, linewidth=4, color='r')
        plot.set_title(f"Final price distribution for {name} Stock after {number} days", weight='bold').set_color('white')
        plot.grid()
        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()
