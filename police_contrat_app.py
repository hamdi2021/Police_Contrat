import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class PoliceContratApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recherche Police-Contrat")
        self.root.geometry("600x400")
        self.root.configure(bg="#f5f5f5")
        
        # Charger les données
        self.load_data()
        
        # Créer l'interface
        self.create_widgets()
        
    def load_data(self):
        try:
            with open('/home/ubuntu/polices_contrats.json', 'r') as f:
                self.polices_contrats = json.load(f)
            print(f"Données chargées avec succès: {len(self.polices_contrats)} correspondances")
        except Exception as e:
            print(f"Erreur lors du chargement des données: {e}")
            self.polices_contrats = {}
            
    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#f5f5f5", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Titre
        title_label = tk.Label(
            main_frame, 
            text="Recherche Police-Contrat", 
            font=("Arial", 18, "bold"),
            bg="#f5f5f5",
            fg="#333333",
            pady=10
        )
        title_label.pack()
        
        # Frame de recherche
        search_frame = tk.Frame(main_frame, bg="white", padx=15, pady=15, relief=tk.RAISED, bd=1)
        search_frame.pack(fill=tk.X, pady=10)
        
        # Label d'instruction
        instruction_label = tk.Label(
            search_frame,
            text="Entrez un numéro de Police pour trouver le Contrat correspondant:",
            font=("Arial", 10),
            bg="white",
            anchor="w"
        )
        instruction_label.pack(fill=tk.X, pady=(0, 10))
        
        # Frame pour le champ de recherche et le bouton
        input_frame = tk.Frame(search_frame, bg="white")
        input_frame.pack(fill=tk.X)
        
        # Champ de recherche
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(
            input_frame,
            textvariable=self.search_var,
            font=("Arial", 12),
            width=30
        )
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.search_entry.bind("<Return>", lambda event: self.search_police())
        
        # Bouton de recherche
        search_button = ttk.Button(
            input_frame,
            text="Rechercher",
            command=self.search_police
        )
        search_button.pack(side=tk.RIGHT)
        
        # Frame pour les résultats
        self.result_frame = tk.Frame(main_frame, bg="#f5f5f5", padx=15, pady=15)
        self.result_frame.pack(fill=tk.BOTH, expand=True)
        
        # Label pour afficher le résultat
        self.result_label = tk.Label(
            self.result_frame,
            text="",
            font=("Arial", 12),
            bg="#f5f5f5",
            justify=tk.LEFT,
            anchor="w"
        )
        self.result_label.pack(fill=tk.X)
        
        # Statistiques
        stats_frame = tk.Frame(main_frame, bg="#f5f5f5")
        stats_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=10)
        
        stats_label = tk.Label(
            stats_frame,
            text=f"Base de données: {len(self.polices_contrats)} correspondances Police-Contrat",
            font=("Arial", 8),
            fg="#666666",
            bg="#f5f5f5"
        )
        stats_label.pack(side=tk.LEFT)
        
        # Mettre le focus sur le champ de recherche
        self.search_entry.focus_set()
        
    def search_police(self):
        police = self.search_var.get().strip()
        
        if not police:
            messagebox.showwarning("Champ vide", "Veuillez entrer un numéro de Police")
            return
        
        # Rechercher dans les données
        if police in self.polices_contrats:
            contrat = self.polices_contrats[police]
            self.show_success(police, contrat)
        else:
            self.show_error(police)
    
    def show_success(self, police, contrat):
        # Configurer le label de résultat pour afficher le succès
        self.result_label.configure(
            text=f"Le Contrat correspondant à la Police {police} est :\n\n{contrat}",
            fg="#3c763d",
            bg="#dff0d8",
            padx=10,
            pady=10
        )
        
        # Configurer le frame de résultat
        self.result_frame.configure(bg="#dff0d8", relief=tk.SOLID, bd=1)
        
    def show_error(self, police):
        # Configurer le label de résultat pour afficher l'erreur
        self.result_label.configure(
            text=f"Aucun Contrat trouvé pour la Police {police}",
            fg="#a94442",
            bg="#f2dede",
            padx=10,
            pady=10
        )
        
        # Configurer le frame de résultat
        self.result_frame.configure(bg="#f2dede", relief=tk.SOLID, bd=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = PoliceContratApp(root)
    root.mainloop()
