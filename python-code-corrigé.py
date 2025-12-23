from numpy import array

# Fonction pour saisir et valider la taille du tableau
def sasir():
    n=int(input("Donner le taille du tableau=:"))
    while not (3 <=n<= 5):
        n=int(input("Donner taille du tableau=:"))
    return n

# Fonction pour remplir le tableau avec des valeurs positif est unique
def remplir(t, n):
    for i in range(n):
        t[i] = int(input("t[" + str(i) + "] = "))
        while not (t[i] > 0 and unique(t,i) ):
            t[i] = int(input("t[" + str(i) + "] = "))

def unique(t,x):
    i=0
    test=False
    while test==False and i<x:
        if t[i]==t[x]:
            test=True
        else:
            i=i+1
    return not(test)

def affichage(t,n):
    for i in range(n):
        print(t[i],end="|")
   
  
# Programme Principal
n=sasir()
t=array([int()]*n)
remplir(t,n)
affichage(t,n)
