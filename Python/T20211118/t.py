import re

l1 = "Beautiful is better than ugly."

matches = re.findall("beautiful", l1, re.IGNORECASE)

print(matches)
