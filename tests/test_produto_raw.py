from app.core.criacao_bd import ProdutoRaw

def test_produto_raw_criacao():
    produto = ProdutoRaw(
    fonte="kabum",
    categoria="ram",
    nome="Memória DDR4 Teste",
    preco=199.90,
    url="http://teste.com",
    especificacoes={"socket": "AM4"}
    )

    registro = produto.registro_json()

    assert registro["fonte"] == "kabum"
    assert registro["categoria"] == "ram"
    assert registro["preco"] == 199.90
    assert "data_registro" in registro