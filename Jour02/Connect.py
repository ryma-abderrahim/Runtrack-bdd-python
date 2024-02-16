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

# Exécuter la requête pour récupérer tous les étudiants
cur.execute("SELECT * FROM etudiant")

# Récupérer tous les enregistrements
result = cur.fetchall()

# Afficher le résultat dans la console
for row in result:
  print(row)

# Fermer la connexion à la base de données
cur.close()
db.close()