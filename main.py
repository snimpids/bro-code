'''
Created on Nov 28, 2016

@author: Matt
'''

import os

badStrings = ['h1','h2','h3','h4','h5','h6','h7','h8','h9','p1','t1','(G)','b1','Hack','h1C','Beta','f1','o1','b2','b3','b4','b5','b6','f2','hI','h2C','h3C','h4C','BIOS','o2','NG-Dump','V1.1','V1.2','f1+C','T+','f2','f3','f4','a1','t3','t2','t4','(Sample)','[b1]','T-','(NP)','Preview Version','Event Version']

def removeBadRom(ROM):
    for bad in badStrings:
        if bad in ROM:
            return 1

filepath = 'D:/Games/SNES/'
directory = 'D:/Games/SNESRoms/'

if not os.path.exists(directory):
    os.makedirs(directory)

content_list = []
allROMS = []
goodROMS = []

for content in os.listdir(filepath): # "." means current directory
    content_list.append(content)

# Removing all actual ROMs in the main directory from the working list.
for item in content_list:
    if 'Hack' in item:
        content_list.remove(item)

# Putting all the ROMs files into one list, regardless of version or quality.       
for item in content_list:
    for files in os.listdir(filepath + item):
        allROMS.append(files)
            
for ROM in allROMS:
    if '[!]' in ROM:
        goodROMS.append(ROM)
    elif '(U)' in ROM:
        goodROMS.append(ROM)
    elif '(E)' in ROM:
        goodROMS.append(ROM)
    elif '(J)' in ROM:
        goodROMS.append(ROM)
        
print len(goodROMS)

for i in range(0,len(badStrings)):
    for ROM in goodROMS:
        if removeBadRom(ROM) == 1:
            goodROMS.remove(ROM)

print len(goodROMS)

# for ROM in goodROMS:
#     print ROM

for ROM in goodROMS:
    for content in os.listdir(filepath):
        for files in os.listdir(filepath + content):
            if files == ROM:
                os.rename(filepath + content + '/' + files, directory + '/' + files)