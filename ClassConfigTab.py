import tkinter as tk
from tkinter import ttk


class ClassConfigTab(ttk.Frame):
    """Content for the required tab for creating a class mod."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label_classname = ttk.Label(self, text="Class name (Required):")
        self.entry_classname = ttk.Entry(self, width=50)
        self.label_subclassnames = ttk.Label(self,
                                        text="Subclass name(s) (Optional):")
        self.entry_subclassnames = ttk.Entry(self, width=100)
        self.label_subclass_level = ttk.Label(self,
                                         text="Subclass level (Optional):")
        self.entry_subclass_level = ttk.Entry(self, width=5)

        self.place_widgets()

    def place_widgets(self):

        # Place widgets
        self.label_classname.grid(column=0,
                             row=0,
                             padx=10,
                             pady=5,
                             sticky=tk.W)
        self.entry_classname.grid(column=0,
                             row=1,
                             padx=10,
                             pady=0,
                             sticky=tk.W)
        self.label_subclassnames.grid(column=0,
                                 row=2,
                                 padx=10,
                                 pady=5,
                                 sticky=tk.W)
        self.entry_subclassnames.grid(column=0,
                                 row=3,
                                 padx=10,
                                 pady=0, sticky=tk.W)
        self.label_subclass_level.grid(column=1, row=2, padx=10, pady=5,
                                  sticky=tk.W)
        self.entry_subclass_level.grid(column=1,
                                  row=3,
                                  padx=10,
                                  pady=0)
