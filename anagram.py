def anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return "Anagram"
    else:
        return "Not Anagram"
s1=input("Enter the String1")
s2=input("Enter the String2")
print(anagram(s1,s2))
