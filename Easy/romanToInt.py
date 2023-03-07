def romanToInt(s: str) -> int:
    answer = 0
    num = 0
    tmp = 0
    count = len(s) - 1
    while (count >= 0):
        if(s[count - 1] == 'I'):
            num = 1
        if (s[count - 1] == 'V'):
            num = 5
        if (s[count - 1] == 'X'):
            num = 10
        if (s[count - 1] == 'L'):
            num = 50
        if (s[count - 1] == 'C'):
            num = 100
        if (s[count - 1] == 'D'):
            num = 500
        if (s[count - 1] == 'M'):
            num = 1000
        if (num < tmp):
            answer -= num
        else:
            answer += num
        tmp = num
    return answer
s = "III"
# s = "LVIII"
# s = "MCMXCIV"
print(romanToInt(s))