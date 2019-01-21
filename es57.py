file=open("catalogo_film.csv","r")
li=[]
diz={}
i=0

file.readline()
for line in file:
    line=line.strip("\n").split(";")
    li.append(line)

a=int(input("Che tipo di analisi vuoi effettuare?\n1 - Numero di film per genere\n2 - Numero di film per regista\n3 - Numero di film per attore\n4 - Numero di film per costo\n"))

#"Film divisi per genere:"
if a==1:
    for i in range(len(li)):
        if li[i][1] in diz:
            diz[li[i][1]]+=1
        else:
            diz[li[i][1]]=1

    print(diz)

#"Film divisi per regista:"
if a==2:
    for i in range(len(li)):
        if li[i][3] in diz:
            diz[li[i][3]]+=1
        else:
            diz[li[i][3]]=1

    print(diz)

#"Film divisi per attore:"
if a==3:
    for i in range(len(li)):
        if li[i][4] in diz:
            diz[li[i][4]]+=1
        else:
            diz[li[i][4]]=1

    print(diz)

#"Film divisi per costo:"
if a==4:
    for i in range(len(li)):
        if li[i][5] in diz:
            diz[li[i][5]]+=1
        else:
            diz[li[i][5]]=1

    print(diz)
