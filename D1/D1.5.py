with open("input.txt","r") as f: data=f.readlines()
d = [int(x[:-1]) for x in data] 
out = 1
for i in d:
    for j in d:
        for k in d:
            if (i+j+k == 2020):
                print(i*j*k)
                exit()