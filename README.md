**PROBLEM
Écrire un programme qui permet de remplir un tableau T1 par n entiers positifs et uniques, avec 5 ≤ n ≤ 10, puis affiche le tableau
# 📋 Programme - Gestion de Tableaux

## 🎯 Description
Un programme ui permet de remplir un tableau avec des **entiers positifs uniques** et de l'afficher proprement. Le programme inclut des contrôles de saisie robustes pour garantir l'intégrité des données.


## 🚀 Exemples d'exécution
🎯 PROGRAMME DE REMPLIR TABLEAU UNIQUE🎯

Entrez la taille du tableau (entre 5 et 10) : 6

🎯 EXEMPLE RÉEL DE TABLEAU REMPLI (n=7)
Index	Valeur	Validation
T1[1]	12	✅ Positif et unique
T1[2]	5	✅ Positif et unique
T1[3]	18	✅ Positif et unique
T1[4]	5	❌ Rejeté (déjà présent)
T1[5]	7	✅ Positif et unique
T1[6]	-3	❌ Rejeté (négatif)
T1[7]	9	✅ Positif et unique
┌───┬───┬───┬───┬───┬───┬───┐
│ 12│ 5 │ 18│ 7 │ 9 │   │   │
└───┴───┴───┴───┴───┴───┴───┘
  ↑   ↑   ↑   ↑   ↑
  T1[1] à T1[5] valides     
  📋 CONTRAINTES DU TABLEAU
Propriété	Règle	Exemple Valide	Exemple Invalide
Taille (n)	5 ≤ n ≤ 10	n=7 ✅	n=3 ❌
Valeurs	Entiers positifs	15 ✅	-5 ❌
Unicité	Aucun doublon	8,15,22 ✅	8,15,8 ❌
Type	Entiers uniquement	10 ✅	3.14 ❌

