import random
a = ''
b = ''
c = ''
d = []
e = []
f = []
cmd = '0'
z = 0
print("Welcome to offconsole! Read document with comands before use.")
while cmd != '':
    cmd = input("Your command:")
    if cmd == "write":
        yourgroup = input("Select group(a, b or c): ")
        yourtext = input("Text: ")
        if yourgroup == "a":
            a.append(yourtext)
        elif yourgroup == "b":
            b.append(yourtext)
        else:
            c.append(yourtext)
        print("Successfully!")
    if cmd == "check":
        yourgroup = input("Select group: ")
        if yourgroup == "a":
            print(a)
        elif yourgroup == "b":
            print(b)
        else:
            print(c)
            if yourgroup == "d":
                print(d)
            elif yourgroup == "e":
                print(e)
            elif yourgroup == "f":
                print(f)
            elif yourgroup == newgroup:
                print(newgroupcol)
    if cmd == "gen":
        x = int(input("first: "))
        y = int(input("second: "))
        gen = random.randint(x,y)
        yourgroup = input("Select group(d, e or f): ")
        if yourgroup == "a":
            d.append(gen)
        elif yourgroup == "b":
            e.append(gen)
        else:
            f.append(gen)
        print("Successfully!")
    if cmd == "new":
        newgroup = input("Group name(you are creating a list of 3 cells): ")
        newgroupcol = [[] for i in range(3)]
        print("Successfully!")
    if cmd == "fill":
        col = int(input("How many cells would you like to fill per one time: "))
        for i in range(col):
            inf = input("What you would like to write?: ")
            newgroupcol[z].append(inf)
            z += 1
        print("Successfully!")
    if cmd == "fillspecial":
        colspec = int(input("What cell would you like to fill: "))
        inf = input("What would you like to write?: ")
        newgroupcol[colspec].append(inf)
        print("Successfully!")
    if cmd == "credits":
        print("Noobisbro, 2021.")
    



        
    


        
        

