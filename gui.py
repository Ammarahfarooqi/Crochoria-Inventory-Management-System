import tkinter as tk
from add_window import open_add_window
from display_window import open_display_window
from search_window import open_search_window
from delete_window import open_delete_window
from update_window import open_update_window
from summary_window import open_summary_window
from inventory_manager import inventory

window = tk.Tk()
window.title("Crochoria Inventory System")
window.geometry("600x400")
heading = tk.Label(
    window,
    text = "🌸 Crochoria Inventory System 🌸",
    font = ("Comic Sans MS",20,"bold"),
    fg = "deeppink",    
    bg="#FFF0F5")
heading.pack()

button_frame = tk.Frame(
    window,
    bg="#FFF0F5"
)
button_frame.pack(pady=20)

button_style = {
    "font": ("Comic Sans MS", 12, "bold"),
    "bg": "white",
    "fg": "deeppink",
    "width": 20,
    "cursor": "hand2",
    "relief": "raised"
}

#add product
add_button = tk.Button(
    button_frame,
    text="➕ Add Product",
    command=lambda: open_add_window(window),  
    **button_style
)
add_button.grid(row=0, column=0, padx=10, pady=10)

#Display Product
display_button = tk.Button(
    button_frame,
    text="👀 Display Products",
    command=lambda: open_display_window(window),
    **button_style
)
display_button.grid(row=0, column=1, padx=10, pady=10)

#Search Product
search_button = tk.Button(
    button_frame,
    text="🔍 Search Product",
    command=lambda: open_search_window(window),
    **button_style
)
search_button.grid(row=1, column=0, padx=10, pady=10)

#Delete Product
del_button = tk.Button(
    button_frame,
    text="➖ Delete Product",
    command=lambda: open_delete_window(window),
    **button_style
)
del_button.grid(row=1, column=1, padx=10, pady=10)

#Update Product
update_button = tk.Button(
    button_frame,
    text="✏️ Update Product",
    command=lambda: open_update_window(window),
    **button_style
)
update_button.grid(row=2, column=0, padx=10, pady=10)

#summary
summ_button = tk.Button(
    button_frame,
    text="💸 Inventory Summary",
    command=lambda: open_summary_window(window),
    **button_style
)
summ_button.grid(row=2, column=1, padx=10, pady=10)
#exit
exit_button = tk.Button(
    button_frame,
    text="🛑 Exit",
    command=window.destroy,
    **button_style
)
exit_button.grid(row=3, column=1, padx=10, pady=10)

window.configure(bg="#FFF0F5")

window.mainloop()
