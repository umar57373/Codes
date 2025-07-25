def (n):
    arr = []
    a, b = 0, 1
    for _ in range(n):
        arr.append(a)
        a, b = b, a + b
    return arr

n = int(input("Enter the number of terms: "))
print(f"Fibonacci series is {fibonacci(n)}")
