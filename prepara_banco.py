import mysql.connector
from mysql.connector import errorcode

print('Conectando...')
try: 
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password= 'admin'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACESS_DENIED_ERROR:
            print('Existe algo de errado no de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")
cursor.execute("CREATE DATABASE `jogoteca`;")
cursor.execute("USE `jogoteca`;")

#criando tabelas
TABLES = {}
TABLES['Jogos'] = ('''
  CRETATE TABLE `jogos` (
  `id` int (11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL, 
  `categoria` varchar(40) NOT NULL, 
  `console` varchar(20) NOT NULL,
  PRIMARY KEY(`id`)
  ) ENGINE = InnoDB DEFAULT CHARTSET = utf8 COLLATE = utf8_bin;''')

TABLES['Usuarios'] = ('''
  CRETATE TABLE `usuarios` (
  `nome` varchar(20) NOT NULL, 
  `nickname` varchar(8) NOT NULL, 
  `senha` varchar(100) NOT NULL,
  PRIMARY KEY(`nickname`)
  ) ENGINE = InnoDB DEFAULT CHARTSET = utf8 COLLATE = utf8_bin;''')

for tabela_nome in TABLES:
      table_sql = TABLES[tabela_nome]
      try:
            print("Criando tabela {}:" .format(tabela_nome), end='')
            cursor.execute(table_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print("Já existe")
            else:
                  print(err.msg)
      else:
            print("OK")

#INSERINDO USUÁRIOS
usuario_sql = "INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)"

usuarios = [
      ("Pedro Aiko", "aikola", "vascodagama"),
      ("Enzo Marques", "Enzo", "Deusebom"),
      ("Gabriel Gomes", "Biel", "vaicorinthians")
]

cursor.executemany(usuario_sql, usuarios)

cursor.execute("select * from jogoteca.usuarios")
print(" ----------------- Usuários: ------------")
for user in cursor.fetchall():
      print(user[1])

#inserindo jogos
jogos_sql = 'INSERT INTO jogos(nome, categoria, console) VALUES(%s, %s, %s)'
jogos = [
      ('Tetrs', 'Arcade', 'Atari'),
      ('FIFA', 'Esportes', 'XBOX/PS5/PC'),
      ('Zelda', 'Aventura', 'Nintendo SWITCH'),
      ('Need for speed', 'Corrida', 'XBOX/PS5/PC'),
      ('GOD OF WAR', 'Guerra', 'PS5/PC'), 
      ('GTA V', 'Mundo aberto', 'XBOX/PS5/PC')
]

cursor.executemany(jogos_sql, jogos)

cursor.execute('select * from jogoteca.jogos')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()