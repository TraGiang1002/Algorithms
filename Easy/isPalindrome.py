def isPalindrome(x: int) -> bool:
    s = str(x)
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

# x = 121
# x = -121
x = 10
print(isPalindrome(x))