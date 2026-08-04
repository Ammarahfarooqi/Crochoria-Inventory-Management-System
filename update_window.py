import tkinter as tk
from inventory_manager import inventory

def open_update_window(window):
    update_window = tk.Toplevel(window)
    update_window.title("Update Product")
    update_window.geometry("400x420")
    update_window.configure(bg="#FFF0F5")
    title = tk.Label(
        update_window,
        text="✏ Update Product",
        font=("Comic Sans MS",16,"bold"),
        fg="deeppink",
        bg="#FFF0F5"
    )

    title.pack(pady=10)

    form_frame = tk.Frame(
        update_window,
        bg="#FFF0F5"
    )
    
    form_frame.pack(pady=10)

    id_label = tk.Label(
        form_frame,
        text="Product ID",
        bg="#FFF0F5",
        fg="deeppink",
        font=("Comic Sans MS", 11)
    )
    id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    
    id_entry = tk.Entry(
        form_frame,
        width=25,
        font=("Comic Sans MS",11)
    )
    id_entry.grid(row=0, column=1, padx=10, pady=5)
    
    price_label = tk.Label(
        form_frame,
        text="Price",
        bg="#FFF0F5",
        fg="deeppink",
        font=("Comic Sans MS", 11)
    )
    price_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    
    price_entry = tk.Entry(
        form_frame,
        width=25,
        font=("Comic Sans MS",11)
    )
    price_entry.grid(row=3, column=1, padx=10, pady=5)
    
    stock_label = tk.Label(
        form_frame,
        text="Stock",
        bg="#FFF0F5",
        fg="deeppink",
        font=("Comic Sans MS", 11)
    )
    stock_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    
    stock_entry = tk.Entry(
        form_frame,
        width=25,
        font=("Comic Sans MS",11)
    )
    stock_entry.grid(row=4, column=1, padx=10, pady=5)

    result_label = tk.Label(
        update_window,
        text="",
        bg="#FFF0F5",
        fg="deeppink",
        font=("Comic Sans MS",11)
    )

    result_label.pack()

    def update_product():
        try:
            product_id = int(id_entry.get())
            price = float(price_entry.get())
            stock = int(stock_entry.get())

        except ValueError:
            result_label.config(text="Please enter valid values.")
            return

        if inventory.update_product_by_id(product_id, price, stock):
            inventory.save_products()
            result_label.config(text="Product updated successfully!")

        else:
            result_label.config(text="Product not found.")

    update_button = tk.Button(
        update_window,
        text="🌸 Update Product",
        command=update_product,
        font=("Comic Sans MS", 11, "bold"),
        bg="white",
        fg="deeppink",
        cursor="hand2"
    )

    update_button.pack(pady=10)
    id_entry.bind("<Return>", lambda event: update_product())
    id_entry.focus()
    