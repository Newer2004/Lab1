"""
def IsPolindrome(s,r):
    if(s==r):
        print("Polindrome")
    else:
        print("Not polindrome")
s=input()
r=s[::-1]
IsPolindrome(s,r)
"""
my_str = input()
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")