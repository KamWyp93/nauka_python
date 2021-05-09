ptaki = ["papuga", "wrobel", "kaczka", "orzel"]

for p in ptaki:
    print(p)


for idx in range(len(ptaki)):
    if idx == 3:
        print(str(idx) + " " + ptaki[idx] + " duzy ptak")
    else:
        print(str(idx) + " " + ptaki[idx])
