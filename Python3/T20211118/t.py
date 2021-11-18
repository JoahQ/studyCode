import re

# l1 = "Beautiful is better than ugly."
#
# matches = re.findall("beautiful", l1, re.IGNORECASE)
#
# print(matches)

zen = """Although never is 
often better than *right* now.
If the implementation 
is hard to explain, 
it's a bad idea.
If the implementation 
is easy to explain, 
it may be a good 
idea.Namespaces 
are one honking 
great idea -- let's 
do more of those!
"""

m = re.findall("^If", zen, re.MULTILINE)

print(m)

print("-"*10)

string = "Two too."
mm = re.findall("t[ow]o", string, re.IGNORECASE)

print(mm)

print("+"*11)

line = "123?34 hello?"
m = re.findall("\\d", line, re.IGNORECASE)
print(m)
print("".join(m))
