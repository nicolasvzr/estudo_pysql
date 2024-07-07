from database_connection import create_connection

def main():
    connection = create_connection()
    cursor = connection.cursor()

    print("conectei ao banco de dados")

    #Inserir no banco de dados

    sql = "INSERT INTO cliente (cliente_id, nome, email) VALUES (%s, %s, %s)"
    valores = [
        (9,'Miguel Rodrigues', ' miguel.rodrigues@gmail.com' )
        #(6, 'Sofia Martins', 'sofia.martins@outlook.com'),
        #(7, 'José Ferreira', 'jose.ferreira@uol.com.br')
    ]

    for valor in valores:
        cursor.execute(sql, valor)
        connection.commit()

print("Inserção realizada com sucesso!")

def close_connection(cursor, conexao):
    cursor.close()
    conexao.close()

if __name__ == "__main__":
    main()