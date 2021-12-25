import numpy as np
import matplotlib.pyplot as plt

def stock_monte_carlo(df, start_price, days, name):
    dt = 1 / days
    mu = df[name].mean()
    sigma = df[name].std()

    price = np.zeros(days)
    price[0] = start_price

    shock = np.zeros(days)
    drift = np.zeros(days)

    for x in range(1, days):
        shock[x] = np.random.normal(loc=mu * dt, scale=sigma * np.sqrt(dt))

        drift[x] = mu * dt

        price[x] = price[x - 1] + (price[x - 1] * (drift[x] + shock[x]))

    return price

def prediction(df, days, name):
    start_price = df[0][name]  # Taken from above

    for run in range(100):
        plt.plot(stock_monte_carlo(df, start_price, days, name))

    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.title('Monte Carlo Analysis for Google')

    return plt

def final_price(df, days, name):
    mu = df[name].mean()
    sigma = df[name].std()
    start_price = df[0][name]
    runs = 10000
    simulations = np.zeros(runs)
    for run in range(runs):
        simulations[run] = stock_monte_carlo(start_price, days, mu, sigma)[days - 1]

    q = np.percentile(simulations, 1)

    plt.hist(simulations, bins=200)
    plt.figtext(0.6, 0.8, s="Start price: $%.2f" % start_price)
    plt.figtext(0.6, 0.7, "Mean final price: $%.2f" % simulations.mean())
    plt.figtext(0.6, 0.6, "VaR(0.99): $%.2f" % (start_price - q,))
    plt.figtext(0.15, 0.6, "q(0.99): $%.2f" % q)
    plt.axvline(x=q, linewidth=4, color='r')
    plt.title(u"Final price distribution for Google Stock after %s days" % days, weight='bold')

    return plt