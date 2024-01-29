import tkinter as tk
from tkinter import ttk


class LocalizationTab(ttk.Frame):
    """This will contain what is going to be shown on the localization tab."""

    def __init__(self, config_tab, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_tab = config_tab

        self.label_main_name = ttk.Label(self, text="Description:")

        config_tab.classname.trace_add("write", self.update_label)

        self.place_widgets()

    def place_widgets(self):
        self.label_main_name.grid(column=0,
                                  row=0,
                                  padx=10,
                                  pady=5,
                                  sticky=tk.W)

    def update_label(self, *args):
        self.label_main_name[
            "text"] = f"{self.config_tab.classname.get()} Description:"
