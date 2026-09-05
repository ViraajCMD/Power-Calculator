print("Welcome the calculator!")

base = int(input("Enter the number: "))
exponent = int(input("Enter the power: "))

result = 1

for i in range(exponent):
    result = result * base

print("Result:", result)
