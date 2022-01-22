first_number = 0
second_number = 1
fib= []

for i in range(0,10):
    if i<=1:
        result = i
    else:
        result = first_number+second_number
        first_number = second_number
        second_number = result
    print(result)
