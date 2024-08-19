import tkinter as tk
from tkinter import ttk
import pandas as pd

f = pd.read_csv('formate-scurt.csv')

# Function to enable or disable entry widget
def toggle_entry(entry, var):
    if var.get():
        entry.config(state='normal')
    else:
        entry.config(state='disabled')

# Main function to create the form
def create_form():
    elements = f.aparat[:20].values

    root = tk.Tk()
    root.title("Dynamic Form with Checkboxes")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    for idx, element in enumerate(elements):
        var = tk.BooleanVar()
        checkbox = ttk.Checkbutton(frame, text=element, variable=var)
        checkbox.grid(row=idx, column=0, sticky=tk.W)

        entry = ttk.Entry(frame, state='disabled')
        entry.grid(row=idx, column=1, sticky=(tk.W, tk.E))

        # Use lambda to pass the current entry and var to the toggle function
        var.trace_add('write', lambda *args, e=entry, v=var: toggle_entry(e, v))

    root.mainloop()

create_form()
