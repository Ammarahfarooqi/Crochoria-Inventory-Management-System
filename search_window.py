import tkinter as tk
from inventory_manager import inventory

def open_search_window(window):
    search_window = tk.Toplevel(window)
    search_window.title("Search Product")
    search_window.geometry("400x420")
    search_window.configure(bg="#FFF7D1")

    title = tk.Label(
    search_window,
    text="⌕ Search Product",
    font=("Tiny5",20,"bold"),
    fg="#ED589B",
    bg="#FFF7D1"
)
    title.pack(pady=10)
    
    search_type = tk.StringVar()
    search_type.set("ID")

    search_label = tk.Label(
        search_window,
        text="Enter Product ID",
        bg="#FFECC8",
        fg="#ED589B",
        font=("Tiny5",11)
        )
    search_label.pack()

    search_entry = tk.Entry(
        search_window,
        width=25,
        font=("Tiny5",11)
    )

    search_entry.pack(pady=5)

    result_box = tk.Text(
        search_window,
        width=40,
        height=8,
        font=("Special Elite",13),
        bg="#FFECC8",
        fg="#ED589B",
    )
    result_box.pack(pady=10)

    def change_label():
        search_entry.delete(0, "end")
        result_box.delete("1.0", "end")
        
        if search_type.get() == "ID":
            search_label.config(text="Enter Product ID")
        else:
            search_label.config(text="Enter Product Name")
    
    id_radio = tk.Radiobutton(
        search_window,
        text="Search by ID",
        variable=search_type,
        value="ID",
        bg="#FFECC8",
        command=change_label
        )
    
    name_radio = tk.Radiobutton(
        search_window,
        text="Search by Name",
        variable=search_type,
        value="Name",
        bg="#FFECC8",
        command=change_label
        )
    
    id_radio.pack()
    name_radio.pack()

    def search_product():
        result_box.delete("1.0","end")

        if search_type.get() == "ID":
            try:
                product = inventory.find_product_by_id(
                    int(search_entry.get())
                )

            except ValueError:
                result_box.insert("end","Please enter a valid Product ID.")
                return
        else:
            product = inventory.find_product_by_name(
                search_entry.get()
            )

        if product:
            result_box.insert(
                "end",
                f"ID : {product.prod_id}\n"
                f"Name : {product.name}\n"
                f"Category : {product.category}\n"
                f"Price : {product.price}\n"
                f"Stock : {product.stock}"
            )
        else:
            result_box.insert("end","Product not found.")

    search_button = tk.Button(
        search_window,
        text="⌕ Search",
        command=search_product,
        font=("Tiny5", 11, "bold"),
        bg="#FFECC8",
        fg="#ED589B",
        cursor="hand2"
    )

    search_button.pack(pady=10)
    search_entry.bind("<Return>", lambda event: search_product())
    search_entry.focus()    
