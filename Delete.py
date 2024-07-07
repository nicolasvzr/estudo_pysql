from database_connection import create_connection

def main():
    connection = create_connection()
    cursor = connection.cursor()

    sql_delete = 'DELETE FROM cliente where cliente_id = 8'
    cursor.execute(sql_delete)

    connection.commit()
    
    print("Exclusão realizada com sucesso!")

def close_connection(cursor, conexao):
    cursor.close()
    conexao.close()

if __name__ == "__main__":
    main()


