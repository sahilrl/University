#leetcode submission

from re import sub

s = 'A man, a plan, a canal: Panama'

def isPalindrome(s):
    pat=r"[^A-Za-z0-9]+"
    s = sub(pat, "", s).lower()
    print("The string is:",s)
    return s == s[::-1]
print(isPalindrome(s))

