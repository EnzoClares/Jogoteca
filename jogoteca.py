from flask import Flask, render_template, request, redirect, session, flash

##request captura a informação que mandada pelo forms do novo.html
##session guarda informações
##flash permite a adição de mensagens curtas na interface  

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
app.secret_key = 'alura' ##chave secreta para evitar erro no login

@app.route('/')
def index():

  return render_template('lista.html', titulo = 'Jogos', jogos=lista)

@app.route('/novo')
def novo():
  if 'usuario_logado' not in session or session['usuario_logado'] == None:
    return redirect('/login')
  return render_template('novo.html', titulo = 'Novo Jogo')

@app.route('/criar', methods=['POST',]) ##é preciso avisar para o flask que usaremos o method post
def criar():
  nome = request.form['nome']
  categoria = request.form['categoria'] 
  console = request.form['console']
  jogo = jogos(nome, categoria, console)
  lista.append(jogo)
  return redirect ('/') ##redirecionar para a página inicial

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/autenticar', methods = ['POST',])
def autenticar():
  if "1234" == request.form['senha']:
    session['usuario_logado'] = request.form['usuario']
    flash(session['usuario_logado'] + ' logado com sucesso')
    return redirect('/')
  else:
    flash('Falha no login')
    return redirect('/login')
  
@app.route('/logout')
def logout():
  session['usuario_logado'] = None
  flash('Logout realizado com sucesso')
  return redirect('/')


app.run(debug=True) ##Roda a aplicação

