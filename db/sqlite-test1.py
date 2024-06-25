import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from datetime import datetime
from tkcalendar import DateEntry

# Function to create SQLite database and table
def create_database():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS results (
                    id INTEGER PRIMARY KEY,
                    nume_proba TEXT,
                    seria TEXT,
                    analiza TEXT,
                    solicitant TEXT,
                    aparat TEXT,
                    data_intrare DATE,
                    data_eliberare DATE,
                    utilizator TEXT,
                    rezultat TEXT
                 )''')
    conn.commit()
    conn.close()

# Function to insert data into SQLite database
def insert_data(nume_proba, seria, analiza, solicitant, aparat, data_intrare, data_eliberare, utilizator, rezultat):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''INSERT INTO results (nume_proba, seria, analiza, solicitant, aparat, data_intrare, data_eliberare, utilizator, rezultat)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (nume_proba, seria, analiza, solicitant, aparat, data_intrare, data_eliberare, utilizator, rezultat))
    conn.commit()
    conn.close()

# Function to export SQLite data to Excel
def export_to_excel():
    conn = sqlite3.connect('data.db')
    query = "SELECT * FROM results"
    df = pd.read_sql_query(query, conn)
    conn.close()

    filename = f"results_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"
    df.to_excel(filename, index=False)
    messagebox.showinfo("Export Complete", f"Data exported to {filename}")

# Function to handle form submission
def submit_form():
    # Get values from form fields
    nume_proba = entry_nume_proba.get()
    seria = entry_seria.get()
    analiza = entry_analiza.get()
    solicitant = entry_solicitant.get()
    aparat = entry_aparat.get()
    data_intrare = cal_data_intrare.get_date().strftime('%Y-%m-%d')
    data_eliberare = cal_data_eliberare.get_date().strftime('%Y-%m-%d')
    utilizator = entry_utilizator.get()
    rezultat = entry_rezultat.get('1.0', tk.END).strip()  # Get text from Text widget

    # Insert into database
    insert_data(nume_proba, seria, analiza, solicitant, aparat, data_intrare, data_eliberare, utilizator, rezultat)

    # Clear form fields after submission
    entry_nume_proba.delete(0, tk.END)
    entry_seria.delete(0, tk.END)
    entry_analiza.delete(0, tk.END)
    entry_solicitant.delete(0, tk.END)
    entry_aparat.delete(0, tk.END)
    cal_data_intrare.set_date(datetime.now())
    cal_data_eliberare.set_date(datetime.now())
    entry_utilizator.delete(0, tk.END)
    entry_rezultat.delete('1.0', tk.END)

# Create SQLite database if it doesn't exist
create_database()

# Create tkinter GUI
root = tk.Tk()
root.title("Data Entry Form")

# Labels and Entry widgets for form
label_nume_proba = ttk.Label(root, text="Nume proba:")
label_nume_proba.grid(row=0, column=0, padx=10, pady=5)
entry_nume_proba = ttk.Entry(root, width=40)
entry_nume_proba.grid(row=0, column=1, padx=10, pady=5)

label_seria = ttk.Label(root, text="Seria:")
label_seria.grid(row=1, column=0, padx=10, pady=5)
entry_seria = ttk.Entry(root, width=40)
entry_seria.grid(row=1, column=1, padx=10, pady=5)

label_analiza = ttk.Label(root, text="Analiza:")
label_analiza.grid(row=2, column=0, padx=10, pady=5)
entry_analiza = ttk.Entry(root, width=40)
entry_analiza.grid(row=2, column=1, padx=10, pady=5)

label_solicitant = ttk.Label(root, text="Solicitant:")
label_solicitant.grid(row=3, column=0, padx=10, pady=5)
entry_solicitant = ttk.Entry(root, width=40)
entry_solicitant.grid(row=3, column=1, padx=10, pady=5)

label_aparat = ttk.Label(root, text="Aparat:")
label_aparat.grid(row=4, column=0, padx=10, pady=5)
entry_aparat = ttk.Entry(root, width=40)
entry_aparat.grid(row=4, column=1, padx=10, pady=5)

label_data_intrare = ttk.Label(root, text="Data intrare:")
label_data_intrare.grid(row=5, column=0, padx=10, pady=5)
cal_data_intrare = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
cal_data_intrare.grid(row=5, column=1, padx=10, pady=5)
cal_data_intrare.set_date(datetime.now())

label_data_eliberare = ttk.Label(root, text="Data eliberare:")
label_data_eliberare.grid(row=6, column=0, padx=10, pady=5)
cal_data_eliberare = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
cal_data_eliberare.grid(row=6, column=1, padx=10, pady=5)
cal_data_eliberare.set_date(datetime.now())

label_utilizator = ttk.Label(root, text="Utilizator:")
label_utilizator.grid(row=7, column=0, padx=10, pady=5)
entry_utilizator = ttk.Entry(root, width=40)
entry_utilizator.grid(row=7, column=1, padx=10, pady=5)

label_rezultat = ttk.Label(root, text="Rezultat:")
label_rezultat.grid(row=8, column=0, padx=10, pady=5)
entry_rezultat = tk.Text(root, height=5, width=30)
entry_rezultat.grid(row=8, column=1, padx=10, pady=5)

# Submit button
submit_button = ttk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=9, column=0, columnspan=2, pady=10)

# Export button
export_button = ttk.Button(root, text="Export to Excel", command=export_to_excel)
export_button.grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()
