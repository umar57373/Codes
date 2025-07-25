def (s):
    seen={}
    for i in s:
        seen[i] = seen.get(i,0)+1
    return seen
s=list(map(int,input("Enter the Elements: ").split()))
print(f"Frequencys is: {Frequecy_of_elements(s)}")
