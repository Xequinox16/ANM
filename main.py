import os
import time
from datetime import datetime
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
ANM = []

os.system("title ANM")


def save():
        global ANM
        try:
            with open('ANM.json', 'w') as f:
                json.dump(ANM, f)
        except:
            pass


def load():
        global ANM
        try:
            with open('ANM.json', 'r') as f:
                ANM = json.load(f)
        except:
            ANM = []
            save()

def clear():
    os.system("cls")


def StringSplitList(x,y):
    string=""
    firstLoop = True
    for i in x:
        if firstLoop == True:
            string+=str(i)
        else:
            string+=str(y)+str(i)
        firstLoop = False
    return(string)


def getDate():
    year = time.strftime("%Y")
    day = time.strftime("%d")
    month = time.strftime("%m")
    return([year,month,day])

def view():
    if len(ANM) <= 0:
        print("Theres nothing to view!")
        input()
        menu("start")
    else:
        clear()
        for i in range(0,len(ANM)):
            firstIrit = True
            print(ANM[i][0])
            for y in ANM[i]:
                if firstIrit == True:
                    firstIrit = False
                else:
                    print("           "+str(y))
        input()
        menu("start")


def add():
    global ANM
    clear()
    print("-"*20)
    print("[1]: Add User")
    print("[2]: Add Entry")
    print("[3]: Return")
    print("-"*20)
    choice = input("[]>")
    try:
        choice = int(choice)
    except:
        add()

    if choice == 2:
        if len(ANM) <= 0:
            print("Theres nothing to add to!")
            input()
            add()
        print("-"*20)
        for i in range(0,len(ANM)):
            print("["+str(i+1)+"]: "+ANM[i][0])
        print("-"*20)
        Pog = input("Select A Pog: ")
        try:
            Pog = int(Pog)
        except:
            add()
        Pog = Pog-1
        clear()
        print("-"*20)
        print("Follow This Format: 10,20")
        print("-"*20)
        entry = input("Enter a new entry: ")
        entry = entry.split(",")
        if len(entry) <= 0:
            add()
        elif len(entry) > 2:
            add()
        try:
            int(entry[0])
            int(entry[1])
        except:
            add()
        date = getDate()
        date = StringSplitList(date,"/")
        entry.append(date)
        ANM[Pog].append(entry)
        save()
        print("Finished!")
        input()
        add()
    elif choice == 1:
        clear()
        print("-"*20)
        print("Enter A Name: ")
        print("-"*20)
        inpuut = input("[]> ")
        ANM.append([str(inpuut)])
        print("Pog Added.")
        input()
        add()
    elif choice == 3:
        menu("start")
    else:
        add()


def plural(x):
    if x == 1 or x == -1:
        return("")
    else:
        return("s")


def stats():
    load()
    if len(ANM) <= 0:
        print("Theres no data!")
        input()
        menu("start")
    clear()
    print("/"*40)
    for i in range(0,len(ANM)):
        pack = []
        pack.append(ANM[i][0])
        pog = ANM[i]
        for y in range(1,len(pog)):
            pack.append(pog[y][0])
            pack.append(pog[y][1])

        numbers = []
        top = 0
        topCount = 0
        for y in range(1,len(pack)):
            numbers.append(int(pack[y]))
        for y in range(1,len(pack)):
            if numbers.count(int(pack[y])) > top:
                top = int(pack[y])
                topCount = numbers.count(int(pack[y]))

        print(pog[0])
        print("             Most Frequent Number: ["+ str(top) + "] Occurences: [" + str(topCount)+"]")
    print("/"*40)
    input("Press Any Key To Continue.")
    menu("start")
    """
    data = []
    for i in range(0,len(ANM)):
        data.append([str(ANM[i][0])])
        for y in range(1,len(ANM[i])):
            data[i].append(ANM[i][y][0])
            data[i].append(ANM[i][y][1])
        numbers = []
        for z in range(0,len(data)):
            for y in range(1,len(data[z])):
                try:
                    numbers.append(int(data[z][y]))
                except:
                    pass

        mostFrequent = 0
        Occurences = 0
        for y in numbers:
            if numbers.count(y) > mostFrequent:
                mostFrequent = y
                Occurences = numbers.count(y)
        print(ANM[i][0])
        print("             This Pog's Most Frequent Number Is: " + str(mostFrequent) + " , With " + str(Occurences)+" Occurence" + plural(Occurences) + "!")
    input()
        """




def menu(x):
    load()
    global ANM
    clear()
    def start():
        print("-"*20)
        print("[1]: View")
        print("[2]: Add")
        print("[3]: Remove")
        print("[4]: Stats")
        print("-"*20)
        choice = input("[]:> ")
        try:
            choice = int(choice)
        except:
            menu("start")
        if choice == 1:
            view()
        elif choice == 2:
            add()
        elif choice == 3:
            pass
        elif choice == 4:
            stats()
        else:
            menu("start")
    exec(str.lower(x)+"()")
menu("start")
