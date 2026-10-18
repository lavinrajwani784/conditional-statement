lst = ["apple","bannana","guvava","mango","kiwi"]

print("length of the list: " ,len(lst))
print("first element of the list: " ,lst[0])
print("last element of the list: " ,lst[-1])

lst.append("watermelon")
print("updated list: ",lst)

lst.remove("kiwi")
print("updated list: ",lst)

lst.sort()
print("updated list: ",lst)

lst.pop(2)
print("updated list: ",lst)

lst.reverse()
print("updated list: ",lst)

print("multiplication: ",lst*2)

print("sliced: ",lst[:4])

lst.clear()
print("updated list: ",lst)