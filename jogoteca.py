from flask import Flask, render_template

app = Flask(__name__) ##Referência ao próprio arquivo(garante com que o código rode)

@app.route('/inicio')
def ola():

  jogos = ["Mario", "FIFA", "PES", "ZELDA"]

  return render_template("lista.html", titulo = "Jogos", jogos=jogos)

app.run() ##Roda a aplicação

