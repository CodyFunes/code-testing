import tkinter as tk

window = tk.Tk()
window.title("The Knight in shining armor")

window.configure(bg="lightblue")
label = tk.Label(window, text="Enter Hero's Name", fg="black", bg="lightblue")
label.pack()


def hero_name():

    user_input = entry.get()
    window.tk(print("user entered:", user_input))


#label = tk.Label(window, text="enter name")
#label.pack()


entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="continue", command=hero_name)
button.pack()



window.mainloop()
