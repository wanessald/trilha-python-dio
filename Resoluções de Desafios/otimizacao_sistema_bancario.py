def menu():
    acoes = """
        === Escolha a operação que deseja executar ===    
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nu]\tNovo Usuário
        [nc]\tNova Conta
        [lsu]\tListar Usuários
        [lsc]\tListar Contas
        [q]\tSair
        ==============================================
    => """

    return input(acoes)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe um usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})

    print("Usuário criado com sucesso!")

    return usuarios

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_usuarios(usuarios):
    if usuarios:
        print("\n ==== Lista de Usuários ====")
        for usuario in usuarios:
            print(
                f"Nome: {usuario['nome']}, "
                f"CPF: {usuario['cpf']}, "
                f"Data de Nascimento: {usuario['data_nascimento']}, "
                f"Endereço: {usuario['endereco']}"
            )
    else:
        print("\n Não há usuários cadastrados!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\nUsuário não encontrado, por favor cadastre um usuário antes de criar uma conta.")
        return
    
    return {
        "agencia": agencia, 
        "numero_conta": numero_conta, 
        "usuario": usuario
    }

def listar_contas(contas):
    if contas:
        print("\n ==== Lista de Contas ====")
        for conta in contas:
            print(
                f"Agência: {conta['agencia']}, "
                f"Número da Conta: {conta['numero_conta']}, "
                f"Titular: {conta['usuario']['nome']}"
            )
    else:
        print("\n Não há contas cadastradas!")
    
def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:

        opcao = menu()

        if opcao == "d":
            print("=="*24)
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            cadastrar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lsu":
            listar_usuarios(usuarios)

        elif opcao == "lsc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()