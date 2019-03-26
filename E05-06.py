class E05:
    def __init__(self, lista):
        self.t=lista

    def minuscole(self):
        list=self.t
        lidef=[]
        for line in list:
            liinner=[]
            for el in line:
                el=el.lower()
                liinner.append(el)
            lidef.append(liinner)

        return(lidef)

class Stopwords:
    def __init__(self, file):
        self.f=file

    def listcreate(self):
        raw=self.f
        listopwords=[]
        for line in raw:
            line=line.strip("\n")
            listopwords.append(line)
        return(listopwords)

class E06:
    def __init__(self, raw):
        self.stop=raw

    def stopword(self):
        tokenraw=self.stop
        lidef=[]
        for line in tokenraw:
            liinner=[]
            for word in line:
                if word in liststopwords:
                    word=word.replace(word,"")
                    if len(word)!=0:
                        liinner.append(word)
                else:
                    liinner.append(word)
            lidef.append(liinner)
        return(lidef)

#main
li=[["I", "Promessi", "Sposi"], ["Il", "signore", "degli", "anelli"], ["Il", "cacciatore", "di", "aquiloni"] ]
minuscole=E05(li)

file=open("stopwordsraw.txt","r")
stopwords=Stopwords(file)

tokenmin=minuscole.minuscole()
print(tokenmin)

liststopwords=stopwords.listcreate()

tokennostop=E06(tokenmin)
tokendef=tokennostop.stopword()
print(tokendef)
