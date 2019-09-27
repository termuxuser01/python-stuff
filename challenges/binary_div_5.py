# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input 
# and then check whether they are divisible by 5 or not. 
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.

def val_check(bin_nums):
  for i in bin_nums.split(","):
    for n in i:
      if n != "1" and n != "0":
        print("BINARY!!!")
        bin_acc()
    if len(i) > 4:
      print("FOUR DIGITS!!!")
      bin_acc()
    elif int(i, 2) % 5 == 0:
      print(i, end=",")


def bin_acc():
    bin_nums = input("write a list of four digit binary numbers:\n")
    val_check(bin_nums)

bin_acc()



