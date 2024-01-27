import tkinter as tk
import webbrowser


def open_link(url):
    webbrowser.open_new(url)


# creating tkinter window
window = tk.Tk()
window.title("BG3 Mod Creation Tool")
window.geometry("800x600")
# tabControl = ttk.Notebook(root)
#
# tab1 = ttk.Frame(tabControl)
# tab2 = ttk.Frame(tabControl)
#
# tabControl.add(tab1, text='Config')
# tabControl.add(tab2, text='Tab 2')
# tabControl.pack(expand=1, fill="both")
#
# ttk.Label(tab1,
#           text="Welcome to \
# GeeksForGeeks").grid(column=0,
#                      row=0,
#                      padx=30,
#                      pady=30)
# ttk.Label(tab2,
#           text="Lets dive into the\
# world of computers").grid(column=0,
#                           row=0,
#                           padx=30,
#                           pady=30)

# Creating Menubar 
menubar = tk.Menu(window)

# Adding File Menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Class", command=None)
file_menu.add_command(label="New Race", command=None)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.destroy)

# Adding tools Menu
tools_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(label="Norbyte's Baldur's Gate 3 Script Extender",
                       command=lambda: open_link(
                           "https://github.com/Norbyte/bg3se"))
tools_menu.add_command(label="BG3 Multi-Tool", command=lambda: open_link(
    "https://github.com/ShinyHobo/BG3-Modders-Multitool"))
tools_menu.add_command(label="Lslib",
                       command=lambda: open_link(
                           "https://github.com/Norbyte/lslib"))

# Adding Help Menu 
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=lambda: open_link(
    "https://github.com/Warraybe/BG3-Create-Class"))

# display Menu 
window.config(menu=menubar)
tk.mainloop()
