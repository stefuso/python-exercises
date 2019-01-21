file1=open("dataset_cognomi_nomi_eta_comunenascita.txt","r")
li=[]
diz={}
i=0

for line in file1:
    line=line.strip("\n").split(";")
    li.append(line)

while i<len(li):
    if li[i][1] in diz:
        diz[li[i][1]]+=1
    else:
        diz[li[i][1]]=1
    i+=1

print(diz)
