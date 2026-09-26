catalogo = {
    "feijao": {"nome": "FEIJAO", "preco": 6.50, "estoque": 10},
    "patinho": {"nome": "PATINHO", "preco": 10, "estoque": 10},
    "batata": {"nome": "BATATA", "preco": 2, "estoque": 10}
}


for numero, chave in enumerate(list(catalogo.keys()), start=1):
    produto = catalogo[chave]
    print(f"{numero} -- {produto["nome"]} R${produto["preco"]:.2f}, estoque {produto['estoque']}")