# Fichier animal.py
import sqlite3
from animal import *
from cage import *


class AnimalManager:
    def __init__(self, db_name='zoo.db'):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def ajouter_animal(self,animal_id, nom, race, cage_id, date_naissance, pays_origine):
        self.cur.execute("INSERT INTO animal (id,nom, race, cage_id, date_naissance, pays_origine) VALUES (?,?,?,?,?)",(animal_id,nom,race,cage_id,date_naissance, pays_origine))
        self.conn.commit()

    def supprimer_animal(self, animal_id):
        self.cur.execute("DELETE FROM animal WHERE id = {}", (animal_id,))
        self.conn.commit()

    def modifier_animal(self, animal_id, nom, race, cage_id, date_naissance, pays_origine):
        self.cur.execute("UPDATE animal SET nom = ?, race = ?, cage_id = ?, date_naissance = ?, pays_origine = ? WHERE id = ?", (nom, race, cage_id, date_naissance, pays_origine, animal_id))
        self.conn.commit()

    def afficher_animaux(self):
        self.cur.execute("SELECT * FROM animal")
        animaux = self.cur.fetchall()
        for animal in animaux:
            print(animal)

    def fermer_connexion(self):
        self.conn.close()