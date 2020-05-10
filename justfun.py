from module import listchanger
from module import just_copied
print("Insert 3 numbers")
#TODO Make this look better
a = int(input())
x = int(input())
y = int(input())
list = [a, x, y]
print(f"The values before the module runs is {list}")
listchanger(list)
print(f"These are the values after the listchanger module {list}")

print("Insert some text please")
text = str(input())
just_copied(text)

