# Fichier cage.py
import sqlite3

class CageManager:
    def __init__(self, db_name='zoo.db'):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def ajouter_cage(self, superficie, capacite_max):
        self.cur.execute("INSERT INTO cage (superficie, capacite_max) VALUES (?, ?)", (superficie, capacite_max))
        self.conn.commit()

    def supprimer_cage(self, cage_id):
        self.cur.execute("DELETE FROM cage WHERE id = ?", (cage_id,))
        self.conn.commit()

    def modifier_cage(self, cage_id, superficie, capacite_max):
        self.cur.execute("UPDATE cage SET superficie = ?, capacite_max = ? WHERE id = ?", (superficie, capacite_max, cage_id))
        self.conn.commit()

    def afficher_cages(self):
        self.cur.execute("SELECT * FROM cage")
        cages = self.cur.fetchall()
        for cage in cages:
            print(cage)

    def calculer_superficie_totale(self):
        self.cur.execute("SELECT SUM(superficie) FROM cage")
        superficie_totale = self.cur.fetchone()[0]
        print(f"La superficie totale de toutes les cages est de {superficie_totale} m².")

    def fermer_connexion(self):
        self.conn.close()