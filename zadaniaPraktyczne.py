# -*- coding: utf-8 -*-
## Zad 1. a)
def odwroc_tekst(napis):
    assert type(napis) == str
    L = []
    L = napis.split()
    OL= []
    for i in reversed (L):
        OL.append(i)
    napis = " ".join(OL)
    return napis



## Zad 1. b)
def odkoduj(napis):
    assert type(napis) == str
    slownik = {"@": "e", "U": " ", "e": "r", "*": "ko"}
    n = []
    for i in range(len(napis)):
        if napis[i] in slownik.keys():
            n.append(slownik.get(napis[i]))
        else:
            n.append(napis[i])
    odkodowany = ""
    print odkodowany.join(n)


## Zad. 2.
def piramida_cyfrowa(n):
    assert n>0
    assert type(n) == int
    if n>0:
        print n*str(n)
        piramida_cyfrowa(n-1)
        



## Zad 3. a)
def ciag_rek(n):
    assert type(n)==int and n>0
    if n==1:
        return 2
    else:
        return 0.5*ciag_rek(n-1)+2



def ciag_bez(n):
    assert type(n)==int and n>0
    a=2
    for i in range(2, n+1):
        a=0.5*a+2
    return a


## Zad 3. b)
import pier2

def ciagB(n):
    assert type(n)==int
    assert n>0
    if n==1:
        return 2
    else:
        return ciagB(n-1) * pier2



