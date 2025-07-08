from flask import Flask, render_template, request

##request captura a informação que mandada pelo forms do novo.html

class jogos:
  def __init__(self, nome, categoria, console):
    self.nome = nome
    self.categoria = categoria
    self.console = console

jogo1 = jogos('Tetris', 'Arcade', 'Atari')
jogo2 = jogos('FIFA', 'Esportes', 'XBOX/PS5/PC')
jogo3 = jogos('Zelda', 'Aventura', 'Nintendo SWITCH')

lista = [jogo1, jogo2, jogo3]

app = Flask(__name__) ##Referência ao próprio arquivo(garante com que o código rode)

@app.route('/')
def index():
  jogo1 = jogos('Tetris', 'Arcade', 'Atari')
  jogo2 = jogos('FIFA', 'Esportes', 'XBOX/PS5/PC')
  jogo3 = jogos('Zelda', 'Aventura', 'Nintendo SWITCH')

  lista = [jogo1, jogo2, jogo3]

  return render_template('lista.html', titulo = 'Jogos', jogos=lista)

@app.route('/novo')
def novo():
  return render_template('novo.html', titulo = 'Novo Jogo')

@app.route('/criar', methods=['POST',]) ##é preciso avisar para o flask que usaremos o method post
def criar():
  nome = request.form['nome']
  categoria = request.form['categoria'] 
  console = request.form['console']
  jogo = jogos(nome, categoria, console)
  lista.append(jogo)
  return render_template('lista.html', titulo = 'Jogos', jogos = lista) 

app.run(debug=True) ##Roda a aplicação

