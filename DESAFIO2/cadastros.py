from validacoes import validar_codigo, validar_entrada, validar_tipos
from utilidades import limpar_tela

livros = []
categorias_livros = (
    "Ficção",
    "Não ficção",
    "Romance",
    "Fantasia",
    "Ficção científica",
    "Mistério",
    "Suspense",
    "Terror",
    "Biografia",
    "História",
    "Autoajuda",
    "Negócios",
    "Tecnologia",
    "Ciência",
    "Infantil",
    "Poesia",
    "Quadrinhos",
    "Didático",
)
def cadastro_livro():
    
    while True: # Cadastros seguidos!
        limpar_tela()
        print('{:=^40}'.format(' CADASTRO DE LIVROS '))
        opcao = str(input(f'Deseja cadastrar um livro? [S/N] ')).upper()
        while opcao not in ('S','N'):
                opcao = str(input('ERRO! Deseja cadastrar? [S/N] ')).upper()    
        if opcao == 'N':
            break

        # Passagem de parâmetros/Função!
        id_livro = validar_codigo(livros, 'LIVRO')
        titulo = validar_entrada('TITÚLO DA OBRA')
        autor = validar_entrada('AUTOR')
        categoria = validar_tipos('CATEGORIA', categorias_livros)
            
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
            'Codigo': id_livro,
            'Título': titulo,
            'Autor': autor,
            'Categoria': categoria,
            'Quantidade': quantidade,
            'Disponiveis': quantidade
            }
        
        livros.append(dados_livros)

        print('→ LIVRO CADASTRADO COM SUCESSO!') 
        input('Pressione ENTER para continuar...')


usuarios = []
tipos_usuario = ('Estudante','Funcionario','Professor')
def cadastro_usuario():
    
    while True: # Cadastros seguidos!
        limpar_tela()
        print('{:=^40}'.format(' CADASTRO DE USUÁRIOS '))
        opcao = str(input('Deseja cadastrar um usuário? [S/N] ')).upper()
        while opcao not in ('S','N'):
                opcao = str(input('ERRO! Deseja cadastrar? [S/N] ')).upper()    
        if opcao == 'N':
            break

        # Passagem de parâmetros/Função!
        id_usuario = validar_codigo(usuarios, 'USUÁRIO') 
        nome_usuario = validar_entrada('NOME COMPLETO DO USUÁRIO')

        print('\033[7m\033[1;30;33m ESTUDANTE | FUNCIONARIO | PROFESSOR \033[m')
        tipo_usuario = validar_tipos('TIPO DE USUÁRIO', tipos_usuario)
        curso_setor = validar_entrada('CURSO OU SETOR')
                      
        dados_usuarios = {
                  'Codigo': id_usuario,
                  'Nome': nome_usuario,
                  'Tipo de usuário': tipo_usuario,
                  'Curso ou setor': curso_setor
            }
        
        usuarios.append(dados_usuarios)

        print('→ USUÁRIO CADASTRADO COM SUCESSO!') 
        input('Pressione ENTER para continuar...')