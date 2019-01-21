a=int(input("Inserisci un operando: "))
b=int(input("Inserisci un altro operando: "))

if a<b:
    print(str(b) + " e' il maggiore dei due.")

elif b<a:
    print(str(a) + " e' il maggiore dei due.")

elif b==a:
    print("I due numeri sono uguali.")
