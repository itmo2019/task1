import re, sys;

s = ''
for line in sys.stdin:
    s += line

se = set()

for line in re.findall(r'{(.*?)}', s, re.DOTALL):
    for prop in re.findall(r'[a-zA-Z\-]*?:', line):
        se.add(prop)

print(se, len(se))