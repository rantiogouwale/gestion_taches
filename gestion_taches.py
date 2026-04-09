taches = []

def ajouter_tache(titre):
    taches.append({"titre": titre, "completee": False})
    print(f"Tâche '{titre}' ajoutée.")
