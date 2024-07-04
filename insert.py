import mysql.connector

conexao = mysql.connector.connect(
    host ='127.0.0.1',
    user = 'root',
    password = '12Ngh67LL@',
    database = 'aula'
)


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

cursor.close()
conexao.close()