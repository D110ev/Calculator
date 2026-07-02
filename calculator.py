print("=== Simple Calculator ===")
print("Operations: +(add), -(subtract), *(multiplication), /(division)")
print("type 'exit' to quit")

while True:
    #get the first number
    user_input1 = input("Enter the first number: (or exit to quit)").strip()
    if user_input1.lower() == 'exit':
        break
    num1 = float(user_input1)
    #get the mathematical operator
    operation = input("Enter operation: ").strip()
    if operation.lower() == 'exit':
        break

    #get the second number 
    user_input2 = input("Enter the second number: (or exit to quit)").strip()
    if user_input2.lower()== 'exit':
         break
    num2 = float(user_input2)

    #perform the operation
    if operation == "+":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}\n")
    elif operation == "-":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}\n")
    elif operation == "*":
        result = num1*num2
        print(f"Result: {num1} * {num2} = {result}\n")
    elif operation == "/":
        if num2 == 0:
            print("Invalid: Division by 0 is not allowed")
            continue
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}\n")
    else:
        print("Invalid operation")
        continue

    #display the result
    