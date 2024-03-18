from tkinter import *


window = Tk()
window.title("Mile to km converter")
window.config(padx=30, pady=30)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=3)
is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)
result_label = Label(text="0")
result_label.grid(row=1, column=1)
km_label = Label(text="km")
km_label.grid(row=1, column=2)
mile_entry = Entry(width=10)
mile_entry.grid(row=0, column=1)


def calculate():
    result_label["text"] = str(float(mile_entry.get()) * 1.60934)


calculate_button = Button(text="calculate", command=calculate)
calculate_button.grid(row=3, column=1)

window.mainloop()
