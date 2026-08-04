import tkinter as tk
from inventory_manager import inventory
def open_delete_window(window):
    delete_window = tk.Toplevel(window)
    delete_window.title("Delete Product")
    delete_window.geometry("400x250")
    delete_window.configure(bg="#FFF0F5")   
    title = tk.Label(
        delete_window,
        text="➖ Delete Product",
        font=("Comic Sans MS",16,"bold"),
        fg="deeppink",
        bg="#FFF0F5"
    )
    title.pack(pady=10)
    id_label = tk.Label(
        delete_window,
        text="Enter Product ID",
        font=("Comic Sans MS",11),
        bg="#FFF0F5",
        fg="deeppink"
    )
    id_label.pack()
    id_entry = tk.Entry(
        delete_window,
        width=25,
        font=("Comic Sans MS",11)
    )

    id_entry.pack(pady=5)
    result_label = tk.Label(
        delete_window,
        text="",
        bg="#FFF0F5",
        fg="deeppink",
        font=("Comic Sans MS",11)
    )

    result_label.pack(pady=10)

    def delete_product():

        try:
            product_id = int(id_entry.get())

        except ValueError:
            result_label.config(text="Please enter a valid Product ID.")
            return

        if inventory.delete_product_by_id(product_id):

            inventory.save_products()

            result_label.config(text="Product deleted successfully!")

        else:

            result_label.config(text="Product not found.")

    delete_button = tk.Button(
        delete_window,
        text="🗑 Delete",
        command=delete_product,
        font=("Comic Sans MS",11,"bold"),
        bg="white",
        fg="deeppink",
        cursor="hand2"
    )

    delete_button.pack(pady=10)
    id_entry.bind("<Return>", lambda event: delete_product())