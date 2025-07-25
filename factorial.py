def factorial(n):
    if n==0:
        return 0
    if n==1:
        return 1
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
n=int(input())
print(f"Factorial Number is {factorial(n)}")

