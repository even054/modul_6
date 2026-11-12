handlekurv = ["melk", "brød", "ost", "egg"]
priser = [22, 35, 89, 45]

print("Varer i handlekurven:")
for i in range(0, len(handlekurv)):
    print(f"- {handlekurv[i]}")

total = 0
for pris in priser:
    total += pris

print(f"Totalt: {total} kr")

if len(handlekurv) == 0:
    print("Handlekurven er tom.")

print("Din tur kommer om:")
teller = 3
while teller > 0:
    print(teller)
    teller -= 1
print("Neste kunde!")

# --- Refleksjon ---
# 1. Manglet innrykk på linje 6, manglet kolon på linje 9, tildelingsoperator brukt i stedet for sammenligningsoperator på linje 14
# 2. Loopen startet på 1 i stedet for 0 på linje 5, total = 0 var inne i selve loopen på linje 10, while-loopen på linje 19 startet på 1 i stedet for 0
# 3. Fordi at loopen startet på 1 i stedet for 0 på linje 5, det kan skrives slikt:
"""
for i in handlekurv:
    print(f"- {i}")
"""
# 4. Det er lurt å sjekke loops, begge av de feilene var i en for- og while loop.