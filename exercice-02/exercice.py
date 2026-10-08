temperatures = [-99,-3, 0, 15, 31, 84] 

for temperature in temperatures:
    if temperature < 0:
        print(f"{temperature}°C: Gel")
    elif temperature < 15:
        print(f"{temperature}°C: Froid")
    elif temperature < 25:
        print(f"{temperature}°C: Doux")
    else:
        print(f"{temperature}°C: Chaud")

annees = [2024, 1900, 2000, 488, 1963, 1768]
for annee in annees:
    if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
        print(f"{annee} est une année bissextile.")
    else:
        print(f"{annee} n'est pas une année bissextile.")


