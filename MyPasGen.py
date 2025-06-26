#TESTOVACI VERZE:

import tkinter as tk
from tkinter import END
import random
import string

# vytvoření hlavního okna aplikace
root = tk.Tk()

# Tvorba checkbuttonu pro specifikaci hesla
options = ["Upper Case", "Lower Case", "Digits", "Symbols"]
vars = [tk.BooleanVar(value=True) for _ in options]

# Vytvoření a umístění prvků
entry_vars = []  # Seznam pro uchování instancí StringVar pro vstupní pole

for i, option in enumerate(options):
    # Checkbutton
    checkbutton = tk.Checkbutton(root, text=option, variable=vars[i])
    checkbutton.grid(row=i, column=0, sticky='w')
    
    # StringVar pro vstupní pole
    entry_var = tk.StringVar(value="5")  # Přednastavená hodnota
    entry_vars.append(entry_var)
    
    # Vstupní pole
    entry = tk.Entry(root, textvariable=entry_var)
    entry.grid(row=i, column=1, sticky='w')
    
# Funkce pro omezení hodnoty v Entry
def check_entry_value(entry_var, option):
    try:
        value = int(entry_var.get())
        if value < 1:
            entry_var.set("1")
        elif option == "Upper Case" and value > len(string.ascii_uppercase):
            entry_var.set(str(len(string.ascii_uppercase)))
        elif option == "Lower Case" and value > len(string.ascii_lowercase):
            entry_var.set(str(len(string.ascii_lowercase)))
        elif option == "Digits" and value > len(string.digits):
            entry_var.set(str(len(string.digits)))
        elif option == "Symbols" and value > len(entry_symbols.get()):
            entry_var.set(str(len(entry_symbols.get())))
    except ValueError:
        entry_var.set("1")

# Přiřazení funkce k události FocusOut
entry.bind('<FocusOut>', lambda event, entry_var=entry_var, option=option: check_entry_value(entry_var, option))
    
# Tlačítka pro změnu čísla
button_positions = [(row, column) for row in range(1, 5) for column in range(1, 5) if column in (3, 4)]

for i, (row, column) in enumerate(button_positions):
    button_text = "<" if column == 3 else ">"
    button = tk.Button(root, text=button_text, width=2, height=1, font=('Arial', 6))
    button.grid(row=row, column=column, sticky='w')

# Funkce pro snížení hodnoty vstupního pole
def decrease_value(entry_var, option, i):
    value = int(entry_var.get())
    if value > 0:
        entry_var.set(str(value - 1))
        check_entry_value(entry_var, option, i)

# Funkce pro zvýšení hodnoty vstupního pole
def increase_value(entry_var, option, i):
    value = int(entry_var.get())
    entry_var.set(str(value + 1))
    check_entry_value(entry_var, option, i)
    
#Vytvoreni chceckbutton pro Unikatni
var_unique = tk.BooleanVar(value=True)
unique_checkbutton = tk.Checkbutton(root, text="Unique Characters", variable=var_unique)
unique_checkbutton.grid(row=6, column=0, sticky='w')

vars.append(var_unique)

# vytvoření vstupního pole pro symboly
entry_symbols = tk.Entry(root)
entry_symbols.insert(0, "'`!?.:;$%&@~,#()<>{}[]_*-+^=/|\\")
entry_symbols.grid(row=5, column=1, sticky='w')

# vytvoření vstupního pole pro mnozstvi znaku
entry = tk.Entry(root)
entry.insert(0, "20")
entry.grid(row=7, column=0, sticky='w')

# definujeme hodnotu a udrzujeme rozmezi
def check_number():
    try:
        number = int(entry.get())
        entry.delete(0, END)
        entry.insert(0, max(12, min(number, 99)))
    except ValueError:
        entry.delete(0, END)
        entry.insert(0, 20)
        
# fce pro snizeni hodnoty
def decrease_number():
    number = int(entry.get()) - 1
    if number < 12:
        number = 12
    entry.delete(0, END)
    entry.insert(0, number)

# vytvoření snizujiciho tlačítka
decrease_button = tk.Button(root, text="<", command=decrease_number)
decrease_button.grid(row=7, column=1, sticky='w')
        
# fce pro zvyseni hodnoty
def increase_number():
    number = int(entry.get()) + 1
    if number > 99:
        number = 99
    entry.delete(0, END)
    entry.insert(0, number)

# vytvoření zvysujiciho tlačítka
increase_button = tk.Button(root, text=">", command=increase_number)
increase_button.grid(row=7, column=2, sticky='w')

# funkce pro generator
def generate_password(length):
    # seznam možných znaků
    characters = []

    # přidání vybraných typů znaků do seznamu
    if vars[0].get():
        characters += string.ascii_uppercase
    if vars[1].get():
        characters += string.ascii_lowercase
    if vars[2].get():
        characters += string.digits
    if vars[3].get():
        characters += entry_symbols.get()

    # garantované znaky pro jednotlivé typy
    guaranteed_characters = []

    # získání počtu garantovaných znaků pro jednotlivé typy
    for i, entry_var in enumerate(entry_vars):
        count = int(entry_var.get())
        if count > 0:
            # vybrání garantovaných znaků s unikátními symboly
            unique_characters = random.sample(characters, count)
            guaranteed_characters += unique_characters

            # odebrání garantovaných znaků ze seznamu znaků
            for char in unique_characters:
                characters.remove(char)

    # zbývající znaky
    remaining_length = length - len(guaranteed_characters)
    remaining_characters = random.choices(characters, k=remaining_length)

    # spojení garantovaných znaků s ostatními znaky
    password = guaranteed_characters + remaining_characters

    # převrácení pořadí znaků pro výslednou náhodnost
    random.shuffle(password)

    # vložení hesla do listboxu
    listbox.insert(tk.END, ''.join(password))


# funkce pro generator
def generate_password(length):
    
    # seznam možných znaků
    characters = []
    guaranteed_characters = []

    if vars[0].get():
        characters += string.ascii_uppercase
        guaranteed_characters += random.sample(string.ascii_uppercase, int(entry_vars[0].get()))

    if vars[1].get():
        characters += string.ascii_lowercase
        guaranteed_characters += random.sample(string.ascii_lowercase, int(entry_vars[1].get()))

    if vars[2].get():
        characters += string.digits
        guaranteed_characters += random.sample(string.digits, int(entry_vars[2].get()))

    if vars[3].get():
        characters += entry_symbols.get()
        guaranteed_characters += random.sample(entry_symbols.get(), int(entry_vars[3].get()))

    # doplnění garantovaných znaků s náhodnými znaky ze všech dostupných znaků
    remaining_length = length - len(guaranteed_characters)
    if remaining_length > 0:
        random_characters = random.choices(characters, k=remaining_length)
        password = "".join(guaranteed_characters + random_characters)
    else:
        password = "".join(guaranteed_characters)
        
# náhodné rozmístění garantovaných znaků
    random.shuffle(guaranteed_characters)

# generování zbývajících znaků
    remaining_length = length - len(guaranteed_characters)
    remaining_characters = random.choices(characters, k=remaining_length)

# spojení garantovaných znaků s ostatními znaky
    password = guaranteed_characters + remaining_characters

# převrácení pořadí znaků pro výslednou náhodnost
    random.shuffle(password)

# vložení hesla do listboxu
    listbox.insert(tk.END, ''.join(password))

# vytvoření tlačítka pro vygenerování hesla
generate_button = tk.Button(root, text="GENERATE", command=lambda: generate_password(int(entry.get())))
generate_button.grid(row=8, column=1)

# vytvoření listboxu pro zobrazování hesel
listbox = tk.Listbox(root)
listbox.grid(row=9, column=0, columnspan=3)

# spuštění smyčky hlavního okna aplikace
root.mainloop()