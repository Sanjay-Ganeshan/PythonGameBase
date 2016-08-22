import os
import glob

projName = str(raw_input("Project Name? - "))
os.mkdir(projName)
os.mkdir(projName + '\\Content')
os.mkdir(projName + '\\Content\\Music')
os.mkdir(projName + '\\Code')
os.mkdir(projName + '\\ReqContent')
itemsToCopy = glob.glob("Base\\Code\\*")
#print itemsToCopy
for item in itemsToCopy:
    os.system("COPY " + item + ' ' + projName + "\\Code")
itemsToCopy = glob.glob("Base\\Content\\*.*")
#print itemsToCopy
for item in itemsToCopy:
    os.system("COPY " + item + ' ' + projName + "\\Content")

itemsToCopy = glob.glob("Base\\Content\\Music\\*")
#print itemsToCopy
for item in itemsToCopy:
    os.system("COPY " + item + ' ' + projName + "\\Content\\Music")

itemsToCopy = glob.glob("Base\\ReqContent\\*")
#print itemsToCopy
for item in itemsToCopy:
    os.system("COPY " + item + ' ' + projName + "\\ReqContent")
os.rename(projName + "\\Code\\GameBase.py",projName + "\\Code\\" + projName + ".py")