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

# Récupérer les noms et les capacités de la table "salle"
cur.execute("SELECT nom, capacite FROM salle")
resultats = cur.fetchall()

# Afficher les résultats en console
result=[]
for nom, capacite in resultats:
    result.append(f"('{nom}',{capacite})")

print (result) 

# Fermer la connexion à la base de données
cur.close()
db.close()