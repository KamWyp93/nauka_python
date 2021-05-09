samolot = {"nazwa": "boeing",
           "przebieg": 10000,
           "type": "pasazerski"}

# magazyn = {"x01": "mleko", "x02": "kawa"}
#
# print(magazyn["x01"])
print(samolot["nazwa"])
print(samolot["przebieg"])
print(samolot["type"])

print("------------------------------")


for key in samolot:
    print(key + " " + str(samolot[key]))
