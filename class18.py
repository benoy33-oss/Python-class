try:
 def add(a,b):
    return a + b
 def subtract(a,b):
    return a - b
 def multiply(a,b):
    return a * b
 def divide(a,b):
    return a // b
 a = float(input("Enter a number: "))
 b = float(input("Enter b number: "))
 operation = input("Pick an operation: add, subtract, multiply and divide.")
 if operation == add:
   print(add(a,b))
 if operation == subtract:
    print(subtract(a,b))
except ValueError:
   print("That was not a number!")
except ZeroDivisionError:
   print("You cannot divide with 0")
else:
   print("Here is your answer!")
finally:
   print("Thanks for using the calculator!")
