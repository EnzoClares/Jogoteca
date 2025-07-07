from flask import Flask

app = Flask(__name__) ##Referência ao próprio arquivo(garante com que o código rode)

@app.route('/inicio')
def ola():
  return "<h1> Olá Mundo </h1>"

app.run() ##Roda a aplicação

