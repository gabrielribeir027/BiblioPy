from cadastros import cadastro_livro, cadastro_usuario, livros, usuarios
from utilidades import limpar_tela
from listagens import listagem_cadastros
from emprestimos import emprestimo_livro

while True:
    limpar_tela()
    print('{:=^40}'.format(' BIBLIOPY | MENU PRINCIPAL ')) 
    print('''    1 - Cadastrar livro
    2 - Cadastrar usuário
    3 - Listar livros
    4 - Listar usuários
    5 - Realizar empréstimo
    6 - Realizar devolução
    7 - Consultar situação de um livro
    8 - Consultar resumo da biblioteca
    9 - Encerrar aplicação''')

    try:
        opcao = int(input('Informe a opção desejada: '))
        if opcao < 1 or opcao > 9:
            print('OPÇÃO INVÁLIDA! ')
            input('Pressione ENTER para continuar...')
            continue
    except ValueError:
        print('APENAS NÚMEROS! ')
        input('Pressione ENTER para continuar...')
        continue

    match opcao:
        case 1:
            cadastro_livro()
        case 2:
            cadastro_usuario()
        case 3:
            listagem_cadastros(livros, 'LIVROS')
        case 4:
            listagem_cadastros(usuarios, 'USUÁRIOS')
        case 5:
            emprestimo_livro()
        case 9:
            print('PROGRAMA FINALIZADO...')
            break
    