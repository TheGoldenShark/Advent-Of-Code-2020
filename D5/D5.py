with open("input.txt","r") as f: data=f.readlines()
data = [x[:-1] for x in data] 

max = 0
for i in data:
    row = int(i[:7].replace("F","0").replace("B","1"),2)
    column = int(i[-3:].replace("L","0").replace("R","1"),2)
    id = row * 8 + column
    if id>max: max=id

print(max)