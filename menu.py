from controller import salvar, listar, presenca, salvarpresenca

def menu():
    menu = 1

    while (menu != 0):

        menu = int(input("1 - Fazer cadastro\n2 - Registrar presença\n3 - CRIAR LISTAR \n0 - Sair do sistema\n "))

        match menu:

            case 1:
                            pessoa = {}
                            pessoa['nome'] = input("Digite seu nome: ")
                            pessoa['cpf'] = input("Digite seu cpf: ")
                            pessoa['telefone'] = input("digite seu telefone")
                            pessoa['senha'] = int(input("Digite sua senha: "))

                            salvar(pessoa)

            case 2:
                registro = {}
                registro['nomes'] = input("Digite seu nome: ")
                registro['senhas'] = input("Digite sua senha: ")                           
                registro['horas'] = input('Digite que horário você chegou na aula: ')

                salvarpresenca(registro)

            case 3:
                listar()
                presenca()


