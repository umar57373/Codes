def (arr):
    num=set(arr)
    n=1
    while n in num:
        n+=1
    return n
arr=list(map(int,input("Enter the Array: ").split()))
print(f"Missing Number is: {missing_num(arr)}")
