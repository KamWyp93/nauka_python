samochody = ["syrena", "polonez"]

print(samochody[0])
print(samochody[1])

#print(samochody[3])

for s in samochody:   # to s to jest zmienna, moze miec dowolna nazwe
    print(s)

for idx in range (len(samochody)):
    print("idx: " + str(idx) + " : " + samochody[idx])
