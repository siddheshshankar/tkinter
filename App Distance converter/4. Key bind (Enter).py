import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Distance Converter")

metres_value = tk.StringVar()
feet_value = tk.StringVar()

def calculate_feet(*args):
    try:
        metres = float(metres_value.get())
        feet = metres * 3.28084
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass


main = ttk.Frame(root, padding=(30, 15))
main.grid()

root.columnconfigure(0, weight=1)

# -- Widgets --

metres_label = ttk.Label(main, text="metres")
metres_input = ttk.Entry(main, width=10, textvariable=metres_value)
feet_label = ttk.Label(main, text="feet")
feet_display = ttk.Label(main, textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

# -- Layout --

metres_label.grid(column=0, row=0, sticky="W", padx=5, pady=5)
metres_input.grid(column=1, row=0, sticky="EW", padx=5, pady=5)
metres_input.focus()

feet_label.grid(column=0, row=1, sticky="W", padx=5, pady=5)
feet_display.grid(column=1, row=1, sticky="EW", padx=5, pady=5)

calc_button.grid(column=0, row=2, columnspan=2, sticky="EW", padx=5, pady=5)

root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)

root.mainloop()