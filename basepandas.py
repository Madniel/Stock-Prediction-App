from datetime import datetime
from tkinter.messagebox import showinfo
import downloader as dl
import dataframes as dfs
import plots as plts
import tkinter as tk
from tkinter import ttk
import pandas as pd
from pandastable import Table
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import Calendar

# Base Information
class BasePandas(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self._frame = tk.Frame
        # Setting default the end date to today
        self.end = datetime.now().date()
        # Start default date set to 1 year back
        self.start = datetime(self.end.year - 1, self.end.month, self.end.day).date()
        self.value_graph = 0
        self.symbol = ''
        self.file = pd.read_csv('companies.csv').set_index('Name')
        self.company_list = self.file.to_dict()['Symbol']
        self.list_comp =sorted(list(self.company_list.keys()))

        # Create the figure that will contain the plot
        self.fig = Figure(figsize=(15, 15), dpi=100)
        self.fig.patch.set_facecolor('#31363B')
        self.label = ttk.Label(self, text="Choose Company:")
        self.label.pack(fill=tk.X, padx=11, pady=(30, 0))

        # create a combobox
        self.selected_comp = tk.StringVar()
        self.companies = ttk.Combobox(self, textvariable=self.selected_comp)
        self.companies['values'] = self.list_comp

        # prevent typing a value
        self.companies['state'] = 'readonly'

        # place the widget
        self.companies.pack(fill=tk.X, padx=11, pady=0)

        self.shortcut = ttk.Frame(self)
        self.shortcut.pack(padx=10, pady=0, fill='x', expand=True)

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
        self.frame = tk.Frame(self, bg='black')
        self.frame.pack(in_=self.bottom, fill='both', expand=True)
        # Set range date
        self.first = tk.Button(self, text=f'From {self.start}', command=self.startdate)
        self.first.pack(in_=self.top, side=tk.LEFT, padx=20, pady=0)

        self.last=tk.Button(self, text=f'To {self.end}', command=self.enddate)
        self.last.pack(in_=self.top, side=tk.RIGHT, padx=20, pady=0)

        # exit button
        self.exit_button = ttk.Button(self, text='Exit', command=lambda: master.quit())
        self.exit_button.pack(in_=self.bottom, ipadx=5, ipady=5, expand=True)
        self.companies.bind('<<ComboboxSelected>>', self.combo)
        self.login_button = ttk.Button(self.shortcut, text="Search", command=lambda: self.entry_fun())
        self.login_button.pack(fill='x', expand=True, pady=0)



    def print_data(self):
        df = dl.dl_df(self.symbol, self.start, self.end)
        df = dfs.daily_return(df)
        df = dfs.show_ma_one(df)
        pt = Table(self.frame, dataframe=df)
        pt.show()
        # plts.plotting(self.fig, df, self.canvas, self.frame, self.value_graph,self.graph_options)

    def entry_fun(self):
        self.symbol = self.comp_name.get()
        if not self.symbol:
            msg = 'Please choose company'
            showinfo(title='Error', message=msg)
            return 0
        self.print_data()


    def combo(self, event):
        name = self.selected_comp.get()
        self.symbol = self.company_list[name]
        self.print_data()

    def startdate(self):
        def print_sel():
            temp = cal.selection_get()
            if temp >= self.end:
                msg = 'Start date cannot be the same day or later than end date'
                showinfo(title='Error', message=msg)
            else:
                self.start = cal.selection_get()
                top.destroy()
                self.first.configure(text=f'From {self.start}')

        top = tk.Toplevel(self.frame)
        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=datetime.now().year - 1, month=datetime.now().month, day=datetime.now().day)
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=print_sel).pack()

    def enddate(self):
        def print_sel():
            temp = cal.selection_get()
            if temp <= self.start:
                msg = 'Start date cannot be the same day or earlier than end date'
                showinfo(title='Error', message=msg)
            else:
             self.end = cal.selection_get()
             top.destroy()
             self.last.configure(text=f'From {self.end}')

        top = tk.Toplevel(self.frame)
        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=print_sel).pack()


