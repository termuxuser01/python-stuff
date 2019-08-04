def nemo(str1):
	a = len(str1)
	b = 0
	for x in range(0, a-1):
		if str1[x] == " ":
			b += 1
		if str1[x] == "n" or str1[x] == "N":
			if str1[x+1] == "E" or str1[x+1] == \
			" E":
				if str1[x+2] == "m" or str1[x+2]\
				== "M":
					if str1[x+3] == "o" or str1[x+3]\
					== "O":
						print(b)
						break
		else:
			continue
phrase = input("enter sentence to find nemo: ")
nemo(phrase)
