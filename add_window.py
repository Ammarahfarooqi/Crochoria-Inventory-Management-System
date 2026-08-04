import tkinter as tk
from product import Product
from inventory_manager import inventory

def open_add_window(window):
    add_window = tk.Toplevel(window)
    add_window.title("➕Add Product")
    add_window.geometry("400x420")
    add_window.configure(bg="#FFF0F5")
    title = tk.Label(
    add_window,
    text="➕ Add Product",
    font=("Comic Sans MS", 16, "bold"),
    fg="deeppink",
    bg="#FFF0F5"
)
    title.pack(pady=10)

    form_frame = tk.Frame(
    add_window,
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

    name_label = tk.Label(
    form_frame,
    text="Product Name",
    bg="#FFF0F5",
    fg="deeppink",
    font=("Comic Sans MS", 11)
)
    name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    name_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Comic Sans MS",11)
)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    category_label = tk.Label(
    form_frame,
    text="Category",
    bg="#FFF0F5",
    fg="deeppink",
    font=("Comic Sans MS", 11)
)
    category_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    category_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Comic Sans MS",11)
)
    category_entry.grid(row=2, column=1, padx=10, pady=5)

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

    def save_product():
        try:
            product_id = int(id_entry.get())
            name = name_entry.get()
            category = category_entry.get()
            price = float(price_entry.get())
            stock = int(stock_entry.get())

        except ValueError:
            message_label.config(
                text="❌ Invalid input!",
                fg="red"
            )
            return

        if name.strip() == "" or category.strip() == "":
            message_label.config(
                text="❌ Name and Category cannot be empty!",
                fg="red"
            )
            return

        if price < 0 or stock < 0:
            message_label.config(
                text="❌ Price/Stock cannot be negative!",
                fg="red"
            )
            return

        if inventory.id_exists(product_id):
            message_label.config(
                text="❌ Product ID already exists!",
                fg="red"
            )
            id_entry.focus()
            return

        product = Product(product_id,name,category,price,stock)
        if inventory.add_product(product):
            inventory.save_products()
            add_window.destroy()

        
    add_product_button = tk.Button(
        add_window,
        text="🌸 Save Product",
        command=save_product,
        font=("Comic Sans MS", 11, "bold"),
        bg="white",
        fg="deeppink",
        cursor="hand2"
    )

    add_product_button.pack(pady=15)

    def check_id(event=None):
        try:
            product_id = int(id_entry.get())
        except ValueError:
            message_label.config(
                text="Enter a valid ID",
                fg="red"
            )
            return

        if inventory.id_exists(product_id):
            message_label.config(
                text="❌ Product ID already exists!",
                fg="red"
            )
            id_entry.focus()
        else:
            message_label.config(
                text="✅ ID Available",
                fg="green"
            )
            name_entry.focus()

    message_label = tk.Label(
        form_frame,
        text="",
        bg="#FFF0F5",
        font=("Comic Sans MS",10,"bold")
    )

    message_label.grid(row=5,column=0,columnspan=2)

    id_entry.bind("<Return>", check_id)

    id_entry.focus()
    name_entry.bind("<Return>", lambda event: category_entry.focus())
    category_entry.bind("<Return>", lambda event: price_entry.focus())
    price_entry.bind("<Return>", lambda event: stock_entry.focus())
    stock_entry.bind("<Return>", lambda event: save_product())
