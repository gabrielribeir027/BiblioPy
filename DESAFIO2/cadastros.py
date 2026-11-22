from validacoes import validar_codigo

livros = []
def cadastro_livro():
    print('{:=^40}'.format(' CADASTRO DE LIVROS '))
    while True: 
        # Condição para cadastro seguido!
        opcao = str(input('Deseja cadastrar um livro? [S/N] ')).upper()
        while opcao not in ('S','N'):
             opcao = str(input('ERRO! Deseja cadastrar? [S/N] ')).upper()    
        if opcao == 'N':
            break

        id_livro = validar_codigo(livros, 'LIVRO') # Passagem de parâmetros/Função!

        while True: # Título vazio, ou números!
            titulo = str(input('TÍTULO DA OBRA: ').capitalize().strip())
            if titulo and not titulo.isdigit(): 
                break
            print('TÍTULO INVÁLIDO! ', end='')

        while True: # Nome do autor vazio, ou números!
            autor = str(input('NOME DO AUTOR: ').capitalize().strip())
            if autor and not autor.isdigit():
                break
            print('AUTOR INVÁLIDO! ', end='')

        while True: # Categoria vazia, ou números!
            categoria = str(input('CATEGORIA DO LIVRO: ').capitalize().strip())
            if categoria and not categoria.isdigit():
                break
            print('CATEGORIA INVÁLIDA! ', end='')
        while True:
                try:
                    quantidade = int(input('QUANTIDADE DE EXEMPLARES: '))
                    if quantidade > 0:
                        break
                    else:
                        print('DEVE SER MAIOR QUE ZERO!', end='')
                except ValueError:
                    print('DIGITE APENAS NÚMEROS! ', end='')       
        dados_livros = {
            'codigo': id_livro,
            'titulo': titulo,
            'autor': autor,
            'categoria': categoria,
            'quantidade': quantidade
            }
        livros.append(dados_livros)
        for d in livros:
            print(d)

usuarios = []
def cadastro_usuario():
    print('{:=^40}'.format(' CADASTRO DE USUÁRIOS '))
    while True: 
        # Condição para cadastro seguido!
        opcao = str(input('Deseja cadastrar um usuário? [S/N] ')).upper()
        while opcao not in ('S','N'):
                opcao = str(input('ERRO! Deseja cadastrar? [S/N] ')).upper()    
        if opcao == 'N':
            break
        id_usuario = validar_codigo(usuarios, 'USÚARIO') # Passagem de parâmetros/Função!
        dados_usuarios = {
                  'codigo': id_usuario,
            #      'nome': nome_usuario,
            #      'tipo_usuario': tipo_usuario,
            #      'curso_setor': curso_setor
            }
        usuarios.append(dados_usuarios)
        for d in usuarios:
            print(d)

