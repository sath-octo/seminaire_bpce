def meilleure_commune(data):
    spots = {}
    for observation in data:
        if observation["libelle_commune"] not in spots:
            spots[observation["libelle_commune"]] = 0
        spots[observation["libelle_commune"]] += 1
    return (max(spots, key=spots.get), max(spots.values()))

def taille_moyenne_mm(data):
    total = 0
    count = 0
    for observation in data:
        if observation["taille_individu"] is not None:
            count += 1
            total += observation["taille_individu"]
    return total / count