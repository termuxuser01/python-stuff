#here we will try some loops#
x = 0
while x <= 10:
    if x == 0:
        print("x is equal to zero")
    elif x % 2 == 0:
        print("x is even")
        print(x)
    else:
        print("x is odd")
        print(x)
    x += 1
lt1 = [(1, 2), (1, 3), (4, 6)]
print(
    type(lt1)
    )
print(
    type(lt1[1])
    )
for a in lt1:
    print(a)
y = 0
while y == y:
    if y == 0:
        print("y is equal to zero")
    elif y % 2 == 0:
        print("y is even")
        print(y)
    elif y > 10:
        print("funcion limit reached")
        break
    else:
        print("y is odd")
        print(y)
    y += 1
print("break worked")

inpt = int(input("enter a number"))
nl = [1 , 4, 6, 45, 87, 68, 98, 7]
for num in nl:
    if num == inpt:
        print("number exists")
        break
else: 
    print("number doesnt exit")
