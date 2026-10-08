import outils

notes_brutes = ["12.5", "15", "abc", "9", "18.25"]

notes_converties = [outils.convertir_note(note) for note in notes_brutes if outils.convertir_note(note) != "None"]
print(f"Notes converties : {notes_converties}")
print(f"Nombre de notes non valides : {len(notes_brutes) - len(notes_converties)}")
print(f"Nombre de notes valides : {len(notes_converties)}")
print(f"Moyenne : {outils.moyenne(notes_converties):.2f}")
for note in notes_converties:
    print(f"Note : {note}, Mention : {outils.mention(note)}")