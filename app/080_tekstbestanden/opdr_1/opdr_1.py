# Opdracht 1 while-loops
# Naam student: Hassan Aljasem
# Groep:

# Jouw code komt hier

vraag1 = input("Wat vind je van de huidige regering?\n")
vraag2 = input("Wat vind je van de Python-lessen tot nu toe?\n")
vraag3 = input("Wat vind jij de mooiste stad van Nederland?\n")

with open("enquete_resultaten.txt", "w") as bestand:
    bestand.write("Antwoorden op de enquete:\n")
    bestand.write(f"1. {vraag1}\n")
    bestand.write(f"2. {vraag2}\n")
    bestand.write(f"3. {vraag3}\n")

print("Bedankt! Je antwoorden zijn opgeslagen.")
