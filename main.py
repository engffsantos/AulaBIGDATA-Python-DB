import mysql.connector
from mysql.connector import errorcode
def conecta(query, values=0):
    try:
        cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='empresa')
        cursor = cnx.cursor()
        if values==0:
            cursor.execute(query)
        else:
            cursor.execute(query, values)
        fech = cursor.fetchall()
        return fech
    except mysql.connector.Error as erro:
        if erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuário ou senha inválidos")
        elif erro.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados não existe")
        else:
            print(erro)
    finally:
        cursor.close()
        cnx.close()
# Função para inserir um novo funcionário
def inserir_funcionario():
    # Coletar os dados do novo funcionário
    primeiro_nome = input("Primeiro nome: ")
    segundo_nome = input("Segundo nome: ")
    ultimo_nome = input("Último nome: ")
    data_nascimento = input("Data de nascimento (AAAA-MM-DD): ")
    cpf = input("CPF: ")
    rg = input("RG: ")
    endereco = input("Endereço: ")
    cep = input("CEP: ")
    cidade = input("Cidade: ")
    fone = input("Telefone: ")
    codigo_departamento = input("Código do departamento: ")
    funcao = input("Função: ")
    salario = input("Salário: ")

    # Inserir o novo funcionário na tabela
    query = "INSERT INTO funcionarios (PrimeiroNome, SegundoNome, UltimoNome, DataNasci, CPF, RG, Endereco, CEP, Cidade, Fone, CodigoDepartamento, Funcao, Salario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (primeiro_nome, segundo_nome, ultimo_nome, data_nascimento, cpf, rg, endereco, cep, cidade, fone, codigo_departamento, funcao, salario)
    conecta(query, values)
    print("Funcionário inserido com sucesso!")

# Função para atualizar os dados de um funcionário existente
def atualizar_funcionario():
    # Coletar o código do funcionário a ser atualizado
    codigo = input("Código do funcionário a ser atualizado: ")

    # Verificar se o funcionário existe na tabela
    query = "SELECT * FROM funcionarios WHERE Codigo = %s"
    values = (codigo,)
    cursor = conecta(query, values)
    result = cursor.fetchone()

    if result is None:
        print("Funcionário não encontrado!")
        return

    # Coletar os novos dados do funcionário
    primeiro_nome = input(f"Novo primeiro nome ({result[1]}): ") or result[1]
    segundo_nome = input(f"Novo segundo nome ({result[2]}): ") or result[2]
    ultimo_nome = input(f"Novo último nome ({result[3]}): ") or result[3]
    data_nascimento = input(f"Nova data de nascimento ({result[4]}): ") or result[4]
    cpf = input(f"Novo CPF ({result[5]}): ") or result[5]
    rg = input(f"Novo RG({result[6]}): ") or result[6]
    endereco = input(f"Novo endereço ({result[7]}): ") or result[7]
    cep = input(f"Novo CEP ({result[8]}): ") or result[8]
    cidade = input(f"Nova cidade ({result[9]}): ") or result[9]
    fone = input(f"Novo telefone ({result[10]}): ") or result[10]
    codigo_departamento = input(f"Novo código de departamento ({result[11]}): ") or result[11]
    funcao = input(f"Nova função ({result[12]}): ") or result[12]
    salario = input(f"Novo salário ({result[13]}): ") or result[13]
# Atualizar os dados do funcionário na tabela
    query = "UPDATE funcionarios SET PrimeiroNome = %s, SegundoNome = %s, UltimoNome = %s, DataNasci = %s, CPF = %s, RG = %s, Endereco = %s, CEP = %s, Cidade = %s, Fone = %s, CodigoDepartamento = %s, Funcao = %s, Salario = %s WHERE Codigo = %s"
    values = (primeiro_nome, segundo_nome, ultimo_nome, data_nascimento, cpf, rg, endereco, cep, cidade, fone, codigo_departamento, funcao, salario, codigo)
    conecta(query, values)
    print("Funcionário atualizado com sucesso!")
def apagar_funcionario():
# Coletar o código do funcionário a ser apagado
    codigo = input("Código do funcionário a ser apagado: ")
    # Verificar se o funcionário existe na tabela
    query = "SELECT * FROM funcionarios WHERE Codigo = %s"
    values = (codigo,)
    cursor = conecta(query, values)

    if cursor is None:
        print("Funcionário não encontrado!")
        return

    # Confirmar a exclusão do funcionário
    confirmar = input(f"Tem certeza que deseja apagar o funcionário {result[1]} {result[2]} {result[3]}? (s/n) ")

    if confirmar.lower() == "s":
        # Apagar o funcionário da tabela
        query = "DELETE FROM funcionarios WHERE Codigo = %s"
        values = (codigo,)
        conecta(query, values)


        print("Funcionário apagado com sucesso!")
def lista_funcionario():
    query = "SELECT CONCAT(PrimeiroNome, ' ', UltimoNome) AS nome_completo, Salario FROM funcionarios"
    cursor = conecta(query)
    for i in cursor:
        print(i[0], "-", i[1])
def lista_expecifica():
    query = """SELECT *, DATEDIFF(CURDATE(), DataNasci)/365.25 AS idade
    FROM funcionarios
    WHERE DATEDIFF(CURDATE(), DataNasci)/365.25 < 30
    AND Salario > 1000 """
    cursor = conecta(query)
    for i in cursor:
        print(i[0], "-", i[1])

while True:
    print("\n*** MENU PRINCIPAL ***\n",'=='*15)
    print("1 - Inserir\n"
          "2 - Atualizar\n"
          "3 - Apagar Funcionario\n"
          "4 - Listar Funcionario\n"
          "5 - Listar Funcionarios com idade menor 30 anos e com salario maior do que R$1000,00 \n"
          "6 - Sair")
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        inserir_funcionario()
    elif opcao == "2":
        atualizar_funcionario()
    elif opcao == "3":
        apagar_funcionario()
    elif opcao == "4":
        lista_funcionario()
    elif opcao == "5":
        lista_expecifica()
    elif opcao == "6":
        break
    else:
        print("Opção inválida!")

#funcionario_atualizado = ("João", "Carlos", "Silva", "1980-07-15", "123.456.789-00", "12.345.678-9", "Rua A, 123", "12345-000", "São Paulo", "(11) 98765-4321", 1, "Gerente", 11000.00)