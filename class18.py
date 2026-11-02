try:
 def add(a,b):
    return a + b
 def subtract(a,b):
    return a - b
 def multiply(a,b):
    return a * b
 def divide(a,b):
    return a // b
 num_1 = float(input("Enter a number: "))
 num_2 = float(input("Enter b number: "))
 operation = input("Pick an operation: add, subtract, multiply and divide.")
 if operation == "add":
   print(add(num_1,num_2))
 elif operation == "subtract":
    print(subtract(num_1,num_2))
 elif operation == "multiply":
    print(multiply(num_1,num_2))
 elif operation == "divide":
    print(divide(num_1,num_2))
 else:
    print("That is not an operation")
except ValueError:
   print("That was not a number!")
except ZeroDivisionError:
   print("You cannot divide with 0")
else:
   print("Here is your answer!")
finally:
   print("Thanks for using the calculator!")
