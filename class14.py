def total_calc(bill_amount, tip_perc):
    # define function to calculate the tip on bill
    total = bill_amount*(1 + 0.01*tip_perc)
    total  = round(total,2)
    print(f"Please pay ${total}")

# specify only bill_amount
# default value of tip percentage is used

total_calc(1000,10)

def cube(number):
    return number*number*number

# define a function which will execute cube function if the user entered number is divisible by three
def by_three(number):
    if number %3 ==0:
        return cube(number)
    else:
        return False
# display result
print(by_three(27))
print(by_three(35))

def factorial(x):
    """this is a recursive function to find the factiorial of an integer"""

    if x==0 or x==1:
        return 1
    else:
        #calling function inside a function
        return x*factorial(x-1)
#display result
print(factorial.__doc__)
print("the factorial of 0:",factorial(0))
print("the factorial of 1:",factorial(1))
print("the factorial of 2:",factorial(2))
print("the factorial of 3:",factorial(3))
print("the factorial of 4:",factorial(4))
print("the factorial of 5:",factorial(5))
print("the factorial of 10:",factorial(10))