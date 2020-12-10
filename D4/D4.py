with open("input.txt","r") as f: data=f.readlines()
# with open("test.txt","r") as f: data=f.readlines()
data = [x[:-1] for x in data]
dataProcessed = []
temp=[]
for i in data:
    if i== '':
        dataProcessed.append(temp)
        temp = []
    else:
        temp.extend([x.split(":") for x in i.split(" ")])
dataProcessed.append(temp)

valid = 0
terms = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
for i in dataProcessed:
    count = 0
    for x in i:
        if x[0] in terms:
            count += 1
    if count == 7:
        valid +=1
    
print(valid)