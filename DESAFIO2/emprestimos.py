from cadastros import usuarios, livros
from validacoes import validar_codigo_emprestimos, validar_positivo
from utilidades import limpar_tela
def emprestimo_livro():

    while True:
        limpar_tela()
        print('{:=^40}'.format(' EMPRÉSTIMO DE LIVROS '))
        opcao = str(input(f'Deseja emprestar um livro? [S/N] ')).upper()
        while opcao not in ('S','N'):
                opcao = str(input('ERRO! Deseja emprestar? [S/N] ')).upper()    
        if opcao == 'N':
            break

        usuario_emprestimo = validar_codigo_emprestimos(usuarios, 'usuário')
        livro_emprestimo = validar_codigo_emprestimos(livros, 'livro')
        quantidade_emprestimo = validar_positivo('QUANTIDADE DE DIAS DE EMPRÉSTIMO')