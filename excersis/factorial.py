a = input("enter a number: ")
num = int(a)
def factorial(num):
  f = 1
  while num > 0:
    f *= num
    num -= 1
    if num == 0:
      print(f)
    else:
      continue
  
factorial(num)
