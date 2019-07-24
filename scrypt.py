from flask import Flask, url_for, render_template, redirect
import psycopg2 as psy
import os
app = Flask(__name__)

#Connexion à la base de données 
def connexionDB():
    try:
        DATABASE_URL = os.environ['DATABASE_URL']
        connexion = psy.connect(DATABASE_URL, sslmode='require')
        print('ok')
        return connexion
    except psy.OperationalError:
        print('Erreur lors de la connexion à la base de données!!!')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/apprenant/inscription")
def inscriptionApprenant():
    return render_template('scolarite/inscription.html', referentiels=findAllReferentiel())

def createTable():
    connexion = connexionDB()
    cursor = connexion.cursor()
    cursor.execute("CREATE TABLE maj(idapp serial, nomapp varchar(100))")
    connexion.commit()

def findAllReferentiel():
    connexion = connexionDB()
    cursor = connexion.cursor()
    sql = " SELECT * FROM referentiel "
    cursor.execute(sql)
    donnees = cursor.fetchall()
    return donnees

if __name__ == "__main__":
    app.run()
