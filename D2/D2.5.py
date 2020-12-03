import re
with open("input","r") as f: data=f.readlines()
d = [[z for z in y if z != ''] for y in [re.split("\s|-|:|\n", x) for x in data]]
out = 0
for i in d:
    if ((i[3][int(i[0])-1] == i[2]) != (i[3][int(i[1])-1] == i[2])):
        out+=1
print(out) 