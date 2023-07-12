import tkinter as tk
import math


# function to calculate combat level
def calculate_combat_level():
    attack = int(attack_entry.get())
    strength = int(strength_entry.get())
    defence = int(defence_entry.get())
    hitpoints = int(hitpoints_entry.get())
    prayer = int(prayer_entry.get())
    ranged = int(ranged_entry.get())
    magic = int(magic_entry.get())

    base = 0.25 * (defence + hitpoints + math.floor(prayer / 2))

    melee = 0.325 * (attack + strength)
    ranged = 0.325 * ranged
    magic = 0.325 * magic

    if melee >= ranged and melee >= magic:
        combat_level = base + melee
    elif ranged >= melee and ranged >= magic:
        combat_level = base + ranged
    else:
        combat_level = base + magic

    result_label.config(text=f"Projected Combat Level: {combat_level}")


# setup GUI
root = tk.Tk()
root.title("OSRS Combat Level Calculator")

# create entry fields and labels
attack_entry = tk.Entry(root)
strength_entry = tk.Entry(root)
defence_entry = tk.Entry(root)
hitpoints_entry = tk.Entry(root)
prayer_entry = tk.Entry(root)
ranged_entry = tk.Entry(root)
magic_entry = tk.Entry(root)

tk.Label(root, text="Attack Level:").pack()
attack_entry.pack()
tk.Label(root, text="Strength Level:").pack()
strength_entry.pack()
tk.Label(root, text="Defence Level:").pack()
defence_entry.pack()
tk.Label(root, text="Hitpoints Level:").pack()
hitpoints_entry.pack()
tk.Label(root, text="Prayer Level:").pack()
prayer_entry.pack()
tk.Label(root, text="Ranged Level:").pack()
ranged_entry.pack()
tk.Label(root, text="Magic Level:").pack()
magic_entry.pack()

# create calculate button
tk.Button(root, text="Calculate Combat Level", command=calculate_combat_level).pack()

# label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# run the GUI
root.mainloop()
