from datetime import datetime
from tkinter.messagebox import showinfo
import downloader as dl
import dataframes as dfs
import predictions as predict
import tkinter as tk
from tkinter import ttk
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Base Information
class MonteCarlo(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self._frame = tk.Frame
        # Setting default the end date to today
        self.end = datetime.now().date()
        # Start default date set to 1 year back
        self.start = datetime(self.end.year - 1, self.end.month, self.end.day).date()
        self.file = pd.read_csv('companies.csv').set_index('Name')
        self.company_list = self.file.to_dict()['Symbol']
        self.list_comp =sorted(list(self.company_list.keys()))

        # Create the figure that will contain the plot
        self.fig = Figure(figsize=(15, 15), dpi=100)
        self.fig.patch.set_facecolor('#31363B')

        self.label = tk.Label(self, text="Choose Company:")
        self.label.pack(fill=tk.X, padx=11, pady=(30, 10))

        # create a combobox
        self.selected_comp = tk.StringVar()
        self.companies = ttk.Combobox(self, textvariable=self.selected_comp)
        self.companies['values'] = self.list_comp

        # prevent typing a value
        self.companies['state'] = 'readonly'

        # place the widget
        self.companies.pack(fill=tk.X, padx=11, pady=0)

        self.shortcut = ttk.Frame(self)
        self.shortcut.pack(padx=10, pady=10, fill='x', expand=True)

        # Symbol
        self.search_label = ttk.Label(self.shortcut, text="Write symbol of Company:")
        self.search_label.pack(fill='x', expand=True)
        self.comp_name = tk.StringVar()
        self.search_entry = ttk.Entry(self.shortcut, textvariable=self.comp_name)
        self.search_entry.pack(fill='x', expand=True)
        self.search_entry.focus()

        self.top = tk.Frame(self)
        self.top.pack(side=tk.TOP)

        self.bottom = tk.Frame(self)
        self.bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # exit button
        self.exit_button = ttk.Button(self, text='Exit', command=lambda: master.quit())
        self.exit_button.pack(in_=self.bottom, ipadx=5, ipady=5, expand=True)

        self.frame = tk.Frame(self, bg='black')
        self.frame.pack(in_=self.bottom,fill='both', expand=True)

        # Create Canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        # Placing the canvas on the Tkinter window
        self.canvas.get_tk_widget().pack(in_=self.bottom)


        self.companies.bind('<<ComboboxSelected>>', self.combo)
        self.login_button = ttk.Button(self.shortcut, text="Search", command=lambda:self.entry_fun())
        self.login_button.pack(fill='x', expand=True, pady=10)

    def print_data(self):
        name = list(self.company_list.keys())[list(self.company_list.values()).index(self.symbol)]
        df = dl.dl_df(self.symbol, self.start, self.end)
        df = dfs.daily_return(df)
        df = dfs.show_ma_one(df)
        predict.prediction(self.fig, self.canvas, self, df, name)

    def entry_fun(self):
        self.symbol = self.comp_name.get().upper()
        if not self.symbol:
            msg = 'Please choose company'
            showinfo(title='Error', message=msg)
            return 0
        self.print_data()


    def combo(self, event):
        name = self.selected_comp.get()
        self.symbol = self.company_list[name]
        self.print_data()
        
