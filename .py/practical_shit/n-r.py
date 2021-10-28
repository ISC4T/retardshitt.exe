# FACTORIAL DEF
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact = fact * num
    return(fact)

# INPUTS
print("_______________________________________________")
Num1 = int(input("(n): "))
Num2 = int(input("(r): "))
hva = input("Avhengig(A) eller Uavhengig(U)?: ")
print("_______________________________________________")

# AWNSERS
if hva == "A":
    print((factorial(Num1))/(factorial(Num1 - Num2)))
elif hva == "U":
    print(Num1 ** Num2)
print("_______________________________________________")