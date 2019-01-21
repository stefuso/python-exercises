a=int(input("Quanti CD vuoi acquistare? "))

if a<1000:
    print("Il prezzo e' pari a " + str(a*5) + " Euro.")

else:
    prezzo1=int(5000+(a-1000)*4)
    prezzo2=int((a-((a-800)/20))*5)
    b=int(input("Sono disponibili due tipi di sconto:\n    1: Pagare i CD che eccedono i primi 1000 al prezzo di 4€ l’uno (i primi 1000 cd sono comunque tariffati a 5€ l’uno)\n    2: Pagare tutti i CD 5€ l’uno, ma ogni 20 cd venduti oltre i primi 800, uno viene regalato\n"))
    if b==1:
        print("Il prezzo e' pari a " + str(prezzo1) + " Euro.")
    elif b==2:
        print("Il prezzo e' pari a " + str(prezzo2) + " Euro.")
    elif b!=1 or b!=2:
        print("Non e' stato inserito un valore valido.")

    if prezzo1<prezzo2:
        print("Lo sconto piu' conveniente e' il numero 1. Il prezzo totale infatti e' pari a " + str(prezzo1) + " Euro contro i " + str(prezzo2) + " Euro del secondo sconto." )

    elif prezzo2<prezzo1:
        print("Lo sconto piu' conveniente e' il numero 2. Il prezzo totale infatti e' pari a " + str(prezzo2) + " Euro contro i " + str(prezzo1) + " Euro del primo sconto." )

    elif prezzo1==prezzo2:
        print("I due sconti si equivalgono. La scelta del tipo di sconto e' dunque indifferente.")
