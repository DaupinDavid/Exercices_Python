ventes = [
    {"produit": "Café", "prix": 2.5, "quantité": 120},
    {"produit": "Thé", "prix": 2.0, "quantité": 80},
    {"produit": "Jus", "prix": 3.5, "quantité": 45},
]

ca_par_produit = {vente["produit"]: vente["prix"] * vente["quantité"] for vente in ventes}
print (f"{ca_par_produit}")

ca_total = sum(ca_par_produit.values())
print(f"Chiffre d'affaires total : {ca_total:.2f}€")

print(f"Produit le plus rentable : {max(ca_par_produit, key=ca_par_produit.get)} = {max(ca_par_produit.values()):.2f}€")