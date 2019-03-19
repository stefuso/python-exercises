import codecs

class E03:
    def __init__(self, stringa):
        self.s=stringa

    def esercizio(self):
        li=[]
        i=0

        str=self.s


        for el in str:
            el=el.split()
            li.append(el)

        return(li)

#main
token=[]
stringa=""

while stringa != "0":
    stringa=str(input("Inserisci un testo da tokenizzare (0 per inizializzare la tokenizzazione): "))
    token.append(stringa)

token=token[:-1]
file=E03(token)
print(file.esercizio())
