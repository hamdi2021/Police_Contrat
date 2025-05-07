import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

class PoliceContratApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Police Contrat App")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        # Application title
        title_label = tk.Label(self, text="Police Contrat App", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=20)

        # Welcome message
        message_label = tk.Label(self, text="Bienvenue à l'application Police Contrat", font=("Helvetica", 12))
        message_label.pack(pady=10)

        # Status button
        status_button = tk.Button(self, text="Afficher le statut", command=self.show_status)
        status_button.pack(pady=20)

    def show_status(self):
        # Show application status
        messagebox.showinfo("Statut", "Application is running")

if __name__ == "__main__":
    app = PoliceContratApp()
    app.mainloop()
