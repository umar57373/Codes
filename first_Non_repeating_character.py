def (s):
    seen={}
    for i in s:
        seen[i] = seen.get(i,0)+1
    for i in s:
        if seen[i]==1:
            return i
    return "All Characters Are Repeated"
s=input()
print(first_Non_repeating_character(s))
