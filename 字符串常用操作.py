s='rfgSF'
print(s.lower())
print(s.upper())
print(s.split('f'))
print(s.count('f'))
print(s.find('F'))
# print(s.index('2'))
print(s.startswith("f"))
print(s.endswith("w"))

print(s.replace("f","w"))

print(s.center(20,'-'))

s='  244 424   '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s='rjkegoel'
print(s.lstrip('rj'))
print(s.rstrip('el'))