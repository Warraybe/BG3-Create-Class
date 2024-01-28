import tkinter as tk
import tkinter.ttk as ttk
import webbrowser

from ConfigTab import ConfigTab
from CreateFiles import create_files
from CreateFolders import create_folders


def open_link(url):
    webbrowser.open_new(url)


def create_mod(mod_type):
    # Create main and sub variables
    main_name = str(tabcontrol.children["!frame"].children["!entry"].get())
    sub_names = tabcontrol.children["!frame"].children["!entry2"].get()

    if sub_names:
        sub_names = [sub.strip() for sub in sub_names.split(",")]

    if mod_type == "class":
        sub_level = tabcontrol.children["!frame"].children["!entry3"].get()
        if sub_level:
            sub_level = int(sub_level)
        create_folders(main_name)
        create_files(main_name, sub_names, sub_level)


def create_localization_tab(localization_tab):
    main_name = str(tabcontrol.children["!frame"].children["!entry"].get())
    sub_names = tabcontrol.children["!frame"].children["!entry2"].get()

    label_main_name = ttk.Label(localization_tab,
                                text=f"{main_name} Description:")
    entry_main_desc = ttk.Entry(localization_tab, width=100)

    label_main_name.grid(column=0,
                         row=0,
                         padx=10,
                         pady=5,
                         sticky=tk.W)
    entry_main_desc.grid(column=0,
                         row=1,
                         padx=10,
                         pady=0,
                         sticky=tk.W)


def create_class():
    menubar.add_command(label="Create Class",
                        command=lambda: create_mod("class"))
    # Clear tabs
    for tab in tabcontrol.winfo_children():
        if str(tab) == tabcontrol.select():
            tab.destroy()

    # Create tabs
    config_tab = ConfigTab(tabcontrol)
    localization_tab = ttk.Frame(tabcontrol)
    tabcontrol.add(config_tab, text='Required Settings')
    tabcontrol.add(localization_tab, text='Localization Settings')
    tabcontrol.pack(expand=1, fill="both")

    # create_localization_tab(localization_tab)


# Create tkinter window
window = tk.Tk()
window.title("BG3 Mod Creation Tool")
window.geometry("800x150")

# Create tab controller
tabcontrol = ttk.Notebook(window)

# Create Menubar
menubar = tk.Menu(window)

# Add File Menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Class", command=create_class)
file_menu.add_command(label="New Race", command=None)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.destroy)

# Add tools Menu
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

# Add Help Menu
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=lambda: open_link(
    "https://github.com/Warraybe/BG3-Create-Class"))

# Display window
window.config(menu=menubar)
tk.mainloop()
