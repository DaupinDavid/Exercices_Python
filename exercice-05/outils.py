def convertir_note(texte):
    try:
        return float(texte)
    except ValueError:
        return "None"

def moyenne(valeurs):
    if not valeurs:
        return 0
    return sum(valeurs) / len(valeurs)

def mention(note):
    if note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    elif note >= 10:
        return "Passable"
    else:
        return "Insuffisant"



