# Opdracht 1 lists
# Naam student: Hassan ALJASEM
# Groep: 

# Maak 4 dictionaries aan met gegevens van personen
dict_1 = { "id": 0, "voornaam": "Jan", "achternaam": "Jansen" }
dict_2 = { "id": 1, "voornaam": "Sanne", "achternaam": "de Vries" }
dict_3 = { "id": 2, "voornaam": "Mo", "achternaam": "Bakker" }
dict_4 = { "id": 3, "voornaam": "Lotte", "achternaam": "Visser" }

# Maak een list aan en voeg de dictionaries toe met de .append() methode
mylist = []
mylist.append(dict_1)
mylist.append(dict_2)
mylist.append(dict_3)
mylist.append(dict_4)

# Print de volledige naam van de 2e persoon
# We gebruiken index [1] omdat de lijst bij 0 begint (0=1e, 1=2e)
print(mylist[1]["voornaam"], mylist[1]["achternaam"])