


class TelaPreco():
    def pedeDados(self) -> float:
        while True:
            entradaPreco = input("Insira o preco: R$")

            if entradaPreco == '':
                return None
            else:
                entradaPreco.replace(",", ".")
                try:
                    preco = round(float(entradaPreco), 2)
                    return preco
                except Exception: #ValueError
                    print("Valor inválido. Tente novamente.")

