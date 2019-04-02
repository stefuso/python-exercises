import requests
from bs4 import BeautifulSoup

player1=raw_input("Who's the first player you want to compare? ")
player2=raw_input("And who's the second? ")

li1=[]
li2=[]

player1spl=player1.split()
nome1=player1spl[0]
cognome1=player1spl[1]

player2spl=player2.split()
nome2=player2spl[0]
cognome2=player2spl[1]

l1=cognome1[:1]
coshort1=cognome1[:5]
noshort1=nome1[:2]

l2=cognome2[:1]
coshort2=cognome2[:5]
noshort2=nome2[:2]

url1="https://www.basketball-reference.com/players/"+l1+"/"+coshort1+noshort1+"01.html"
url1=url1.lower()

url2="https://www.basketball-reference.com/players/"+l2+"/"+coshort2+noshort2+"01.html"
url2=url2.lower()

page1=requests.get(url1)
page2=requests.get(url2)

soup1=BeautifulSoup(page1.content, "lxml")
soup2=BeautifulSoup(page2.content, "lxml")

soup11=soup1.find('div', attrs={'class': 'p1'})
stats11=soup11.find_all("p")
soup12=soup1.find('div', attrs={'class': 'p2'})
stats12=soup12.find_all("p")

stats11=str(stats11)
stats11=stats11.replace("</p>","")
stats11=stats11[1:-1].replace("<p>","").split(",")

stats12=str(stats12)
stats12=stats12.replace("</p>","")
stats12=stats12[1:-1].replace("<p>","").split(",")

i=1
while i<len(stats11):
    li1.append(float(stats11[i]))
    i+=2

i=1
while i<len(stats12):
    li1.append(float(stats12[i]))
    i+=2

soup21=soup2.find('div', attrs={'class': 'p1'})
stats21=soup21.find_all("p")
soup22=soup2.find('div', attrs={'class': 'p2'})
stats22=soup22.find_all("p")

stats21=str(stats21)
stats21=stats21.replace("</p>","")
stats21=stats21[1:-1].replace("<p>","").split(",")

stats22=str(stats22)
stats22=stats22.replace("</p>","")
stats22=stats22[1:-1].replace("<p>","").split(",")

i=1
while i<len(stats21):
    li2.append(float(stats21[i]))
    i+=2

i=1
while i<len(stats22):
    li2.append(float(stats22[i]))
    i+=2

count1=0
count2=0
e=0
lididasc=["Games Played","PTS","TRB","AST","FG%","FG3%","FT%","eFG%"]

for el in li1:
    if el>li2[e]:
        count1+=1
        print(player1+" beats "+player2+" in the following stat: "+str(lididasc[e])+" ("+str(li1[e])+" vs "+str(li2[e])+")")
    elif el<li2[e]:
        count2+=1
        print(player2+" beats "+player1+" in the following stat: "+str(lididasc[e])+" ("+str(li2[e])+" vs "+str(li1[e])+")")
    else:
        print(player1+" equals "+player2+" in the following stat: "+str(lididasc[e])+" ("+str(li1[e])+" vs "+str(li2[e])+")")
    e+=1

if count1>count2:
    print(player1+" beats "+player2+" with a total of "+str(count1)+" points against "+cognome2+"'s "+str(count2)+" points")
elif count2>count1:
    print(player2+" beats "+player1+" with a total of "+str(count2)+" points against "+cognome1+"'s "+str(count1)+" points")
else:
    print(player1+" and "+player2+" totaled the same amount of points ("+count1+"). It's a tie!")
