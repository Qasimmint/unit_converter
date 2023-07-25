from tkinter import *
from tkinter import messagebox
import math

root = Tk()
root.title("Python Unit Converter")
root.iconbitmap(r"C:\Users\qk633\Downloads\converter.png")
root.geometry("600x500")
root.configure(background="white")

head_font = ("monospace", 40)
body_font = ("Arial", 15)
btn_font = ("fancy", 18)

def kg_to_g():
    try:
        var = float(unit_screen.get())
        to_kilo = var * 1000
        to_gram = var / 1000
        calculated_result.config(text=f"Kilogram: {to_kilo} Kilograms _____ Gram: {to_gram}grams")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid input")
        unit_screen.delete(0, END)

def met_to_cent():
    try:
        var = float(unit_screen.get())
        to_meter = var * 1000
        to_cent = var / 1000
        calculated_result.config(text=f"Kilogram: {to_meter} Meter _____ Gram: {to_cent} centimeter")

    except ValueError:
        messagebox.showerror("Error", "Please enter the valid entry")
        unit_screen.delete(0, END)

def areaOfCircle():
    try:
        var = float(unit_screen.get())
        to_circlArea = (math.pi * (var**2))
        calculated_result.config(text=f"Area of circle is as {to_circlArea}")

    except ValueError:
        messagebox.showerror("Error", "Please enter the valid entry")
        unit_screen.delete(0, END)

def celciusToKelvin():
    try: 
        var = float(unit_screen.get())
        to_celcius = var + 273.15
        to_kelvin = var - 199
        calculated_result.config(text=f"Celcius: {to_celcius}C \n Kelvin: {to_kelvin}K")

    except ValueError:
        messagebox.showerror("Error", "Please enter the valid entry")
        unit_screen.delete(0, END)

def farenheitToKelvin():
    try:
        var = float(unit_screen.get())
        to_kelvin = ((var - 32)/1.8) + 273.15
        to_fht_cel = (var + 273.15)
        to_fht = (1.8 * to_fht_cel) + 32
        calculated_result.config(text=f"Celcius: {to_kelvin}K \n Kelvin: {to_fht}F")

    except ValueError:
        messagebox.showerror("Error", "Please enter the valid entry")
        unit_screen.delete(0, END)

def farenheitToCelcius():
    try:
        var = float(unit_screen.get())
        to_fht = (1.8 * var) + 32
        to_celcius = (var - 32)/1.8
        calculated_result.config(text=f"Farenheit: {to_fht}F \n Celcius: {to_celcius}C")

    except ValueError:
        messagebox.showerror("Error", "Please enter the valid entry")
        unit_screen.delete(0, END)

head = Label(root, text="Welcome To Python Unit Converter", fg="purple", bg="white", font=head_font, padx=10, pady=10, anchor='center', justify='center')
head.pack()

button_frame = Frame(root)
button_frame.pack(pady=10)

kg_btn = Button(button_frame, padx=10, pady=5, fg='black', bg='purple', font=btn_font, text="Kilogram ⇌ Gram", command=kg_to_g)
kg_btn.pack(side="left", padx=5, pady=5)

cent_btn = Button(button_frame, padx=10, pady=5, fg='purple', bg='black', font=btn_font, text="Meter ⇌ Centimeter", command=met_to_cent)
cent_btn.pack(side="left", padx=5, pady=5)

circle = Button(button_frame, fg="black", bg="yellow", padx=10, pady=5, text="Area of circle", font=body_font, command=areaOfCircle)
circle.pack(side="left", padx=5, pady=10)

cel_to_kel = Button(button_frame, fg="red", bg="blue", padx=10, pady=5, text="Celcius ⇌ Kelvin", font=body_font, command=celciusToKelvin)
cel_to_kel.pack(side="left", padx=5, pady=10)

far_to_kel = Button(button_frame, fg="white", bg="brown", padx=10, pady=5, text="Farenheit ⇌ Kelvin", font=body_font, command=farenheitToKelvin)
far_to_kel.pack(side="left", padx=5, pady=10)

far_to_cel = Button(button_frame, fg="white", bg="pink", padx=10, pady=5, text="Farenheit ⇌ Celcius", font=body_font, command=farenheitToCelcius)
far_to_cel.pack(side="left", padx=5, pady=10)

unit_screen = Entry(root, width=100, bg='grey', fg='black', font=body_font, bd=4, borderwidth=2)
unit_screen.pack(padx=5, pady=10)

calculated_result = Label(root, text="", font=body_font, fg="purple", padx=10)
calculated_result.pack()

root.mainloop()
