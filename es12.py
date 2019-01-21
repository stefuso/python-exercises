a=int(input("Inserisci un numero: "))
b=int(input("Inserisci un altro numero: "))

if a%b==0:
    print(str(b)+" e' un divisore di "+str(a))

if b%a==0:
    print(str(a)+" e' un divisore di "+str(b))

elif a%b!=0:
    print("I due numeri non hanno divisori in comune")
