import tkinter as tk
from inventory_manager import inventory

def open_search_window(window):
    search_window = tk.Toplevel(window)
    search_window.title("Search Product")
    search_window.geometry("400x420")
    search_window.configure(bg="#FFF0F5")

    title = tk.Label(
    search_window,
    text="🔍 Search Product",
    font=("Comic Sans MS",16,"bold"),
    fg="deeppink",
    bg="#FFF0F5"
)
    title.pack(pady=10)
    id_label = tk.Label(
    search_window,
    text="Enter Product ID",
    bg="#FFF0F5",
    fg="deeppink",
    font=("Comic Sans MS",11)
)
    id_label.pack()
    id_entry = tk.Entry(
    search_window,
    width=25,
    font=("Comic Sans MS",11)
)
    id_entry.pack(pady=5)
    result_box = tk.Text(
    search_window,
    width=40,
    height=8,
    font=("Comic Sans MS",10)
)
    result_box.pack(pady=10)

    def search_product():
        try:
            product_id = int(id_entry.get())
        except ValueError:
            result_box.delete("1.0", "end")
            result_box.insert("end", "Please enter a valid Product ID.")
            return

        product = inventory.find_product_by_id(product_id)

        result_box.delete("1.0", "end")

        if product:
            result_box.insert(
                "end",
                f"ID: {product.prod_id}\n"
                f"Name: {product.name}\n"
                f"Category: {product.category}\n"
                f"Price: {product.price}\n"
                f"Stock: {product.stock}"
            )
        else:
            result_box.insert("end", "Product not found.")

    search_button = tk.Button(
        search_window,
        text="🔍 Search",
        command=search_product,
        font=("Comic Sans MS", 11, "bold"),
        bg="white",
        fg="deeppink",
        cursor="hand2"
    )

    search_button.pack(pady=10)
    id_entry.bind("<Return>", lambda event: search_product())
    id_entry.focus()