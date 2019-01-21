i=0
li=[]
diz={}
a=True

while a!=False:
    if a!=0:
        a=int(input("Inserisci un numero (0 per calcolare la moda): "))
        li.append(a)
    elif a==0:
        a=False

while i<len(li):
    if li[i] in diz:
        diz[li[i]]+=1
    else:
        diz[li[i]]=1
    i+=1

keys=sorted(diz.values())
greater=keys[-1]

if greater!=1:
    for number, frequency in diz.items():
        if frequency == greater:
            print ("Il numero " + str(number) + " e' la moda, ed e' stato ripetuto " + str(greater) + " volte.")

elif greater==1:
    for number, frequency in diz.items():
        if frequency == greater:
            print ("Il numero " + str(number) + " e' la moda, ed e' stato ripetuto " + str(greater) + " volta.")
