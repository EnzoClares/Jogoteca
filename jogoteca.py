from flask import Flask, render_template

class jogos:
  def __init__(self, nome, categoria, console):
    self.nome = nome
    self.categoria = categoria
    self.console = console

app = Flask(__name__) ##Referência ao próprio arquivo(garante com que o código rode)

@app.route('/inicio')
def ola():
  jogo1 = jogos('Tetris', 'Arcade', 'Atari')
  jogo2 = jogos('FIFA', 'Esportes', 'XBOX/PS5/PC')
  jogo3 = jogos('Zelda', 'Aventura', 'Nintendo SWITCH')

  lista = [jogo1, jogo2, jogo3]

  return render_template('lista.html', titulo = 'Jogos', jogos=lista)

@app.route('/novo')
def novo():
  return render_template('novo.html', titulo = 'Novo Jogo')

app.run() ##Roda a aplicação

