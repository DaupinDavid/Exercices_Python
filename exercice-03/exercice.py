temperatures = [12.5, 14, 9.5, 17, 21, 19.5, 11]

temperature_moyenne = sum(temperatures) / len(temperatures)
temperature_min = min(temperatures)
temperature_max = max(temperatures)
print(f"Moyenne = {temperature_moyenne:.2f}°C.")
print(f"Min = {temperature_min:.2f}°C.")
print(f"Max = {temperature_max:.2f}°C.")

print(f"\nJours > 15°C = {len([temperature for temperature in temperatures if temperature > 15])}.")

Fahrenheit_temperatures = [(temperature * 9/5) + 32 for temperature in temperatures]
print(f"\nTempératures en Fahrenheit : {Fahrenheit_temperatures}")

for jours, temperature in enumerate(temperatures, start=1):
    print(f"Jour {jours}: {temperature}°C")
