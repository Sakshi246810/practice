n = int(input("enter the number : "))
temp=0
for i in range(2,n//2):
    if(n%i == 0):
        temp = 1
        break

if temp == 1:
    print("given number is a not prime number")
else:
    print("given number is a prime number")


def prime(x, y):
    prime_list = []
    for i in range(x, y):
        for j in range(2, int(i / 2) + 1):
            if i % j == 0:
                break
        else:
            prime_list.append(i)

    return prime_list

lst = prime(2, 15)
print("The prime numbers in this range are: ", lst)






