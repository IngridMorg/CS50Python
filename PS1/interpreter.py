string = input("Expression: ")
# split the input
expression = string.split()
print(expression)
# we need to determine the operator
x = int(expression[0])
z = int(expression[2])
print(expression[1])
match expression[1]:
    case '+':
        n = x + z
        print(n)
    case '-':
        n = x - z
        print(n)
    case '*':
        n = x * z
        print(n)
    case '/':
        n = x / z
        print(n)
    case _:
        print("Invalid input")
