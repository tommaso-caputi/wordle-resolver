import pickle

f = open("280000_parole_italiane.txt", "r")
temp = []
c = 0
for word in f:
    if len(word) == 6:
        c += 1
        temp.append(word)
print(temp)
print(c)
with open("parole", "w") as file:
    for word in temp:
        file.write(word)
