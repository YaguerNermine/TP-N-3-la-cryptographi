# coding: utf-8

from string import ascii_letters, digits

ACCENTS = "àâäèéêëîïòôöùûüç"
ALPHABET = ascii_letters + ACCENTS + digits


def input_mode():
    """
    rien -> chaine de caractère

    Demande a l'utilisateur de saisir si il veut chiffrer ou déchiffrer
    un message 'c' pour chiffrer et 'd' pour déchiffrer
    """
    choice = ''
    input_ok = False

    while not input_ok:
        choice = input("Voulez-vous chiffrer ou déchiffrer un message (c/d) ? ").lower()

        if choice != 'c' and choice != 'd':
            print("Option invalide")
        else:
            input_ok = True
    return choice


def input_cle():
    """
        rien -> entier

        Demande a l'utilisateur la clé de chiffrement compris entre 1 et la taille
        de l'alphabet
    """
    key = ''
    input_ok = False
    MIN = 1
    MAX = len(ALPHABET)

    while not input_ok:
        choice = int(input("Entrez la clé de chiffrement ({}-{}) : ".format(MIN, MAX)))

        if choice < MIN or choice > MAX:
            print("Clé invalide")
        else:
            input_ok = True
    return choice


def pos(letter):
    """
    chaine de caractère -> entier

    Donne la position du caractère passer en paramètre dans notre alphabet retourne -1 si le caractère n'y est pas
    """

    for i in range(0, len(ALPHABET)):
        if ALPHABET[i] == letter:
            return i
    return -1


def car(n):
    """
    entier -> chaine de caractère

    Retourne le caractère a l'indice n de l'alphabet
    """
    return ALPHABET[n]


def chiffre_cesar(c, n):
    """
    chaine de caractère -> chaine de caractère

    Retourne le caractère de l'alphabet c décalerer de n dans l'alphabet
    """
    if pos(c) != -1:
        if pos(c) + n > len(ALPHABET) - 1:
            dist = pos(ALPHABET[len(ALPHABET) - 1]) - pos(c)
            n = n - dist - 1
            return car(n)
        else:
            return car(pos(c) + n)
    return c


def cesar(message, mode, cle):
    """
    chaine de caractère, chaine de caractère, entier -> chaine de caractère

    Chiffre ou déchiffre un message selon une clé donner en paramètre
    """
    text = ""

    if mode == "c":
        for letter in message:
            text += chiffre_cesar(letter, cle)
    if mode == "d":
        for letter in message:
            text += chiffre_cesar(letter, -cle)
    return text


def input_methode():
    """
    rien -> chaine de caractère

    Demande a l'utilisateur la méthode de chiffrement par cesar (c) ou vigenere (v)
    """

    choice = ''
    input_ok = False

    while not input_ok:
        choice = input("Quelle méthode voulez-vous utiliser : Cesar (c) ou Vigenere (v) ? ").lower()

        if choice != 'c' and choice != 'v':
            print("Option invalide")
        else:
            input_ok = True
    return choice


def vigenere(message, mode, mot_cle):
    def associate_word_key_to_message(msg, word):

        sentence_cipher = ''
        j = 0
        for i in range(len(msg)):

            if pos(msg[i]) != - 1:
                sentence_cipher += word[j]
                j += 1
                if j == len(word):
                    j = 0
            else:
                sentence_cipher += ' '
        return sentence_cipher

    print(message)
    word_string = associate_word_key_to_message(message, mot_cle)

    text = ""

    if mode == 'c':
        for i in range(len(message)):
            text += chiffre_cesar(message[i], pos(word_string[i]))
    if mode == 'd':
        for i in range(len(message)):
            text += chiffre_cesar(message[i], -pos(word_string[i]))

    return text


def main():
    app_close = False

    while not app_close:
        message = input("Entrez votre message :\n")
        mode = input_mode()
        method = input_methode()
        text = ''

        if method == 'v':
            key = input("Entrez le mot-clé : ")
            text = vigenere(message, mode, key)
        else:
            key = input_cle()
            text = cesar(message, mode, key)

        print(text)

        choice = input("Voulez vous continuer ? (O/n)").lower()

        if choice == 'n':
            app_close = True


main()
"""
a = cesar("help me obi wan kanobi you are my only hope.", "c", 23)
b = cesar(a, "d", 23)

print("Chiffrer = {}\nDechiffrer = {}".format(a, b))
c = vigenere("help me obi wan kanobi you are my only hope.", "c", "python")
d = vigenere(c, "d", "python")
"""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
