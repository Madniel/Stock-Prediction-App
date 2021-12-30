from datetime import datetime
from tkinter.messagebox import showinfo
import downloader as dl
import plots as plts
import tkinter as tk
from tkinter import ttk
from calendar import month_name
import pandas as pd
from pandastable import Table
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import Calendar, DateEntry


def print_dataframe(company):
    name = company.get()
    if not name:
        msg = 'Please choose company'
        showinfo(
            title='Error',
            message=msg
        )
        return 0

    df = dl.single_df(name, start, end)
    pt = Table(frame, dataframe=df)
    pt.show()
    plts.plotting(fig, df, canvas, root)

def combo_dataframe(event):
    name = selected_comp.get()
    symbol = company_list[name]
    df = dl.single_df(symbol, start, end)
    pt = Table(frame, dataframe=df)
    pt.show()
    plts.plotting(fig, df, canvas, root)

def example1():
    def print_sel():
        temp = cal.selection_get()
        if temp >= end.date():
            msg = 'Start date cannot be the same day or later than end date'
            showinfo(
                title='Error',
                message=msg
            )
        else:
            global start
            start = cal.selection_get()

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=datetime.now().year - 1, month=datetime.now().month, day=datetime.now().day)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

def example2():
    def print_sel():
        temp = cal.selection_get()
        if temp <= start.date():
            msg = 'Start date cannot be the same day or earlier than end date'
            showinfo(
                title='Error',
                message=msg
            )
        else:
         global end
         end = cal.selection_get()

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

comp_name = tk.StringVar()
password = tk.StringVar()


# Setting default the end date to today
end = datetime.now()
# Start default date set to 1 year back
start = datetime(end.year - 1, end.month, end.day)

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

# Sign in frame
shortcut = ttk.Frame(root)
shortcut.pack(padx=10, pady=10, fill='x', expand=True)


# email
search_label = ttk.Label(shortcut, text="Write symbol of Company:")
search_label.pack(fill='x', expand=True)

search_entry = ttk.Entry(shortcut, textvariable=comp_name)
search_entry.pack(fill='x', expand=True)
search_entry.focus()

ttk.Button(root, text='From', command=example1).pack(padx=10, pady=10)
ttk.Button(root, text='To', command=example2).pack(padx=10, pady=10)

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