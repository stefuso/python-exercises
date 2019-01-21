def bubblesort(con):
    while con==False:
        li2 = li.copy()
        a=0
        while a<9:
            if li[a]>li[a+1]:
                num=li[a]
                li[a]=li[a+1]
                li[a+1]=num
            a+=1
        if li2==li:
            con=True
    return(li)

li=[]
li2=[]
i=0
con=False

while i<10:
    num=int(input("Inserisci un numero: "))
    li.append(num)
    i+=1

funz=bubblesort(con)
print(funz)
