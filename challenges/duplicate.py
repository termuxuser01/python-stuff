# rite a program that accepts a sequence of whitespace separated words as input
#  and prints the words after removing all duplicate words and sorting them alphanumerically.

str1 = input("enter whitspace seperated words:\n")

print(sorted(list(set(str1.split(" ")))))
