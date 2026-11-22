from cadastros import cadastro_livro, cadastro_usuario

while True:
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
    opcao = int(input('Informe a opção desejada: '))
    
    match opcao:
        case 1:
            cadastro_livro()
        case 2:
            cadastro_usuario()
        case 9:
            print('PROGRAMA FINALIZADO...')
            break
        case _:
            print('Opção inválida! TENTE NOVAMENTE')
    