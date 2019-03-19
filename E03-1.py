import codecs

class Es01:
    def __init__(self, nomefile, ncolonna):
        self.f=nomefile
        self.n=ncolonna

    def esercizio(self):
        li=[]
        i=self.n

        file=codecs.open(self.f,"r",encoding="latin-1")
        file.readline()
        file=file.read()
        file=file.replace("\r","")
        lista=file.split("\n")

        for el in lista:
            el=el.split(";")
            li.append(el[i])

        return(li)

#main
colonna=int(input("Quale colonna vuoi estrarre?\n0 - prima colonna\n1 - seconda colonna\n"))
file=Es01("movies.csv", colonna)
print(file.esercizio())
