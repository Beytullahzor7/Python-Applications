def küpleri_al():

    for i in range(1,6):
        yield (i*i*i)

generator = küpleri_al()
print("SAYILARIN KÜPLERİ")
print("-------------------")

iterator = iter(generator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print("-------------------")


