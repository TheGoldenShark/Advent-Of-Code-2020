with open("input.txt","r") as f: data=f.readlines()
d = [int(x[:-1]) for x in data] 
for i in d:
    for j in d:
        if (i+j == 2020):
            print(i*j)
            exit()