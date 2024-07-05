import mysql.connector
from config import db_config

db_host = db_config['host']
db_user = db_config['user']
db_password = db_config['password']
db_name = db_config['database']

conexao = mysql.connector.connect(
    host = db_host,
    user = db_user,
    password = db_password,
    database = db_name
)

print("conectei ao banco de dados")

cursor = conexao.cursor()

#Inserir no banco de dados

sql = "INSERT INTO cliente (cliente_id, nome, email) VALUES (%s, %s, %s)"
valores = (1, 'Joao', 'Joao@gmail.com')

cursor.execute(sql, valores)

conexao.commit()

print("Inserção realizada com sucesso!")


# sql_select = 'SELECT * FROM cliente'

# cursor.execute(sql_select)
# resultados = cursor.fetchall()

# for resultado in resultados:
#     cliente_id, nome, email = resultado
#     print(f"ID: {cliente_id}, Nome: {nome}, email:{email}")

#cursor.close()
conexao.close()