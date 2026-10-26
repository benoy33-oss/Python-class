print("===============================")
print(" SHOPPING DISCOUNT CALCULATOR ")
print("===============================")
valid = False
while not valid:
    try:
        bill = float(input("Enter bill number: "))
        discount = float(input("Enter discount percent: "))
        n = int(input("Enter number of people: "))
        percent = (discount * bill) / 100
        gross_bill = bill - percent
        total = gross_bill / n
    except ValueError:
        print("Only type numbers")
    except ZeroDivisionError:
        print("You cannot divide ny 0")
    else:
        print("Total: ", gross_bill)
        print("Each person pays: ", total)
        valid = True
    finally:
        print("Attempt finished")
