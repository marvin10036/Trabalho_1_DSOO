


class TelaPreco():
    def pede_dados(self) -> float:
        while True:
            entrada = input("Insira o preco: R$")

            if entrada == '':
                return None
            else:
                entrada.replace(",", ".")
                try:
                    preco = round(float(entrada), 2)
                    return preco
                except Exception: #ValueError
                    print("Valor inválido. Tente novamente.")

