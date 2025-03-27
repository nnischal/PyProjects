def get_number(number): 
    while True:
        operand1 = input("Number " + str(number) + ": ") # Get the number from user
        try:
            return float(operand1)
            
        except:
            print("Invalid number")
    return operand1

operand1 = get_number(1)  # Get the first number from user
operand2 = get_number(2) # Get the second number from user

sign = input("Sign: ") # Get the sign from user

result = 0
if sign == "+":
    result = (operand1) + (operand2)
elif sign == "-":
    result = (operand1) - (operand2)
elif sign == "*":
    result = (operand1) * (operand2)
elif sign == "/":
    if (operand2) != 0:
        result = (operand1) / (operand2)
    else: 
        print("Division by zero is not allowed")
print(result) 