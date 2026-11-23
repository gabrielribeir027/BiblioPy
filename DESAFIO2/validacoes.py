def validar_codigo(lista, tipo):
    while True:
        try:
            opcao = int(input(f'CÓDIGO {tipo}: '))
            if opcao <= 0:
                print('O CÓDIGO DEVE SER MAIOR QUE 0! ',end='') 
                continue     
            codigo_existe = False
            for c in lista:
                if opcao == c['codigo']:
                    codigo_existe = True 
                    break
            if codigo_existe:
                print('CÓDIGO JÁ CADASTRADO! ', end='')
                continue
            else: 
                return opcao
        except ValueError: 
            print('DIGITE APENAS NÚMEROS! ',end='')
            continue

def validar_entrada(tipo): # Válidas as entradas de LETRAS!
    while True:
        opcao = str(input(f'{tipo}: ').title().strip())
        if opcao and not opcao.isdigit(): 
            break
        print('TEXTO INVÁLIDO! ', end='')
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
            print(f'TEXTO INVÁLIDO! ', end='')
    return opcao