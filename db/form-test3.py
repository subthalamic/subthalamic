import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import pandas as pd
from datetime import datetime
from tkcalendar import DateEntry
import sqlite3
import hashlib
import os

f = pd.read_csv('formate-scurt.csv')
elements = f.aparat[:19].values

###########################################################################

# Hash a password for storing
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Verify a stored password against one provided by user
def verify_password(stored_password, provided_password):
    return stored_password == hash_password(provided_password)


# Load user credentials from file
def load_credentials():
    credentials = {}
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            for line in file:
                username, hashed_password = line.strip().split(":")
                credentials[username] = hashed_password
    return credentials


# Save new user credentials to file
def save_credentials(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username}:{hash_password(password)}\n")


# Login window
def login_window():
    def check_credentials():
        username = username_entry.get()
        password = password_entry.get()

        credentials = load_credentials()

        if username in credentials and verify_password(credentials[username], password):
            login_success()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def open_signup_window():
        signup_window()

    login_win = tk.Tk()
    login_win.title("Login")

    tk.Label(login_win, text="Username").pack()
    username_entry = tk.Entry(login_win)
    username_entry.pack()

    tk.Label(login_win, text="Password").pack()
    password_entry = tk.Entry(login_win, show="*")
    password_entry.pack()

    tk.Button(login_win, text="Login", command=check_credentials).pack()
    tk.Button(login_win, text="Sign Up", command=open_signup_window).pack()

    login_win.mainloop()


# Sign-up window
def signup_window():
    def signup():
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        credentials = load_credentials()

        if username in credentials:
            messagebox.showerror("Error", "Username already exists")
        else:
            save_credentials(username, password)
            messagebox.showinfo("Success", "Account created successfully")
            signup_win.destroy()

    signup_win = tk.Tk()
    signup_win.title("Sign Up")

    tk.Label(signup_win, text="Username").pack()
    username_entry = tk.Entry(signup_win)
    username_entry.pack()

    tk.Label(signup_win, text="Password").pack()
    password_entry = tk.Entry(signup_win, show="*")
    password_entry.pack()

    tk.Label(signup_win, text="Confirm Password").pack()
    confirm_password_entry = tk.Entry(signup_win, show="*")
    confirm_password_entry.pack()

    tk.Button(signup_win, text="Sign Up", command=signup).pack()

    signup_win.mainloop()


# Function called after successful login
def login_success():
    messagebox.showinfo("Login Successful", "Welcome!")
    main_window()

###########################################################################




# Main window after login
def main_window():

    # Function to enable or disable entry widget
    def toggle_entry(entry1, entry2, var):
        if var.get():
            entry1.config(state='normal')
            entry2.config(state='normal')
        else:
            entry1.config(state='disabled')
            entry2.config(state='disabled')

    # Function to get values of all entries
    def get_entry_values(entries_vars):
        aparatl = []
        for entry1, entry2, var in entries_vars:
            if var.get():  # Only add value if checkbox is checked
                aparatl.append(var.get())
                aparatl.append(entry1.get())
                aparatl.append(entry2.get())

        # Get values from form fields
        nume_proba = entry_nume_proba.get()
        seria = entry_seria.get()
        analiza = entry_analiza.get()
        solicitant = entry_solicitant.get()
        data_intrare = entry_data_intrare.get_date().strftime('%Y-%m-%d')
        data_eliberare = entry_data_eliberare.get_date().strftime('%Y-%m-%d')
        utilizator = entry_utilizator.get()
        rezultat = entry_rezultat.get('1.0', tk.END).strip()  # Get text from Text widget

        # Clear form fields after submission
        entry_nume_proba.delete(0, tk.END)
        entry_seria.delete(0, tk.END)
        entry_analiza.delete(0, tk.END)
        entry_data_intrare.set_date(datetime.now())
        entry_data_eliberare.set_date(datetime.now())
        entry_utilizator.delete(0, tk.END)
        entry_rezultat.delete('1.0', tk.END)

        intrare = []

        g = pd.read_csv('inregistrari.csv')

        intrare.append(g.Nr.max() + 1)
        intrare.append(data_intrare)
        intrare.append(data_eliberare)
        intrare.append(nume_proba)
        intrare.append(seria)
        intrare.append(analiza)
        intrare.append(solicitant)
        intrare.append(utilizator)
        intrare.append(rezultat)
        intrare.append(rezultat)
        intrare.append(aparatl)

        print(intrare)
        print(len(intrare))

        i = pd.DataFrame(intrare).T

        i.columns = g.columns

        print(i)

        g = pd.concat([g, i], axis=0)

        g.to_csv('inregistrari.csv', index=False, header=True)
        print(g)

    root = tk.Tk()
    root.title('form')

    framel = ttk.Frame(root, padding='10')
    framel.grid(row=0, column=0)

    label_nume_proba = ttk.Label(framel, text="Nume produs")
    label_nume_proba.grid(row=0, column=0, padx=10, pady=5)
    entry_nume_proba = ttk.Entry(framel, width=40)
    entry_nume_proba.grid(row=0, column=1, padx=10, pady=5)

    label_seria = ttk.Label(framel, text="Seria:")
    label_seria.grid(row=1, column=0, padx=10, pady=5)
    entry_seria = ttk.Entry(framel, width=40)
    entry_seria.grid(row=1, column=1, padx=10, pady=5)

    label_analiza = ttk.Label(framel, text="Analiza:")
    label_analiza.grid(row=2, column=0, padx=10, pady=5)
    entry_analiza = ttk.Entry(framel, width=40)
    entry_analiza.grid(row=2, column=1, padx=10, pady=5)

    label_solicitant = ttk.Label(framel, text="Solicitant:")
    label_solicitant.grid(row=3, column=0, padx=10, pady=5)
    entry_solicitant = tk.StringVar()
    entry_solicitantCD = ttk.Radiobutton(framel, text="CD", variable=entry_solicitant, value="CD")
    entry_solicitantCC = ttk.Radiobutton(framel, text="CC", variable=entry_solicitant, value="CC")
    entry_solicitantCD.grid(row=3, column=1, padx=10, pady=5)
    entry_solicitantCC.grid(row=4, column=1, padx=10, pady=5)

    label_data_intrare = ttk.Label(framel, text='data intrare')
    label_data_intrare.grid(row=5, column=0, padx=10, pady=5)
    entry_data_intrare = DateEntry(framel, width=12, background='darkblue', foreground='white', borderwidth=2)
    entry_data_intrare.grid(row=5, column=1, padx=10, pady=5)
    entry_data_intrare.set_date(datetime.now())

    label_data_eliberare = ttk.Label(framel, text='data eliberare')
    label_data_eliberare.grid(row=6, column=0, padx=10, pady=5)
    entry_data_eliberare = DateEntry(framel, width=12, background='darkblue', foreground='white', borderwidth=2)
    entry_data_eliberare.grid(row=6, column=1, padx=10, pady=5)
    entry_data_eliberare.set_date(datetime.now())

    label_utilizator = ttk.Label(framel, text="Utilizator:")
    label_utilizator.grid(row=7, column=0, padx=10, pady=5)
    entry_utilizator = ttk.Entry(framel, width=40)
    entry_utilizator.grid(row=7, column=1, padx=10, pady=5)

    label_rezultat = ttk.Label(framel, text="Rezultat:")
    label_rezultat.grid(row=8, column=0, padx=10, pady=5)
    entry_rezultat = tk.Text(framel, height=5, width=30)
    entry_rezultat.grid(row=8, column=1, padx=10, pady=5)

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

    entries_vars = []

    for idx, element in enumerate(elements):
        var = tk.BooleanVar()
        checkbox = ttk.Checkbutton(frame, text=element, variable=var)
        checkbox.grid(row=idx, column=0, sticky=tk.W)

        ttk.Label(frame, text=f.val1[idx]).grid(row=idx, column=1)

        entry1 = ttk.Entry(frame, state='disabled')
        entry1.grid(row=idx, column=2, sticky=(tk.W, tk.E))

        ttk.Label(frame, text=f.val2[idx]).grid(row=idx, column=3)

        entry2 = ttk.Entry(frame, state='disabled')
        entry2.grid(row=idx, column=4, sticky=(tk.W, tk.E))

        entries_vars.append((entry1, entry2, var))

        # Use lambda to pass the current entry and var to the toggle function
        var.trace_add('write', lambda *args, e1=entry1, e2=entry2, v=var: toggle_entry(e1, e2, v))

    get_values_button = ttk.Button(framel, text="Adauga intrare", command=lambda: get_entry_values(entries_vars))
    get_values_button.grid(row=9, column=0, columnspan=2, pady=10)

    root.mainloop()


# Start with login window
login_window()
