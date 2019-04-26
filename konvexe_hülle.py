#Algorithmische Geometrie
#Aufgabe 1
#Nummer : 22328

import numpy
import scipy.spatial
import matplotlib.pyplot as plt

def my_function():
  #Eingabe ein Zahle

  i: int = 0
  list = []
  max: int = 20
  print("Zahle :")
  n = int(input())
  #Erzeugung n Punkte
  while i < n + 1:
      list = numpy.random.randint(max, size=(n, 2))
      if i == n:
          break
      i += 1
  print(list)
  # Berechnung der konvexen Huelle
  CH = scipy.spatial.ConvexHull(list)

  # Ausgabe der Anzahl der Ecken
  e = len(CH.vertices)
  print(e)




#Zusammenhang zwischen der Anzahl n der Eingabepunkte und der durchschnittlichen Anzahl e(n)
def zusammenhang ():
    Quad = 30  #Laenge des Quadrats
    n = 10   #Menge von erzeugten Punkten
    i: int = 0
    e: float = 0 #Anzahle der Ecken
    array = []
    medium = []
    ntable = numpy.array([])
    meantable = numpy.array([])
    while n < 100:
        while i < Quad+1:
            table = numpy.random.randint(Quad, size=(n, 2))

            #Berechnung der konvexen Huelle
            hull = scipy.spatial.ConvexHull(table)

            #Ausgabe der Anzahl der Ecken
            e =len(hull.vertices)

            #Zusammenhang zwischen n und (len(hull.vertices))
            array.append((len(hull.vertices)))
            i += 10

        medium.append((n, (numpy.mean(array))))
        ntable = numpy.append(ntable, n)
        meantable = numpy.append(meantable, numpy.mean(array))
        i = 0
        n += 5

    #Erzeugung der Tabelle mit n und medium
    for elt in enumerate(medium):
        print(elt)
    #Zusammenhang zwischen n und e(n)
    p = numpy.polyfit(ntable, meantable, 3)
    print("e(n) = ", p[3], "n³", p[2], "n²", p[1], "n", p[0])

    #Graphisch darstellung
    plt.plot(meantable, ntable , 'ro')
    plt.show()


my_function()
print("Aufgabe 1 Teil c :")
zusammenhang()