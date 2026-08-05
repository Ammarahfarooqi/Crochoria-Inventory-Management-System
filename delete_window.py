import tkinter as tk
from inventory_manager import inventory


def open_delete_window(window):
    delete_window = tk.Toplevel(window)
    delete_window.title("Delete Product")
    delete_window.geometry("400x420")
    delete_window.configure(bg="#FFF7D1")   
    title = tk.Label(
        delete_window,
        text="➖ Delete Product",
        font=("Tiny5",16,"bold"),
        fg="#ED589B",
        bg="#FFF7D1"
    )
    title.pack(pady=10)
    id_label = tk.Label(
        delete_window,
        text="Enter Product ID",
        font=("Tiny5",11),
        bg="#FFECC8",
        fg="#ED589B"
    )
    id_label.pack()
    id_entry = tk.Entry(
        delete_window,
        width=25,
        font=("Tiny5",11)
    )

    id_entry.pack(pady=5)
    result_label = tk.Label(
        delete_window,
        text="",
        bg="#FFF7D1",
        fg="#ED589B",
        font=("Tiny5",11)
    )

    result_label.pack(pady=10)

    info_label = tk.Label(
        delete_window,
        text="",
        bg="#FFF7D1",
        fg="#ED589B",
        font=("Tiny5",11),
        justify="left"
    )

    yes_button = tk.Button(
        delete_window,
        text="✔ Yes",
        font=("Tiny5",13,"bold"),
        bg="#FFECC8",
        fg="#ED589B",
        cursor="hand2"
    )

    no_button = tk.Button(
        delete_window,
        text="✖ No",
        font=("Tiny5",13,"bold"),
        bg="#FFECC8",
        fg="#ED589B",
        cursor="hand2"
    )

    def delete_product():
        try:
            product_id = int(id_entry.get())
        except ValueError:
            result_label.config(text="❌ Please enter a valid Product ID.")
            return

        product = inventory.find_product_by_id(product_id)

        if not product:
            result_label.config(text="❌ Product not found.")
            info_label.pack_forget()
            yes_button.pack_forget()
            no_button.pack_forget()
            return

        result_label.config(text="")

        info_label.config(
            text=f"""Delete this product?

    ID: {product.prod_id}
    Name: {product.name}"""
        )

        info_label.pack(pady=5)

        def confirm_delete():
            inventory.delete_product_by_id(product_id)
            inventory.save_products()

            info_label.config(text="✅ Product deleted successfully!")
            delete_window.after(1000, delete_window.destroy)
            yes_button.pack_forget()
            no_button.pack_forget()

        def cancel_delete():
            info_label.config(text="Deletion cancelled.")
            delete_window.after(1000, delete_window.destroy)
            yes_button.pack_forget()
            no_button.pack_forget()

        yes_button.config(command=confirm_delete)
        no_button.config(command=cancel_delete)

        yes_button.pack(side="left", padx=60, pady=10)
        no_button.pack(side="right", padx=60, pady=10)

    delete_button = tk.Button(
        delete_window,
        text="🗑 Delete",
        command=delete_product,
        font=("Tiny5",11,"bold"),
        bg="#FFECC8",
        fg="#ED589B",
        cursor="hand2"
    )

    delete_button.pack(pady=10)
    id_entry.focus()

    id_entry.bind("<Return>", lambda event: delete_product())

