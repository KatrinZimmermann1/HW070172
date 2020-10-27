#orginal

print("This Program ilustrates a chaotic function")
x = eval(input("Enter Number between 0 and 1: "))
for i in range(10):
    x = 3.9 * x * (1-x)
    print(x)

#exercise 3

print("This Program ilustrates a chaotic function")
x = eval(input("Enter Number between 0 and 1: "))
for i in range(10):
    x = 2.0 * x * (1-x)
    print(x)


#using 3.9: x is chaotic

#using 2.0: x is incremental and always converge to 0.5 
