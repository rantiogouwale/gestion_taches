taches = []

def ajouter_tache(titre):
    taches.append({"titre": titre, "completee": False})
    print(f"Tâche '{titre}' ajoutée.")

def supprimer_tache(titre):
    global taches
    taches = [t for t in taches if t["titre"] != titre]
    print(f"Tâche '{titre}' supprimée.")
