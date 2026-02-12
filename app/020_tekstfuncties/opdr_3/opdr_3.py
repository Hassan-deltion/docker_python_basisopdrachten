# Opdracht 3
# Naam student: Hassan Aljasem
# Groep: ...
 
# Eén boom bestaat uit deze 8 regels:
boom = [
    "    *    ",
    "   ***   ",
    "  *****  ",
    " ******* ",
    "*********",
    "  *****  ",
    "   ***   ",
    "   ***   "
]
 
# Aantal bomen naast elkaar
aantal_bomen = 5
 
# Print elke rij van de bomen naast elkaar
for regel in boom:
    print(regel * aantal_bomen)