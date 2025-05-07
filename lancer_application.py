#!/usr/bin/env python3
import os
import sys
import tkinter as tk
from tkinter import messagebox

# Import from police_contrat_app.py
from police_contrat_app import PoliceContratApp

if __name__ == "__main__":
    try:
        # Start the Tkinter application
        app = PoliceContratApp()
        app.mainloop()
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")
