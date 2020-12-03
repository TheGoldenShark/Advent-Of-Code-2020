with open("input.txt","r") as f: data=f.readlines()
data = [x[:-1] for x in data] 
moves = [[1,1],[3,1],[5,1],[7,1],[1,2]]
out = 1
for i in moves:
    c = 0
    x = 0
    y = 0
    while (y!=len(data)-1):
        x = (x + i[0]) % len(data[1])
        y += i[1]
        if data[y][x] == '#': c+=1
    out *= c
print(out)