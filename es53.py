file=open("database531.txt","w+")
i=1

while i<6:
    nome=str(input("Inserisci il nome dello studente %d: " %(i)))
    cognome=str(input("Inserisci il cognome dello studente %d: " %(i)))
    matricola=str(input("Inserisci il numero di matricola dello studente %d: " %(i)))
    file.write(nome + "," + cognome + "," + matricola + "\n")
    i+=1

file.close()
