file1=open("dataset_cognomi_nomi_eta_comunenascita.txt","r")
li=[]
diz={}
i=0

for line in file1:
    line=line.strip("\n").split(";")
    li.append(line)

while i<len(li):
    if li[i][0] in diz:
        diz[li[i][0]]+=1
    else:
        diz[li[i][0]]=1
    i+=1

chiavi=sorted(diz.values())
maggiore=chiavi[-1]

for name, age in diz.items():
    if age == maggiore:
        print (name, maggiore)
