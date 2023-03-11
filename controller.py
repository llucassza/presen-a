def salvar(nome): 
    with open ("pessoas.txt", "a") as arquivo:  
        arquivo.write(f"{nome}\n") 

def salvarpresenca(nome): 
    with open ("presenca.txt", "a") as arquivo:  
        arquivo.write(f"{nome}\n") 

def listar():
    nomes = [] 
    with open("pessoas.txt", "r") as arquivo: 
        for name in arquivo:
            name = name.strip() 
            nomes.append(name) 
        return nomes

def presenca():
    nomes = [] 
    with open("presenca.txt", "r") as arquivo: 
        for name in arquivo:
            name = name.strip() 
            nomes.append(name) 
        return nomes