from flask import Flask,render_template

app = Flask(__name__)
# {{ url_for('home') }}
@app.route('/')
def home():
    test()
    return render_template("Menu.html")

@app.route("/connexion/")
def index():
    return render_template("Connexion.html")

@app.route("/animaux/")
def animaux():
    return render_template("AjoutAnimaux.html")

@app.route
def utilisateurs():
    return render_template("AjoutUtilisateur.html")

def test():
    print("test")


if __name__ == '__main__':
    app.run()
