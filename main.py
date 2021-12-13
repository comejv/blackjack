# Projet Blackjack
from random import shuffle

# Cartes
card_dic = {"AS": "As de Pique", "2S": "Deux de Pique", "3S": "Trois de Pique", "4S": "Quatre de Pique", "5S": "Cinq de Pique", "6S": "Six de Pique",
            "7S": "Sept de Pique", "8S": "Huit de Pique", "9S": "Neuf de Pique", "0S": "Dix de Pique", "JS": "Valet de Pique", "QS": "Dame de Pique", "KS": "Roi de Pique",
            "AD": "As de Carreau", "2D": "Deux de Carreau", "3D": "Trois de Carreau", "4D": "Quatre de Carreau", "5D": "Cinq de Carreau", "6D": "Six de Carreau",
            "7D": "Sept de Carreau", "8D": "Huit de Carreau", "9D": "Neuf de Carreau", "0D": "Dix de Carreau", "JD": "Valet de Carreau", "QD": "Dame de Carreau", "KD": "Roi de Carreau",
            "AH": "As de Coeur", "2H": "Deux de Coeur", "3H": "Trois de Coeur", "4H": "Quatre de Coeur", "5H": "Cinq de Coeur", "6H": "Six de Coeur",
            "7H": "Sept de Coeur", "8H": "Huit de Coeur", "9H": "Neuf de Coeur", "0H": "Dix de Coeur", "JH": "Valet de Coeur", "QH": "Dame de Coeur", "KH": "Roi de Coeur",
            "AC": "As de Trefle", "2C": "Deux de Trefle", "3C": "Trois de Trefle", "4C": "Quatre de Trefle", "5C": "Cinq de Trefle", "6C": "Six de Trefle",
            "7C": "Sept de Trefle", "8C": "Huit de Trefle", "9C": "Neuf de Trefle", "0C": "Dix de Trefle", "JC": "Valet de Trefle", "QC": "Dame de Trefle", "KC": "Roi de Trefle"}


def paquet():
    """Crée un paquet de 52 cartes

    Returns:
        [liste]: 52 items
    """
    return [item for item in card_dic]


def initPioche(n=1):
    """Ajoute à la pioche n paquets de 52 cartes et les mélange

    Args:
        n (entier, optionnel): nombre de joueurs -> nombre de paquets ; par défaut 1

    Returns:
        [liste]: liste mélangée de n fois 52 cartes
    """
    pioche = []
    for i in range(n):
        pioche += paquet()
    shuffle(pioche)
    return pioche


def piocheCarte(pioche):
    """Renvoie un item au hasard de la liste donnée : pioche une carte parmi la pioche

    Args:
        pioche (liste): liste de cartes créée avec la fonction initPioche

    Returns:
        string: une carte séléctionnée au hasard dans la pioche, carte enlevée de la liste de pioche
    """
    return pioche.pop(0)    # Le sommet de la pioche est en indice 0


def valeurCarte(carte, joueur):
    """Renvoie la valeur numérique de la carte piochée

    Args:
        carte (string): carte sortie de la pioche grâce à piocheCarte

    Returns:
        entier: valeur numérique entre 1 et 11
    """
    valeur = carte[0]
    if 48 < ord(valeur) < 58:
        return int(valeur)
    elif valeur in "JQK0":
        return 10
    elif valeur == 'A':
        print(
            f"{joueur}, vous avez pioché un As, quelle valeur voulez-vous qu'il prenne ?")
        rep = input(
            " Répondez 1 ou 11.")
        while not(rep == '1' or rep == '11'):
            rep = input("Veuillez répondre par 1 ou 11.")
        return int(rep)


def initJoueurs(n):
    """Créée une liste des personnes qui jouent

    Args:
        n (entier): nombre de joueurs

    Returns:
        liste: liste des noms
    """
    liste_des_noms = []
    #! Faire en sorte que deux joueurs ne puissent s'appeller de la même manière
    print("Attention, vous ne pouvez pas donner deux fois le même nom pour deux joueurs.")
    for i in range(n):
        liste_des_noms.append(input(f"Nom du joueur {i+1} :\n"))
    return liste_des_noms


def initScores(joueurs, s=0, p=100):
    """Assigne à chaque joueur une liste contenant le score et le portefeuille de chaque joueur, le tout dans un dictionnaire

    Args:
        joueurs (liste): liste créée avec initJoueurs
        v (entier, optionnel): Score de départ des joueurs. 0 par défaut.
        m (entier, optionnel): mise de départ des joueurs. 100 par défaut.

    Returns:
        dictionnaire: Dictionnaire assignant à chaque nom de joueur son score et son portefeuille
    """
    #! Toujours rajouter le croupier
    joueur_score = {}
    for i in joueurs:
        joueur_score[i] = [s, p, []]    # Liste vide pour les cartes piochées
    return joueur_score


def premierTour(joueurs, pioche):
    """Test le programme en simulant un tour de jeu

    Args:
        joueurs (liste): liste des noms des joueurs
        pioche_ (liste): contient toutes les cartes mélangées

    Returns:
        dictionnaire: Nom, scores, portefeuille et cartes piochées de chaque joueur après avoir pioché deux cartes
    """
    scores = initScores(joueurs)

    for joueur in joueurs:
        scores[joueur][2].append(piocheCarte(pioche))
        scores[joueur][2].append(piocheCarte(pioche))
        scores[joueur][0] += valeurCarte(scores[joueur][2][0], joueur)
        scores[joueur][0] += valeurCarte(scores[joueur][2][0], joueur)
        print(
            f"{joueur}, vous avez {card_dic[scores[joueur][2][0]]} et {card_dic[scores[joueur][2][1]]} comme main de départ. Vous avez {scores[joueur][0]} points.")
    return scores

#! Implémenter les gains d'argent et la gestion des égalités


def gagnant(scores):
    """Renvoie le nom du gagnant (plus proche de 21 sans le dépasser) grâce au tableau de scores trié et transformé en liste de tuples ("joueur",score)

    Args:
        scores (dictionnaire): assigne à chaque joueur un score
    """
    tri_score = sorted(
        scores.items(), key=lambda x: x[1][0])  # On trie avec le score de chacun
    # Ici joueur est un entier, pas le nom du joueur
    for joueur in range(len(tri_score)):
        print(
            f'{tri_score[joueur][0]} a atteint {tri_score[joueur][1][0]} points. Il lui reste {tri_score[joueur][1][1]} rubis.')
    e = 1
    for joueur in range(len(tri_score)):    # On vérifie si il y a une égalité
        if tri_score[len(tri_score)-1-joueur][1][0] == tri_score[len(tri_score)-joueur-2][1][0] and len(tri_score) > 1:
            e += 1   # Si égalité, il y a e gagnants
        else:
            break
    if e > 1:
        print(f"Il y a égalité entre {e} joueurs. ")
        for i in range(e):
            print(tri_score[-1-i][0])
    else:
        print(tri_score[-1][0], "a gagné la partie avec",
              tri_score[-1][1], "points. Bravo !")


def tourJoueur(joueur, tour, scores):
    """Rappel le nombre de points, demande si le joueur dont c'est le tour veut piocher, lui donne son nouveau score et le met à jour dans le tableau de score. Supprime le joueur du tableau de score s'il dépasse 21.

    Args:
        joueur (string): nom du joueur dont c'est le tour
        tour (entier): nombre de tour de jeu
        scores (dictionnaire): assigne à chaque joueur un score
    """
    print(
        f"C'est le tour {tour} de {joueur}. Vous avez {scores[joueur][0]} points.")
    print("Votre main est : ",sep='')
    print(*[card_dic[i] for i in scores[joueur][2]], sep=', ')
    piocher = input(
        f"{joueur}, voulez-vous piocher une cartes ? Oui(o) ou Non(n)\n").lower()
    while not(piocher in "ouinon"):
        piocher = input(
            f"{joueur}, vous pouvez répondre seulement par Oui(o) ou Non(n)\n").lower()
    if piocher == 'o' or piocher == 'oui':
        scores[joueur][2].append(piocheCarte(pioche))
        scores[joueur][0] += valeurCarte(scores[joueur][2][-1], joueur)
        print(
            f"Vous avez pioché {scores[joueur][2][-1]}.\nVotre nouveau score est de {scores[joueur][0]}.")

    elif piocher == 'n' or piocher == 'non':
        joueEncore[joueur] = 2

    if scores[joueur][0] > 21:
        print("Vous avez dépassé 21 : vous avez perdu.")
        joueEncore[joueur] = 3
        del scores[joueur]


# Variables de départ
nb_tour = 1
joueurs = initJoueurs(int(input("Combien de joueurs ?\n")))
pioche = initPioche(len(joueurs))
scores = premierTour(joueurs, pioche)

# Création liste des éliminés : 1 en jeu, 2 arrête de piocher, 3 a perdu
joueEncore = {}
for joueur in joueurs:
    joueEncore[joueur] = 1

jeu = True
while jeu:
    for joueur in joueurs:
        if joueEncore[joueur] == 1:
            tourJoueur(joueur, nb_tour, scores)
    nb_tour += 1
    if not(1 in joueEncore.values()):
        jeu = False

gagnant(scores)
