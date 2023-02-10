def polindrome(s):
    return s == s[::-1]
s=str(input())
ans=polindrome(s)
if ans:
    print("Yes")
else:
    print("No")