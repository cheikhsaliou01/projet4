import sqlite3
con = sqlite3.connect('gestion.db')
print("Database created and Successfully Connected to SQLite!!")
curseur = con.cursor()


def createtable():
    req = '''' create table contacts(
        id integer primary key autoincrement,
        nom text not null,
        prenom text not null,
        email text ,
        numero_telephone numeric not null,
        adresse text not nul
    )'''
    curseur.execute(req)
    con.commit()


def insert(nom, prenom, email, numero_telephone, adresse):
    curseur.execute("insert into contacts (nom,prenom,email,numero_telephone,adresse) values (?,?,?,?,?)",
                    (nom, prenom, email, numero_telephone, adresse))
    con.commit()


def update_contact(id, nom):
    curseur.execute(
        "update contacts set Nom = '%s' where Id= '%s' " % (nom, id))
    con.commit()
    print("Contact modifier avec succes")


def delete_contact(id):
    curseur.execute("DELETE FROM contacts WHERE id=%s " % (id))
    con.commit()
    print("Donnees supprimer avec succes")


def readSqliteTable():
    sql_select_query = ''' select * from contacts'''
    curseur.execute(sql_select_query)
    records = curseur.fetchall()
    print("Le nombre de ligne est : ", len(records))
    for row in records:
        print("id :", row[0])
        print("nom :", row[1])
        print("prenom :", row[2])
        print("email :", row[3])
        print("numero_telephone :", row[4])
        print("adresse :", row[5])
        print("\n")
        con.commit()


def afficher(id):
    req = '''select * from contacts where id = ?'''
    curseur.execute(req, (id,))
    record = curseur.fetchone()
    print("Le nombre de ligne est : ", len(record))
    for items in record:
        print(items)
    con.commit()
    print("Affichage des donnees\n")


def recherchercontact(numero_telephone):
    req = ("select * FROM contacts WHERE numero_telephone==%s " %
           (numero_telephone))
    recorder = curseur.execute(req)
    for row in recorder:
        print("id :", row[0])
        print("nom :", row[1])
        print("prenom :", row[2])
        print("email :", row[3])
        print("numero_telephone :", row[4])
        print("adresse :", row[5])
        print("\n")
        con.commit()


def main():
    print("---!Application de Gestion des Contacts!---")
    choix = input("Donner votre choix de 1 a 5?\n")
    if int(choix) == 1:
        nom = input("Saisisser le nom du contacts\n ")
        prenom = input("Saisisser le prenom du contacts:\n")
        email = input("Donner votre email:\n")
        numero_telephone = input("Ecrire votre numero de tel:\n")
        adresse = input("Donner votre adresse:\n")
        insert(nom, prenom, email, numero_telephone, adresse)
        print("DONNEES ENREGISTRER AVEC SUCCES!!:\n")
    elif int(choix) == 2:
        readSqliteTable()
        id = input("saisisser l'id  a modifier:\n")
        afficher(id)
        nom = input("Donner le nom a modifier:\n")
        nom = input("Donner le nouveau nom :\n")
        update_contact(nom, id)
    elif int(choix) == 3:
        readSqliteTable()
        d = int(input("Donner l'id a supprimer :\n"))
        delete_contact(d)

    elif int(choix) == 4:
        readSqliteTable()
    elif int(choix) == 5:
        numtel = input("Saisir le numero de contact a rechercher\n")
        print("numero de telephone trouver\n")
        recherchercontact(numtel)

    else:
        print("choix nom disponible")


main()


con.commit()
con.close()
