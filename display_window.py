import tkinter as tk
from inventory_manager import inventory

def open_display_window(window):
    display_window = tk.Toplevel(window)
    display_window.title("Display Products")
    display_window.geometry("600x400")
    display_window.configure(bg="#FFF0F5")

    title = tk.Label(
        display_window,
        text="🌸 Products 🌸",
        font=("Comic Sans MS",16,"bold"),
        fg="deeppink",
        bg="#FFF0F5"
    )

    title.pack(pady=10)
    text_box = tk.Text(
        display_window,
        width=60,
        height=15,
        font=("Comic Sans MS",10)
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
                f"ID: {item.prod_id}\n"
                f"Name: {item.name}\n"
                f"Category: {item.category}\n"
                f"Price: {item.price}\n"
                f"Stock: {item.stock}\n"
                "-------------------------\n"
            )