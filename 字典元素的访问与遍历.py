d={'hello':10,'world':20,'python':30}
print(d['hello'])
print(d.get('hello'))

print(d.get('java'))
print(d.get('java','难受啊'))

for item in d.items():
    print(item)

for key,value in d.items():
    print(key,'---->',value)