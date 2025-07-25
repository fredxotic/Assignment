first_input = int(input("Enter the first number: "))
second_input = int(input("Enter the second number: "))
calculation = input("Enter the operation (+, -, *, /): ")

if calculation == "+":
    result = first_input + second_input
elif calculation == "-":
    result = first_input - second_input
elif calculation == "*":
    result = first_input * second_input
elif calculation == "/":
    result = first_input / second_input
else:
    result = "Invalid operation"

print(f"{first_input} {calculation} {second_input} = {result}")