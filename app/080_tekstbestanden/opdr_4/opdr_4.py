# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:

# Party enquete

vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

antwoorden = {}

for i, vraag in enumerate(vragen, start=1):
    print(f"{i}. {vraag}")
    antwoord = input()
    antwoorden[vraag] = antwoord

print("\nBedankt voor het invullen!")
print("See you at the party.\n")

with open("party_enquete.txt", "a") as bestand:
    bestand.write("----\n")
    bestand.write(f"voornaam: {antwoorden[vragen[0]]}\n")
    bestand.write(f"achternaam: {antwoorden[vragen[1]]}\n")
    bestand.write(f"drank: {antwoorden[vragen[2]]}\n")
    bestand.write(f"eten: {antwoorden[vragen[3]]}\n\n")
