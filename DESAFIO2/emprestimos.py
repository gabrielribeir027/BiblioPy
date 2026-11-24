from cadastros import usuarios
def emprestimo_livro():
    for u in usuarios:
        print(u['Codigo'])
        input('----')