listaOrganizacoes = []
listaPropriedades = []

def listarPropriedades(listaPropriedades):

    contador = 1
    for propriedades in listaPropriedades:
        print(f'{contador}. {propriedades}')
        contador += 1

def adicionarPropriedade(listaPropriedades):

    nomePropriedade = input('Digite o nome da propriedade: ')
    localizacaoPropridade = input('Digite a localizacao da propriedade: ')
    tipoDeCultulra = input('Digite a cultura que a propriedade produz: ')

    novaPropriedade = {
        "nome" : nomePropriedade,
        "localizacao": localizacaoPropridade,
        "cultura": tipoDeCultulra
    }

    listaPropriedades.append(novaPropriedade)
    print('Propriedade adicionada com sucesso.')

def excluirPropriedade(listaPropriedades):
    
    listarPropriedades(listaPropriedades)
    try:
        escolha = int(input('Escolha a propriedade a ser excluida: '))
    except:
        print('Operacao nao concluida, escolha um numero inteiro valido.')
    
    if escolha <= len(listaPropriedades):
        listaPropriedades.pop(escolha-1)
        print('Propriedade excluida com sucesso.')
    else:
        print('Operacao nao concluida, propriedade nao existe.')
   

def atualizarPropriedades(listaPropriedades):
    
    listarPropriedades(listaPropriedades)
    try:
        escolha = int(input('Escolha a propriedade a ser atualizada: '))
    except:
        print('Operacao nao concluida, escolha um numero inteiro valido.')
    
    if escolha <= len(listaPropriedades):
        nomePropriedade = input('Digite o nome da propriedade: ')
        localizacaoPropridade = input('Digite a localizacao da propriedade: ')
        tipoDeCultulra = input('Digite a cultura que a propriedade produz: ')

        novaPropriedade = {
            "nome" : nomePropriedade,
            "localizacao": localizacaoPropridade,
            "cultura": tipoDeCultulra
        }

        listaPropriedades[escolha-1] = novaPropriedade
        print('Propriedade atualizada com sucesso.')
    else:
        print('Operacao nao concluida, propriedade nao existe.')
    

def listarOrganizacoes(listaOrganizacoes):

    contador = 1
    for organizacao in listaOrganizacoes:
        print(f'{contador}. {organizacao}')
        contador += 1

def criarOrganicao(listaOrganizacoes):

    nomeOrganizacao = input('Digite o nome da organizacao: ')
    segmentoOrganizacao = input('Digite o segmento da organizacao: ')
    propriedadesOrganizacao = []
    while True:
        print('Adicione uma propriedade a organizacao: ')
        listarPropriedades(listaPropriedades)
        try:
            escolha = int(input('Escolha uma propriedade: '))
        except:
            print('Operacao nao concluida, escolha um numero inteiro valido.')
        if escolha <= len(listaPropriedades):
            propriedadesOrganizacao.append(listaPropriedades[escolha-1])
        else:
            print('Operacao nao concluida, propriedade nao existe.')
        parar = input('Deseja adicionar mais uma propriedade? (s) sim (n) nao: ')
        if parar.lower() == 'n':
            break
        
    novaOrganizacao = {
        "nome" : nomeOrganizacao,
        "segmento": segmentoOrganizacao,
        "propriedades": propriedadesOrganizacao
    }
    
    listaOrganizacoes.append(novaOrganizacao)
    print('Organizacao criada com sucesso.')
    
def excluirOrganizacao(listaOrganizacoes):
        
    listarOrganizacoes(listaOrganizacoes)
    try:
        escolha = int(input('Escolha a organizacao a ser excluida: '))
    except:
        print('Operacao nao concluida, escolha um numero inteiro valido.')
    if escolha <= len(listaOrganizacoes):
        listaOrganizacoes.pop(escolha-1)
        print('Organizacao excluida com sucesso.')
    else:
        print('Operacao nao concluida, organizacao nao existe.')
    
        
def atualizarOrganizacoes(listaOrganizacoes):
    
    listarOrganizacoes(listaOrganizacoes)
    try:
        escolhaOrganizacao = int(input('Escolha a organizacao a ser atualizada: '))
    except:
        print('Operacao nao concluida, escolha um numero inteiro valido.')
    if escolhaOrganizacao <= len(listaOrganizacoes):
        nomeOrganizacao = input('Digite o nome da organizacao atualizada: ')
        segmentoOrganizacao = input('Digite o segmento da organizacao atualizada: ')
        propriedadesOrganizacao = []
        while True:
            print('Adicione uma propriedade a organizacao atualizada: ')
            listarPropriedades(listaPropriedades)
            try:
                escolhaPropriedade = int(input('Escolha uma propriedade: '))
            except:
                print('Operacao nao concluida, escolha um numero inteiro valido.')
            propriedadesOrganizacao.append(listaPropriedades[escolhaPropriedade-1])
            parar = input('Deseja adicionar mais uma propriedade? (s) sim (n) nao: ')
            if parar.lower() == 'n':
                break
            
        novaOrganizacao = {
            "nome" : nomeOrganizacao,
            "segmento": segmentoOrganizacao,
            "propriedades": propriedadesOrganizacao
        }
        listaOrganizacoes[escolhaOrganizacao-1] = novaOrganizacao
        print('Organizacao atualizada com sucesso.')
    else:
        print('Essa organizacao nao existe na lista')  
    

while True:


    print('\n1. Adicionar propriedade\n2. Listar propriedades')
    print('3. Excluir propriedade\n4. Atualizar propriedade')
    print('5. Criar organizacao\n6. Listar organizacoes')
    print('7. Excluir organizacao\n8. Atualizar organizacao\n9. Sair\n')
    try:
        escolha = int(input('Escolha uma opcao: '))
    except:
        print('Operacao nao concluida, escolha um numero inteiro valido.')

    if escolha == 1:
        adicionarPropriedade(listaPropriedades)
    if escolha == 2:
        listarPropriedades(listaPropriedades)
    if escolha == 3:
        excluirPropriedade(listaPropriedades)
    if escolha == 4:
        atualizarPropriedades(listaPropriedades)
    if escolha == 5:
        criarOrganicao(listaOrganizacoes)
    if escolha == 6:
        listarOrganizacoes(listaOrganizacoes)
    if escolha == 7:
        excluirOrganizacao(listaOrganizacoes)
    if escolha == 8:
        atualizarOrganizacoes(listaOrganizacoes)
    if escolha == 9:
        break
    if escolha < 1 or escolha > 9:
        print('\nEscolha uma opcao valida.')
    

    