import mysql.connector

# Se connecter à la base de données
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sql1234@",
  database="LaPlateforme"
)

# Créer un curseur pour exécuter les requêtes
cur = db.cursor()


# Récupérer les employes qui ont un salaire sup à 3000 
cur.execute("SELECT * FROM employe WHERE salaire > 3000")
resultats = cur.fetchall()

# Afficher les résultats en console
print("Listes des employés avec un salaire >3000")
for row in resultats:
    print(row)

# Récupérer tout les employer avec leur service 
cur.execute("SELECT * FROM employe JOIN service ON employe.id_service = service.id")
resultats = cur.fetchall()

print ("\nlistes des employer et leurs services")
# Afficher les résultats en console
for row in resultats:
    print(row)


# Fermer la connexion à la base de données
cur.close()
db.close()


print("\nClasse Employe")
#----------------------Classe employe---------------------------------#
class Employe:
    def __init__(self):
        self.connexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sql1234@",
            database="LaPlateforme"
        )

    def get_employes(self):
        cursor = self.connexion.cursor()
        cursor.execute("SELECT employe.nom, service.nom AS service FROM employe INNER JOIN service ON employe.id_service = service.id")
        employes = cursor.fetchall()
        cursor.close()
        return employes

    def create_employe(self, nom, service_id):
        cursor = self.connexion.cursor()
        cursor.execute("INSERT INTO employe (nom, id_service) VALUES (%s, %s)", (nom, service_id))
        self.connexion.commit()
        cursor.close()

    def update_employe(self, employe_id, nom, service_id):
        cursor = self.connexion.cursor()
        cursor.execute("UPDATE employe SET nom = %s, id_service = %s WHERE id = %s", (nom, service_id, employe_id))
        self.connexion.commit()
        cursor.close()

    def delete_employe(self, employe_id):
        cursor = self.connexion.cursor()
        cursor.execute("DELETE FROM employe WHERE id = %s", (employe_id,))
        self.connexion.commit()
        cursor.close()

# Exemple d'utilisation de la classe
employe = Employe()

# Récupérer tous les employés et leur service respectif
resultat = employe.get_employes()
for ligne in resultat:
    print("Nom:", ligne[0])
    print("Service:", ligne[1])
    print()

# Créer un nouvel employé
employe.create_employe("John Doe", 1)

# Mettre à jour un employé existant
employe.update_employe(1, "Jane Smith", 2)

# Supprimer un employé
employe.delete_employe(1)