#L'objectif est de vérifier si un mot de passe saisi en entrer est fiable ou non. V1.0

#Importation librairies
import os
import string

#Fonction pour charger le mot de passe plus rapidement
def load_passwords(filename):
    #Utilisation de l'encodage classique (utf-8)
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        #Lecture de toutes les lignes dans le fichier filename
        for line in f:
            #generator yield pour retourner les élements de la liste ('Rockyou.txt' dans ce script)
            yield line.strip()

#Fonction pour vérifier si le mdp possède un caractère spécial
def has_special_char(password):
    special_chars = set(string.punctuation)
    return any(char in special_chars for char in password)

#Fonction pour vérifier si le mdp possède une lettre
def has_letter(password):
    return any(char.isalpha() for char in password)

#Fonction pour vérifier si le mdp possède un chiffre
def has_digit(password):
    return any(char.isdigit() for char in password)

#Fonction principale de vérification
def verificationPassword(pwdInput):
    filename = "rockyou.txt"
    #Vérifier si la liste existe
    if os.path.exists(filename):
        #1ere vérification: si le mot de passe est dans la liste
        for password in load_passwords(filename):
            if password == pwdInput:
                return "Bad Password :/ (found in common passwords)"
    else:
        return "List unfoundable."
    #2eme vérification: si le mot de passe a au moins: 1 chiffre, 1 lettre, 1 caractère spécial
    if not has_special_char(pwdInput) or not has_letter(pwdInput) or not has_digit(pwdInput):
        return "Bad Password :/ (missing special characters, letters, or digits)"

    return "Good Password !"

#Demande à l'utilisateur le mot de passe à vérifier
pwdInput = input("Mot de passe à vérifier : ")
print(verificationPassword(pwdInput))



#Ce code peut être grandement amélioré que ce soit en terme de sécurité et en terme d'optimisation.
#Have a good day !