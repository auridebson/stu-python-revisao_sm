estoque = []

def adicionar_fruta():
            nome_fruta = str(input("Digite o nome da fruta: "))

            while True:
                try:
                    quantidade_fruta = int(input("Digite a quantidade de frutas no estoque: "))
                    if quantidade_fruta >= 1:
                        break
                    else:
                        print("Digite um valor positivo")
                except ValueError:
                     print("ERROR, digite um valor válido")
                
            while True:
                try:
                    preco_fruta = float(input("Digite o preço da fruta: "))

                    if preco_fruta > 0:
                        break
                    else:
                        print("Insira um valor válido")
                except ValueError:
                     print("ERROR, digite um valor válido")

            dicionario_fruta = {
                "Nome": nome_fruta,
                "Quantidade": quantidade_fruta,
                "Preço": preco_fruta
            }

            estoque.append(dicionario_fruta)
            return "Fruta adicionada com sucesso"


def deletar_fruta():
            for posicao,fruta in enumerate(estoque):
                print(f"""
                {posicao} -> {fruta["Nome"]}
""")
            try:
                posicao_excluida = int(input("Digite o número da fruta que você quer deletar: "))
                if posicao_excluida >= 0 and posicao_excluida < len(estoque):
                    estoque.pop(posicao_excluida)
                    return "Fruta excluída com sucesso"
                else:
                    return "Meu fiiiii, digite uma posição dentro da lista que eu mostrei"
            except ValueError:
                 print("ERROR, digite um valor válido")
                 


def visualizar_frutas():
    for i ,fruta in enumerate(estoque):
        print(f"{i+1} - {fruta}")



while True:
    try:
        menu = int(input("""
        Escolha uma opção
        1 - Adicionar Fruta
        2 - Excluir Fruta
        3 - Ver todas as Frutas
        0 - Sair do menu
    """))
        match menu:
            case 1:
                print(adicionar_fruta())
            case 2:
                print(deletar_fruta())
            case 3:
                visualizar_frutas()
            case 0:
                print("Fim do programa")
                break
            case _:
                print("Opção inválida")
    except ValueError:
         print(f"ERROR: Digite um valor válido")