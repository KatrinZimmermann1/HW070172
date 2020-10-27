#exercise 5

print("This Program ilustrates a chaotic function")
x = eval(input("Enter Number between 0 and 1: "))
n = eval(input("How many numbers should I print? "))
for i in range(n):
    x = 2.0 * x * (1-x)
    print(x)
