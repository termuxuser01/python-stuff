def animal_crakers(animal):
    a = list(animal)
    spacei = a.index(' ')
    b = a[:spacei]
    c = a[spacei:]
    if b[0] == c[0]:
        print("cracker passed")
    else:
        print("craker failed")

animal_crakers('hello world')
