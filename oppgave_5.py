# Del 1 - Slå opp og endre
"""priser = {
    "kaffe": 25,
    "rundstykke": 30,
    "suppe": 65,
    "eple": 10
}

# 1.
print(f"Hele ordboka: {priser}")
print(f"Pris på et rundstykke: {priser["rundstykke"]} kr")

# 2.
priser["te"] = 20
priser["kaffe"] = 28
print(f"Hele ordboka: {priser}")

# 3. Jeg tror det kommer error på at det ikke finnes i ordboka
#print(priser["pizza"])

# 4. 
vare = input("Hva vil du kjøpe? ")

if vare in priser:
    print(f"{vare} koster {priser[vare]} kr.")
else:
    print(f"Beklager, vi har ikke {vare}.")"""

# Del 2 - Ordbøker og løkker
priser = {
    "kaffe": 25,
    "rundstykke": 30,
    "suppe": 65,
    "eple": 10
}

# 1. Trodde egentlig at prisene skulle bli skrevet ut, men selve varen ble skrevet ut
"""for noe in priser:
    print(noe)"""

# 2.
"""for rett, pris in priser.items():
    print(f"{rett}: {pris} kr")"""

# 3.
"""kurv = ["kaffe", "rundstykke", "kaffe", "brownie"]
total = 0

for rett in kurv:
    if rett in priser:
        total += priser[rett]
    else:
        print(f"{rett} finnes ikke på menyen.")

print(f"Totalen på handlekurven er: {total}")"""

# --- Utvidelse ---
kurv1 = ["kaffe", "rundstykke", "kaffe", "brownie"]
kurv2 = ["eple", "suppe", "cookie"]

def regn_total(kurv: list[str], priser: dict[str, int]) -> int:
    total = 0

    for rett in kurv:
        if rett in priser:
            total += priser[rett]
        else:
            print(f"{rett} finnes ikke på menyen.")

    return total
            
print(regn_total(kurv1, priser))
print(regn_total(kurv2, priser))

# --- Refleksjon ---
# 1. Fordi at ordbøker lagrer data som nøkkel-verdi-par, da kan en nøkkel kobles direkte opp mot en verdi, lister kan på en måte gjøre det også men det er mye mer uoversiktlig
# 2. Det var en KeyError, nøkkelen fantes ikke i ordboken. I forhold til IndexError i en liste så er det egentlig det samme, indeksen fantes ikke i listen
# 3. Den gikk gjennom nøklene, når du bruker .items() får du de satt opp som nøkkel-verdi-par.
# 4. Kantina får ikke to kaffer på menyen, den bare overwriter den tidligere prisen med den nye. Du kan ikke ha to like nøkler i en ordbok.