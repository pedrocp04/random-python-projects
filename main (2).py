income = float(input("Enter the annual income: "))

if income <= 85528:
    count = (income * 0.18) - 556.2
    tax = round(count,0)
else:
    count = ((income - 85528) * 0.32) + 14839.2
    tax = round(count,0)

if tax < 0:
    tax = 0

#tax = round(tax, 0)
print("The tax is:", tax, "thalers")
