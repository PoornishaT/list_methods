myList_1 = ["cat", "rat", "cow", "horse"]
myList_2 = [10, 20, 40, 40]
# append function
myList_1.append("donkey")
print(myList_1)
# copy function
myList_3 = myList_2.copy()
print(myList_3)
# sum function
print(sum(myList_2))
# count function
print(myList_1.count("rat"))
# extend function
myList_3.extend(myList_1)
print(myList_3)
# insert function
myList_2.insert(2, 30)
# pop
myList_1.pop(3)
print(myList_1)
# calculates no. of elements
print(len(myList_2))
# returns the max and min elements
print(max(myList_2))
print(min(myList_2))
# removes the first occurance of it
myList_2.remove(40)
print(myList_2)
# sorts and reverse the list
myList_1.sort()
print(myList_1)
myList_1.reverse()
print(myList_1)
# removes all the element from list
myList_3.clear()
print(myList_3)
