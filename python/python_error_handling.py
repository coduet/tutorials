
try:
    number = int(input("Enter a number : "))
    print(number)
    print(number/0)
except ZeroDivisionError: #multiple except to handle different types of errors
    print("Division by zero not allowed.")
except ValueError as error:
    print(error)