num = [20,40,3,4,333,1,50,100]
largest_num = num[0]
for i in num:
    if i > largest_num:
        largest_num = i

print(largest_num)

def largest_array(lst):
    max_num = lst[0]
    for i in lst:
        if i > max_num:
            max_num = i

    return max_num

list1 = list()
for i in range(0,5):
    val = input("enter the values for list:")
    list1.append(val)

print(list1)
largest_number = largest_array(list1)

print(largest_number)