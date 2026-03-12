# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

tekst = input("Geef de tekst die wilt encrypten..\n")

verschuiving = 5
resultaat = ""

for char in tekst:
    if char.isalpha():
        if char.islower():
            nieuwe_code = (ord(char) - ord('a') + verschuiving) % 26 + ord('a')
            resultaat += chr(nieuwe_code)
        else:
            nieuwe_code = (ord(char) - ord('A') + verschuiving) % 26 + ord('A')
            resultaat += chr(nieuwe_code)
    else:
        resultaat += char

print(resultaat)
