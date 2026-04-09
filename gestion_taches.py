taches = []

def ajouter_tache(titre):
    taches.append({"titre": titre, "completee": False})
    print(f"Tâche '{titre}' ajoutée.")

def supprimer_tache(titre):
    global taches
    taches = [t for t in taches if t["titre"] != titre]
    print(f"Tâche '{titre}' supprimée.")

def modifier_tache(ancien_titre, nouveau_titre):
    for t in taches:
        if t["titre"] == ancien_titre:
            t["titre"] = nouveau_titre
            print(f"Tâche renommée en '{nouveau_titre}'.")
            return
    print("Tâche introuvable.")
