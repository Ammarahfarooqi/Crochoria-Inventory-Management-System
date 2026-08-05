import tkinter as tk
from inventory_manager import inventory

def open_summary_window(window):

    summary_window = tk.Toplevel(window)
    summary_window.title("Inventory Summary")
    summary_window.geometry("420x420")
    summary_window.configure(bg="#FFF7D1")

    title = tk.Label(
        summary_window,
        text="🤑 Inventory Summary",
        font=("Tiny5",20,"bold"),
        fg="#ED589B",
        bg="#FFF7D1"
    )
    title.pack(pady=15)

    total_products = len(inventory.products)

    total_stock = 0
    total_value = 0

    for item in inventory.products:
        total_stock += item.stock
        total_value += item.stock * item.price

    card_style = {
        "bg": "#FFECC8",
        "bd": 3,
        "relief": "groove",
        "width": 28,
        "height": 4
    }

    # Card 1
    card1 = tk.Frame(summary_window, **card_style)
    card1.pack(pady=8)

    tk.Label(
        card1,
        text="📦 Total Products",
        font=("Special Elite",13,"bold"),
        fg="#DD6FA1",
        bg="#FFECC8"
    ).pack()

    tk.Label(
        card1,
        text=total_products,
        font=("Special Elite",16,"bold"),
        bg="#FFECC8",
        fg="#834112"
    ).pack()

    # Card 2
    card2 = tk.Frame(summary_window, **card_style)
    card2.pack(pady=8)

    tk.Label(
        card2,
        text="📦 Total Stock",
        font=("Special Elite",13,"bold"),
        fg="#DD6FA1",
        bg="#FFECC8"
    ).pack()

    tk.Label(
        card2,
        text=total_stock,
        font=("Special Elite",16,"bold"),
        bg="#FFECC8",
        fg="#834112"
    ).pack()

    # Card 3
    card3 = tk.Frame(summary_window, **card_style)
    card3.pack(pady=8)

    tk.Label(
        card3,
        text="💲Inventory Value",
        font=("Special Elite",13,"bold"),
        fg="#DD6FA1",
        bg="#FFECC8"
    ).pack()

    tk.Label(
        card3,
        text=f"Rs. {total_value:.2f}",
        font=("Special Elite",16,"bold"),
        bg="#FFECC8",
        fg="#834112"
    ).pack()