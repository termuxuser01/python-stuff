#the second part
s = 1 
ref = 1

if s is ref:
    print("s is copy")
else:
    print("s is not copy")

t = 1
if t is s:
    print("t is s")
else:
    print("not")

print(1 != 2)
print(1 < 2 and 2 < 3)
print(1 > 2 and 3 < 2)
print(1 > 2 or 2 < 3)
x = [list(range(0, 11))]
print(x)
print(
    type(x)
    )
list(range(0, 101, 10))

i = 1

for letter in 'abcd':
    print("at {} you have {}".format(i,letter))
    i += 1
    if i == 5:
        print("limit reached")
        break
for i,l in enumerate('abcd'):
    print("at {} you have {} ".format(i,l))
f = list(enumerate('abcd'))
print(f)
