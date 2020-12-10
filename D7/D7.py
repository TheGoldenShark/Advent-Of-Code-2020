# with open("input.txt","r") as f: data=f.readlines()
with open("test.txt","r") as f: data=f.readlines()
data = [[y.replace(".", "").replace(" bags", "").replace(" bag", "").split(", ") for y in x[:-1].split(" contain ")] for x in data] 
for i in range(0, len(data)):
    for j in range(0, len(data[i][1])):
        data[i][1][j] = data[i][1][j].split(" ", 1)

start = "shiny gold"
currentBags = set([start])
children = set()
bagsCount = 1

while (len(currentBags) > 0):
    for i in data:
        if i[0][0] in currentBags:
            for k in i[1]:
                if k[0] != 'no':
                    children.add(k[1])
                    bagsCount *= int(k[0])
    currentBags = set(children)
    children = set()

print(bagsCount)