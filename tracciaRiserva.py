# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

import codecs
nomeEsercizio = 'Riserva01'

##########################################################
# INTRODUZIONE
##########################################################
#
# I file descritti qua di seguito contengono informazioni sui movimenti
# di una popolazione di orsi che vivono in un parco naturale.
# Il rilevamento della posizione di un orso non e' continuo ma avviene solamente
# quando l'orso passa vicino a certi punti (chiamati postazioni di rilevazione).
##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e alcuni file di dati.
# I file con i dati sono:
#
# - File 1) distanze.csv
#   Il file memorizza le distanze tra le postazioni di rilevazione.
#   Una postazione di rilevazione e' identificata da una lettera
#   maiuscola dell'alfabeto.
#   Un esempio del contenuto del file e' il seguente. Nell'esempio
#   non considerate il simbolo di # e gli spazi.
#
#        Postazione1;Postazione2;Distanza
#        A;B;211\r\n
#        A;C;470\r\n
#        A;D;275\r\n
#        A;E;229\r\n
#        A;F;290\r\n
#        A;G;299\r\n
#        A;H;348\r\n
#
#   La prima riga contiene l'intestazione delle colonne.
#   In tute le righe le informazioni sono separati da ; (punto e virgola) e
#   i \r\n rappresentano i caratteri di a capo.
#   Nell'esempio qua sopra, la prima riga di dati ci dice la
#   postazione A dista 211 metri dalla postazione B.
#   Nota bene: se nel file e' presente la distanza tra A e B (come
#   nell'esempio qua sopra), per risparmiare spazio non viene memorizzata
#   la distanza tra B ed A, visto che e' identica.
#
#
# - File 2) percorsi.csv
#   Questo file memorizza lo spostamento fatto dagli orsi
#   nelle giornate di osservazione.
#   Un esempio del contenuto del file e' il seguente.
#   Nella prima riga c'e' intestazione del file.
#   Nell'esempio non considerate il simbolo di # e gli spazi.
#
#      id_orso;data;Postazione1;Postazione2;...;PostazioneN\r\n
#      0;01/03/2010;J;Y;W\r\n
#      1;01/03/2010;U;Q\r\n
#      2;01/03/2010;V;A;J;Z;I;Q\r\n
#      ...
#
#   Ogni riga contiene informazioni sul percorso svolto da un orso in uno specifico giorno.
#   Per esempio, la prima riga di dati
#   0;01/03/2010;J;Y;W
#   ci dice che l'orso 0 il giorno 01/03/2010 ha svolto un percorso che e' passato per le
#   postazioni di rilevamento J, Y e W (nell'ordine con cui sono elencate).
#   Le postazioni di rilevamento sono identifiate con le
#   Lettere dell'alfabeto. I percorsi svolti dagli orsi possono toccare un
#   numero variabile di postazioni, per questo motivo il numero di postazioni toccate
#   puo' variare da una riga all'altra.


##########################################################
# DESCRIZIONE DEL LAVORO DA SVOLGERE
##########################################################
#
# Implementate le seguenti funzioni, il commento che precede
# ogni funzione vi spieghera' cosa fare in dettaglio.
# Controllate nel corpo principale del programma (in fondo
# allo script), come vengono invocate le funzioni che
# implementerete.
# Per favore NON USATE le istruzioni input() o raw_input()
# nel codice che scriverete.
# Se volete potete implementare delle funzioni aggiuntive
# rispetto a quelle gia' presenti qua sotto.

##########################################################
# INIZIO DELLA PARTE DA EDITARE
##########################################################

cognome='Fusai' # inserisci qua il tuo cognome
nome='Stefano' # inserisci qua il tuo nome

# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file contenente le distanze tra le postazioni.
#   La funzione deve restituire le informazioni sulle distanze tra postazioni,
#   sotto forma di un dizionario con la struttura descritta nell'esempio seguente:
#         {
#          'AB':518, 'BC':231,
#          ...
#         }
#   La prima coppia chiave valore nell'esempio qua sopra indica che la distanza tra
#   la postazione A e la postazione B e' di 518 metri, la seconda coppia chiave
#   valore indica che la distanza tra la postazione B e la postazione C e' 231 metri.
#   Si ricorda che ogni singola postazione e' contraddistinta da un'unica lettera dell'alfabeto.
#   Per maggiori informazioni sui dati coinvolti si faccia riferimento
#   alla descrizione del file contenente i dati.
#   Nell'esempio qua sopra le distanze devono essere valori interi, mentre la chiave
#   deve essere una stringa formata dalle due postazioni coinvolte.

def leggiDistanzePostazioni(filename):
    diz={}

    with open(filename,"r",encoding="utf-8",errors="ignore") as file:
        file.readline()
        for line in file:
            line=line.strip("\r\n").split(";")
            key=line[0]+line[1]
            dist=int(line[2])
            diz[key]=dist

    return(diz)

# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file con le informazioni sulle postazioni raggiunte
#   dagli orsi durante gli spostamenti.
#   La funzione deve restituire una struttura dati come nell'esempio seguente.
#              [ (id_orso, giorno, stringa_percorso), (id_orso, giorno, stringa_percorso), ...   ]
#   Per esempio, la funzione leggendo le seguenti righe del file (i \r\n sono stati omessi)
#        id_orso;data;Postazione1;Postazione2;...
#        0;01/03/2010;J;Y;W
#        2;01/03/2010;V;A;J;Z;I;Q
#        ...
#   dovrebbe restituire la seguente struttura dati:
#        [ (0,'01/03/2010', 'JYW'),  (2,'01/03/2010', 'VAJZIQ'), ... ]
#   Ogni elemento della lista e' una tupla che contiene, l'id dell'orso, la data in cui l'orso
#   ha svolto il suo percorso e una stringa formata dalle lettere delle Postazioni toccate dall'orso.

def caricaPercorsi(fname):
    li=[]

    with open(fname,"r",encoding="utf-8",errors="ignore") as file:
        file.readline()
        for line in file:
            line=line.strip("\r\n").split(";")
            id=int(line[0])
            data=line[1]
            post=""
            for n in range(2, len(line)):
                post+=line[n]

            tupla=id,data,post
            li.append(tupla)

    return(li)

# - La funzione seguente accetta come parametri in ingresso
#   le strutture dati restituite rispettivamente dalle funzioni
#   leggiDistanzePostazioni() e caricaPercorsi().
#   La funzione deve restituire una struttura dati come nell'esempio seguente.
#        {id_orso1:totale_strada_percorsa1, id_orso2:totale_strada_percorsa2, ...}
#           ...
#   dove per ogni orso deve essere calcolato il totale dello spazio percorso sulla
#   base dei dati ricevuti in ingresso.

def calcolaLunghezzaCammini(distanze, percorsi):
    diz={}
    for line in percorsi:
        orso=line[0]
        post_raw=line[2]
        for n in range(0, len(post_raw)):
            post=""
            try:
                post=post_raw[n]+post_raw[n+1]
            except:
                break
            try:
                dist=distanze[post]
            except:
                dist=distanze[post[::-1]]
            if orso in diz:
                diz[orso]+=dist
            else:
                diz[orso]=dist

    return(diz)

# - La funzione seguente classifica una distanza percorsa in scaglioni.
#   NOTA BENE: questa funzione e' GIA' IMPLEMENTATA,
#   NON DOVETE MODIFICARLA, dovete SOLO USARLA negli
#   esercizi seguenti.

def categoriaOrso(distanza):
    if distanza < 300:
        return 'Ammalato'
    elif distanza <500:
        return 'Pigro'
    elif distanza <1000:
        return 'Ok'
    else:
        return 'Iperattivo'


# - La funzione seguente accetta in ingresso la struttura dati restituita dalla funzione calcolaLunghezzaCammini().
#   La funzione deve classificare le distane totali percorse dagli orsi in scaglioni utilizzando la funzione dichiarata qua sopra.
#   La funzione deve restituire la seguente struttura dati
#   { 'Ammalato':[id_orso, metri_percorsi], 'Pigro':[id_orso, metri_percorsi], ...}
#   In cui per ogni categoria vengono riportati i dati dell'orso (appartenente alla categoria) che ha percorso piu' strada.

def individua(lunghezza):
    diz={}
    liamm=[]
    lipig=[]
    liok=[]
    liip=[]

    for orso in lunghezza:
        metri_percorsi=lunghezza[orso]
        id_orso=orso
        distanza=categoriaOrso(metri_percorsi)
        if distanza=="Ammalato":
            liamm.append((metri_percorsi,id_orso))
        elif distanza=="Pigro":
            lipig.append((metri_percorsi,id_orso))
        elif distanza=="Ok":
            liok.append((metri_percorsi,id_orso))
        else:
            liip.append((metri_percorsi,id_orso))

    liamm.sort()
    try:
        maxamm=liamm[-1]
    except:
        maxamm=[-1,"xxx"]

    liip.sort()
    try:
        maxip=liip[-1]
    except:
        maxip=[-1,"xxx"]

    lipig.sort()
    try:
        maxpig=lipig[-1]
    except:
        maxpig=[-1,"xxx"]

    liok.sort()
    try:
        maxok=liok[-1]
    except:
        maxok=["xxx",-1]

    diz["Ammalato"]=[maxamm[1],maxamm[0]]
    diz["Pigro"]=[maxpig[1],maxpig[0]]
    diz["Ok"]=[maxok[1],maxok[0]]
    diz["Iperattivo"]=[maxip[1],maxip[0]]

    return(diz)


# - La funzione seguente accetta in ingresso la struttura dati
#   restituita dalla funzione caricaPercorsi().
#   La funzione deve individuare l'id dell'orso che per primo arriva a visitare
#   tutte le stazioni A, B, C, D, E, F, G, H, I in un qualsiasi ordine.
#   Considerate i dati ottenuti dalla funzione caricaPercorsi()
#   come se fossero ordinati temporalmente.

def giramondo(percorsi):
    diz={}
    alfabeto=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    for line in percorsi:
        id=line[0]
        data=line[1]
        postaz=line[2]
        
##########################################################
# Fine del compito e della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


print('Esercizio %s.' % (nomeEsercizio))

print('Ciao %s, %s .' % (nome, cognome))

print("1) Eseguo la funzione leggiDistanzePostazioni: ")
fname1='distanze.csv'
dist = leggiDistanzePostazioni(fname1)
print(dist)

print('2) Eseguo la funzione caricaPercorsi: ')
fname2='percorsi.csv'
perc = caricaPercorsi(fname2)
print(perc)

print('3) Eseguo la funzione calcolaLunghezzaCammini: ')
lung = calcolaLunghezzaCammini(dist, perc)
print(lung)

print('4) Eseguo la funzione categoriaOrso: ')
categoria = categoriaOrso(5500)
print(categoria)

print('Eseguo la funzione individua: ')
ris = individua(lung)
print(ris)

print('5) Eseguo la funzione giramondo: ')
ris = giramondo(perc)
print(ris)


print('Nome dello script eseguito')
print(__file__) # Questa istruzione stampa il nome dello script, ignoratela.
