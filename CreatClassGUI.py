import tkinter as tk
import tkinter.ttk as ttk
import webbrowser

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
        sub_level = tabcontrol.children["!frame"].children["!entry3"].get()

    if mod_type == "class":
        sub_level = tabcontrol.children["!frame"].children["!entry3"].get()
        if sub_level:
            sub_level = int(sub_level)

        create_folders(main_name)
        create_files(main_name, sub_names, sub_level)


def create_class():
    menubar.add_command(label="Save",
                        command=lambda: create_mod("class"))
    # Clear tabs
    for tab in tabcontrol.winfo_children():
        if str(tab) == tabcontrol.select():
            tab.destroy()

    # Create tabs
    config_tab = ttk.Frame(tabcontrol)
    tab2 = ttk.Frame(tabcontrol)
    tabcontrol.add(config_tab, text='Config')
    tabcontrol.add(tab2, text='Tab 2')
    tabcontrol.pack(expand=1, fill="both")

    # Create widgets
    label_classname = ttk.Label(config_tab, text="Class name (Required):")
    entry_classname = ttk.Entry(config_tab, width=50)
    label_subclassnames = ttk.Label(config_tab,
                                    text="Subclass name(s) (Optional):")
    entry_subclassnames = ttk.Entry(config_tab, width=100)
    label_subclass_level = ttk.Label(config_tab,
                                     text="Subclass level (Optional):")
    entry_subclass_level = ttk.Entry(config_tab, width=5)

    # Place widgets
    label_classname.grid(column=0,
                         row=0,
                         padx=10,
                         pady=0,
                         sticky=tk.W)
    entry_classname.grid(column=0,
                         row=1,
                         padx=10,
                         pady=0,
                         sticky=tk.W)
    label_subclassnames.grid(column=0,
                             row=2,
                             padx=10,
                             pady=0,
                             sticky=tk.W)
    entry_subclassnames.grid(column=0,
                             row=3,
                             padx=10,
                             pady=0, sticky=tk.W)
    label_subclass_level.grid(column=1, row=2, padx=10, pady=0, sticky=tk.W)
    entry_subclass_level.grid(column=1,
                              row=3,
                              padx=10,
                              pady=0)

    ttk.Label(tab2,
              text="Lets dive into the\
    world of computers").grid(column=0,
                              row=0,
                              padx=30,
                              pady=30)


# Create tkinter window
window = tk.Tk()
window.title("BG3 Mod Creation Tool")
window.geometry("800x600")

# Mod type
mod_type = None

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
