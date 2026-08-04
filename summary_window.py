import tkinter as tk
from inventory_manager import inventory

def open_summary_window(window):

    summary_window = tk.Toplevel(window)
    summary_window.title("Inventory Summary")
    summary_window.geometry("350x250")
    summary_window.configure(bg="#FFF0F5")

    title = tk.Label(
        summary_window,
        text="💸 Inventory Summary",
        font=("Comic Sans MS",16,"bold"),
        fg="deeppink",
        bg="#FFF0F5"
    )
    title.pack(pady=15)

    total_products = len(inventory.products)

    total_stock = 0
    total_value = 0

    for item in inventory.products:
        total_stock += item.stock
        total_value += item.stock * item.price

    summary = tk.Label(
        summary_window,
        text=f"""Total Products : {total_products}

Total Stock : {total_stock}

Inventory Value : Rs. {total_value:.2f}
""",
        font=("Comic Sans MS",12),
        fg="deeppink",
        bg="#FFF0F5",
        justify="left"
    )

    summary.pack(pady=20)