from random import randrange

f = open("./names.txt", "r")

rf = str(f.read()).split("\n")
num = randrange(len(rf))

print(rf[num])



