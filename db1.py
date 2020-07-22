import csv

global f


def csv_open(a):
    return open(a + ".csv", "w")


#def csv_close():
#    return close()

def write(a, b):
    f = csv_open(a)
    csvwriter = csv.writer(f)
    csvwriter.writerow(b)
    f.close()
    
def slct():
    return

def insert(a, b = "", c = 1):
    if c == 0:
        write(a, b)
        return

    if c == 1 and a[1] == "into":
        write(a[2], a[3:])

def create(args):

    if cm_par[1] == "table":
        name = cm_par[2]
        csv_open(name)
        print ("Table ", name, " created")

        if len(cm_par) > 3:
            headers = cm_par[3:]
            insert(name, headers, 0)
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