from utilidades import limpar_tela

def listagem_cadastros(lista, tipo):
    limpar_tela()
    print('{:=^40}'.format(f' LISTA DE {tipo} '))

    tamanho_listas = len(lista)

    if tamanho_listas == 0:
        print(f'{tipo} AINDA NÃO CADASTRADOS! ')
        
    else:
        for c in lista:
            for chave, valor in c.items():
                print(f'\033[1;33m{chave}\033[m: {valor}')
            print('='*40)
    input('Pressione ENTER para continuar...')
    