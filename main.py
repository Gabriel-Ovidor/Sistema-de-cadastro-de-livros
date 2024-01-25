import json

livros = []

def cadastrar_livro():
    print("\n=== Cadastrar Livro ===")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    ano = input("Digite o ano da publicação: ")
    editora = input("Digite o nome da editora: ")
    genero = input("Digite o gênero do livro: ")
    paginas = input("Digite a quantidade de páginas do livro: ")
    preço = input("Digite o valor do livro: ")
    isbn = input("Digite o ISBN do livro: ")
    
    livro = {"Título": titulo, "Autor": autor, "Ano": ano, "Editora": editora, "Gênero": genero, "Páginas": paginas, "Preço": preço, "ISBN": isbn}
    livros.append(livro)
    print('Cadastro efetuado!')

def listar_livros():
    print("\n=== Listar Livros ===")
    if not livros:
        print("\033[91mNenhum livro encontrado.\033[0m")
    else:
        for index, livro in enumerate(livros, start=1):
            print(f'\033[92m{index}. \033[0m{"="*30}')
            print(f'\033[1mTítulo:\033[0m {livro["Título"]}')
            print(f'\033[1mAutor:\033[0m {livro["Autor"]}')
            print(f'\033[1mAno:\033[0m {livro["Ano"]}')
            print(f'\033[1mEditora:\033[0m {livro["Editora"]}')
            print(f'\033[1mGênero:\033[0m {livro["Gênero"]}')
            print(f'\033[1mPáginas:\033[0m {livro["Páginas"]}')
            print(f'\033[1mPreço:\033[0m {livro["Preço"]}')
            print(f'\033[1mISBN:\033[0m {livro["ISBN"]}')
            print()

def editar_livro():
    print("\n=== Editar Livro ===")
    listar_livros()
    indice = int(input('Digite o número do livro que deseja editar: ')) - 1
    
    if 0 <= indice < len(livros):
        novo_titulo = input(f'Novo título ({livros[indice]["Título"]}): ') or livros[indice]["Título"]
        novo_autor = input(f'Novo autor ({livros[indice]["Autor"]}): ') or livros[indice]["Autor"]
        novo_ano = input(f'Novo ano ({livros[indice]["Ano"]}): ') or livros[indice]["Ano"]
        nova_editora = input(f'Nova editora ({livros[indice]["Editora"]}): ') or livros[indice]["Editora"]
        novo_genero = input(f'Novo gênero ({livros[indice]["Gênero"]}): ') or livros[indice]["Gênero"]
        nova_pagina = input(f'Nova página ({livros[indice]["Páginas"]}): ') or livros[indice]["Páginas"]
        novo_preço = input(f'Novo preço ({livros[indice]["Preço"]}): ') or livros[indice]["Preço"]
        novo_isbn = input(f'Novo ISBN ({livros[indice]["ISBN"]}): ') or livros[indice]["ISBN"]
        
        livros[indice] = {
            "Título": novo_titulo,
            "Autor": novo_autor,
            "Ano": novo_ano,
            "Editora": nova_editora,
            "Gênero": novo_genero,
            "Páginas": nova_pagina,
            "Preço": novo_preço,
            "ISBN": novo_isbn
        }
        print('Livro editado com sucesso!')
    else:
        print('O livro não foi encontrado.')

def excluir_livro():
    print("\n=== Excluir Livro ===")
    listar_livros()
    indice = int(input('Digite o número do livro que deseja excluir: ')) - 1
    
    if 0 <= indice < len(livros):
        livro_excluido = livros.pop(indice)
        print(f'O livro "{livro_excluido["Título"]}" foi excluído de sua base!')
    else:
        print('Livro não encontrado.')

def salvar_em_arquivo():
    print("\n=== Salvar em Arquivo ===")
    with open('livros.json', 'w') as arquivo:
        json.dump(livros, arquivo)
    print('Dados salvos em "livros.json')

def carregar_de_arquivo():
    print("\n=== Carregar de Arquivo ===")
    try:
        with open('livros.json', 'r') as arquivo:
            livros.extend(json.load(arquivo))
        print('Dados carregados de "livros.json".')
    except FileNotFoundError:
        print('Arquivo "livros.json" não encontrado.')

while True:
    print("\nEscolha uma opção:")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Editar livro")
    print("4. Excluir livro")
    print("5. Salvar em arquivo")
    print("6. Carregar arquivo")
    print("7. Sair")

    escolha = input("Opção: ")

    if escolha == "1":
        cadastrar_livro()
    elif escolha == "2":
        listar_livros()
    elif escolha == "3":
        editar_livro()
    elif escolha == "4":
        excluir_livro()
    elif escolha == "5":
        salvar_em_arquivo()
    elif escolha == "6":
        carregar_de_arquivo()
    elif escolha == "7":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")

        