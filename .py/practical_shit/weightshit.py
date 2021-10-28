# INPUTS
print("_______________________________________________")
Wheight = input("Wheigh?: ")
KorL = input("(K)g or (L)bs?: ")

# AWNSERS
print("_______________________________________________")
if KorL.upper() == "K":
    print(("Wheight in Lbs: "), ((float(Wheight)) * 2.205))
elif KorL.upper() == "L":
    print(("Wheight in Kg: "), ((float(Wheight)) / 2.205))
print("_______________________________________________")