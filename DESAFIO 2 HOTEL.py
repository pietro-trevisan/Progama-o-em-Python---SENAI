# Desafio 2 ( ajudas externas )

nome_cliente = input("Digite o nome do cliente: ")
idade_cliente = int(input("Digite a idade do cliente: "))


preco_simples = 100.00
preco_duplo = 150.00
preco_luxo = 250.00


print("\nEscolha o tipo de quarto:")
print("1. Simples - R$ 100,00 por dia")
print("2. Duplo - R$ 150,00 por dia")
print("3. Luxo - R$ 250,00 por dia")

quarto_cliente = int(input("Digite o número do quarto desejado: "))


if quarto_cliente == 1:
    preco_cliente = preco_simples
elif quarto_cliente == 2:
    preco_cliente = preco_duplo
elif quarto_cliente == 3:
    preco_cliente = preco_luxo
else:
    preco_cliente = 0
    print("Opção inválida!")


dias_cliente = int(input(f"\nQuantos dias {nome_cliente} ficará no hotel? "))


valor_total = preco_cliente * dias_cliente


if idade_cliente < 18:
    valor_total *= 0.9  # 10% de desconto


print(f"\nResumo da estadia:")
print(f"Cliente: {nome_cliente}")
print(f"Idade: {idade_cliente} anos")
print(f"Valor a pagar pela estadia: R$ {valor_total:.2f}")


