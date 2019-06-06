num1 = float(input("Enter first number: "))
print("Pick an operator:\n1. Add\n2. Subtract\n3. Divide\n4. Multiply ")
op = input("Enter 1-4: ")
num2 = float(input("Enter second number: "))

if op == "1":
    print(num1 + num2)
elif op == "2":
    print(num1 - num2)
elif op == "3":
    print(num1 / num2)
elif op == "4":
    print(num1 * num2)
else:
    print("Invalid operator")
