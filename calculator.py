def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x/y

print("Welcome to the calculator.")
print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")

operation = input("Select an operation: (1, 2, 3, or 4)")
num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))

if operation == '1':
    print(num1," + ",num2," = ",add(num1, num2))
elif operation == '2':
    print(num1," - ", num2," = ",subtract(num1, num2))
elif operation == '3':
    print(num1," * ",num2," = ",multiply(num1, num2))
elif operation == '4':
    print(num1,"/",num2," = ",divide(num1, num2))
else:
    print("Invalid entry. :(")
