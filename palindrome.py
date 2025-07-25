def palindrome(s):
    rev=s[::-1]
    if s==rev:
        return "Palindrome"
    else:
        return "Not Palindrome"
s=input()
print(palindrome(s))

