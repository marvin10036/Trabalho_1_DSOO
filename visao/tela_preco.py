from visao.tela import Tela


class TelaPreco(Tela):
    def pede_valor(self) -> float:
        while True:
            entrada = input("Insira o preco: R$")

            if entrada == '':
                return None
            else:
                entrada = entrada.replace(",", ".")
                try:
                    preco = round(float(entrada), 2)
                    return preco
                except Exception: #ValueError
                    print("Valor inválido. Tente novamente.")
