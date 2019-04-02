def tweetOrari(nomefile, listaParole):
    dizT={}
    with open (nomefile, "r") as file:
        for line in file:
            line=line.strip("\r\n").split("|||")
            tweet=line[4]
            tweet=tweet.split()

            data=line[1].split()
            orario=data[3]
            orario=orario.split(":")
            ora=int(orario[0])

            a=0
            for word in listaParole:
                for parola in tweet:
                    if word.lower()==parola.lower():
                        a+=1

            if a==len(listaParole):
                if ora in dizT:
                    dizT[ora]+=1
                else:
                    dizT[ora]=1
            else:
                if ora not in dizT:
                    dizT[ora]=0

    return(dizT)

def calcolaFollower(nomefile, daescludere):
    dizF={}
    with open (nomefile, "r") as file:
        if daescludere!=0:
            for i in range(0, daescludere):
                file.readline()
        else:
            for line in file:
                frag=line.strip("\r\n").split("|||")
                user=frag[2]
                follower=int(frag[3])

                if user in dizF:
                    dizF[user]+=follower
                else:
                    dizF[user]=follower
    return(dizF)

def contaMenzioni(nomefile, blackList):
    dizM={}
    lipunt=[",",";",".",":","-","_","'",'"']
    with open (nomefile, "r") as file:
        for line in file:
            frag=line.strip("\r\n").split("|||")
            tweet=frag[4]
            tweetsplit=tweet.split()
            for word in tweetsplit:
                for punt in lipunt:
                    word=word.replace("@ ","@")
                    word=word.replace(punt,"")
                if "@" in word:
                    print(word)


#main
dizcontatweet=tweetOrari("tweet.txt",["Luna","lunera!"])
print(dizcontatweet)

dizcalcolafollower=calcolaFollower("tweet.txt",0)
print(dizcalcolafollower)

dizcontamenzioni=contaMenzioni("tweet.txt",0)
print(dizcontamenzioni)
