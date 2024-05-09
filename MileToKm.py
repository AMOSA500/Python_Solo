from tkinter import *


def mileToKmCal():
    try:
        mile = float(mile_entry.get())
    except ValueError:
        km.config(text="Invalid Input")
    result = round(mile * 1.609)
    km.config(text=f"{result}")

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)



mile_entry = Entry()
mile_entry.grid(row=0, column=1)

mile_label = Label(text="mile")
mile_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

km = Label(text="0")
km.grid(row=1, column=1)

km_lable = Label(text="km")
km_lable.grid(row=1, column=2)

calculate_btn = Button(text="calculate", command=mileToKmCal, width=17, background="red", font=("Arial", 12, "bold"))
calculate_btn.grid(row=2, column=1)


window.mainloop()
