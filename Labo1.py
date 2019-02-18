import sqlite3
from sqlite3 import Error

#----Fonctions----
def menu():
    print("""
	Menu :
		1 = Ajouter un étudiant
		2 = Afficher les étudiants
		3 = Rechercher un étudiant
		4 = Supprimer un étudiant
		Q = Quitter le programme""")

def newEtu() :
    etuNom = input("\nNom? ")
    etuPrenom = input("Prénom? ")
    etuEmail = input("Adresse Email? ")
    return etuNom, etuPrenom, etuEmail

def remplissage(cur):
    # Opération sur la DB
    cur.execute('CREATE TABLE IF NOT EXISTS etudiants (etuID INTEGER PRIMARY KEY, etuNom TEXT, etuPrenom TEXT, etuEmail TEXT)')
    cur.execute("INSERT INTO etudiants (etuNom, etuPrenom, etuEmail) VALUES(?,?,?)",(newEtu()))

def modEtu(cur, id):
    cmd = "SELECT * FROM etudiants WHERE etuID = " + id
    cur.execute(cmd)
    for etudiant in cur :
        print("Nom : " + etudiant[1] + "\nPrénom : " + etudiant[2] + "\nEmail : " + etudiant[3])
    modDonnee = input("Quelle donnée voulez-vous modifier? ")
    newDonnee = str(input("Inserez la nouvelle donnée : "))
    cmd2 = "UPDATE etudiants SET etu" + modDonnee.lower() + " = \"" + newDonnee + "\" WHERE etuID = " + id
    cur.execute(cmd2)

def seeEtu(cur) :
    cur.execute("SELECT * FROM etudiants")
    for etudiant in cur :
        print(etudiant[0], "= Nom : " + etudiant[1] + ", Prénom : " + etudiant[2])
    print("\nVoulez vous modifier un étudiant?")
    menu1 = input("Inserez son ID ou Q pour revenir au menu ").upper()
    if menu1 == "Q" :
        return
    else :
        modEtu(cur, menu1)

def findEtu() :
    etuID = input("Quel ID voulez-vous chercher? ")
    cmd = "SELECT * FROM etudiants WHERE etuID = " + etuID
    cur.execute(cmd)
    etudiant = cur.fetchone()
    print(etudiant[0], "= Nom : " + etudiant[1] + ", Prénom : " + etudiant[2])

def delEtu() :
    etuID = input("Quel ID voulez-vous supprimer? ")
    verif = input("Voulez-vous VRAIMENT le supprimer? ").lower()
    if verif == "oui" :
        cmd = "DELETE FROM etudiants WHERE etuID = " + etuID
        cur.execute(cmd)
        print("Étudiant supprimé")

#-Variables Globales-
choix = "x"

#----Programme----
try:
    db = sqlite3.connect('data/Ecole.db')
    cur = db.cursor()
except Error as e:
    print(e)

while choix != "Q" :
    menu()
    choix = input("Que voulez-vous faire? ").upper()

    if choix == "1" :
        remplissage(cur)
        db.commit()
    if choix == "2" :
        seeEtu(cur)
        db.commit()
    if choix == "3" :
        findEtu()
        db.commit()
    if choix == "4" :
        delEtu()
        db.commit()