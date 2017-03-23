import random  # nécessaire pour manipuler aléatoirement

#####
##VARIABLES GLOABLES
#####
mainprincipal = []
compteMain = []


########################################
# Fonction pour mélanger aléatoirement le sabot (nécéssaire au moins 1 fois)
def shuffle(listeCarte):
    listeCarte = list(listeCarte)
    random.shuffle(listeCarte)  # shuffle pour mélanger aléatoirement le sabot
    return listeCarte


# Fonction pour récupérer aléatoirement une carte
def choix(listeCarte):
    # choix au hasard mais vaut mieux éviter. On peut partir sur la dernière carte du talon
    choixCarte = random.choice(listeCarte)
    return choixCarte


# Fonction pour retirer la carte choisie de la liste
def retirerSabot(listeCarte, ChoixCarte):
    cpt = 0
    for i in listeCarte:
        if ChoixCarte == i:
            del listeCarte[cpt]  # on retire la carte choisie
        else:
            cpt += 1


# Compter les cartes
def compte(listeCarte):
    if listeCarte == "2" or listeCarte == "3" or listeCarte == "4" or listeCarte == "5" or listeCarte == "6":
        cpt = -1
    elif listeCarte == "7" or listeCarte == "8" or listeCarte == "9":
        cpt = 0
    else:  # if x == "10" or x == "V" or  x == "D" or  x == "R" or   x == "A"
        cpt = 1
    return cpt


# Ajout dans main principal
def AjoutDansMain(carte):
    global mainprincipal
    mainprincipal.append(carte)  # append permet d'ajouter
    for i in mainprincipal:
        print(i)


# Pour compter la main (pas pour faire 21)
def AjoutCompte(ChoixCarte):
    global compteMain
    somme = 0
    y = compte(ChoixCarte)
    compteMain.append(y)
    for i in compteMain:
        somme += i
        # print(i)
    print("calcul : ", somme)


# pour continuer le jeu
def ContinuerJeu(var1, listeCarte):
    reponse = int(var1)
    if reponse == 1:
        choixCarte = choix(listeCarte)
        print("Carte tirée : ", choixCarte)
        print("cartes en main : ")
        AjoutDansMain(choixCarte)
        retirerSabot(listeCarte, choixCarte)
        print("SAbot restant : ", listeCarte)
        AjoutCompte(choixCarte)


def menu():
    x = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R", "A"]
    listeCarte = shuffle(x)
    print(listeCarte)
    # tirer une carte au hasard
    # 1ere Sortie
    var1 = 1
    while var1 == 1:
        var1 = input("Continuer Jeu")
        ContinuerJeu(var1, listeCarte)
        var1 = int(var1)

        print("\n")


menu()
