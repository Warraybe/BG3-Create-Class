import tkinter as tk
from tkinter import ttk


class LocalizationTab(ttk.Frame):
    """This will contain what is going to be shown on the localization tab."""

    def __init__(self, config_tab, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label_main_name = ttk.Label(self,
                                         text=f"{config_tab.entry_classname.get()} Description:")

        self.place_widgets()

    def place_widgets(self):
        self.label_main_name.grid(column=0,
                                  row=0,
                                  padx=10,
                                  pady=5,
                                  sticky=tk.W)
