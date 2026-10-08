produit = "Clavier"
prix_ht = 19.90
quantité = 3
taux_tva = 0.2

total_ht = (prix_ht * quantité)
total_ttc = (total_ht) * (1 + taux_tva)

print(f"Le produit \"{produit}\" coûte {total_ttc:.2f}€ TTC.")

prix_texte = f"Le produit \"{produit}\" coûte {total_ttc:.2f}€ TTC."

