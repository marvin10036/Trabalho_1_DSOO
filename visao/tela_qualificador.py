from visao.tela import Tela


class TelaQualificador(Tela):
    def pede_titulo(self) -> str:
        return super()._pede_str("Insira o titulo: ")

    def pede_descricao(self) -> str:
        return super()._pede_str("Insira a descricao: ")

    def continuar(self, msg) -> bool:
        print(msg)
        entrada = input("Deseja inserir mais qualificadores? [S/N] ").capitalize()
        if entrada == 'S':
            return True
        else:
            return False

    def imprime_qualificador(self, titulo: str, descricao: str):
            print("- Titulo: {} \tDescricao: {}".format(titulo, descricao))

#teste para TelaQualificador
if __name__ == "__main__":
    tela = TelaQualificador()
    tela.pedeTitulo()