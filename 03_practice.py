price = int(input("Enter The Price of Doughnut:"))
quantity = int(input("Enter The quantity of Doughnut:"))

amount = price*quantity

if amount >= 1000:
    print(" YAy you have got a 10% discount on your order")
    discount = amount*10/100
    amount = amount-discount
else:
    amount < 1000
    print("you got a 5% discount")
    discount = amount*5/100
    amount = amount-discount

print("Your total amount is", amount)
