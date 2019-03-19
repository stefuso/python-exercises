import codecs

class Es01:
    def __init__(self, stringa, token):
        self.s=stringa
        self.t=token

    def esercizio(self):
        li=[]
        i=0

        str=self.s
        num=self.t

        str=str.split()

        for el in str:
            if i<num:
                li.append(el)
            else:
                break
            i+=1

        return(li)

#main
stringa=str(input("Inserisci un testo da tokenizzare: "))
ntoken=int(input("Quanti token vuoi estrarre? "))
file=Es01(stringa, ntoken)
print(file.esercizio())
