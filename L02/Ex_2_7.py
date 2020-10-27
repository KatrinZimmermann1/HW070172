#exercise 7

def chaos(a):
    a = 3.9 * a * (1-a)
    return a

    

print("This Program ilustrates a chaotic function")
n = eval(input("How many numbers should I print? "))
x = eval(input("Enter a value between 0 and 1: "))
y = eval(input("Enter a different value between 0 and 1: "))
for i in range(n):
    x = chaos(x)
    y = chaos(y)
    print(x, y)
