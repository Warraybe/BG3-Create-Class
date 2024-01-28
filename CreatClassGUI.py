import tkinter as tk
import tkinter.ttk as ttk
import webbrowser

from ClassConfigTab import ClassConfigTab
# from CreateFiles import create_files
# from CreateFolders import create_folders
from LocalizationTab import LocalizationTab
from MetaTab import MetaTab


def open_link(url):
    webbrowser.open_new(url)


def create_mod(mod_type):
    pass
    # create_folders(main_name)
    # create_files(main_name, sub_names, sub_level)


def create_class():
    menubar.add_command(label="Create Class",
                        command=lambda: create_mod("class"))
    # Clear tabs
    for tab in nb.winfo_children():
        if str(tab) == nb.select():
            tab.destroy()

    # Create tabs
    config_tab = ClassConfigTab(nb)
    localization_tab = LocalizationTab(config_tab, nb)
    meta_tab = MetaTab(nb)
    nb.add(config_tab, text='Configure class')
    nb.add(meta_tab, text="Meta")
    nb.add(localization_tab, text='Localization')

    nb.pack(expand=1, fill="both")


# Create tkinter window
root = tk.Tk()
root.title("BG3 Mod Creation Tool")
root.geometry("650x150")

# Create notebook
nb = ttk.Notebook(root)

# Create Menubar
menubar = tk.Menu(root)

# Add File Menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Class", command=create_class)
file_menu.add_command(label="New Race")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Add tools Menu
tools_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(
    label="Norbyte's Baldur's Gate 3 Script Extender",
    command=lambda: open_link(
        "https://github.com/Norbyte/bg3se"))
tools_menu.add_command(label="BG3 Multi-Tool",
                       command=lambda: open_link(
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
root.config(menu=menubar)
root.mainloop()
