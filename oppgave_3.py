# Del 1 - Nedtelling

"""teller = 5

while teller > 0:
    print(teller)
    teller -= 1

print("Kaffepause!")"""

# 1. Tror at den teller ned til 1, også kommer Kaffepause!
# 2. Da er også 0 inkludert
# 3. Tror at løkken ikke vil kjøre, man vil bare få Kaffepause!

# Del 2 - En uendelig løkke, med vilje

"""teller = 5

while teller > 0:
    print(teller)
    #teller -= 1

print("Kaffepause!")"""

# 2. Jeg tror at løkken vil printe 5 tallet uendelig

# Del 3 - Innlogging med flere forsøk

"""riktig_brukernavn = "michael"
riktig_passord = "python123"

forsok = 0
feil_forsok = 3
innlogget = False

while forsok < 3:
    brukernavn = input("Hva er brukernavnet ditt? ")
    passord = input("Hva er passordet ditt? ")

    forsok += 1

    if brukernavn == riktig_brukernavn and passord == riktig_passord:
        print(f"Velkommen, {brukernavn}")
        innlogget = True
        break
    else:
        print(f"Feil brukernavn eller passord, du har {feil_forsok - forsok} forsøk igjen!")
else:
    print("For mange feil forsøk, kontoen er låst.")"""

# 3. Test disse tre filfellene:
# Forventer at man får "Velkommen, michael"
# Forventer at man får "Feil brukernavn eller passord, du har 2 forsøk igjen", så et forsøk igjen og at man kommer inn på siste
# Etter tre feil så forventer jeg at man får "For mange feil forsøk, kontoen er låst."

# --- Utvidelse ---
# Synes det er enklest å lese med for-loop, mindre kode.
riktig_brukernavn = "michael"
riktig_passord = "python123"

feil_forsok = 3
innlogget = False

for forsok in range(1, 4):
    brukernavn = input("Hva er brukernavnet ditt? ")
    passord = input("Hva er passordet ditt? ")

    if brukernavn == riktig_brukernavn and passord == riktig_passord:
        print(f"Velkommen, {brukernavn}")
        innlogget = True
        break
    else:
        print(f"Feil brukernavn eller passord, du har {feil_forsok - forsok} forsøk igjen!")
else:
    print("For mange feil forsøk, kontoen er låst.")

# --- Refleksjon ---
# 1. Det som skjedde var at while-løkken aldri kjørte fordi at teller var 0. Kondisjonen i while-løkka var at den kjørte hvis teller var over 0.
# 2. Den stoppet aldri fordi at kondisjonen som var i while-løkken aldri ble endret, den var uendelig True. Det som må gjøres er at man må endre variabelen som får while-løkken til å kjøre. For eksempel legge til teller -= 1.
# 3. Enten kan den stoppe hvis man har brukt opp forsøkene sine, eller at man har skrevet riktig passord og brukernavn.
# 4. while passet godt fordi at løkken kjørte uendelig til brukeren hadde skrevet inn riktig passord og brukernavn, for passer bra hvis du vet antall forsøk og while passer hvis du ikke vet.