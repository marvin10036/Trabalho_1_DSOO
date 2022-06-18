

class Tela():
    def imprime(self, texto: str):
        print(texto)

    #imprime linha no estilo -----"texto"-----
    def imprime_titulo(self, texto: str):
        tamanho = len(texto)
        lados = (40 - tamanho) // 2

        if tamanho <= 40:
            print('-' * lados, end='')
            print(texto, end='')
            print('-' * lados, end='')

            if (tamanho % 2) != 0:
                print('-')
            else:
                print()
        else:
            print(texto)

    def imprime_linha_de_fechamento(self):
        print('-' * 40, end='')
        print()

    def _pede_str(self, msg_input: str):
        entrada = input(msg_input).capitalize()
        if entrada == '':
            return None
        else:
            return entrada

    def _pede_int(self, msg_input: str):
        while True:
            entrada = input(msg_input).capitalize()
            try:
                entrada = int(entrada)
            except ValueError:
                print("Entrada inserida inválida: favor inserir valor inteiro.")
            else:
                return entrada

    def _seleciona_opcao_int(self, n_de_opcoes: int):
        while True:
            entrada = input("Selecione uma opcao: ")

            try:
                entrada = int(entrada)
                if entrada >= 0 and entrada <= n_de_opcoes: #dentro da faixa de opcoes
                    return entrada
                else:
                    raise ValueError
            except ValueError:
                print("Entrada inserida inválida: favor inserir valor inteiro dentro da faixa de opcoes fornecidas.")

    def _pergunta_sim_ou_nao(self, texto:str) -> bool:
        entrada = input("{} [S/N] ".format(texto)).upper()
        if entrada == "S":
            return True
        else:
            return False