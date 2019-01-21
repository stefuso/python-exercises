a=int(input("Inserisci il valore del lato a: "))
b=int(input("Inserisci il valore del lato b (maggiore o uguale al lato a): "))
c=int(input("Inserisci il valore del lato c (maggiore o uguale al lato b): "))

if c>(a+b):
    print("I lati inseriti non rappresentano un triangolo.")

elif a==b==c:
    print("I lati inseriti rappresentano un triangolo equilatero.")

elif a==b or a==c or b==c:
    print("I lati inseriti rappresentano un triangolo isoscele.")

else:
        print("I lati inseriti rappresentano un triangolo scaleno.")
