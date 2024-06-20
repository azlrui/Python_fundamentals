import sqlite3

def question2_1():
    db = sqlite3.connect('books.db')
    cursor = db.cursor()

    for row in cursor.execute("SELECT * FROM `livres` WHERE `nom_auteur` = ?", ("Steinbeck",)):
        print(row)

    return db.close()


def question2_2(query) :
    db = sqlite3.connect("books.db")
    cursor = db.cursor()

    for row in cursor.execute("SELECT * FROM `livres` WHERE `nom_auteur` = ?", (query, )):
        print(row)

    return db.close()

def question2_2_2(query) :
    db = sqlite3.connect("books.db")
    cursor = db.cursor()

    for row in cursor.execute("SELECT * FROM `livres` WHERE `année` = ?", (query, )):
        print(row)

    return db.close()

def question3(auteur = "Steinbeck"):
    db = sqlite3.connect("books.db")
    cursor = db.cursor()

    for row in cursor.execute("SELECT * FROM `livres` WHERE `nom_auteur` = ?", (auteur, )):
        print(row)

    print(cursor.description)

    field_names = [x[0] for x in cursor.description]
    print(field_names)

    records = tuple(cursor.execute("SELECT * FROM `livres` WHERE `nom_auteur` = ?", (auteur, )))

    for record in records:
        for i in range(len(field_names)):
            print(f"{field_names[i]} : {record[i]}, ", end ="")
        print("\n")

    return db.close()

def question4(token):
    db = sqlite3.connect("books.db")
    cursor = db.cursor()

    for row in cursor.execute(f"SELECT * FROM `livres` WHERE `nom_auteur` = '{token}'"):
        print(row)

def dict_factory(cursor, row):
    return dict([(col[0], row[idx]) for idx, col in enumerate(cursor.description)])

def question5():
    db = sqlite3.connect("books.db")
    db.row_factory = dict_factory

    cursor = db.cursor()
    for row in cursor.execute(" SELECT * FROM `livres` WHERE `nom_auteur` = ?",("Steinbeck",)) :
        print(row)

if __name__ == "__main__":
    #question2_1()
    #question2_2(input("Quel auteur cherchez-vous?"))
    #question2_2_2(input("Quelle année cherchez-vous?"))
    #question3()
    #question4(input("token"))
    question5()

