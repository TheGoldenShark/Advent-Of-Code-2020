with open("input.txt","r") as f: data=f.readlines()
d = [x[:-1] for x in data] 
x = 0
y = 0
c = 0
while (y!=len(data)-1):
    x = (x + 3) % len(data[1])
    y += 1
    if data[y][x] == '#': c+=1
print(c)