
import tkinter as tk
import math
import random
import winsound
import threading
from tkinter import messagebox
from pathlib import Path


root = tk.Tk()
root.title("Horror Demo - Harmless Simulation")
root.geometry("560x430")
root.resizable(False, False)
root.configure(bg="#101010")

# Center window
root.update_idletasks()
x = (root.winfo_screenwidth() - 560) // 2
y = (root.winfo_screenheight() - 430) // 2
root.geometry(f"+{x}+{y}")

# Animation canvas
canvas = tk.Canvas(
    root,
    width=560,
    height=235,
    bg="#101010",
    highlightthickness=0
)
canvas.pack()

skull = canvas.create_text(
    280, 115,
    text="☠",
    font=("Segoe UI Symbol", 115),
    fill="#eeeeee"
)

title = tk.Label(
    root,
    text="UNKNOWN ENTITY",
    font=("Arial", 23, "bold"),
    fg="#ff3030",
    bg="#101010"
)
title.pack(pady=5)

subtitle = tk.Label(
    root,
    text="THIS IS A HARMLESS HORROR SIMULATION",
    font=("Arial", 10, "bold"),
    fg="#aaaaaa",
    bg="#101010"
)
subtitle.pack(pady=5)

status = tk.Label(
    root,
    text="Your computer is safe. This is only a demo.",
    font=("Arial", 10),
    fg="white",
    bg="#101010"
)
status.pack(pady=8)

def animate():
    animate.phase += 0.12

    offset = math.sin(animate.phase) * 12
    angle_color = (
        "#ff2222"
        if math.sin(animate.phase * 2) > 0
        else "#eeeeee"
    )

    canvas.coords(skull, 280, 115 + offset)
    canvas.itemconfig(skull, fill=angle_color)

    root.after(35, animate)

animate.phase = 0

def play_laugh():
    sound = Path(__file__).with_name("evil-laugh.wav")

    if not sound.exists():
        messagebox.showinfo("Sound missing", "evil-laugh.wav dosyasını main.py yanına koy.")
        return

    winsound.PlaySound(
        str(sound),
        winsound.SND_FILENAME | winsound.SND_ASYNC
    )

def close_demo():
    winsound.PlaySound(None, winsound.SND_ASYNC)
    root.destroy()

buttons = tk.Frame(root, bg="#101010")
buttons.pack(pady=15)

tk.Button(
    buttons,
    text="PLAY EVIL LAUGH",
    command=play_laugh,
    bg="#990000",
    fg="white",
    activebackground="#cc0000",
    font=("Arial", 10, "bold"),
    width=18,
    relief="flat"
).pack(side="left", padx=8)

tk.Button(
    buttons,
    text="CLOSE DEMO",
    command=close_demo,
    bg="#333333",
    fg="white",
    font=("Arial", 10, "bold"),
    width=15,
    relief="flat"
).pack(side="left", padx=8)

root.protocol("WM_DELETE_WINDOW", close_demo)

animate()
root.mainloop()
