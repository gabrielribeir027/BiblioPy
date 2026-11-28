from cadastros import usuarios, livros
from validacoes import validar_codigo_emprestimos, validar_positivo
from utilidades import limpar_tela

emprestimos = []

def emprestimo_livro():

    while True:
        limpar_tela()
        print('{:=^40}'.format(' EMPRÉSTIMO DE LIVROS '))
        opcao = str(input(f'Deseja emprestar um livro? [S/N] ')).upper()
        while opcao not in ('S','N'):
                opcao = str(input('ERRO! Deseja emprestar? [S/N] ')).upper()    
        if opcao == 'N':
            break
        print('\033[7m\033[1;30;33m DIGITE 0 PARA CANCELAR. \033[m')
        
        usuario_emprestimo = validar_codigo_emprestimos(usuarios, 'usuário')
        if usuario_emprestimo is None:
            print('→ EMPRÉSTIMO CANCELADO COM SUCESSO. ') 
            input('Pressione ENTER para continuar...')
            continue

        livro_emprestimo = validar_codigo_emprestimos(livros, 'livro')
        if livro_emprestimo is None:
            print('→ EMPRÉSTIMO CANCELADO COM SUCESSO. ') 
            input('Pressione ENTER para continuar...')
            continue
        
        livro_encontrado = False
        for livro in livros:
            if livro['Codigo'] == livro_emprestimo:
                livro_encontrado = True
                break
        if livro_encontrado:
            if livro['Disponiveis'] > 0:
                livro['Disponiveis'] -= 1
            else:
                print('LIVRO INDISPONÍVEL! ')
                input('Pressione ENTER para continuar...')

        quantidade_emprestimo = validar_positivo('QUANTIDADE DE DIAS DE EMPRÉSTIMO')

        dados_emprestimo = {
             'Código do Usuário': usuario_emprestimo,
             'Código do Livro': livro_emprestimo,
             'Dias de empréstimo': quantidade_emprestimo
        }

        emprestimos.append(dados_emprestimo)
