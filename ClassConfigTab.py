import tkinter as tk
from tkinter import ttk


class ClassConfigTab(ttk.Frame):
    """Content for the required tab for creating a class mod."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.classname = tk.StringVar(name="classname")

        self.place_widgets()

    def place_widgets(self):
        label_classname = ttk.Label(self, text="Class name:")
        entry_classname = ttk.Entry(self, width=50, textvariable=self.classname)
        label_subclassnames = ttk.Label(self,
                                        text="Subclass name(s) (Optional, comma separated):")
        entry_subclassnames = ttk.Entry(self, width=100)
        label_subclass_level = ttk.Label(self,
                                         text="Subclass level (Optional, Defaults to 1):")
        entry_subclass_level = ttk.Entry(self, width=5)

        # Place widgets
        label_classname.grid(column=0,
                             row=0,
                             padx=10,
                             pady=5,
                             sticky=tk.W)
        entry_classname.grid(column=0,
                             row=1,
                             padx=10,
                             pady=0,
                             sticky=tk.W)
        label_subclassnames.grid(column=0,
                                 row=2,
                                 padx=10,
                                 pady=5,
                                 sticky=tk.W, columnspan=2)
        entry_subclassnames.grid(column=0,
                                 row=3,
                                 padx=10,
                                 pady=0, sticky=tk.W, columnspan=2)
        label_subclass_level.grid(column=1, row=0, padx=10, pady=5,
                                  sticky=tk.W)
        entry_subclass_level.grid(column=1,
                                  row=1,
                                  padx=10,
                                  pady=0)
