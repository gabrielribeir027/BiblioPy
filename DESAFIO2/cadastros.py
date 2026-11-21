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

        while True: # Estrutura sem letras / menor q 0!
            try:
                id_livro = int(input('CÓDIGO: '))
                if id_livro > 0:
                    codigo_existe = True # Abre
                    while codigo_existe: # Códigos Repetidos!
                        codigo_existe = False # Fecha
                        for livro in livros:
                            if livro['codigo'] == id_livro:
                                codigo_existe = True
                        if codigo_existe:
                            while True:
                                try:
                                    id_livro = int(input('CÓDIGO JÁ CADASTRADO! TENTE OUTRO: '))
                                    codigo_existe = True
                                    if id_livro > 0:
                                        break
                                except ValueError:
                                    print('ERRO! DIGITE SOMENTE NÚMEROS.')
                    break
                else:
                    print('O CÓDIGO DEVE SER MAIOR QUE ZERO!')
            except ValueError:
                print('ERRO! DIGITE SOMENTE NÚMEROS.')
    
        while True: # Título vazio, ou números!
            titulo = str(input('TÍTULO DA OBRA: ').capitalize().strip())
            if titulo and not titulo.isdigit(): 
                break
            print('ERRO, TÍTULO INVÁLIDO!')

        while True: # Nome do autor vazio, ou números!
            autor = str(input('NOME DO AUTOR: ').capitalize().strip())
            if autor and not autor.isdigit():
                break
            print('AUTOR INVÁLIDO! TENTE NOVAMENTE!')

        while True: # Categoria vazia, ou números!
            categoria = str(input('CATEGORIA DO LIVRO: ').capitalize().strip())
            if categoria and not categoria.isdigit():
                break
            print('CATEGORIA INVÁLIDA! TENTE NOVAMENTE!')
        while True:
                try:
                    quantidade = int(input('QUANTIDADE DE EXEMPLARES: '))
                    if quantidade > 0:
                        break
                    else:
                        print('A QUANTIDADE DEVE SER MAIOR QUE ZERO!')
                except ValueError:
                    print('ERRO! DIGITE NOVAMENTE.')       
        dados_livros = {
            'codigo': id_livro,
            'titulo': titulo,
            'autor': autor,
            'categoria': categoria,
            'quantidade': quantidade
            }
        livros.append(dados_livros)

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

        while True: # Estrutura sem letras / menor q 0!
            try:
                id_usuario = int(input('CÓDIGO: '))
                if id_usuario > 0:
                    codigo_existe = True # Abre
                    while codigo_existe: # Códigos Repetidos!
                        codigo_existe = False # Fecha
                        for livro in livros:
                            if livro['codigo'] == id_usuario:
                                codigo_existe = True
                        if codigo_existe:
                            while True:
                                try:
                                    id_usuario = int(input('CÓDIGO JÁ CADASTRADO! TENTE OUTRO: '))
                                    codigo_existe = True
                                    if id_usuario > 0:
                                        break
                                except ValueError:
                                    print('ERRO! DIGITE SOMENTE NÚMEROS.')
                    break
                else:
                            print('O CÓDIGO DEVE SER MAIOR QUE ZERO!')
            except ValueError:
                        print('ERRO! DIGITE SOMENTE NÚMEROS.')

                        
            dados_usuarios = {
                 'codigo': id_usuario,
                 'nome': nome_usuario,
                 'tipo_usuario': tipo_usuario,
                 'curso_setor': curso_setor
            }
        usuarios.append(dados_usuarios)
