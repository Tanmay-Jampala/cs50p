x = int(input("What's x? "))
y = input("Enter the operator: ")
z = int(input("What's y? "))

x, y, z = x, y.strip(), z

expression = f"{x} {y} {z}"
x, y, z = expression.split(" ")
if y == "/" and z == "0":
    print("Error: Division by zero is not allowed.")
else: 
    print(eval(expression))