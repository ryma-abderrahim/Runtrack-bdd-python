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

# Récupérer la superficie de touts les étages 
cur.execute("SELECT SUM(superficie) FROM etage")
resultats = cur.fetchall()

# Convertir le résultat en une chaîne de caractères et enlever le mot "Decimal"
superficie = str(resultats[0][0]).replace("Decimal", "")

# Afficher les résultats en console
print (f"Ls superficie de La Plateforme est de {superficie} m²") 

# Fermer la connexion à la base de données
cur.close()
db.close()