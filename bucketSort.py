from random import randint, shuffle
import matplotlib as mpl
import timeit


Dlista = [10000, 20000, 30000, 40000, 50000]


def geraLista(tam):
    lista = []
    for i in range(tam):
        lista.append(randint(0,tam))
    shuffle(lista)

    return lista

def insertionSort(lista):
    for i in range(1,len(lista)):
        x = lista[i]
        j = i-1
        while j>=0 and x<lista[j]:
            lista[j+1] = lista[j]
            j=j-1
        lista[j+1] = x

    return lista

def bucketSort (lista):
    k = len(lista) - 1
    buckets = [[] for i in range (k)]
    maxValue = max(lista)
    for i in range(k, -1, -1):
        buckets[lista[i] * k // (maxValue + 1)].insert(0, lista[i])
    for i in range(0, k):
        insertionSort(buckets[i])
    returnList = []
    for bucket in buckets:
        returnList.extend(bucket)
    return returnList

mpl.use('Agg')
import matplotlib.pyplot as plt
def desenhaGrafico(x,y,ym,yp,xl = "Tamanho", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Pior Tempo")
    ax.plot(x,ym, label = "Melhor Tempo")
    ax.plot(x,yp, label = "Medio Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('GraficoBucketSort.png')

MelhorCaso = []
PiorCaso = []
MedioCaso = []

for i in Dlista:
    medio = geraLista(i)
    melhor = sorted(medio)
    pior = sorted(melhor, reverse=True)

    MelhorCaso.append(timeit.timeit("aux={}\naux = bucketSort(aux)".format(melhor.copy()),setup="from __main__ import bucketSort",number=1))
    PiorCaso.append(timeit.timeit("aux={}\naux = bucketSort(aux)".format(pior.copy()),setup="from __main__ import bucketSort",number=1))
    MedioCaso.append(timeit.timeit("aux={}\naux = bucketSort(aux)".format(medio.copy()),setup="from __main__ import bucketSort",number=1))
    print("Ordenado um i em Dlista!")


desenhaGrafico(Dlista,MedioCaso,MelhorCaso,PiorCaso)

import itertools as it
tamlista = list(it.permutations(list(range(6))))
tempoIteracao = []
listaOrig = []
for lista in tamlista:
    tempoIteracao.append(timeit.timeit("bucketSort({})".format(list(lista).copy()),setup="from __main__ import bucketSort",number=1))
    listaOrig.append(list(lista))

print("O tempo minimo foi de {}".format(min(tempoIteracao)))
print("lista que teve tempo minimo foi:{}".format(listaOrig[tempoIteracao.index(min(tempoIteracao))]))
print("O tempo maximo foi de {}".format(max(tempoIteracao)))
print("lista que teve tempo maximo foi:{}".format(listaOrig[tempoIteracao.index(max(tempoIteracao))]))


