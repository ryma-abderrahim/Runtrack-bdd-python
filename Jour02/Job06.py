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

# Récupérer la capacité total de toute les salles 
cur.execute("SELECT SUM(capacite) FROM salle")
resultats = cur.fetchall()

# Convertir le résultat en une chaîne de caractères et enlever le mot "Decimal"
capacite = str(resultats[0][0]).replace("Decimal", "")

# Afficher les résultats en console
print (f"La capacité de toutes les salles est de {capacite} m²") 

# Fermer la connexion à la base de données
cur.close()
db.close()