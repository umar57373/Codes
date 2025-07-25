def count_vowels(s):
    vowels={'a','e','i','o','u'}
    v=0
    c=0
    st=s.strip()
    for i in st:
        if i in vowels:
            v+=1
        else:
            c+=1
    return v,c
s=input()
res=count_vowels(s)
print(res)
