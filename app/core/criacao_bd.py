from datetime import datetime, timezone

class ProdutoRaw:
    def __init__(self, fonte: str, categoria: str, nome: str, preco: float, url: str, especificacoes: dict):
        self.fonte = fonte
        self.categoria = categoria
        self.nome = nome
        self.preco = preco
        self.url = url
        self.especificacoes = especificacoes
        self.data_registro = datetime.now(timezone.utc).isoformat() 

    def registro_json(self) -> dict:
        #saber qual é a fita sobre essa setinha, se tem função real ou simplesmente estetica
        return {
            "fonte": self.fonte,
            "categoria": self.categoria,
            "nome": self.nome,
            "preco": self.preco,
            "url": self.url,
            "data_registro": self.data_registro,
            "especificacoes": self.especificacoes
        }
    


