# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input 
# and then check whether they are divisible by 5 or not. 
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.

def bin_acc():
    global bin_nums
    bin_nums = input("write a list of four digit binary numbers:\n")

bin_acc()
while True:
    try:
        for i in int(bin_nums.split(",")):
            for n in i:
                if int(n) != 1 or int(n) != 0:
                    print("BINARY!!!")
                    bin_acc()
            if len(i) > 4:
                print("FOUR DIGITS!!!")
                bin_acc()
            elif int(i) % 5 == 0:
                print(i, end=",")
            else:
                continue
    except ValueError:
        print("HMMMMM...")
        bin_acc()
    except TypeError:
        print("HMMMMM...")
        bin_acc()

    break
