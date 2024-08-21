import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3
import hashlib
import os

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

# Main window after login
def main_window():
    def browse_db():
        db_path = filedialog.askopenfilename(title="Select Database File",
                                             filetypes=(("SQLite files", "*.sqlite;*.db"), ("All files", "*.*")))
        if db_path:
            db_label.config(text=db_path)
            global conn
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS records (id INTEGER PRIMARY KEY, data TEXT)''')
            conn.commit()

    def insert_data():
        data = data_entry.get()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO records (data) VALUES (?)", (data,))
            conn.commit()
            messagebox.showinfo("Success", "Data inserted successfully")
        else:
            messagebox.showerror("Error", "No database connection")

    main_win = tk.Tk()
    main_win.title("Database Insertion")

    tk.Button(main_win, text="Browse Database", command=browse_db).pack()
    db_label = tk.Label(main_win, text="No database selected")
    db_label.pack()

    tk.Label(main_win, text="Data to insert").pack()
    data_entry = tk.Entry(main_win)
    data_entry.pack()

    tk.Button(main_win, text="Insert Data", command=insert_data).pack()

    main_win.mainloop()

# Start with login window
login_window()
