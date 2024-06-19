import tkinter as tk
from tkinter import ttk, simpledialog
import numpy as np
import cv2
from PIL import Image, ImageTk

class StructuringElementDialog(simpledialog.Dialog):
    def __init__(self, parent):
        self.size = None
        self.shape = None
        super().__init__(parent, "Choisir les paramètres de l'élément structurant")

    def body(self, frame):
        tk.Label(frame, text="Taille de l'élément structurant :").grid(row=0, column=0, sticky=tk.W)
        self.size_var = tk.StringVar()
        self.size_combo = ttk.Combobox(frame, textvariable=self.size_var)
        self.size_combo['values'] = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
        self.size_combo.current(0)
        self.size_combo.grid(row=0, column=1)

        tk.Label(frame, text="Forme de l'élément structurant :").grid(row=1, column=0, sticky=tk.W)
        self.shape_var = tk.StringVar()
        self.shape_combo = ttk.Combobox(frame, textvariable=self.shape_var)
        self.shape_combo['values'] = ["Rectangle", "Ellipse", "Croix"]
        self.shape_combo.current(0)
        self.shape_combo.grid(row=1, column=1)

        return frame

    def apply(self):
        self.size = int(self.size_var.get())
        self.shape = self.shape_var.get()