file1=open("dataset_cognomi_nomi_eta_comunenascita.txt","r")
li=[]
i=0
m=0
f=0

for line in file1:
    line=line.strip("\n").split(";")
    li.append(line)

while i<len(li):
    if li[i][2]=="M":
        m+=1

    elif li[i][2]=="F":
        f+=1

    i+=1

print("Numero persone: "+str(i),"\nNumero maschi: "+str(m),"\nNumero femmine: "+str(f))
