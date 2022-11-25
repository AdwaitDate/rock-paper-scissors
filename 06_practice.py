list1 = [["harry", 1], ["larry", 2], ["carry", 3], ["marie", 23]]
for lollipops, item in list1:
    if type(item) == int:
        if item > 6 or type(item) == bool:
            print(item)
# print(item)
