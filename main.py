from datetime import datetime
import dataframes as dfs
import downloader as dl
import plots as plts
import predictions as predicts
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
import pandas as pd
import numpy as np
from tkinter import *
import sys
from pandastable import Table
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)


def plot(df):
    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.plot(df['Adj Close'])

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

def print_dataframe(email):
    # Dataframe
    name = email.get()
    if not name:
        name = 'GOOG'
    # Setting the end date to today
    end = datetime.now()
    # Start date set to 1 year back
    start = datetime(end.year - 1, end.month, end.day)
    df = dl.single_df(name, start, end)
    pt = Table(frame, dataframe=df)
    pt.show()
    plot(df)

# root window
root = tk.Tk()
root.geometry("1000x800")
root.resizable(True, True)
root.title('Stcok Prediction')
# store email address and password
email = tk.StringVar()
password = tk.StringVar()
# the figure that will contain the plot
fig = Figure(figsize=(15, 15), dpi=100)


label = ttk.Label(text="Please select Company:")
label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_month = tk.StringVar()
companies = ttk.Combobox(root, textvariable=selected_month)

# get first 3 letters of every month name
companies['values'] = ['Choose', 'GOOG', 'AMZN', 'CDR.WA']

# prevent typing a value
companies['state'] = 'readonly'

# place the widget
companies.pack(fill=tk.X, padx=5, pady=5)


def print_dataframe(event):
    # Dataframe
    name = selected_month.get()
    if not name:
        name = 'GOOG'
    # Setting the end date to today
    end = datetime.now()
    # Start date set to 1 year back
    start = datetime(end.year - 1, end.month, end.day)
    df = dl.single_df(name, start, end)
    pt = Table(frame, dataframe=df)
    pt.show()
    plot(df)



# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


# email
email_label = ttk.Label(signin, text="Company:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

frame = tk.Frame(root)
frame.pack(fill='both', expand=True)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
# placing the canvas on the Tkinter window
canvas.get_tk_widget().pack()
# print_dataframe(frame, name)
companies.bind('<<ComboboxSelected>>', print_dataframe)
login_button = ttk.Button(signin, text="Search", command=lambda:print_dataframe(email))
login_button.pack(fill='x', expand=True, pady=10)


root.mainloop()