from module import listchanger
print("Insert 3 numbers")
a = int(input())
x = int(input())
y = int(input())
list = [a, x, y]
print(f"The values before the module runs is {list}")
listchanger(list)
print(f"These are the values after the listchanger module {list}")
