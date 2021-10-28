# INPUTS
print("_______________________________________________")

nok = int(input("Amount(NOK): "))
currancy = input("USD, CNY, GBP, EUR, DKK, SKK? ")
currancy = currancy.lower()

print("_______________________________________________")

# CONVERTER
if currancy == "usd":
    print(("USD ="), (nok * 0.12))
    
elif currancy == "cny":
    print(("CNY ="), (nok * 0.78))

elif currancy == "gbp":
    print(("GBP ="), (nok * 0.086))

elif currancy == "eur":
    print(("EUR ="), (nok * 0.100))

elif currancy == "dkk":
    print(("DKK ="), (nok * 0.74))

elif currancy == "skk":
    print(("SKK ="), (nok * 2.02))

print("_______________________________________________")