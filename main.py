from datetime import datetime
from tkinter.messagebox import showinfo
import downloader as dl
import plots as plts
import tkinter as tk
from tkinter import ttk
import pandas as pd
from pandastable import Table
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import Calendar


def print_data(name):
    df = dl.single_df(name, start, end)
    pt = Table(frame, dataframe=df)
    pt.show()
    plts.plotting(fig, df, canvas, root)

def entry_fun(company):
    name = company.get()
    if not name:
        msg = 'Please choose company'
        showinfo(title='Error', message=msg)
        return 0
    print_data(name)

def combo(event):
    name = selected_comp.get()
    symbol = company_list[name]
    print_data(symbol)

def startdate():
    def print_sel():
        temp = cal.selection_get()
        if temp >= end:
            msg = 'Start date cannot be the same day or later than end date'
            showinfo(title='Error', message=msg)
        else:
            global start
            start = cal.selection_get()
            top.destroy()
            first.configure(text=f'From {start}')

    top = tk.Toplevel(root)
    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=datetime.now().year - 1, month=datetime.now().month, day=datetime.now().day)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

def enddate():
    def print_sel():
        temp = cal.selection_get()
        if temp <= start:
            msg = 'Start date cannot be the same day or earlier than end date'
            showinfo(title='Error', message=msg)
        else:
         global end
         end = cal.selection_get()
         top.destroy()
         last.configure(text=f'From {end}')

    top = tk.Toplevel(root)
    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()


# Create root window
root = tk.Tk()
root.geometry("1530x930+200+50")
root.resizable(True, True)
root.title('Stock Prediction')

# Choose Style
style = ttk.Style(root)
root.tk.call('source', 'breeze-dark.tcl')
style.theme_use('breeze-dark')

# Setting default the end date to today
end = datetime.now().date()
# Start default date set to 1 year back
start = datetime(end.year - 1, end.month, end.day).date()

# Create the figure that will contain the plot
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

shortcut = ttk.Frame(root)
shortcut.pack(padx=10, pady=10, fill='x', expand=True)

# Symbol
search_label = ttk.Label(shortcut, text="Write symbol of Company:")
search_label.pack(fill='x', expand=True)
comp_name = tk.StringVar()
search_entry = ttk.Entry(shortcut, textvariable=comp_name)
search_entry.pack(fill='x', expand=True)
search_entry.focus()


top = tk.Frame(root)
top.pack(side=tk.TOP)

bottom = tk.Frame(root)
bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Set range date
first = tk.Button(root, text=f'From {start}', command=startdate)
first.pack(in_=top, side=tk.LEFT, padx=20, pady=10)

last=tk.Button(root, text=f'To {end}', command=enddate)
last.pack(in_=top, side=tk.RIGHT, padx=20, pady=10)

# exit button
exit_button = ttk.Button(root, text='Exit', command=lambda: root.quit())
exit_button.pack(in_=bottom, ipadx=5, ipady=5, expand=True)

frame = tk.Frame(root, bg='black')
frame.pack(in_=bottom,fill='both', expand=True)

# Create Canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

# Placing the canvas on the Tkinter window
canvas.get_tk_widget().pack(in_=bottom)
companies.bind('<<ComboboxSelected>>', combo)
login_button = ttk.Button(shortcut, text="Search", command=lambda:entry_fun(comp_name))
login_button.pack(fill='x', expand=True, pady=10)

root.mainloop()