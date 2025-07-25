def (n):
    s=str(n)
    summ=0
    for i in s:
        summ+=int(i)
    return summ
n=input("enter the digits: ")
print(f"sum of digits: {sum_of_digits(n)}")
