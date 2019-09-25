


f = {}

def fib(n):
    if n <= 1:
        return n
    if n in f:
        return f[n]
    else:
        num = fib(n - 1) + fib(n - 2)
        return num
    f[n] = num

while True:
    fib_num = input("enter the fibonacci number to calculate:\n")
    if fib_num == "q":
        for k in f.keys():
            print("{} is {}".format(k, f[k]))
        break
    else:
        print(fib(int(fib_num)))
    

  
