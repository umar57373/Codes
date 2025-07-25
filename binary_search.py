def (arr,Key):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==Key:
            return mid
        elif arr[mid]>Key:
            high = mid-1
        else:
            low = mid+1
    return -1
arr=list(map(int,input("Enter the Sorted Elements: ").split()))
Key = int(input("Enter the Key Value: "))
print(binary_search(arr,Key))
