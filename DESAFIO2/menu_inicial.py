while True:
    print('''BIBLIOPY | MENU PRINCIPAL
    1 - Cadastrar livro
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
        case 9:
            print('PROGRAMA FINALIZADO...')
            break
    print('Opção inválida! TENTE NOVAMENTE')
    