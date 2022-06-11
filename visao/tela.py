

class Tela():
    def imprime(self, texto: str):
        print(texto)

    #imprime linha no estilo -----"texto"-----
    def imprime_titulo(self, texto: str):
        tamanho = len(texto)
        lados = (40 - tamanho) // 2

        if tamanho <= 40:
            print()
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
        entrada = input(msg_input)
        if entrada == '':
            return None
        else:
            return entrada