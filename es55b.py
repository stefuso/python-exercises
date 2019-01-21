file1=open("dataset_cognomi_nomi_eta_comunenascita.txt","r")
li=[]
i=0
f1=0
f2=0
f3=0
f4=0
f5=0
f6=0

for line in file1:
    line=line.strip("\n").split(";")
    li.append(line)

while i<len(li):
    if 1<=int(li[i][3])<10:
        f1+=1
    if 10<=int(li[i][3])<20:
        f2+=1
    if 20<=int(li[i][3])<29:
        f3+=1
    if 30<=int(li[i][3])<39:
        f4+=1
    if 40<=int(li[i][3])<49:
        f5+=1
    if 50<=int(li[i][3])<59:
        f6+=1
    i+=1
    
print(f1,f2,f3,f4,f5,f6)
