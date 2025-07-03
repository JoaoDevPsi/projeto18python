class Produto:
    def __init__(self, id, nome, descricao, quantidade_disponivel, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.quantidade_disponivel = quantidade_disponivel
        self.preco = preco

    def to_dict(self):
        return {
            "ID": self.id,
            "Nome": self.nome,
            "Descricao": self.descricao,
            "QuantidadeDisponivel": self.quantidade_disponivel,
            "Preco": self.preco
        }

    @staticmethod
    def from_dict(data):
        return Produto(
            data.get("ID"),
            data.get("Nome"),
            data.get("Descricao"),
            data.get("QuantidadeDisponivel"),
            data.get("Preco")
        )

class Venda:
    def __init__(self, id_venda, produto_id, quantidade_vendida, data_venda):
        self.id_venda = id_venda
        self.produto_id = produto_id
        self.quantidade_vendida = quantidade_vendida
        self.data_venda = data_venda

    def to_dict(self):
        return {
            "IDVenda": self.id_venda,
            "ProdutoID": self.produto_id,
            "QuantidadeVendida": self.quantidade_vendida,
            "DataVenda": self.data_venda
        }

    @staticmethod
    def from_dict(data):
        return Venda(
            data.get("IDVenda"),
            data.get("ProdutoID"),
            data.get("QuantidadeVendida"),
            data.get("DataVenda")
        )
