from flask import Flask, render_template, request, redirect, session, flash, url_for

##request captura a informação que mandada pelo forms do novo.html
##session guarda informações
##flash permite a adição de mensagens curtas na interface
##url_for dinamização de urls  

class jogos:
  def __init__(self, nome, categoria, console):
    self.nome = nome
    self.categoria = categoria
    self.console = console

jogo1 = jogos('Tetrs', 'Arcade', 'Atari')
jogo2 = jogos('FIFA', 'Esportes', 'XBOX/PS5/PC')
jogo3 = jogos('Zelda', 'Aventura', 'Nintendo SWITCH')

lista = [jogo1, jogo2, jogo3]

class usuario:
  def __init__(self, nome, nickname, senha):
    self.nome = nome
    self.nickname = nickname
    self.senha = senha

usuario1 = usuario("Pedro Aiko", "aikola", "vascodagama")
usuario2 = usuario("Enzo Marques", "Enzo", "Deusebom")
usuario3 = usuario("Gabriel Gomes", "Biel", "vaicorinthians")

usuarios = {usuario1.nickname : usuario1,
          usuario2.nickname : usuario2,
          usuario3.nickname : usuario3
}

app = Flask(__name__) ##Referência ao próprio arquivo(garante com que o código rode)
app.secret_key = 'alura' ##chave secreta para evitar erro no login

@app.route('/')
def index():

  return render_template('lista.html', titulo = 'Jogos', jogos=lista)

@app.route('/novo')
def novo():
  if 'usuario_logado' not in session or session['usuario_logado'] == None:
    return redirect(url_for('login', proxima = url_for('novo')))
  ##querystring -> parte da URL para parâmetros e valores para o servidor
  return render_template('novo.html', titulo = 'Novo Jogo')

@app.route('/criar', methods=['POST',]) ##é preciso avisar para o flask que usaremos o method post
def criar():
  nome = request.form['nome']
  categoria = request.form['categoria'] 
  console = request.form['console']
  jogo = jogos(nome, categoria, console)
  lista.append(jogo)
  return redirect (url_for('index')) ##redirecionar para a página inicial

@app.route('/login')
def login():
  proxima = request.args.get("proxima")
  return render_template('login.html', proximas = proxima)

@app.route('/autenticar', methods = ['POST',])
def autenticar():
  if request.form['usuario'] in usuarios:
    usuario = usuarios[request.form['usuario']]
    if request.form['senha'] == usuario.senha:
      session['usuario_logado'] = usuario.nickname
      flash(usuario.nickname + ' logado com sucesso')
      proxima_pag = request.form['proxima']
      return redirect(proxima_pag)
  else:
    flash('Falha no login')
    return redirect(url_for('login'))



  if "1234" == request.form['senha']:
    session['usuario_logado'] = request.form['usuario']
    flash(session['usuario_logado'] + ' logado com sucesso')
    proxima_pag = request.form['proxima']
    return redirect(proxima_pag)
  else:
    flash('Falha no login')
    return redirect(url_for('login'))
  
@app.route('/logout')
def logout():
  session['usuario_logado'] = None
  flash('Logout realizado com sucesso')
  return redirect(url_for('index'))


app.run(debug=True) ##Roda a aplicação

