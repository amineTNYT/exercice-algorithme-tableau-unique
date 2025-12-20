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
        while not (t[i] > 0 and nb_occurrence(t, i+1, t[i]) == 1):
            t[i] = int(input("t[" + str(i) + "] = "))

def nb_occurrence(t,n,x):
    nb = 0
    for i in range(n):
        if t[i] == x:
            nb += 1
    return nb
# Fonction pour afficher les éléments du tableau séparés par "|"
def affichage(t,n):
    for i in range(n):
        print(t[i],end="|")
   
  
# Programme Principal
n=sasir()
t=array([int()]*n)
remplir(t,n)
affichage(t,n)
