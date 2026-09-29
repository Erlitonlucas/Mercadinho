#All documentation can be found in: 

import subprocess
import random    

saldo = round(random.uniform(200, 300), 2)
produto_escolhido: dict

catalogo = {
    "feijao": {"nome": "FEIJAO", "preco": 6.50, "estoque": 10},
    "patinho": {"nome": "PATINHO", "preco": 10, "estoque": 10},
    "batata": {"nome": "BATATA", "preco": 2, "estoque": 10}
}

lista = list(catalogo.keys())

#def exibirSaldoCatalogo usage documented here:
def exibirSaldoCatalogo():
    print(f"\tSeu saldo atual é de R${saldo:.2f}")
    print("\tEscolha uma das opções abaixo, digitando um número correspondente ao produto\n")

    for indice, key in enumerate(catalogo, start=1):
        produto = catalogo[key]
        print(f"{indice} -- {produto['nome']} R${produto['preco']:.2f}, estoque {produto['estoque']}")


#def escolherOpcao usage documented here:
def escolherOpcao():

    #try/except usage documented here:
    try:
        opcao = int(input())
    except ValueError:
        print("Digite apenas os números das opções!")
        input("Pressione Enter para continuar...")
        subprocess.run("cls", shell=True)
        return None
    
    if 1 <= opcao <= len(lista):
        chave = lista[opcao - 1]
        produto_escolhido = catalogo[chave]

        if produto_escolhido['estoque'] > 0:
            return produto_escolhido
        else:
            print(f"Desculpe, estamos sem estoque para {produto_escolhido['nome']}!")
            input("Pressione Enter para continuar...")
            subprocess.run("cls", shell=True)

        
    else:
        print("Coloque uma opção que esteja no catálogo!")
        input("Pressione Enter para continuar...")
        subprocess.run("cls", shell=True)
    return None


def escolherQuantidade(saldo):

    try:
        quantidade = int(input())
    except ValueError:
        print("Digite apenas números!")
        input("Pressione Enter para continuar...")
        subprocess.run("cls", shell=True)
        return None

    if 0 < quantidade <= produto_escolhido['estoque']:
        print(f"""
        Valor total: R${quantidade * produto_escolhido['preco']}
        Confirmar compra?
       -Enter para confirmar-""")
        input()
        produto_escolhido["estoque"] -= quantidade
        saldo -= quantidade * produto_escolhido["preco"]
        return saldo
    else:
        print("Digite um número válido!")
        input("Pressione Enter para continuar...")
        subprocess.run("cls", shell=True)
        return None


#
while True:
    print("\nBEM VINDO AO MERCADINHO DE ERLINANDA!\n")

    exibirSaldoCatalogo()

    produto_escolhido = escolherOpcao()
    if produto_escolhido == None:
        continue

    print(f"Você escolheu {produto_escolhido['nome']}, agora escolha quanto você quer levar")

    quantidade_escolhida = escolherQuantidade(saldo)
    if quantidade_escolhida == None:
        continue
    else:
        saldo = quantidade_escolhida
        
    subprocess.run("cls", shell=True)