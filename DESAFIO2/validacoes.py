def validar_codigo(lista, tipo):
    while True:
        try:
            codigo = int(input(f'CÓDIGO {tipo}: '))
            if codigo <= 0:
                print('O CÓDIGO DEVE SER MAIOR QUE 0! ',end='') 
                continue     
            codigo_existe = False
            for c in lista:
                if codigo == c['codigo']:
                    codigo_existe = True 
                break
            if codigo_existe:
                print('CÓDIGO JÁ CADASTRADO! ', end='')
                continue
            else: 
                return codigo
        except ValueError: 
            print('DIGITE APENAS NÚMEROS! ',end='')
            continue