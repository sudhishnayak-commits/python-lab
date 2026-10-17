l1=['red',10,'orange',30,'blue'] 
print(l1)
l1.append(40)
l1.append('grey')
print(l1)
l1.insert(1,5)
l1.insert(2,'green')
print(l1)
l1.extend([40,'violet'])
print(l1)
l1[2]='pink'
print(l1)
mixed_one=[]
mixed_two=[]
for item in l1:
    if isinstance(item,(int,float)):
        mixed_one.append(item)
    else:
        mixed_two.append(item)
print('mixed_one=',mixed_one)
print('mixed_two=',mixed_two)
