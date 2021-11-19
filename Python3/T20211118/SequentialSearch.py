# -*- coding: utf-8 -*-


def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found


number = range(0, 100)
s1 = ss(number, 2)
print(s1)
s2 = ss(number, 200)
print(s2)
print("---"*15)
print()


def palindrome(word):
    """回文词"""
    word = word.lower()
    return word[::-1] == word


print(palindrome("Mother"))
print(palindrome("Mon"))
print("abcd"[::-1])
