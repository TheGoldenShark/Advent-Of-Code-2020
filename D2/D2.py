import re
with open("input","r") as f: data=f.readlines()
d = [[z for z in y if z != ''] for y in [re.split("\s|-|:|\n", x) for x in data]]
out = 0
for i in d:
    c = i[3].count(i[2])
    if (c >= int(i[0]) and c <= int(i[1])):
       out +=1
print(out) 