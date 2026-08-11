import tkinter as tk
from inventory_manager import inventory

def open_display_window(window):
    display_window = tk.Toplevel(window)
    display_window.title("Display Products")
    display_window.geometry("600x400")
    display_window.configure(bg="#FFF7D1")

    title = tk.Label(
        display_window,
        text="♡ Here You Go Cutie ♡",
        font=("Tiny5",21,"bold"),
        fg="#ED589B",
        bg="#FFF7D1"
    )

    title.pack(pady=10)
    text_box = tk.Text(
        display_window,
        width=60,
        height=15,
        font=("Special Elite",13),
        bg="#FFECC8",
        fg="#DD6FA1"
    )

    text_box.pack(pady=10)
    
    products = inventory.get_products()

    if len(products) == 0:
        text_box.insert("end", "No products available.")
    else:
        for item in products:
            inventory.products.sort(key=lambda x: x.prod_id)
            text_box.insert(
                "end",
                f"ID : {item.prod_id}\n"
                f"Name : {item.name}\n"
                f"Category : {item.category}\n"
                f"Price : {item.price}\n"
                f"Stock : {item.stock}\n"
                "-------------------------\n\n"
            )