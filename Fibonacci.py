# Python code for Fibonacci seqence
def fibonacci(n):
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b


print('FIBANOCCI SEQUENCE')
n = int(input("ENTER THE RANGE OF FIBANOCCI SEQUENCE"))
fibonacci(n)
