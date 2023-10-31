from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(150, 150)
window.config(padx=50, pady=50)


def button_clicked():
    miles = input.get()
    km = float(miles) * 1.609
    result["text"] = round(km, 3)


input = Entry(width=10)
input.insert(END, string=0)
input.grid(column=1, row=1)

label1 = Label(text="Miles")
label1.grid(column=2, row=1)

label2 = Label(text="is equal to ")
label2.grid(column=0, row=2)

result = Label(text=0)
result.grid(column=1, row=2)

label3 = Label(text="Km")
label3.grid(column=2, row=2)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

window.mainloop()
