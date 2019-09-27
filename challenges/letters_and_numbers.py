# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:

count = {
  "Letters": 0,
  "Numbers": 0,
}

for i in input("enter a sequence:\n"):
  if i.isdigit():
    count["Numbers"] += 1
  elif i.isalpha():
    count["Letters"] += 1

print("Letters: {}\nNumbers:{}".format(count["Letters"], count["Numbers"]))
