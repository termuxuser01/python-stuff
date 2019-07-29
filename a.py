a = 3*123.45
b = ['hello', 'how' , 'are', 'you']
c = 'mr' + ' ' + 'Fred' + ' ' + 'BLogger'
d, e, f, = 1, 2, 3
print(a, b, c, d, e, f)
x = 100
print(x)
x-=1
print(x)
x+=23
print(x)
x/=6
print(x)
x*=2.3
print(x)

g = False   
print(type(g))
print(type(b))
print(str(b))

h = int(2.0)
print(type(h))
i = str(2)
print(type(i))
j = dict(one=1, two=2)
print(type(j))

print(b[0])
print(b[-1])
b.insert(0, 'hi')
print(b)
print(len(b))
b.append(['i', 'am', 'ok'])
print(b)
print(len(b))
b.extend(['fine', 'thank', 'you'])
print(b)
print(len(b))

print(b[1:4])
print(b[:4])
print(b[4:])

b.index("how")
"how" in b
print(b)
b.remove("hi")
print(b)
b.pop()
print(b)
print(len(b))
b += ['you']
print(b)
b *= 2
print(b)
print(len(b))
b.pop(5)
print(b)

dict1 = { 
    'fred':'1010 Elm', 
    'ralph':'2020 Maple'
}
print(dict1)
dict1['irving'] = '2026 Fremont'
print(dict1)
dict1['fred'] = '1020 Elm'
print(dict1)
if 'fred' in dict1:
    print('yes');
dict1.get('ralph', 'not')
dict1.get('mark', 'does not exist')
dict2 = {'a':1, 'b':2, 'c':3, 'd':4}
for v in dict2.values():
    print(v)
for k in dict2.keys():
    print(k)
a = 202
b = 5
if a > b:
    print('a is greater')
a = 1.234
print(type(a))
b = 4
print(type(b))
float(b)
print(
     type(
         float(b)
         )
     )
print(
    float(b)
    )
if bool(23):
    print('yes')
import random
r = random.randint(5, 100)
print(r)
