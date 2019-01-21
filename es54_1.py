file=open("database54.txt", "w")
i=1

while i>0:

    a=int(input("Inserisci un numero intero (0 per terminare il programma): "))
    if a==0:
        break

    else:
        file.write(str(a)+",")

    i+=1

file.close()
