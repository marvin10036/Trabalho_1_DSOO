from visao.tela import Tela


class TelaQualificador(Tela):
    def pedeTitulo(self) -> str:
        return super()._pedeStr("Insira o titulo: ")

    def pedeDescricao(self) -> str:
        return super()._pedeStr("Insira a descricao: ")

    def continuar(self, msg) -> str:
        print(msg)
        entrada = input("Deseja inserir mais qualificadores? [S/N] ").capitalize()
        if entrada == 'S':
            return True
        else:
            return False

    def imprimeTitulo(self, msg: str):
        super()._imprimeLinhaTitulo(msg)

    def linhaDeFechamento(self):
        super()._imprimeLinhaFechamento()

    def imprimeQualificador(self, titulo: str, descricao: str):
            print("- Titulo: {} \tDescricao: {}".format(titulo, descricao))

#teste para TelaQualificador
if __name__ == "__main__":
    tela = TelaQualificador()
    tela.pedeTitulo()