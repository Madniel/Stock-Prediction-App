import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

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

def daily_return_all(fig, datas, canvas, root):
    fig.clf()
    plot = fig.add_subplot(111)
    with plt.rc_context({'xtick.color': 'white', 'ytick.color': 'white'}):
        sm = pd.plotting.scatter_matrix(datas,ax=plot, figsize=(10,10), marker = 'o', hist_kwds = {'bins': 10}, s = 60, alpha = 0.8)
        for subaxis in sm:
            for ax in subaxis:
                ax.xaxis.label.set_color('white')  # setting up X-axis label color to yellow
                ax.yaxis.label.set_color('white')
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
        plot.set_xlabel('Expected return').set_color('white')
        plot.set_ylabel('Risk').set_color('white')
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()


