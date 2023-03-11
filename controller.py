def listarPessoa(clientfind):
    index = 0
    flag = 0
    arquivo = open("pessoas.txt", "r")

    for line in arquivo:
        index += 1

        if clientfind ==eval(line)['nome']:

            print(line)
            flag = 1

    if flag == 0:
        print("não encontrado")

def deletarPessoa(clientefind):
    index = 0
    flag = 0
    arquivo = open("pessoas.txt", "r")
    for line in arquivo:
        index += 1

        if clintefind == eval(line)['nome']:
            chave = index
            flag = 1

    arquivo.close()

    if flag == 0:
        print("não encontrado")
    else:

        try:
            with open('pessoas.txt', 'r') as arquivo:
                lines = arquivo.readlines()
                posicao = 1
                with open('pessoas.txt', 'w') as arquivo:

                    for line in lines:
                        if posicao != chave:
                            arquivo.write(line)
                        posicao += 1

            print('pessoa deletada')
        except:
            print('Erro sistema interno ')

# def salvar(nome): ##cria função "salvar" que recebe o dado da variável nome
#     with open ("pessoas.txt", "a") as arquivo: ##cria arquivo pessoas.txt que recebe e armazena os itens da função salvar 
#         arquivo.write(f"{nome}\n") ##inputar dado "nome" a ser salvo no arquivo pessoas.txt

# def listar(): ##cria função listar que lista os itens do arquivo pessoas.txt
#     nomes = [] ##lista em indices, os itens do arquivo pessoas.txt
#     with open("pessoas.txt", "r") as arquivo: ##abre o arquivo pessoas.txt
#         for name in arquivo: ##condição da varivavel nome dentro da função arquivo
#             name = name.strip() ##lista os nomes de uma forma sequencial
#             nomes.append(name) ##insere os itens de nome dentro da lista 
#         return nomes