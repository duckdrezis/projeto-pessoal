import mysql.connector

conexao = mysql.connector.connect( host = 'localhost', user = 'root', password = '_____', database = '____',)
cursor = conexao.cursor()

#CRUD EM PYTHON COM MYSQL PELO VISUAL STUDIO CODE
#CRIAR UM BD NO MYSQL WORKBANCH COM O NOME DA TABELA "Vendas"
#CRIAR COLUNAS COM OS NOMES "idvendas" "nome_produto", "valor"




#CREATE
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("Pizza fatia", "12")'
cursor.execute(comando) # executa comando
conexao.commit() # aqui ele vai editar bd

#READ
comando = f'SELECT * FROM vendas'
cursor.execute(comando) # executa comando
resultado = cursor.fetchall() # aqui ele vai ler o bd
print(resultado) #print exibe o resultado

#UPDATE
comando =f'UPDATE vendas SET nome_produto = "Toddynho" WHERE nome_produto = "todynho" '
cursor.execute(comando)
conexao.commit() #novamente aqui ele vai fazer uma alteração no bd

#DELETE
comando =f'DELETE FROM vendas WHERE idVendas IN (4, 5, 6) '
cursor.execute(comando)
conexao.commit()#adivinha, esse aqui altera o bd

#PRA ENCERRAR OS COMANDOS DO CURSOR E E DA CONEXÃO DEVE EXISTIR OS SEGUINTES ".CLOSE'S"
cursor.close()
conexao.close()