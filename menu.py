from controller import registrar


def menu():
    menu = 1

    while (menu != 0):

        menu = int(
            input("1 - Fazer cadastro\n2 - Registrar presença\n0 - Sair do sistema\n "))

        match menu:

            case 1:
                pessoa = {}
                pessoa["nome"] = input("Digite seu nome: ")
                pessoa["cpf"] = input("Digite seu cpf: ")
                pessoa["telefone"] = input("digite seu telefone")
                pessoa["senha"] = int(input("Digite sua senha: "))

            case 2:
                registrar()
