from visao.tela import Tela


class TelaQualificador(Tela):
    def pede_titulo(self, qualificadores) -> str:
        while True:
            titulo = super()._pede_str("Insira o titulo do qualificador: ")
            for qualificador in qualificadores:
                if qualificador.titulo == titulo:
                    print("Titulo já inserido no conjunto - tente novamente!")
                    break
            else:
                return titulo

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
        if descricao != '':
            print("- Titulo: {} \tDescricao: {}".format(titulo, descricao))
        else:
            print("- Titulo: {}".format(titulo))

#teste para TelaQualificador
if __name__ == "__main__":
    tela = TelaQualificador()
    tela.pedeTitulo()