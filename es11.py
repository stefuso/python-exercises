a=int(input("Inserisci un operando: "))
b=int(input("Inserisci un altro operando: "))
c=int(input("Scegli l'operazione da eseguire sui due operandi: \n   1=somma\n   2=sottrazione\n   3=moltiplicazione\n   4=divisione \n"))

if c==1:
    print("La somma e' pari a " + str(a+b))

elif c==2:
    print("La differenza e' pari a " + str(a-b))

elif c==3:
    print("Il prodotto e' pari a " + str(a*b))

elif c==4:
    print("Il quoziente e' pari a " + str(a/b))

elif c!=1 or c!=2 or c!=3 or c!=4:
    print("Non e' stata scelta un'operazione valida.")
