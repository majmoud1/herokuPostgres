from flask import Flask, url_for, render_template, redirect
import psycopg2 as psy
app = Flask(__name__)

#Connexion à la base de données 
def connexionDB():
    serveur = "ec2-174-129-227-128.compute-1.amazonaws.com"
    bd = "def6p9u6t0o45m"
    userBD = "zdfyfzhzxntvpi"
    mdp = "e691227410d4268e9699a16c8d2b80b902994a58c189d01f7226f6ef75b478e7"
    port ="5432"
    #uri = "postgres://zdfyfzhzxntvpi:e691227410d4268e9699a16c8d2b80b902994a58c189d01f7226f6ef75b478e7@ec2-174-129-227-128.compute-1.amazonaws.com:5432/def6p9u6t0o45m"
    try:
        connexion = psy.connect(host=serveur, database=bd, user=userBD, password=mdp, port=port)
        print('ok')
        return connexion
    except psy.OperationalError:
        print('Erreur lors de la connexion à la base de données!!!')

@app.route('/')
def index():
    render_template('index.html')

@app.route("/apprenant/inscription")
def inscriptionApprenant():
    render_template('scolarite/inscription.html', referentiels=findAllReferentiel())

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