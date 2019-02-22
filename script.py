import re, sys;

s = ''
for line in sys.stdin:
    s += line

se = set()
rules = 0

rules_nests = re.findall(r'{(.*?)}', s, re.DOTALL);

for line in rules_nests:
    for prop in re.findall(r'[a-zA-Z\-]*?:', line):
        rules+=1
        se.add(prop)

print('уникальные правила: ', se)
print('правил: ', rules)
print('уникальных правил: ', len(se))
print('уникальных блоков правил: ', len(rules_nests))