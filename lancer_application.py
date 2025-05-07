#!/usr/bin/env python3
import os
import sys
import subprocess
import tkinter as tk
from tkinter import messagebox

def check_dependencies():
    try:
        import tkinter
        return True
    except ImportError:
        return False

def install_tkinter():
    system = sys.platform
    if system == 'win32':
        messagebox.showinfo("Installation requise", 
                           "Tkinter n'est pas installé. Veuillez installer Python avec l'option Tkinter.")
        return False
    elif system == 'linux':
        try:
            subprocess.run(['sudo', 'apt-get', 'update'], check=True)
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'python3-tk'], check=True)
            return True
        except:
            messagebox.showinfo("Installation requise", 
                               "Tkinter n'est pas installé. Veuillez exécuter: sudo apt-get install python3-tk")
            return False
    elif system == 'darwin':
        messagebox.showinfo("Installation requise", 
                           "Tkinter n'est pas installé. Veuillez installer Python avec l'option Tkinter.")
        return False
    return False

if __name__ == "__main__":
    # Vérifier si tkinter est installé
    if not check_dependencies():
        # Essayer d'installer tkinter
        if not install_tkinter():
            sys.exit(1)
    
    # Exécuter l'application
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    try:
        import police_contrat_app
        from police_contrat_app import PoliceContratApp
        
        root = tk.Tk()
        app = PoliceContratApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite: {e}")
        sys.exit(1)
