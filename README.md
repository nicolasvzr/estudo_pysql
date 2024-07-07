
# Estudo | CRUD 

Este repositório é para armazenar meus estudos sobre como realizar CRUD no banco de dados  utlizando python

##  Banco de dados
Utilizei um banco de dados relacional - **MySQL** 

Eu havia utilizado ele na faculdade, tive uma atividade que o proposito seria adicionar chaves primarias e estrangeiras
- Contem 7 tabelas: Cliente, curso, curso_estudante, empresa, endereço, estudante e funcionário

Nesse estudo utilizei apenas a Cliente que possui os campos: cliente_id, nome e email
## Aprendizados

Durante esse projeto pude melhorar meu raciocinio para construir o código, pesquisar e anotar o que eu errei. Abaixo está o processo para a criação.

1. Ao criar a conexão para o banco de dados decidir melhorar em alguns ponto, por exemplo:
- Não deixar a senha, root etc exposto no codigo, para isso criei um **config.py**  para deixar armazenado.
- Criar um arquivo a parte chamado de **database_connection** apenas com a conexão, chamando o **config.py** 

2. Criei o arquivo **Insert** para realizar o comando INSERT INTO no banco de dados.  Meu maior desafio apesar de ser simples para uns, foi criar classe para ""chamar"" a conexão do banco de dados entre outros. tive alguns erros durante o processo como:
- Atribui tuplas desnecessárias no arquivo do **database_connection**, só percebi ao executar o codigo em outros arquivos;
- O comando de execução do INSERT INTO deve ficar dentro da classe;

3. Commit e fetchall 
 - Aprendi que commit se usa para confirmar a transição e posso usar nos comando de **Insert into, Update, Delete e Create** 
 - E o fetchall usamos apenas no **Select** proprio para consultas. 

4. Sempre fechar o cursor e a conexão no final.




