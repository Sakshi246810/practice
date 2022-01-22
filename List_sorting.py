#sorting using built-in function

list1 =[2,3,4,5,9,510,48,58]
list2 = list1.sort()
print(list2)
print(sorted(list1, reverse=True))

#even number using list comprehesion

list_even = [i for i in list1 if i % 2 == 0]
print("even list is " ,list_even)

#sorting using for loop
for i in range(0,len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] < list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp

print(list1)