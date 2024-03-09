# Write a program to generate the Fibonacci sequence up to 100.

n = 100
n1 = 0
n2 = 1
count = 2
if n < 0:
    print("incorrect input")
elif n == 1:
    print(n1)
else:
    print(n1)
    print(n2)
    while count < n:
        n3=n1+n2
        print(n3)
        count +=1
        n1 = n2
        n2 = n3
