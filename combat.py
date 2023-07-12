import tkinter as tk
import math


# Function to calculate combat level
def calculate_combat_level():
    attack = int(attack_spin.get())
    strength = int(strength_spin.get())
    defence = int(defence_spin.get())
    hitpoints = int(hitpoints_spin.get())
    prayer = int(prayer_spin.get())
    ranged = int(ranged_spin.get())
    magic = int(magic_spin.get())

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

    result_label.config(text=f"Projected Combat Level: {format(combat_level, '.2f')}")


# Setup GUI
root = tk.Tk()
root.title("OSRS Combat Level Calculator")
root.minsize(400, 500)  # Set minimum window size

# Create spinboxes for each skill level
attack_spin = tk.Spinbox(root, from_=1, to=99)
strength_spin = tk.Spinbox(root, from_=1, to=99)
defence_spin = tk.Spinbox(root, from_=1, to=99)
hitpoints_spin = tk.Spinbox(root, from_=10, to=99)
prayer_spin = tk.Spinbox(root, from_=1, to=99)
ranged_spin = tk.Spinbox(root, from_=1, to=99)
magic_spin = tk.Spinbox(root, from_=1, to=99)

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

# Create calculate button
tk.Button(root, text="Calculate Combat Level", command=calculate_combat_level).pack()

# Label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the GUI
root.mainloop()
