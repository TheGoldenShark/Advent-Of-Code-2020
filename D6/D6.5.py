import string

with open("input.txt","r") as f: data=f.readlines()
data = [x[:-1] for x in data]
dataProcessed = []
temp=set(string.ascii_lowercase)
for i in data:
    if i== '':
        dataProcessed.append(temp)
        temp=set(string.ascii_lowercase)
    else:
        temp = temp.intersection(set(i))
dataProcessed.append(temp)

count = 0
for i in dataProcessed:
    count += len(i)

print(count)