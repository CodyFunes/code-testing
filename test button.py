import tkinter as tk

def register_input():
    # Get the value from the entry widget
    value = entry.get()

    # Do something with the value (e.g., print it)
    print("Registered value:", value)

# Create the main window
window = tk.Tk()

# Create an entry widget
entry = tk.Entry(window)
entry.pack()

# Create a button that registers the input when clicked
button = tk.Button(window, text="Register", command=register_input)
button.pack()

# Start the main loop
window.mainloop()