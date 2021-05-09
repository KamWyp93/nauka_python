alkohole = ["piwo", "wino", "wodka"]
procenty = [4.5, 13, 40]

#for a in alkohole:
    #print(a)

for idx in range(len(alkohole)):
    if procenty[idx] < 25:
        print(alkohole[idx] + " ma " + str(procenty[idx]) + " procent")
    else:
        print(alkohole[idx] + " ma " + str(procenty[idx]) + " procent. Uwazaj z tym alkoholem")
