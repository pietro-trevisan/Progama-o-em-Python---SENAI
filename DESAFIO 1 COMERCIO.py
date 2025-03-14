# Desafio 1 ( ajudas externas )
def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    print(f"\nCadastro concluído! Bem-vindo(a), {nome}.\n")
    return nome


produtos = [
    {"id": 1, "nome": "Camiseta", "preco": 29.90},
    {"id": 2, "nome": "Tênis", "preco": 199.90},
    {"id": 3, "nome": "Boné", "preco": 49.90},
    {"id": 4, "nome": "Moletom", "preco": 89.90}
]


def exibir_produtos():
    print("Produtos disponíveis:")
    for produto in produtos:
        print(f"{produto['id']}. {produto['nome']} - R${produto['preco']:.2f}")


def comprar_produto():
    carrinho = []
    while True:
        exibir_produtos()
        escolha = int(input("\nEscolha um produto para adicionar ao carrinho (digite o número ou 0 para finalizar): "))
        
        if escolha == 0:
            break
        

        produto_escolhido = next((p for p in produtos if p['id'] == escolha), None)
        if produto_escolhido:
            carrinho.append(produto_escolhido)
            print(f"{produto_escolhido['nome']} foi adicionado ao seu carrinho.")
        else:
            print("Produto inválido, tente novamente.")
    
    return carrinho


def calcular_total(carrinho):
    total = sum(item['preco'] for item in carrinho)
    return total


def pagar(total):
    if total > 0:
        print(f"\nO valor total de sua compra é R${total:.2f}.")
        forma_pagamento = input("Escolha a forma de pagamento (cartão ou pix): ").strip().lower()
        
        if forma_pagamento == "cartão":
            print("Pagamento aprovado no cartão!")
        elif forma_pagamento == "pix":
            print("Pagamento aprovado via Pix!")
        else:
            print("Forma de pagamento inválida.")
    else:
        print("Não há itens no carrinho para pagar.")


def main():
    # Cadastro do cliente
    nome = cadastrar_usuario()

    # Compra de produtos
    carrinho = comprar_produto()

    # Calcular o valor total
    total = calcular_total(carrinho)
    
    # Pagamento
    pagar(total)


if __name__ == "__main__":
    main()
