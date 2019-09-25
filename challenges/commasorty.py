# Write a program that accepts a comma separated sequence of words as input 
#and prints the words in a comma-separated sequence after sorting them alphabetically.

str1 = input("enter a comma seperated list of words:\n")

for w in sorted(str1.split(",")):
    print(w, end=",")
