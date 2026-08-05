import tkinter as tk

def open_about_window(window):
    about = tk.Toplevel(window)
    about.title("About")
    about.geometry("400x420")
    about.configure(bg="#FFF7D1")

    tk.Label(
        about,
        text="✌㋡ About Diva",
        font=("Tiny5",18,"bold"),
        fg="#ED589B",
        bg="#FFF7D1"
    ).pack(pady=15)

    tk.Label(
        about,
        text="""
Developed By :

Ammarah Farooqi,

CSIT Student

Python + Tkinter Project

© 2026
""",
        font=("Special Elite",13),
        bg="#FFECC8",
        fg="#834112",
        justify="center"
    ).pack()

    tk.Button(
        about,
        text="Close",
        command=about.destroy,
        bg="#FFECC8",
        fg="#ED589B",
        font=("Special Elite",11,"bold"),
        cursor="hand2"
    ).pack(pady=20)
    