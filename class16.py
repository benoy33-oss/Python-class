"""try:
    number = int(input("Enter a number: "))
    print("The number entered is", number)
#using value error
except ValueError as ex:
    print("Exception:", ex)"""

"""try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by zero is error !!")
except ValueError:
    print("Please enter valid whole numbers")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")"""

valid = False
while not valid:
    try:
        n = int(input("Enter a number: "))
        while n % 2 == 0:
            print("bye")
            n = int(input("Enter a number: "))
        valid = True
    except ValueError:
        print("Invalid")
