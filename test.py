import tkinter as tk
import math
from tkinter import messagebox

# Function to calculate combat level
def calculate_combat_level(*args):
    try:
        attack = int(attack_var.get())
        strength = int(strength_var.get())
        defence = int(defence_var.get())
        hitpoints = int(hitpoints_var.get())
        prayer = int(prayer_var.get())
        ranged = int(ranged_var.get())
        magic = int(magic_var.get())

        base = 0.25 * (defence + hitpoints + math.floor(prayer / 2))
        melee = 0.325 * (attack + strength)
        ranged = 0.325 * (math.floor(ranged/2) + ranged)
        magic = 0.325 * (math.floor(magic/2) + magic)

        if melee >= ranged and melee >= magic:
            combat_level = base + melee
        elif ranged >= melee and ranged >= magic:
            combat_level = base + ranged
        else:
            combat_level = base + magic

        result_label.config(text=f"Projected Combat Level: {round(combat_level, 2)}")
    except ValueError: # Ignore when the Spinboxes are empty or not valid integers
        pass

# Display help instructions
def show_help():
    messagebox.showinfo("Instructions", "Enter your current skill levels in the provided fields to calculate your projected combat level.")

# Setup GUI
root = tk.Tk()
root.title("OSRS Combat Level Calculator")
root.minsize(400, 500)  # Set minimum window size

# Create StringVars for each skill level and trace them
attack_var = tk.StringVar(root)
strength_var = tk.StringVar(root)
defence_var = tk.StringVar(root)
hitpoints_var = tk.StringVar(root)
prayer_var = tk.StringVar(root)
ranged_var = tk.StringVar(root)
magic_var = tk.StringVar(root)

# Create spinboxes for each skill level, using the StringVars
attack_spin = tk.Spinbox(root, from_=1, to=99, textvariable=attack_var)
strength_spin = tk.Spinbox(root, from_=1, to=99, textvariable=strength_var)
defence_spin = tk.Spinbox(root, from_=1, to=99, textvariable=defence_var)
hitpoints_spin = tk.Spinbox(root, from_=10, to=99, textvariable=hitpoints_var)
prayer_spin = tk.Spinbox(root, from_=1, to=99, textvariable=prayer_var)
ranged_spin = tk.Spinbox(root, from_=1, to=99, textvariable=ranged_var)
magic_spin = tk.Spinbox(root, from_=1, to=99, textvariable=magic_var)

# Pack spinboxes with their corresponding labels
tk.Label(root, text="Attack Level:").pack()
attack_spin.pack()
tk.Label(root, text="Strength Level:").pack()
strength_spin.pack()
tk.Label(root, text="Defence Level:").pack()
defence_spin.pack()
tk.Label(root, text="Hitpoints Level:").pack()
hitpoints_spin.pack()
tk.Label(root, text="Prayer Level:").pack()
prayer_spin.pack()
tk.Label(root, text="Ranged Level:").pack()
ranged_spin.pack()
tk.Label(root, text="Magic Level:").pack()
magic_spin.pack()

# Label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Button to show instructions
help_button = tk.Button(root, text="Help", command=show_help)
help_button.pack()

# Trace variables
attack_var.trace("w", calculate_combat_level)
strength_var.trace("w", calculate_combat_level)
defence_var.trace("w", calculate_combat_level)
hitpoints_var.trace("w", calculate_combat_level)
prayer_var.trace("w", calculate_combat_level)
ranged_var.trace("w", calculate_combat_level)
magic_var.trace("w", calculate_combat_level)

# Run the GUI
root.mainloop()
