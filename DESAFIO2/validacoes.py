def validar_codigo(lista, tipo):
    while True:
        try:
            opcao = int(input(f'CÓDIGO {tipo}: '))
            if opcao <= 0:
                print('O CÓDIGO DEVE SER MAIOR QUE 0. ',end='') 
                continue     
            codigo_existe = False
            for c in lista:
                if opcao == c['Codigo']:
                    codigo_existe = True 
                    break
            if codigo_existe:
                print('CÓDIGO JÁ CADASTRADO. ', end='')
                continue
            else: 
                return opcao
        except ValueError: 
            print('DIGITE APENAS NÚMEROS. ',end='')
            continue

def validar_entrada(tipo): # Válidas as entradas de LETRAS!
    while True:
        opcao = str(input(f'{tipo}: ').title().strip())
        if opcao and not opcao.isdigit(): 
            break
        print('TEXTO INVÁLIDO. ', end='')
    return opcao

def validar_tipos(tipo,tupla):
    while True:
        tipo_valido = False 
        opcao = str(input(f'{tipo}: ')).title().strip()
        for t in tupla:
            if opcao == t:
                tipo_valido = True
                break
        if tipo_valido:
            break  
        else:
            print(f'TEXTO INVÁLIDO. ', end='')
    return opcao

def validar_positivo(tipo):
    while True:
        try:
            quantidade = int(input(f'{tipo}: '))
            if quantidade > 0:
                return quantidade
            else:
                print('DEVE SER MAIOR QUE ZERO.', end='')
        except ValueError:
            print('DIGITE APENAS NÚMEROS. ', end='')

def validar_codigo_emprestimos(lista, tipo):
    while True:
        print('\033[7m\033[1;30;33m DIGITE 0 PARA CANCELAR. \033[m')
        codigo_usuario = input(f'Informe o código do {tipo}: ')

        if codigo_usuario == '0':
            print('EMPRÉSTIMO CANCELADO. ')
            return None

        try:
            codigo_usuario = int(codigo_usuario)

            codigo_encontrado = False
            for codigos in lista:
                if codigos['Codigo'] == codigo_usuario:
                    codigo_encontrado = True 
                    break
            if codigo_encontrado:
                break
            else:
                print('CÓDIGO NÃO ENCONTRADO!. ', end='')

        except ValueError:
            print('DIGITE UM CÓDIGO VÁLIDO. ', end='')
            continue