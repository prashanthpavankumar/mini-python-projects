a=(input("Enter a number or string: "))
def palindrome(n):
    rev = n[::-1]
    return rev
print(f"The Number or string is {a} if its reversed it will be {palindrome(a)}")
if a == palindrome(a):
    print(f"{a} is a palindrome")
else:
    print(f"{a} is not a palindrome")

