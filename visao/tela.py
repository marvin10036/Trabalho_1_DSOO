

class Tela():
    #imprime linha no estilo -----"texto"-----
    def _imprimeLinhaTitulo(self, texto: str):
        x = len(texto)
        lados = (40 - x) // 2

        if x <= 40:
            print()
            print('-' * lados, end='')
            print(texto, end='')
            print('-' * lados, end='')

            if (x % 2) != 0:
                print('-')
            else:
                print()
        else:
            print(texto)

    def _imprimeLinhaFechamento(self):
        print('-' * 40, end='')
        print()

    def _pedeStr(self, msgInput: str):
        entrada = input(msgInput)
        if entrada == '':
            return None
        else:
            return entrada