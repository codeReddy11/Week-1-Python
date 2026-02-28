i=100
s= str(i)
print(type(s))

s= "Mathematics"
list1 = list(c.upper() for c in s)
set1 = set(c.upper() for c in s)
print(list1)
print(set1)
print(sorted(list1))
print(sorted(set1))


numbers = [5, 2, 9, 1]
print(sorted(numbers))          # ascending
print(sorted(numbers, reverse=True))  # descending

x = 3.14159
print(round(x))
print(round(x, 3))

x = -10.5   
print(abs(x))


t= (1,1,3,3,5,6)
s = {1,1,3,3,5,6}
print(sum(s), sum(t), min(t), max(s))
print(type(s), type(t))

d = dict([('Name','Raj'), ('Age',23), ('Voted', 'Yes')])
print(d)
print(type(d))
for key, value in d.items():
    print(f"key: {key}, value: {value}, Type: {type(value)} ")  # f strings

