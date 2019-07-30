def animal_crakers(animal):
    a = list(animal)
    spacei = a.index(' ')
    b = a[:spacei]
    c = a[spacei+1:]
    if b[0] == c[0]:
        print("cracker passed")
    else:
        print("craker failed")

animalselec = input("select an animal to test: ")
animal_crakers(animalselec)

