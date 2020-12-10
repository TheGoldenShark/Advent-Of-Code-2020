with open("input.txt","r") as f: data=f.readlines()
data = [x[:-1] for x in data] 

max = 0
ids = set()
for i in data:
    row = int(i[:7].replace("F","0").replace("B","1"),2)
    column = int(i[-3:].replace("L","0").replace("R","1"),2)
    ids.add(row * 8 + column)

for i in range(0,127*8+7):
    if (i not in ids):
        if (i-1 in ids and i+1 in ids):
            print(i)
            exit()