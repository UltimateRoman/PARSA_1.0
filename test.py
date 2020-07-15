import csv, time

memno = 0
dictr = []
nmlist = []
mlist = []
flist = []
print("Welcome to Athul's CPADRS")
fln = input("Date:")
file = open("data/"+fln+".csv", "r")
read1 = csv.DictReader(file)
fnames = read1.fieldnames
read1 = csv.reader(file)
for i in read1:
    list1 = {}
    for j in range(len(fnames)):
        if i[j]:
            list1[fnames[j]] = i[j]
    dictr.append(list1)
for n in dictr:
    mbs = int(n['No of members'])
    if mbs+memno >= 10:
        mbs = 10-memno
    memno += mbs
    for count in range(mbs):
        list2 = {}
        list2["Name"] = n["Name"+str(count+1)]
        list2["Gender"] = n["Gender"+str(count+1)]
        list2["Age"] = n["Age"+str(count+1)]
        list2["Family Name"] = n["Family Name"]
        list2["Contact"] = n["Contact No"]
        nmlist.append(list2)
        if list2["Gender"] == "Male":
            mlist.append(list2)
        elif list2["Gender"] == "Female":
            flist.append(list2)
    if memno == 10:
        break

mlist = sorted(mlist, key=lambda k: k['Age']) 

flist = sorted(flist, key=lambda k: k['Age']) 

def telldate():
    return fln

def expm():
    return mlist

def expf():
    return flist
