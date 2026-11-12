# Del 1 - Tuple
"""ukedager = ("mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag")

# 3. Forventer en error fordi at du kan ikke endre en tuple.
#ukedager.append("lillelørdag")

# 4.
#ukedager[0] = "fridag"

for ukedag in ukedager:
    print(f"Dag: {ukedag}")

print(f"Lengde på tuple: {len(ukedager)}")"""

# Del 2 - Set
pameldinger = ["Ada", "Linus", "Grace", "Ada", "Guido", "Linus", "Ada"]

# 1.
print(len(pameldinger))

# 2. Jeg tror det er fire unike deltakere
deltakere = set(pameldinger)
print(deltakere)
print(len(deltakere))

"""
3.
{'Ada', 'Grace', 'Linus', 'Guido'}
{'Guido', 'Ada', 'Linus', 'Grace'}
{'Linus', 'Grace', 'Ada', 'Guido'}
"""

# 4.
deltakere.add("Margaret")
deltakere.add("Grace")
print(len(deltakere))

# 5.
if "Ada" in deltakere:
    print("Ada er i deltakerlista!")

# 6.
#print(deltakere[0])

# --- Utvidelse ---
# Et set har ikke en bestemt rekkefølge, tuple har det.
for navn in deltakere:
    print(f"Velkommen, {navn}!")

# --- Refleksjon ---
# 1. Det kom AttributeError og TypeError, det sier noe om at tuples ikke kan forandres når de er opprettet
# 2. Ville ha valgt det når jeg vil ha en liste som har fast rekkefølge og som ikke kan endres
# 3. Rekkefølgen endret seg for hver gang programmet kjørte, jeg tror ikke et set har indekser fordi at rekkefølgen ikke er fast
# 4. Si at du har to lister, påmeldinger med navn og liste uten noe. Da kan du lage en for loop som sjekker navn i påmeldinger, så et if-statement på om navn ikke finnes i liste så skal liste.append(navn). Da blir alle navn som ikke allerede er i listen lagt til.