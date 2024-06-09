menu = """
__________________________________________________
Olá!!! Bem vindo ao banco! Selecione alguma opção:
==================================================
[1] Sacar
[2] Depositar
[3] Extrato
[4] Novo usuário
[5] Nova conta
[6] Listar contas
[7] Sair
"""
#1
def sacar(*, saldo, valor, limite, numero_saques, limite_saques, extrato):
    if valor > saldo:
        print('Saldo insuficiente!')
        return saldo, numero_saques, extrato

    if valor > limite:
        print('O limite de saque é de R$500!')
        return saldo, numero_saques, extrato

    if numero_saques >= limite_saques:
        print('Limite de saques diários atingido!')
        return saldo, numero_saques, extrato

    saldo -= valor
    numero_saques += 1
    extrato += f"Saque: R$ {valor:.2f}\n"
    print('Saque realizado com sucesso!')
    return saldo, numero_saques, extrato

#2
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f'Depósito de R$ {valor:.2f} realizado! Saldo atual: R$ {saldo:.2f}')
    else:
        print("Valor inválido. Digite um valor válido para depositar.")
    return saldo, extrato

#3
def exibir_extrato(saldo, /, *, extrato):
    print("EXTRATO: ")
    print(extrato)
    print(f"Saldo: R$ {saldo:.2f}")

#4
def criar_usuario(usuarios):
    cpf = input('Informe seu CPF: ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('Este CPF já está em uso!')
        return
    
    nome = input('Informe seu nome completo: ')
    data_nascimento = input('Informe data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe endereço (logradouro, numero - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('!!!!USUARIO CRIADO!!!')

#filtrando 4
def filtrar_usuarios(cpf, usuarios):
    for usuario in usuarios:
        if usuario.get('cpf') == cpf:
            return usuario
    return None

#5
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe seu CPF: ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print('Usuario não encontrado')

#6
def listar_contas(contas):
    for conta in contas:
        linha = f'''\
Agência: {conta['agencia']}
Nº Conta: {conta['numero_conta']}
Titular: {conta['usuario']['nome']}
'''
        print('=' * 100)
        print(linha)

def main(): 
    agencia = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    saques = 0
    limite_saques = 3
    usuarios = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "1":  
            valor_saque = float(input('Informe o valor que deseja sacar: '))
            saldo, saques, extrato = sacar(saldo=saldo, valor=valor_saque, limite=limite, numero_saques=saques, limite_saques=limite_saques, extrato=extrato)

        elif opcao == "2":
            valor_deposito = float(input('Informe o valor que deseja depositar: '))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            print("Saindo! Agradecemos a preferência :)")
            break

main()
