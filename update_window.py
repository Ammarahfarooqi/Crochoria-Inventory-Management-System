import tkinter as tk
from inventory_manager import inventory

def open_update_window(window):
    update_window = tk.Toplevel(window)
    update_window.title("Update Product")
    update_window.geometry("400x420")
    update_window.configure(bg="#FFF7D1")
    title = tk.Label(
        update_window,
        text="𓂃🖋 Update Product",
        font=("Tiny5",18,"bold"),
        fg="#ED589B",
        bg="#FFF7D1"
    )

    title.pack(pady=10)

    form_frame = tk.Frame(
        update_window,
        bg="#FFECC8"
    )
    
    form_frame.pack(pady=10)

    id_label = tk.Label(
        form_frame,
        text="Product ID",
        bg="#FFECC8",
        fg="#ED589B",
        font=("Tiny5", 11)
    )
    id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    
    id_entry = tk.Entry(
        form_frame,
        width=25,
        font=("Tiny5",11)
    )
    id_entry.grid(row=0, column=1, padx=10, pady=5)
    
    price_label = tk.Label(
        form_frame,
        text="Price",
        bg="#FFECC8",
        fg="#ED589B",
        font=("Tiny5", 11)
    )
    price_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    
    price_entry = tk.Entry(
        form_frame,
        width=25,
        font=("Tiny5",11)
    )
    price_entry.grid(row=3, column=1, padx=10, pady=5)
    
    stock_label = tk.Label(
        form_frame,
        text="Stock",
        bg="#FFECC8",
        fg="#ED589B",
        font=("Tiny5", 11)
    )
    stock_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    
    stock_entry = tk.Entry(
        form_frame,
        width=25,
        font=("Tiny5",11)
    )
    stock_entry.grid(row=4, column=1, padx=10, pady=5)

    result_label = tk.Label(
        update_window,
        text="",
        bg="#FFF7D1",
        fg="#ED589B",
        font=("Tiny5",11)
    )

    result_label.pack()

    def load_product(event=None):
        try:
            product_id = int(id_entry.get())
        except ValueError:
            result_label.config(text="Please enter a valid Product ID.", fg="red")
            return

        product = inventory.find_product_by_id(product_id)

        if product:
            price_entry.delete(0, "end")
            stock_entry.delete(0, "end")

            price_entry.insert(0, str(product.price))
            stock_entry.insert(0, str(product.stock))

            result_label.config(text="✅ Product found", fg="green")
            price_entry.focus()

        else:
            result_label.config(text="❌ Product not found", fg="red")
            id_entry.focus()

    def update_product():
        try:
            product_id = int(id_entry.get())
            price = float(price_entry.get())
            stock = int(stock_entry.get())

        except ValueError:
            result_label.config(text="Please enter valid values.", fg="red")
            return

        if inventory.update_product_by_id(product_id, price, stock):
            inventory.save_products()

            result_label.config(
                text="✅ Product updated successfully!",
                fg="green"
            )

            update_window.after(1000, update_window.destroy)

        else:
            result_label.config(
                text="❌ Product not found.",
                fg="red"
            )

    update_button = tk.Button(
        update_window,
        text="🌸 Update Product",
        command=update_product,
        font=("Tiny5", 11, "bold"),
        bg="#FFECC8",
        fg="#ED589B",
        cursor="hand2"
    )

    update_button.pack(pady=10)
    id_entry.bind("<Return>", load_product)
    price_entry.bind("<Return>", lambda event: stock_entry.focus())
    stock_entry.bind("<Return>", lambda event: update_product())
    id_entry.focus()
        