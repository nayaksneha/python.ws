'''Write a program to print the Fibonacci series up to the number 34. '''
fib1 = 0
fib2 = 1
print(fib1)
print(fib2)
for i in range(2,10):
    fib = fib1+fib2
    fib1=fib2
    fib2=fib
    print(fib)
