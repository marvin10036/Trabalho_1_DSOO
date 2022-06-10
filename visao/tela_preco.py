


class TelaPreco():
    def pedeDados(self):
        while True:
            entradaPreco = input("Insira o preco: R$").replace(",", ".")

            try:
                #preco = float()
                preco = round(float(entradaPreco), 2)
                return preco
            except Exception: #ValueError
                print("Valor inválido. Tente novamente.")

