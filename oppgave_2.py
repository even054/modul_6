# Del 1 - Gå gjennom en liste
"""favoritter = ["Hangover", "Prison Break", "Grand Theft Auto V", "Lilyhammer"]

# Runde | Verdien til favoritt | Skrives ut
# 1     |         "Hangover"             | Hangover
# 2     |         "Prison Break"             | Prison Break
# 3     |         "Grand Theft Auto V"             | Grand Theft Auto V
# 4     |         "Lilyhammer"             | Lilyhammer

for favoritt in favoritter:
    print(f"Jeg anbefaler: {favoritt}!")

print("Ferdig med lista!")"""

# Del 2 - Gjenta et bestemt antall ganger
"""bruker_tall = int(input("Skriv inn et tall: "))

for tall in range(1, 11):
    print(f"{tall} x {bruker_tall} = {tall * bruker_tall}")

# 3. Det som mangler er det siste tallet, altså 10. Du må ha range(1, 11) for å få med 10."""

# Del 3 - Summere med en løkke
utgifter = [45, 30, 62, 28, 55] # Hva du brukte i kantina hver dag denne uka
total = 0

for belop in utgifter:
    total += belop

# 1. Jeg tror det blir 220 kr.
# 2. Summen settes til 0 hver runde, men på siste rundes settes den til 55 så stopper for-loopen
# 3. Jeg tror hver iterasjon printes det hva som er i totalen

print(f"Denne uka brukte du {total} kr i kantina, du har brukt i gjennomsnitt {total / len(utgifter)} hver dag!")

# --- Utvidelse ---
# Lagt inn gjennomsnittet over, jeg tror at range(0, 20, 5) gir deg hvert femte tall.

# --- Refleksjon ---
# 1. Tabellen min stemte overens med printsa. Løkkevariabelen endrer seg for hver iterasjon, den endrer seg gjennom lista
# 2. Den stopper på fire fordi at den tar med 0. Det blir fortsatt fem runder fordi 0 er inkludert
# 3. I steg 2 så ble totalen resatt hver iterasjon, siste iterasjon var det som gjald. I steg 3 så ble hver iterasjon printet, altså hver gang summen ble endres så ble det printet.
# 4. Det er sånn Python syntax fungerer, det er identisk fra hvordan funksjoner og if-statements fungerer.