from database_connection import create_connection

def main():
   connection = create_connection()
   cursor = connection.cursor()

   sql_select = 'SELECT * FROM cliente'
   cursor.execute(sql_select)
   
   resultados = cursor.fetchall() 
   
   #Retorna o Total de resultados daquela tabela
   print(f"Total de resultados: {len(resultados)}")
   
   exibir_resultados(resultados)

   close_connection(cursor, connection)

def exibir_resultados(resultados):
    for resultado in resultados:
        cliente_id, nome, email = resultado
        print(f"ID: {cliente_id}, Nome: {nome}, email:{email}")

def close_connection(cursor, conexao):
    cursor.close()
    conexao.close()

if __name__ == "__main__":
    main()