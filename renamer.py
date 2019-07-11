import os
path = input("Input path (use two slashes when you type out the directory. Ex: C:\\path\\otherpath\\thepathafterthat: ")

def listdirectory():
    i = 0
    pdflist = os.listdir(path)
    for i in range(0,len(pdflist)):
        print(i, "-", pdflist[i])

def openfile(x):
    pdflist = os.listdir(path)
    os.chdir(path)
    open(pdflist[x])
    rn = input("What do you want to rename it to?")
    os.rename(pdflist[x],rn)


flag = True

while flag:
    listdirectory()
    openfile(int(input("Enter the number of which file you want to open: ")))
    cont = input("Continue renaming? (y for yes, n for no)?")
    if cont.upper() == "N":
        flag = False