import tkinter as tk
from tkinter import ttk

class MetaTab(ttk.Frame):
    def __init__(self, config_tab, *args, **kwargs):
        super().__init__(*args, **kwargs)