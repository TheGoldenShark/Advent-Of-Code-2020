import string

with open("input.txt","r") as f: data=f.readlines()
# with open("test.txt","r") as f: data=f.readlines()
# with open("test2.txt","r") as f: data=f.readlines()
# with open("test3.txt","r") as f: data=f.readlines()
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

eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
numbers  = ["0","1","2","3","4","5","6","7","8","9"]

valid = 0
for i in dataProcessed:
    count = 0
    for x in i:
        if x[0] == "byr":
            if (int(x[1]) >= 1920 and int(x[1]) <= 2002):
                count += 1
        elif x[0] == "iyr":
            if (int(x[1]) >= 2010 and int(x[1]) <= 2020):
                count += 1
        elif x[0] == "eyr":
            if (int(x[1]) >= 2020 and int(x[1]) <= 2030):
                count += 1
        elif x[0] == "hgt":
            if x[1][-2:] == "in":
                if (int(x[1][:-2]) >= 59 and int(x[1][:-2]) <= 76):
                    count +=1
            elif x[1][-2:] == "cm":
                if (int(x[1][:-2]) >= 150 and int(x[1][:-2]) <= 193):
                    count +=1
        elif x[0] == "hcl":
            if x[1][0] == "#" and len(x[1]) == 7 and set(x[1][1:]).intersection(set(numbers).union(set(list(string.ascii_lowercase)))) == set(x[1][1:]):
                count +=1
        elif x[0] == "ecl":
            if x[1] in eyeColors:
                count+=1 
        elif x[0] == "pid":
            if (len(x[1]) == 9 and set(x[1]).intersection(numbers) == set(x[1])):
                count +=1
    if count == 7:
        valid +=1
    
print(valid)