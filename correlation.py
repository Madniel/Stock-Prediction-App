from datetime import datetime
from tkinter.messagebox import showinfo
import downloader as dl
import dataframes as dfs
import predictions as predict
import plots as plts
import tkinter as tk
from tkinter import ttk
import pandas as pd
from pandastable import Table
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
from typing import Callable
import numpy as np
import seaborn as sns
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Base Information
class Correlation(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self._frame = tk.Frame
        # Setting default the end date to today
        self.end = datetime.now().date()
        # Start default date set to 1 year back
        self.start = datetime(self.end.year - 1, self.end.month, self.end.day).date()

        # Create the figure that will contain the plot
        self.fig = Figure(figsize=(15, 15), dpi=100)
        self.fig.patch.set_facecolor('#31363B')

        self.shortcut = ttk.Frame(self)
        self.shortcut.pack(padx=10, pady=10, fill='x', expand=True)

        # Symbol
        self.search_label = ttk.Label(self.shortcut, text="Write symbols of Companies:")
        self.search_label.pack(fill='x', expand=True)
        self.symbol = []
        self.search_entry =[]

        for i in range(4):
            name = tk.StringVar()
            self.search_entry.append(ttk.Entry(self.shortcut, textvariable=name))
            self.symbol.append(name)
            self.search_entry[i].pack(fill='x', expand=True)
            self.search_entry[i].focus()

        self.top = tk.Frame(self)
        self.top.pack(side=tk.TOP)

        self.bottom = tk.Frame(self)
        self.bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # exit button
        self.exit_button = ttk.Button(self, text='Exit', command=lambda: master.quit())
        self.exit_button.pack(in_=self.bottom, ipadx=5, ipady=5, expand=True)

        self.frame = tk.Frame(self, bg='black')
        self.frame.pack(in_=self.bottom, fill='both', expand=True)

        # Create Canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        # Placing the canvas on the Tkinter window
        self.canvas.get_tk_widget().pack(in_=self.bottom)

        self.login_button = ttk.Button(self.shortcut, text="Search", command=lambda: self.entry_fun())
        self.login_button.pack(fill='x', expand=True, pady=10)

    def print_data(self):
        datas = []
        for i in range(len(self.symbol)):
            name = str(self.symbol[i].get())
            if self.symbol[i].get():
                df = dl.single_df(self.symbol[i].get(), self.start, self.end)
                df = df[['Adj Close']]
                df = df.rename(columns={'Adj Close': name})
                if not i:
                    datas = df
                else:
                    datas[name] = df[name]
        plts.daily_return_all(self.fig, datas, self.canvas, self)

    def entry_fun(self):
        if len(self.symbol)<1:
            msg = 'Please at least one company'
            showinfo(title='Error', message=msg)
            return 0
        self.print_data()


