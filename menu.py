from controller import salvar, listar, presenca, salvarpresenca
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

def menu():
    menu = 1

    while (menu != 0):

        menu = int(input("1 - Fazer cadastro\n2 - Registrar presença\n3 - Gerar listas \n0 - Sair do sistema\n "))

        match menu:

            case 1:
                            pessoa = {}
                            pessoa['Nome'] = input("Digite seu nome: ")
                            pessoa['CPF'] = input("Digite seu cpf: ")
                            pessoa['Telefone'] = input("digite seu telefone: ")
                            pessoa['Senha'] = int(input("Digite sua senha: "))

                            salvar(pessoa)

            case 2:
                registro = {}
                registro['CPF'] = input("Digite seu CPF: ")                          
                registro['Horário de registro'] = (current_time)

                salvarpresenca(registro)
                print(f"Presença Registrada ás {current_time}")

            case 3:
                listar()
                presenca()


