from tkinter import *
import tkinter as tk
from tkinter import ttk
from base import Base
from montecarlo import MonteCarlo
from finalprice import FinalPrice
from correlation import Correlation

# Root class to create the interface and define the controller function to switch frames
class RootApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(NoteBook)

    # Controller function
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

# sub-root to contain the Notebook frame and a controller function to switch the tabs within the notebook
class NoteBook(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.notebook = ttk.Notebook()
        self.base = Base(self.notebook)
        self.carlo = MonteCarlo(self.notebook)
        self.finalprice = FinalPrice(self.notebook)
        self.correlation = Correlation(self.notebook)
        self.notebook.add(self.base, text="Basic Information")
        self.notebook.add(self.carlo, text="Prediction")
        self.notebook.add(self.finalprice, text="Final Price Distribution")
        self.notebook.add(self.correlation, text="Correlation")
        self.notebook.pack()

    # controller function
    def switch_base(self, frame_class):
        new_frame = frame_class(self.notebook)
        self.base.destroy()
        self.base = new_frame

# Notebook - Tab 2
class Tab2(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, text="this is a test - two")
        self.label.pack()

if __name__ == "__main__":
    root = RootApp()

    # Style
    style = ttk.Style(root)
    root.tk.call('source', 'breeze-dark.tcl')
    style.theme_use('breeze-dark')

    root.geometry("1530x930+200+50")
    root.resizable(True, True)
    root.title('Stock Prediction')
    root.mainloop()
