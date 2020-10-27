#exercise 4

print("This Program ilustrates a chaotic function")
x = eval(input("Enter Number between 0 and 1:"))
for i in range(20):
    x = 2.0 * x * (1-x)
    print(x)
