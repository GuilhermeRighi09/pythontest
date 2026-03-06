from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!!</h1>"

@app.route("/curso")
def curso():
    return "<h1>Curso Técnico em Análise de Desenvolvimentos de Sistemas</h1>"

@app.route("/cidade")
def cidade():
    cidade = {
        "cidade": "Piracicaba",
        "ano": "258",
        "estado": "Sao Paulo",
        "Habitantes": 400000
    }
    return cidade

@app.route("/musicas")
def musica():
    musicas = ["Cheiro do Mato", "Blusa Vermelha", "Estrada da Vida"]
    return musicas

if __name__ == "__main__":
    app.run(debug=True)





