import json
from colorama import Fore, Style, init

# Inicialize o colorama
init()

livros = []

def cadastrar_livro():
    print("\n" + "=" * 40)
    print(Fore.CYAN + f"{'SISTEMA DE CADASTRO DE LIVROS':^40}" + Style.RESET_ALL)
    print("=" * 40)
    print(Fore.YELLOW + "CADASTRO DE LIVRO" + Style.RESET_ALL)
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    ano = input("Digite o ano da publicação: ")
    editora = input("Digite o nome da editora: ")
    genero = input("Digite o gênero do livro: ")
    paginas = input("Digite a quantidade de páginas do livro: ")
    preco = input("Digite o valor do livro: ")
    isbn = input("Digite o ISBN do livro: ")

    livro = {"Título": titulo, "Autor": autor, "Ano": ano, "Editora": editora, "Gênero": genero, "Páginas": paginas, "Preço": preco, "ISBN": isbn}
    livros.append(livro)
    print(Fore.GREEN + 'Cadastro efetuado!' + Style.RESET_ALL)

def listar_livros():
    if not livros:
        print(Fore.YELLOW + "Nenhum livro encontrado." + Style.RESET_ALL)
    else:
        print("\n" + "=" * 60)
        print(Fore.CYAN + f"{'SISTEMA DE CADASTRO DE LIVROS':^60}" + Style.RESET_ALL)
        print("=" * 60)
        print(Fore.YELLOW + "LISTA DE LIVROS" + Style.RESET_ALL)
        print(f"{'Nº': <5}{'Título': <20}{'Autor': <20}{'Ano': <5}{'Editora': <15}{'Gênero': <15}{'Páginas': <8}{'Preço': <10}{'ISBN': <15}")
        print("-" * 60)

        for index, livro in enumerate(livros, start=1):
            print(f"{index: <5}{livro['Título'][:20]: <20}{livro['Autor'][:20]: <20}{livro['Ano'][:5]: <5}{livro['Editora'][:15]: <15}{livro['Gênero'][:15]: <15}{livro['Páginas'][:8]: <8}{livro['Preço'][:10]: <10}{livro['ISBN'][:15]: <15}")

        print("-" * 60)

def editar_livro():
    listar_livros()
    indice = int(input('Digite o número do livro que deseja editar: ')) - 1

    if 0 <= indice < len(livros):
        print("\n" + "=" * 40)
        print(Fore.CYAN + f"{'SISTEMA DE CADASTRO DE LIVROS':^40}" + Style.RESET_ALL)
        print("=" * 40)
        print(Fore.YELLOW + "EDITAR LIVRO" + Style.RESET_ALL)
        novo_titulo = input(f'{"Novo título": <30} (ou ENTER para manter o mesmo): ')
        novo_autor = input(f'{"Novo autor": <30} (ou ENTER para manter o mesmo): ')
        novo_ano = input(f'{"Novo ano": <30} (ou ENTER para manter o mesmo): ')
        nova_editora = input(f'{"Nova editora": <30} (ou ENTER para manter o mesmo): ')
        novo_genero = input(f'{"Novo gênero": <30} (ou ENTER para manter o mesmo): ')
        nova_pagina = input(f'{"Nova página": <30} (ou ENTER para manter o mesmo): ')
        novo_preco = input(f'{"Novo preço": <30} (ou ENTER para manter o mesmo): ')
        novo_isbn = input(f'{"Novo ISBN": <30} (ou ENTER para manter mesmo): ')

        print(Fore.GREEN + 'Livro editado com sucesso!' + Style.RESET_ALL)
    else:
        print(Fore.RED + 'O livro não foi encontrado.' + Style.RESET_ALL)

def excluir_livro():
    listar_livros()
    indice = int(input('Digite o número do livro que deseja excluir: ')) - 1

    if 0 <= indice < len(livros):
        livro_excluido = livros.pop(indice)
        print(Fore.RED + f'O livro "{livro_excluido["Titulo"]}" foi excluído de sua base!' + Style.RESET_ALL)
    else:
        print(Fore.RED + 'Livro não encontrado.' + Style.RESET_ALL)

def salvar_em_arquivo():
    with open('livros.json', 'w') as arquivo:
        json.dump(livros, arquivo)
    print(Fore.GREEN + 'Dados salvos em livros.json' + Style.RESET_ALL)

def carregar_de_arquivo():
    try:
        with open('livros.json', 'r') as arquivo:
            livros.extend(json.load(arquivo))
        print(Fore.GREEN + 'Dados carregados de livros.json.' + Style.RESET_ALL)
    except FileNotFoundError:
        print(Fore.RED + 'Arquivo livros.json não encontrado.' + Style.RESET_ALL)

carregar_de_arquivo()

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
        print(Fore.CYAN + "Saindo do programa. Até mais!" + Style.RESET_ALL)
        break
    else:
        print(Fore.RED + "Opção inválida. Tente novamente." + Style.RESET_ALL)





        