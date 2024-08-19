import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from datetime import datetime
from tkcalendar import DateEntry

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

    #Balanta Mettler Toledo AB204-S
    nr0 = len(r0)
    print(len(r0), nr0)
    r0.loc[nr0,'Nr. crt.'] = nr0 + 1
    r0.loc[nr0, 'Data'] = idff.loc[0,'Data_in']
    r0.loc[nr0, 'Operaţia/Denumirea probei'] = idff.loc[0, 'Produs']
    r0.loc[nr0, 'Seria/lot'] = idff.loc[0, 'Seria']
    r0.loc[nr0, 'Masa cântărită, g'] = idff.loc[0, 'aparate1'][0]
    r0.loc[nr0, 'Semnatura persoanei care a efectuat operaţia'] = idff.loc[0, 'Utilizator']
    r0.loc[nr0,'Observaţii'] = idff.loc[0,'Obs']
    print(r0.values)
    print(len(r0), nr0)
    r0.to_csv('registre/0.csv', index=False, header=True)

    #Centrifuga Ortoalesa Digiden 21R
    nr6 = len(r6)
    print(len(r6), nr6)
    #r6.loc[nr6,'Nr. crt.'] = nr6 + 1
    r6.loc[nr6, 'Data'] = idff.loc[0,'Data_in']
    r6.loc[nr6, 'Denumire probă'] = idff.loc[0, 'Produs']
    r6.loc[nr6, 'Tipul probei/lot'] = idff.loc[0, 'Seria']
    r6.loc[nr6, 'Timp de centrifugare'] = idff.loc[0, 'aparate1'][6]
    r6.loc[nr6, 'RPM'] = idff.loc[0, 'aparate2'][6]
    r6.loc[nr6, 'Semnătura operator'] = idff.loc[0, 'Utilizator']
    r6.loc[nr6,'Observaţii'] = idff.loc[0,'Obs']
    print(r6.values)
    print(len(r6), nr6)
    r6.to_csv('registre/6.csv', index=False, header=True)

    # Registru rapoarte
    nr22 = len(r22)
    print(len(r22), nr22)
    r22.loc[nr22, 'Nr. raport de analiza'] = nr22 + 1
    r22.loc[nr22, 'Data primirii probei'] = idff.loc[0, 'Data_in']
    r22.loc[nr22, 'Data eliberarii raportului de analiza'] = idff.loc[0, 'Data_elib']
    r22.loc[nr22, 'Denumire produs'] = idff.loc[0, 'Produs']
    r22.loc[nr22, 'Serie'] = idff.loc[0, 'Seria']
    r22.loc[nr22, 'Rezolutie'] = idff.loc[0, 'Rezultat']
    r22.loc[nr22, 'Semnatura'] = idff.loc[0, 'Utilizator']
    print(r22.values)
    print(len(r22), nr22)
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
    intrare = []

    intrare.append(g.Nr.max() + 1)
    intrare.append(data_intrare)
    intrare.append(data_eliberare)
    intrare.append(nume_proba)
    intrare.append(seria)
    intrare.append(analiza)
    intrare.append(solicitant)
    intrare.append(utilizator)
    intrare.append(rezultat)
    intrare.append(observatii)

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
    g = pd.concat([g,idf], axis=0)

    g.to_csv('inregistrari.csv', index=False, header=True)
    completare_registre(idf)
    print(g)

def show():

    df = pd.read_csv('registre/22.csv')

    # Create the main window
    sh = tk.Tk()
    sh.title("CSV Table Display")

    # Create a Treeview widget
    tree = ttk.Treeview(sh)

    # Define the number of columns
    tree["columns"] = list(df.columns[3:])
    tree["show"] = "headings"  # remove the first empty column

    # Create the column headers
    for column in df.columns[3:]:
        tree.heading(column, text=column)

    # Add the data rows
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    # Pack the Treeview widget into the window
    tree.pack(expand=True, fill='both')

    # Start the Tkinter main loop
    sh.mainloop()

root = tk.Tk()
root.title('form')

# <editor-fold desc="frame1">

frame1 = ttk.Frame(root, padding ='10')
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

label_data_intrare = ttk.Label(frame1, text='data intrare')
label_data_intrare.grid(row=5, column=0, padx=10, pady=5)
entry_data_intrare = DateEntry(frame1, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_data_intrare.grid(row=5, column=1, padx=10, pady=5)
entry_data_intrare.set_date(datetime.now())

label_data_eliberare = ttk.Label(frame1, text='data eliberare')
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

label_observatii = ttk.Label(frame1, text="Observatii:")
label_observatii.grid(row=9, column=0, padx=10, pady=5)
entry_observatii = ttk.Entry(frame1, width=30)
entry_observatii.grid(row=9, column=1, padx=10, pady=5)

# </editor-fold>

# <editor-fold desc="frame2">

frame2 = ttk.Frame(root, padding="10")
frame2.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

checkbox_val = [tk.BooleanVar() for i in range(21)]
checkbox = [None] * 22
param_ap1 = [ttk.Entry(frame2, width = 20, state='disabled') for i in range(21)]
param_ap2 = [ttk.Entry(frame2, width = 20, state='disabled') for i in range(21)]

for i in range(21):
    checkbox[i] = ttk.Checkbutton(frame2, text=f.aparat[i], variable=checkbox_val[i], command=lambda i=i: toggle(i))
    checkbox[i].grid(row=i, column=0, sticky=tk.W)

    ttk.Label(frame2, text=f.val1[i]).grid(row=i, column=1)
    param_ap1[i].grid(row=i, column=2, sticky=(tk.W, tk.E))

    ttk.Label(frame2, text=f.val2[i]).grid(row=i, column=3)
    param_ap2[i].grid(row=i, column=4, sticky=(tk.W, tk.E))

# </editor-fold>

# <editor-fold desc="frame3">
frame3 = ttk.Frame(root, padding="10")
frame3.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

butoane_registre = [ttk.Button(frame3, text=f.aparat[i], command=show).grid(row=i//5, column=i%5, pady=10) for i in range(23)]

# </editor-fold>

get_values_button = ttk.Button(frame1, text="Adauga intrare", command=get_entry_values)
get_values_button.grid(row=10, column=0, columnspan=2, padx=3, pady=3)

root.mainloop()

