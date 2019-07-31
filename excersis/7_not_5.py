#s from 0-1000 dividible by 7 but not 5
def divide():
    for num in range(0, 1001):
        if num % 7 == 0:
            if num % 5 > 0:
                print(num)
            else:
                continue
        else:
            continue

divide()
