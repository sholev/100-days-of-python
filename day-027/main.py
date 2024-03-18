from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
label = Label(text="Tkinter Label", font=("Arial", 24, "bold"))
# label.pack(side="left")
label.grid(row=0, column=0)
label["text"] += " More Text"
label.config(text=label["text"] + " 1")


def button_press():  # Button:
    counter = int(label["text"].split()[-1]) + 1
    label["text"] = f"{entry.get()} {counter}"


button = Button(text="Press me", command=button_press)
button.grid(row=1, column=1)

button2 = Button(text="Button 2")
button2.grid(row=0, column=2)
button2.config(padx=50, pady=50)

# Entry:
entry = Entry(width=5)
entry.grid(row=2, column=3)
entry.get()


window.mainloop()
