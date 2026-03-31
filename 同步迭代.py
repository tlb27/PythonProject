from unittest import case

fruits=['apple','banana','orange','pear']
counts=[1,3,42,56]
for f,c in zip(fruits,counts):
    match f,c:
        case 'apple',1:
            print('1个苹果')
        case 'banana',3:
            print('3个香蕉')
        case 'orange',42:
            print('42个橘子')
        case 'pear',56:
            print('56个等分')