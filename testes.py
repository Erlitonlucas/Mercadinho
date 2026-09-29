import subprocess

catalogo = {
    "feijao": {"nome": "FEIJAO", "preco": 6.50, "estoque": 10},
    "patinho": {"nome": "PATINHO", "preco": 10, "estoque": 10},
    "batata": {"nome": "BATATA", "preco": 2, "estoque": 0}
}

lista = list(catalogo.keys())

def escolherOpcao():

    #try/except usage documented here:
    try:
        opcao = int(input())
    except ValueError:
        print("Digite apenas os números das opções!")
        input("Pressione Enter para continuar...")
        subprocess.run("cls", shell="true")
        return None


    if 1 <= opcao <= 3:
        if catalogo[lista[opcao - 1]]['estoque'] > 0:
            produto_escolhido = catalogo[lista[opcao]]
            return produto_escolhido
        else:
            print("Estamos em falta!")
            input("Pressione Enter para continuar...")
            subprocess.run("cls", shell="true")
            return None
    else:
        print("Opção inexistente!")
        input("Pressione Enter para continuar...")
        subprocess.run("cls", shell="true")
        return None

resultado = escolherOpcao()
print(resultado)

#for indice, chave in enumerate(catalogo, start=1):
#    produto = catalogo[chave]
#    print(f"{indice} -- {produto["nome"]} R${produto["preco"]:.2f}, estoque {produto['estoque']}")



#if opcao == 1:
#  if catalogo['feijao']['estoque'] > 0:
#        produto_escolhido = catalogo['feijao']
#        return produto_escolhido