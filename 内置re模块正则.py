import re
pattern='\d\.\d+'
s='i study python 3.11 every day python 2.7 i love'
match = re.match(pattern,s,re.I)
print(match)
s2='3.11Python'
match2=re.match(pattern,s2)
print(match2)

print(match2.start())
print(match2.end())
print(match2.span())
print(match2.string)
print(match2.group())

match3=re.search(pattern,s)
print(match3.group())
match4=re.findall(pattern,s)
print(match4)