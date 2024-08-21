import pandas as pd
import hashlib
import os
import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from datetime import datetime


# <editor-fold desc="Login">
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
# </editor-fold>


# Main window
def main_window():
    f = pd.read_csv('formate-scurt.csv')

    def toggle(ii):
        if checkbox_val[ii].get():
            param_ap1[ii].config(state='normal')
            param_ap2[ii].config(state='normal')
        else:
            param_ap1[ii].config(state='disabled')
            param_ap2[ii].config(state='disabled')

    def completare_registre(idff):

        r0 = pd.read_csv('registre/0.csv')
        r1 = pd.read_csv('registre/1.csv')
        r2 = pd.read_csv('registre/2.csv')
        r3 = pd.read_csv('registre/3.csv')
        r4 = pd.read_csv('registre/4.csv')
        r5 = pd.read_csv('registre/5.csv')
        r6 = pd.read_csv('registre/6.csv')
        r7 = pd.read_csv('registre/7.csv')
        r8 = pd.read_csv('registre/8.csv')
        r9 = pd.read_csv('registre/9.csv')
        r10 = pd.read_csv('registre/10.csv')
        r11 = pd.read_csv('registre/11.csv')
        r12 = pd.read_csv('registre/12.csv')
        r13 = pd.read_csv('registre/13.csv')
        r14 = pd.read_csv('registre/14.csv')
        r15 = pd.read_csv('registre/15.csv')
        r16 = pd.read_csv('registre/16.csv')
        r17 = pd.read_csv('registre/17.csv')
        r18 = pd.read_csv('registre/18.csv')
        r19 = pd.read_csv('registre/19.csv')
        r20 = pd.read_csv('registre/20.csv')
        r21 = pd.read_csv('registre/21.csv')
        r22 = pd.read_csv('registre/22.csv')

        # Balanta Mettler Toledo AB204-S
        if idff.loc[0, 'aparate'][0]:
            nr0 = len(r0)
            r0.loc[nr0, 'Nr. crt.'] = nr0 + 1
            r0.loc[nr0, 'Data'] = idff.loc[0, 'Data_in']
            r0.loc[nr0, 'Operaţia/Denumirea probei'] = idff.loc[0, 'Produs']
            r0.loc[nr0, 'Serie/Lot'] = idff.loc[0, 'Seria']
            r0.loc[nr0, 'Masa cântărită, g'] = idff.loc[0, 'aparate1'][0]
            r0.loc[nr0, 'Semnătura persoanei care a efectuat operaţia'] = idff.loc[0, 'Utilizator']
            r0.loc[nr0, 'Observaţii'] = idff.loc[0, 'Obs']
            r0.to_csv('registre/0.csv', index=False, header=True)

        # Balanta Radwag – Partner PS4500 R2
        if idff.loc[0, 'aparate'][1]:
            nr1 = len(r1)
            r1.loc[nr1, 'Nr. crt.'] = nr1 + 1
            r1.loc[nr1, 'Data'] = idff.loc[0, 'Data_in']
            r1.loc[nr1, 'Operaţia/Denumirea probei'] = idff.loc[0, 'Produs']
            r1.loc[nr1, 'Serie/Lot'] = idff.loc[0, 'Seria']
            r1.loc[nr1, 'Masa cântărită, g'] = idff.loc[0, 'aparate1'][1]
            r1.loc[nr1, 'Semnătura persoanei care a efectuat operaţia'] = idff.loc[0, 'Utilizator']
            r1.loc[nr1, 'Observaţii'] = idff.loc[0, 'Obs']
            r1.to_csv('registre/1.csv', index=False, header=True)

        # Balanta VWR 611-2271
        if idff.loc[0, 'aparate'][2]:
            nr2 = len(r2)
            r2.loc[nr2, 'Nr. crt.'] = nr2 + 1
            r2.loc[nr2, 'Data'] = idff.loc[0, 'Data_in']
            r2.loc[nr2, 'Operaţia/Denumirea probei'] = idff.loc[0, 'Produs']
            r2.loc[nr2, 'Serie/Lot'] = idff.loc[0, 'Seria']
            r2.loc[nr2, 'Masa cântărită, g'] = idff.loc[0, 'aparate1'][2]
            r2.loc[nr2, 'Semnătura persoanei care a efectuat operaţia'] = idff.loc[0, 'Utilizator']
            r2.loc[nr2, 'Observaţii'] = idff.loc[0, 'Obs']
            r2.to_csv('registre/2.csv', index=False, header=True)

        # Balanta Partner AS 310 R2
        if idff.loc[0, 'aparate'][3]:
            nr3 = len(r3)
            r3.loc[nr3, 'Nr. crt.'] = nr3 + 1
            r3.loc[nr3, 'Data'] = idff.loc[0, 'Data_in']
            r3.loc[nr3, 'Operaţia/Denumirea probei'] = idff.loc[0, 'Produs']
            r3.loc[nr3, 'Serie/Lot'] = idff.loc[0, 'Seria']
            r3.loc[nr3, 'Masa cântărită, g'] = idff.loc[0, 'aparate1'][3]
            r3.loc[nr3, 'Semnătura persoanei care a efectuat operaţia'] = idff.loc[0, 'Utilizator']
            r3.loc[nr3, 'Observaţii'] = idff.loc[0, 'Obs']
            r3.to_csv('registre/3.csv', index=False, header=True)

        # Balanţa termica VWR MB 160
        if idff.loc[0, 'aparate'][4]:
            nr4 = len(r4)
            r4.loc[nr4, 'Nr. crt.'] = nr4 + 1
            r4.loc[nr4, 'Data'] = idff.loc[0, 'Data_in']
            r4.loc[nr4, 'Operaţia'] = idff.loc[0, 'Analiza']
            r4.loc[nr4, 'Denumire probă/Serie'] = f'{idff.loc[0, "Produs"]}/ {idff.loc[0, "Seria"]}'
            r4.loc[nr4, 'Semnătura utilizator'] = idff.loc[0, 'Utilizator']
            r4.loc[nr4, 'Observaţii'] = idff.loc[0, 'Obs']
            r4.to_csv('registre/4.csv', index=False, header=True)

        # Cuptor de calcinare Nabertherm
        if idff.loc[0, 'aparate'][5]:
            nr5 = len(r5)
            r5.loc[nr5, 'Nr. crt.'] = nr5 + 1
            r5.loc[nr5, 'Data'] = idff.loc[0, 'Data_in']
            r5.loc[nr5, 'Operaţia/Denumirea probei'] = idff.loc[0, 'Produs']
            r5.loc[nr5, 'Serie/Lot'] = idff.loc[0, 'Seria']
            r5.loc[nr5, 'Temperatură ºC/ Durata'] = idff.loc[0, 'aparate1'][5]
            r5.loc[nr5, 'Nume și prenume persoana care a efectuat operația'] = idff.loc[0, 'Utilizator']
            r5.loc[nr5, 'Observaţii'] = idff.loc[0, 'Obs']
            r5.to_csv('registre/5.csv', index=False, header=True)

        # Centrifuga Ortoalesa Digicen 21R
        if idff.loc[0, 'aparate'][6]:
            nr6 = len(r6)
            r6.loc[nr6, 'Data'] = idff.loc[0, 'Data_in']
            r6.loc[nr6, 'Denumire probă'] = idff.loc[0, 'Produs']
            r6.loc[nr6, 'Tipul probei/Lot'] = f'{idff.loc[0, "Analiza"]}/ {idff.loc[0, "Seria"]}'
            r6.loc[nr6, 'Timp de centrifugare'] = idff.loc[0, 'aparate1'][6]
            r6.loc[nr6, 'RPM'] = idff.loc[0, 'aparate2'][6]
            r6.loc[nr6, 'Semnătura operator'] = idff.loc[0, 'Utilizator']
            r6.loc[nr6, 'Observaţii'] = idff.loc[0, 'Obs']
            r6.to_csv('registre/6.csv', index=False, header=True)

        # Centrifuga Sigma 2-16P
        if idff.loc[0, 'aparate'][7]:
            nr7 = len(r7)
            r7.loc[nr7, 'Data'] = idff.loc[0, 'Data_in']
            r7.loc[nr7, 'Denumire probă'] = idff.loc[0, 'Produs']
            r7.loc[nr7, 'Tipul probei/Lot'] = f'{idff.loc[0, "Analiza"]}/ {idff.loc[0, "Seria"]}'
            r7.loc[nr7, 'Timp de centrifugare'] = idff.loc[0, 'aparate1'][7]
            r7.loc[nr7, 'RPM'] = idff.loc[0, 'aparate2'][7]
            r7.loc[nr7, 'Semnătura operator'] = idff.loc[0, 'Utilizator']
            r7.loc[nr7, 'Curățarea/Statusul aparatului'] = idff.loc[0, 'stare'][7]
            r7.loc[nr7, 'Observaţii'] = idff.loc[0, 'Obs']
            r7.to_csv('registre/7.csv', index=False, header=True)

        # Etuva Memmert UN 110
        if idff.loc[0, 'aparate'][8]:
            nr8 = len(r8)
            r8.loc[nr8, 'Nr. crt.'] = nr8 + 1
            r8.loc[nr8, 'Data'] = idff.loc[0, 'Data_in']
            r8.loc[nr8, 'Tipul operaţiei'] = idff.loc[0, 'Analiza']
            r8.loc[nr8, 'Temperatura de operare (°C)'] = idff.loc[0, 'aparate1'][8]
            r8.loc[nr8, 'Denumire produs'] = idff.loc[0, "Produs"]
            r8.loc[nr8, 'Serie/Lot'] = idff.loc[0, 'Seria']
            r8.loc[nr8, 'Semnătura persoanei care a efectuat  operaţia'] = idff.loc[0, 'Utilizator']
            r8.loc[nr8, 'Observaţii'] = idff.loc[0, 'Obs']
            r8.to_csv('registre/8.csv', index=False, header=True)

        # Sistem de dozare a proteinei Kjeldahl - Buchi
        if idff.loc[0, 'aparate'][9]:
            nr9 = len(r9)
            r9.loc[nr9, 'Nr. crt.'] = nr9 + 1
            r9.loc[nr9, 'Data'] = idff.loc[0, 'Data_in']
            r9.loc[nr9, 'Denumire operaţie'] = idff.loc[0, 'Analiza']
            r9.loc[nr9, 'Denumire produs, Seria, Data fabricației'] = \
                f'{idff.loc[0, "Produs"]}, {idff.loc[0, "Seria"]}, {idff.loc[0, "aparate1"][9]}'
            r9.loc[nr9, 'Efectuat de/Semnătura'] = idff.loc[0, 'Utilizator']
            r9.loc[nr9, 'Starea aparatului la finalul operării'] = idff.loc[0, 'stare'][9]
            r9.to_csv('registre/9.csv', index=False, header=True)

        # Incubator Biosan ES - 20
        if idff.loc[0, 'aparate'][10]:
            nr10 = len(r10)
            r10.loc[nr10, 'Nr. crt.'] = nr10 + 1
            r10.loc[nr10, 'Data'] = idff.loc[0, 'Data_in']
            r10.loc[nr10, 'Operaţia'] = idff.loc[0, 'Analiza']
            r10.loc[nr10, 'Staus aparat'] = idff.loc[0, 'stare'][10]
            r10.loc[nr10, 'Semnătura utilizator'] = idff.loc[0, 'Utilizator']
            r10.loc[nr10, 'Observații'] = idff.loc[0, 'Obs']
            r10.to_csv('registre/10.csv', index=False, header=True)

        # Liofilizator Cool Safe Model 55-4
        if idff.loc[0, 'aparate'][11]:
            nr11 = len(r11)
            r11.loc[nr11, 'Nr. crt.'] = nr11 + 1
            r11.loc[nr11, 'Data'] = idff.loc[0, 'Data_in']
            r11.loc[nr11, 'Denumire operaţie'] = idff.loc[0, 'Analiza']
            r11.loc[nr11, 'Denumire produs/Seria și data fabricației'] = \
                f'{idff.loc[0, "Produs"]}/ {idff.loc[0, "Seria"]}, {idff.loc[0, "aparate1"][11]}'
            r11.loc[nr11, 'Efectuat operarea/Semnătura'] = idff.loc[0, 'Utilizator']
            r11.loc[nr11, 'Starea aparatului la finalul operării'] = idff.loc[0, 'stare'][11]
            r11.to_csv('registre/11.csv', index=False, header=True)

        # PH-metru Consort si Seven Copact S210
        if idff.loc[0, 'aparate'][12]:
            nr12 = len(r12)
            r12.loc[nr12, 'Data'] = idff.loc[0, 'Data_in']
            r12.loc[nr12, 'Denumire produs'] = idff.loc[0, 'Produs']
            r12.loc[nr12, 'Serie/Lot'] = idff.loc[0, 'Seria']
            r12.loc[nr12, 'Tipul probei'] = idff.loc[0, 'Analiza']
            r12.loc[nr12, 'pH determinat'] = idff.loc[0, 'aparate1'][12]
            r12.loc[nr12, 'Efectuat determinarea si curățarea'] = idff.loc[0, 'Utilizator']
            r12.loc[nr12, 'Starea aparatului la finalul operării'] = idff.loc[0, 'stare'][12]
            r12.to_csv('registre/12.csv', index=False, header=True)

        # Evaporator Rotativ IKA RV 10 Control
        if idff.loc[0, 'aparate'][13]:
            nr13 = len(r13)
            r13.loc[nr13, 'Data'] = idff.loc[0, 'Data_in']
            r13.loc[nr13, 'Denumire probă'] = idff.loc[0, 'Produs']
            r13.loc[nr13, 'Tipul probei/Lot'] = f'{idff.loc[0, "Analiza"]}/ {idff.loc[0, "Seria"]}'
            r13.loc[nr13, 'Timp de evaporare'] = idff.loc[0, 'aparate1'][13]
            r13.loc[nr13, 'Semnătura operator'] = idff.loc[0, 'Utilizator']
            r13.loc[nr13, 'Observaţii'] = idff.loc[0, 'Obs']
            r13.to_csv('registre/13.csv', index=False, header=True)

        # Aparatul Soxhlet VELP
        if idff.loc[0, 'aparate'][14]:
            nr14 = len(r14)
            r14.loc[nr14, 'Nr. crt.'] = nr14 + 1
            r14.loc[nr14, 'Data'] = idff.loc[0, 'Data_in']
            r14.loc[nr14, 'Denumire probă/Produs'] = idff.loc[0, 'Produs']
            r14.loc[nr14, 'Tipul probei/Lot'] = f'{idff.loc[0, "Analiza"]}/ {idff.loc[0, "Seria"]}'
            r14.loc[nr14, 'Solvent utilizat'] = idff.loc[0, 'aparate1'][14]
            r14.loc[nr14, 'Semnătura'] = idff.loc[0, 'Utilizator']
            r14.loc[nr14, 'Observaţii'] = idff.loc[0, 'Obs']
            r14.to_csv('registre/14.csv', index=False, header=True)

        # Vascozimetru Fungilab model Expert R
        if idff.loc[0, 'aparate'][15]:
            nr15 = len(r15)
            r15.loc[nr15, 'Data'] = idff.loc[0, 'Data_in']
            r15.loc[nr15, 'Denumire probă/Lot'] = f'{idff.loc[0, "Produs"]}/ {idff.loc[0, "Seria"]}'
            r15.loc[nr15, 'Vâscozitate (cP)'] = '-'
            r15.loc[nr15, 'Timp de lucru'] = idff.loc[0, 'aparate1'][15]
            r15.loc[nr15, 'Axul'] = idff.loc[0, 'aparate2'][15]
            r15.loc[nr15, 'Semnătura operator'] = idff.loc[0, 'Utilizator']
            r15.loc[nr15, 'Curățare/Statusul aparatului'] = idff.loc[0, 'stare'][15]
            r15.loc[nr15, 'Observaţii'] = idff.loc[0, 'Obs']
            r15.to_csv('registre/15.csv', index=False, header=True)

        # Extractor cu ultrasunete Steel 500-DG
        if idff.loc[0, 'aparate'][16]:
            nr16 = len(r16)
            r16.loc[nr16, 'Nr. crt.'] = nr16 + 1
            r16.loc[nr16, 'Data'] = idff.loc[0, 'Data_in']
            r16.loc[nr16, 'Operaţia/Denumirea probei'] = f'{idff.loc[0, "Analiza"]}/ {idff.loc[0, "Produs"]}'
            r16.loc[nr16, 'Serie/Lot'] = idff.loc[0, 'Seria']
            r16.loc[nr16, 'Timp de extracție/Putere ultrasunete'] = idff.loc[0, 'aparate1'][16]
            r16.loc[nr16, 'Nume și prenume operator'] = idff.loc[0, 'Utilizator']
            r16.loc[nr16, 'Observaţii'] = idff.loc[0, 'Obs']
            r16.to_csv('registre/16.csv', index=False, header=True)

        # Echipament determinare activitate apa Novasina
        if idff.loc[0, 'aparate'][17]:
            nr17 = len(r17)
            r17.loc[nr17, 'Nr. crt.'] = nr17 + 1
            r17.loc[nr17, 'Data'] = idff.loc[0, 'Data_in']
            r17.loc[nr17, 'Operaţia/Denumirea probei'] = f'{idff.loc[0, "Analiza"]}/ {idff.loc[0, "Produs"]}'
            r17.loc[nr17, 'Serie/Lot'] = idff.loc[0, 'Seria']
            r17.loc[nr17, 'Valoarea activității apei cititie'] = idff.loc[0, 'aparate1'][17]
            r17.loc[nr17, 'Nume și prenume operator'] = idff.loc[0, 'Utilizator']
            r17.loc[nr17, 'Observaţii'] = idff.loc[0, 'Obs']
            r17.to_csv('registre/17.csv', index=False, header=True)

        # Moara cu cutite Gm 200
        if idff.loc[0, 'aparate'][18]:
            nr18 = len(r18)
            r18.loc[nr18, 'Nr. crt.'] = nr18 + 1
            r18.loc[nr18, 'Data'] = idff.loc[0, 'Data_in']
            r18.loc[nr18, 'Operaţia/Denumirea probei'] = f'{idff.loc[0, "Analiza"]}/ {idff.loc[0, "Produs"]}'
            r18.loc[nr18, 'Serie/Lot'] = idff.loc[0, 'Seria']
            r18.loc[nr18, 'Nume și prenume operator'] = idff.loc[0, 'Utilizator']
            r18.loc[nr18, 'Observaţii'] = idff.loc[0, 'Obs']
            r18.to_csv('registre/18.csv', index=False, header=True)

        # HPLC
        if idff.loc[0, 'aparate'][19]:
            nr19 = len(r19)
            r19.loc[nr19, 'Nr. crt.'] = nr19 + 1
            r19.loc[nr19, 'Data'] = idff.loc[0, 'Data_in']
            r19.loc[nr19, 'Denumire produs'] = idff.loc[0, "Produs"]
            r19.loc[nr19, 'Seria și data fabricației'] = f'{idff.loc[0, "Seria"]}, {idff.loc[0, "aparate1"][19]}'
            r19.loc[nr19, 'Efectuat determinarea'] = idff.loc[0, 'Utilizator']
            r19.loc[nr19, 'Starea aparatului la finalul operării'] = idff.loc[0, 'stare'][19]
            r19.to_csv('registre/19.csv', index=False, header=True)

        # UV VIS
        if idff.loc[0, 'aparate'][20]:
            nr20 = len(r20)
            r20.loc[nr20, 'Nr. crt.'] = nr20 + 1
            r20.loc[nr20, 'Data'] = idff.loc[0, 'Data_in']
            r20.loc[nr20, 'Denumire produs'] = idff.loc[0, "Produs"]
            r20.loc[nr20, 'Serie/Lot'] = idff.loc[0, 'Seria']
            r20.loc[nr20, 'Tipul probei'] = idff.loc[0, "Analiza"]
            r20.loc[nr20, 'Absorbanța/Lungimea de undă'] = idff.loc[0, "aparate1"][20]
            r20.loc[nr20, 'Efectuat citirea'] = idff.loc[0, 'Utilizator']
            r20.loc[nr20, 'Starea aparatului la finalul operării'] = idff.loc[0, 'stare'][20]
            r20.to_csv('registre/20.csv', index=False, header=True)

        # Probe
        nr21 = len(r21)
        r21.loc[nr21, 'Nr.'] = nr21 + 1
        r21.loc[nr21, 'Denumire probă'] = idff.loc[0, "Produs"]
        r21.loc[nr21, 'Seria'] = idff.loc[0, 'Seria']
        r21.loc[nr21, 'Solicitant'] = idff.loc[0, 'Solicitant']
        r21.loc[nr21, 'Analiza solicitată'] = idff.loc[0, "Analiza"]
        r21.loc[nr21, 'Data primirii'] = idff.loc[0, 'Data_in']
        r21.loc[nr21, 'Data eliberării'] = idff.loc[0, 'Data_elib']
        r21.loc[nr21, 'Nume'] = idff.loc[0, 'Utilizator']
        r21.loc[nr21, 'Semnătura'] = idff.loc[0, 'Utilizator']
        r21.to_csv('registre/21.csv', index=False, header=True)

        # Registru rapoarte
        nr22 = len(r22)
        r22.loc[nr22, 'Nr. raport de analiză'] = nr22 + 1
        r22.loc[nr22, 'Data primirii probei'] = idff.loc[0, 'Data_in']
        r22.loc[nr22, 'Data eliberării raportului de analiză'] = idff.loc[0, 'Data_elib']
        r22.loc[nr22, 'Denumire produs'] = idff.loc[0, 'Produs']
        r22.loc[nr22, 'Serie'] = idff.loc[0, 'Seria']
        r22.loc[nr22, 'Rezoluție'] = idff.loc[0, 'Rezultat']
        r22.loc[nr22, 'Semnătura'] = idff.loc[0, 'Utilizator']
        r22.to_csv('registre/22.csv', index=False, header=True)

    def get_entry_values():

        # <editor-fold desc="frame1 get, clear, append">
        # Get values from form fields
        nume_proba = entry_nume_proba.get()
        seria = entry_seria.get()
        analiza = entry_analiza.get()
        solicitant = entry_solicitant.get()
        data_intrare = entry_data_intrare.get_date().strftime('%Y-%m-%d')
        data_eliberare = entry_data_eliberare.get_date().strftime('%Y-%m-%d')
        utilizator = entry_utilizator.get()
        rezultat = entry_rezultat.get()
        observatii = entry_observatii.get()

        # Clear form fields after submission
        entry_nume_proba.delete(0, tk.END)
        entry_seria.delete(0, tk.END)
        entry_analiza.delete(0, tk.END)
        entry_data_intrare.set_date(datetime.now())
        entry_data_eliberare.set_date(datetime.now())
        entry_utilizator.delete(0, tk.END)
        entry_rezultat.delete(0, tk.END)
        entry_observatii.delete(0, tk.END)

        g = pd.read_csv('inregistrari.csv')
        intrare = [g.Nr.max() + 1, data_intrare, data_eliberare, nume_proba,
                   seria, analiza, solicitant, utilizator, rezultat, observatii]

        # </editor-fold>

        chx = []
        ap1 = []
        ap2 = []
        st = []

        for i in range(21):
            chx.append(checkbox_val[i].get())
            ap1.append(param_ap1[i].get())
            ap2.append(param_ap2[i].get())
            st.append(1)

        intrare.append(chx)
        intrare.append(ap1)
        intrare.append(ap2)
        intrare.append(st)

        idf = pd.DataFrame(intrare).T
        idf.columns = g.columns
        g = pd.concat([g, idf], axis=0)
        print(idf.values)

        g.to_csv('inregistrari.csv', index=False, header=True)
        completare_registre(idf)

    def show(ii):

        df = pd.read_csv(f'registre/{ii}.csv')

        # Create the main window
        sh = tk.Tk()
        sh.title(f"Registru {df.columns[2]}")

        header_frame = ttk.Frame(sh, padding=20)
        header_frame.grid(row=0, column=0, sticky='ew')
        header_text = 'S.C. HOFIGAL EXPORT IMPORT S.A.\nDepartament Cercetare Dezvoltare Brevete'
        label_header = ttk.Label(header_frame, text=header_text, font=('Terminal', '12', 'bold'), cursor='heart')
        label_header.pack(padx=10, pady=15, anchor='w')
        label_title = ttk.Label(header_frame, text=f'{df.columns[1]}\n{df.columns[2]}',
                                font=('Arial', '12', 'bold'), justify='center')
        label_title.pack(padx=10, pady=15, anchor='center')

        table_frame = ttk.Frame(sh, padding=20)
        table_frame.grid(row=1, column=0)

        footer_frame = ttk.Frame(sh, padding=20)
        footer_frame.grid(row=2, column=0, sticky='ew')
        label_format = ttk.Label(footer_frame, text=f"Format - {int(float(df.columns[0]))}",
                                 font=('Terminal', '10'))
        label_format.pack(padx=10, pady=5, anchor='w')
        label_pagina = ttk.Label(footer_frame, text='Pagina: 1', font=('Arial', '10'))
        label_pagina.pack(padx=10, pady=5, anchor='e')

        # <editor-fold desc="Style">

        # Create a style
        style = ttk.Style()

        # Modify the Treeview style
        style.configure("Custom.Treeview",
                        background="#F0F0F0",  # Background color of the cells
                        foreground="black",  # Text color of the cells
                        rowheight=25,  # Row height
                        fieldbackground="#F0F0F0",  # Background color of the entire treeview
                        bordercolor="gray",  # Border color between cells
                        borderwidth=1)  # Border width

        style.map("Custom.Treeview",
                  background=[('selected', '#347083')],  # Background color when a row is selected
                  foreground=[('selected', 'white')])  # Text color when a row is selected

        # Modify the Treeview heading style
        style.configure("Custom.Treeview.Heading",
                        background="#4A8DB8",  # Background color of the headers
                        foreground="white",  # Text color of the headers
                        bordercolor="gray",  # Border color between headers
                        borderwidth=1,  # Border width
                        font=('Helvetica', 10, 'bold'))  # Font for the headers

        style.map("Custom.Treeview.Heading",
                  background=[('active', '#5FA7D0')])  # Background color when the header is clicked
        # </editor-fold>

        # Create a Treeview widget

        tree = ttk.Treeview(table_frame, cursor='gumby', height=20)

        # Define the number of columns
        tree["columns"] = list(df.columns[3:])
        tree["show"] = "headings"  # remove the first empty column

        # Create the column headers
        for column in df.columns[3:]:
            tree.heading(column, text=column)

        for col in df.columns[3:]:
            tree.column(col, width=150, minwidth=150, anchor='center', stretch=True)

        # Add the data rows
        for index, row in df.iterrows():
            tree.insert("", "end", values=list(row[3:]))

        # Pack the Treeview widget into the window
        tree.grid(row=0, column=0, sticky="nsew")

        # Create a vertical scrollbar
        vertical_scrollbar = tk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
        vertical_scrollbar.grid(row=0, column=1, sticky="ns")

        # Create a horizontal scrollbar
        horizontal_scrollbar = tk.Scrollbar(table_frame, orient="horizontal", command=tree.xview)
        horizontal_scrollbar.grid(row=1, column=0, sticky="ew")

        # Link vertical scrollbar to the text widget
        tree.config(yscrollcommand=vertical_scrollbar.set)

        # Link horizontal scrollbar to the text widget
        tree.config(xscrollcommand=horizontal_scrollbar.set)

        # Start the Tkinter main loop
        sh.mainloop()

    root = tk.Tk()
    root.title('form')

    # <editor-fold desc="frame1">

    frame1 = ttk.Frame(root, padding='10')
    frame1.grid(row=0, column=0)

    label_nume_proba = ttk.Label(frame1, text="Nume produs")
    label_nume_proba.grid(row=0, column=0, padx=10, pady=5)
    entry_nume_proba = ttk.Entry(frame1, width=30)
    entry_nume_proba.grid(row=0, column=1, padx=10, pady=5)

    label_seria = ttk.Label(frame1, text="Seria:")
    label_seria.grid(row=1, column=0, padx=10, pady=5)
    entry_seria = ttk.Entry(frame1, width=30)
    entry_seria.grid(row=1, column=1, padx=10, pady=5)

    label_analiza = ttk.Label(frame1, text="Analiza:")
    label_analiza.grid(row=2, column=0, padx=10, pady=5)
    entry_analiza = ttk.Entry(frame1, width=30)
    entry_analiza.grid(row=2, column=1, padx=10, pady=5)

    label_solicitant = ttk.Label(frame1, text="Solicitant:")
    label_solicitant.grid(row=3, column=0, padx=10, pady=5)
    entry_solicitant = tk.StringVar()
    entry_solicitantCD = ttk.Radiobutton(frame1, text="CD", variable=entry_solicitant, value="CD")
    entry_solicitantCC = ttk.Radiobutton(frame1, text="CC", variable=entry_solicitant, value="CC")
    entry_solicitantCD.grid(row=3, column=1, padx=10, pady=5)
    entry_solicitantCC.grid(row=4, column=1, padx=10, pady=5)

    label_data_intrare = ttk.Label(frame1, text='Data intrare')
    label_data_intrare.grid(row=5, column=0, padx=10, pady=5)
    entry_data_intrare = DateEntry(frame1, width=12, background='darkblue', foreground='white', borderwidth=2)
    entry_data_intrare.grid(row=5, column=1, padx=10, pady=5)
    entry_data_intrare.set_date(datetime.now())

    label_data_eliberare = ttk.Label(frame1, text='Data eliberare')
    label_data_eliberare.grid(row=6, column=0, padx=10, pady=5)
    entry_data_eliberare = DateEntry(frame1, width=12, background='darkblue', foreground='white', borderwidth=2)
    entry_data_eliberare.grid(row=6, column=1, padx=10, pady=5)
    entry_data_eliberare.set_date(datetime.now())

    label_utilizator = ttk.Label(frame1, text="Utilizator:")
    label_utilizator.grid(row=7, column=0, padx=10, pady=5)
    entry_utilizator = ttk.Entry(frame1, width=30)
    entry_utilizator.grid(row=7, column=1, padx=10, pady=5)

    label_rezultat = ttk.Label(frame1, text="Rezultat:")
    label_rezultat.grid(row=8, column=0, padx=10, pady=5)
    entry_rezultat = ttk.Entry(frame1, width=30)
    entry_rezultat.grid(row=8, column=1, padx=10, pady=5)

    label_observatii = ttk.Label(frame1, text="Observații:")
    label_observatii.grid(row=9, column=0, padx=10, pady=5)
    entry_observatii = ttk.Entry(frame1, width=30)
    entry_observatii.grid(row=9, column=1, padx=10, pady=5)

    get_values_button = ttk.Button(frame1, text="Adaugă intrare", command=get_entry_values)
    get_values_button.grid(row=10, column=0, columnspan=2, padx=3, pady=3)

    # </editor-fold>

    # <editor-fold desc="frame2">

    frame2 = ttk.Frame(root, padding="10")
    frame2.grid(row=0, column=1, sticky='nsew')

    checkbox_val = [tk.BooleanVar() for i in range(21)]
    checkbox = [ttk.Checkbutton(frame2, text=f.aparat[i], variable=checkbox_val[i],
                                command=lambda i=i: toggle(i)) for i in range(21)]

    label_ap1 = [ttk.Label(frame2, text=f.val1[i]) for i in range(21)]
    label_ap2 = [ttk.Label(frame2, text=f.val2[i]) for i in range(21)]

    param_ap1 = [ttk.Entry(frame2, width=20, state='disabled') for i in range(21)]
    param_ap2 = [ttk.Entry(frame2, width=20, state='disabled') for i in range(21)]

    for i in range(21):
        checkbox[i].grid(row=i, column=0, sticky=tk.W)

        label_ap1[i].grid(row=i, column=1)
        param_ap1[i].grid(row=i, column=2, sticky='ew')

        if f.val1[i] == '-':
            label_ap1[i].grid_remove()
            param_ap1[i].grid_remove()

        label_ap2[i].grid(row=i, column=3)
        param_ap2[i].grid(row=i, column=4, sticky='ew')

        if f.val2[i] == '-':
            label_ap2[i].grid_remove()
            param_ap2[i].grid_remove()

    # </editor-fold>

    # <editor-fold desc="frame3">
    frame3 = ttk.Frame(root, padding="10")
    frame3.grid(row=1, column=0, columnspan=2, sticky='nsew')

    butoane_registre = [ttk.Button(frame3, text=f.aparat[i], command=lambda i=i: show(i)).grid(
        row=i // 5, column=i % 5, pady=10) for i in range(23)]

    # </editor-fold>

    root.mainloop()


login_window()
