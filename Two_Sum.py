def (nums,target):
    seen={}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement],i]
        seen[num]=i
    return []
nums=list(map(int,input("Enter the Elements: ").split()))
target=int(input("Enter the Target Value: "))
print(Two_Sum(nums,target))
            
