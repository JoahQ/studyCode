# -*- coding: utf-8 -*-
import re


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
print()


def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)


print(anagram("and", "andf"))
print(anagram("live", "evil"))
print()
print("count_characters")


def count_characters(string):
    count_dict = {}
    str2 = re.findall("[A-Za-z]", string.lower())
    for c in sorted(str2):
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)
    print(dict(sorted(count_dict.items(), key=lambda d: d[1], reverse=True)))


count_characters("Dynasty")
ssss = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

count_characters(ssss)
