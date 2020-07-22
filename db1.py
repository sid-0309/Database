import csv


def csv_open(x):
    a = open(x + ".csv", "w")
    a.close()

def slct():
    return

def insert():
    return

def create(args):

    if cm_par[1] == "table":
        name = cm_par[2]
        csv_open(name)
        print ("Table ", name, " created")
        return 
    if cm_par[1] == "db":
        print("Not yet availabe")
        return

exitcode = 0

coms = {
    "create":create,
    "select":slct,
    "insert":insert
    }

while exitcode == 0:
    cm = input(">")
    cm_par = cm.split()
    
    for i in coms.keys():
        if i == cm_par[0]:
            coms[i](cm_par[1:])
        else:
            exitcode =1