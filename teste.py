import subprocess
import random

saldo = round(random.uniform(40, 80), 2)

print(f"""
BEM VINDO AO MERCADINHO DE ERLINANDA!""")

catalogo = {
    "feijao": {"nome": "FEIJAO", "preco": 6.50, "estoque": 10},
    "patinho": {"nome": "PATINHO", "preco": 10, "estoque": 10},
    "batata": {"nome": "BATATA", "preco": 2, "estoque": 10},
}

def exibirCatalogo():
    print(f"""
    Seu saldo atual é de R${saldo:.2f}
    Escolha uma das opções abaixo, digitando o número correspondente ao produto
""")
    
    print(f"1 -- {catalogo['feijao']['nome']} R${catalogo['feijao']['preco']:.2f}, estoque: {catalogo['feijao']['estoque']}")
    print(f"2 -- {catalogo['patinho']['nome']} R${catalogo['patinho']['preco']:.2f}, estoque: {catalogo['patinho']['estoque']}")
    print(f"3 -- {catalogo['batata']['nome']} R${catalogo['batata']['preco']:.2f}, estoque: {catalogo['batata']['estoque']}")

while True:

    exibirCatalogo()

    opcao = int(input())

    if opcao == 1:
        produto_escolhido = catalogo['feijao']
    elif opcao == 2:
        produto_escolhido = catalogo['patinho']
    elif opcao == 3:
        produto_escolhido = catalogo['batata']
    else:
        print("Opção inválida!")

    print(f"Você escolheu {produto_escolhido['nome']}, agora escolha quanto você quer levar")
    quantidade = int(input())

    if (produto_escolhido["estoque"] - quantidade) >= 0:
        print(f"""
        Valor total: R${quantidade * produto_escolhido['preco']}
        Confirmar compra?
       -Enter para confirmar-""")
        input()
    else:
        print("Digite um número válido!")

    produto_escolhido["estoque"] -= quantidade
    saldo -= quantidade * produto_escolhido["preco"]
        
    subprocess.run("cls", shell="true")