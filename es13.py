a=int(input("Inserisci un numero: "))

if a<0:
    print(str(a)+" appartiene alla classe K.")

elif 0<=a<=10:
    print(str(a)+" appartiene alla classe A.")

elif 11<=a<=20:
    print(str(a)+" appartiene alla classe B.")

elif 21<=a<=30:
    print(str(a)+" appartiene alla classe C.")

elif 31<=a<=40:
    print(str(a)+" appartiene alla classe E.")

elif 41<=a<=50:
    print(str(a)+" appartiene alla classe F.")

elif 51<=a:
    print(str(a)+" appartiene alla classe G.")
