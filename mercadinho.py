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

#def exibirSaldoCatalogo usage documented here:
def exibirSaldoCatalogo():
    print(f"\tSeu saldo atual é de R${saldo:.2f}")
    print("\tEscolha uma das opções abaixo, digitando um número correspondente ao produto\n")

    for indice, key in enumerate(list(catalogo.keys()), start=1):
        produto = catalogo[key]
        print(f"{indice} -- {produto["nome"]} R${produto["preco"]:.2f}, estoque {produto["estoque"]}")


#def escolherOpcao usage documented here:
def escolherOpcao():

    #try/except usage documented here:
    try:
        opcao = int(input())
    except ValueError:
        print("Digite apenas os números das opções!")
        input("Pressione Enter para continuar...")
        subprocess.run("cls", shell="true")
        return None
    
    if opcao == 1 :
        if catalogo['feijao']['estoque'] > 0 :
            produto_escolhido = catalogo['feijao']
            return produto_escolhido
        else:
            print("Estamos em falta!")
            input("Pressione Enter para continuar...")
            subprocess.run("cls", shell="true")
            return None    
    elif opcao == 2 :
        if catalogo['patinho']['estoque'] > 0 :
            produto_escolhido = catalogo['patinho']
            return produto_escolhido
        else:
            print("Estamos em falta!")
            input("Pressione Enter para continuar...")
            subprocess.run("cls", shell="true")
            return None
    elif opcao == 3 :
        if catalogo['batata']['estoque'] > 0 :
            produto_escolhido = catalogo['batata']
            return produto_escolhido
        else:
            print("Estamos em falta!")
            input("Pressione Enter para continuar...")
            subprocess.run("cls", shell="true")
            return None
    
    else:
        print("Opção inválida!")
        input("Pressione Enter para continuar...")
        subprocess.run("cls", shell="true")
    return None


print("\nBEM VINDO AO MERCADINHO DE ERLINANDA!\n")

#
while True:

    exibirSaldoCatalogo()    

    produto_escolhido = escolherOpcao()

    if produto_escolhido == None :
        continue    

    print(f"Você escolheu {produto_escolhido['nome']}, agora escolha quanto você quer levar")

    try:
        quantidade = int(input())
    except ValueError:
        print("Digite apenas números!")
        input("Pressione Enter para continuar...")
        subprocess.run("cls", shell="true")
        continue

    if (produto_escolhido["estoque"] - quantidade) >= 0:
        print(f"""
        Valor total: R${quantidade * produto_escolhido['preco']}
        Confirmar compra?
       -Enter para confirmar-""")
        input()
        produto_escolhido["estoque"] -= quantidade
        saldo -= quantidade * produto_escolhido["preco"]
    else:
        print("Digite um número válido!")
        input("Pressione Enter para continuar...")
        subprocess.run("cls", shell="true")
        continue

        
    subprocess.run("cls", shell="true")