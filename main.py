from datetime import datetime
from tkinter.messagebox import showinfo

import dataframes as dfs
import downloader as dl
import plots as plts
import predictions as predicts
import tkinter as tk
from tkinter import ttk
from calendar import month_name
import pandas as pd
import numpy as np
from tkinter import *
import sys
from pandastable import Table
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

def _clear():
    for item in canvas.get_tk_widget().find_all():
       canvas.get_tk_widget().delete(item)

def plot(df):
    fig.clf()
    with plt.rc_context({ 'xtick.color': 'white', 'ytick.color': 'white'}):
            # adding the subplot
            plot1 = fig.add_subplot(111)

            # plotting the graph
            plot1.plot(df['Date'],df['Adj Close'])
            # creating the Matplotlib toolbar
            toolbar = NavigationToolbar2Tk(canvas, root)
            toolbar.update()

            # placing the toolbar on the Tkinter window
            canvas.get_tk_widget().pack()

def print_dataframe(company):
    name = company.get()
    if not name:
        msg = 'Please choose company'
        showinfo(
            title='Error',
            message=msg
        )
        return 0
    # Setting the end date to today
    end = datetime.now()
    # Start date set to 1 year back
    start = datetime(end.year - 1, end.month, end.day)
    df = dl.single_df(name, start, end)
    pt = Table(frame, dataframe=df)
    pt.show()
    plot(df)

def combo_dataframe(event):
    name = selected_comp.get()
    end = datetime.now()
    start = datetime(end.year - 1, end.month, end.day)
    symbol = company_list[name]
    df = dl.single_df(symbol, start, end)
    pt = Table(frame, dataframe=df)
    pt.show()
    plot(df)

# root window
root = tk.Tk()
root.geometry("1530x930+200+50")
root.resizable(True, True)
root.title('Stock Prediction')


style = ttk.Style(root)
root.tk.call('source', 'breeze-dark.tcl')
style.theme_use('breeze-dark')

comp_name = tk.StringVar()
password = tk.StringVar()

# the figure that will contain the plot
fig = Figure(figsize=(15, 15), dpi=100)
fig.patch.set_facecolor('#31363B')
label = ttk.Label(text="Choose Company:")
label.pack(fill=tk.X, padx=11, pady=10)

file = pd.read_csv('companies.csv')
file = file.set_index('Name')
company_list = file.to_dict()
company_list = company_list['Symbol']
list_comp = list(company_list.keys())
list_comp_alph = sorted(list_comp)

# create a combobox
selected_comp = tk.StringVar()
companies = ttk.Combobox(root, textvariable=selected_comp)
companies['values'] = list_comp_alph

# prevent typing a value
companies['state'] = 'readonly'

# place the widget
companies.pack(fill=tk.X, padx=11, pady=10)

# Sign in frame
shortcut = ttk.Frame(root)
shortcut.pack(padx=10, pady=10, fill='x', expand=True)


# email
search_label = ttk.Label(shortcut, text="Write symbol of Company:")
search_label.pack(fill='x', expand=True)

search_entry = ttk.Entry(shortcut, textvariable=comp_name)
search_entry.pack(fill='x', expand=True)
search_entry.focus()

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

frame = tk.Frame(root, bg='black')
frame.pack(fill='both', expand=True)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
# placing the canvas on the Tkinter window
canvas.get_tk_widget().pack()
companies.bind('<<ComboboxSelected>>', combo_dataframe)
login_button = ttk.Button(shortcut, text="Search", command=lambda:print_dataframe(comp_name))
login_button.pack(fill='x', expand=True, pady=10)

root.mainloop()