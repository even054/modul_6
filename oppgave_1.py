fruktskal = ["eple", "banan", "pære", "kiwi"]

# 1.
print(type(fruktskal))

# 2. Jeg tror element på indeks 1 er banan, og på 3 er det kiwi
print(fruktskal[1], fruktskal[3])

# 3.
print(len(fruktskal))

# 4. Jeg tror det kommer error at det ikke finnes noe på indeks 4
#print(fruktskal[4])

# 5. Kiwi har indeks 2 nå
fruktskal.append("mango")
fruktskal.remove("banan")
print(len(fruktskal))

# 6. Forventer at jeg får kiwi og banan, ikke Kiwi med stor K

valgt_frukt = input("Hvilken frukt vil du ha? ")

if valgt_frukt in fruktskal:
    print(f"Værsågod, her er en {valgt_frukt}")

    fruktskal.remove(valgt_frukt)
else:
    print(f"Beklager, vi har ikke {valgt_frukt}")

# --- Utvidelse ---
# Det som skjer hvis man har remove på en frukt som ikke finnes er at man får error på at det man spesifiserer ikke er i listen, in hjelper akkurat her fordi remove skjer da kun hvis den er i listen. Har lagt det til over ^

# --- Refleksjon ---
# 1. Fordi at fruktskal[4] går ut i fra indeks som starter på 0, len() går ut i fra antall elementer i lista
# 2. Kiwi fikk en ny indeks fordi at elementet før kiwi ble fjernet, da gikk kiwi en tilbake. Det kan bety at man kan få et annet element en forventet i variabelen sin, lister kan endres og man burde forvente det
# 3. Jeg forventet at det ikke gikk, det skjedde for at programmet ikke tar til tanke på at store bokstaver kan forekomme. Dette kan løses med .lower()
# 4. Det er nyttig fordi man får vekk redundant kode, mye enklere å lese koden når det er mindre innhold som for eksempel en liste gjør