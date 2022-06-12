from tela import Tela

class TelaPessoaJuridica(Tela):
    def __init__(self):
        pass

    def telaSignin(self):
        informacoes = {}
        informacoes["nome"] = self._pede_str("Digite o seu nome: ")
        informacoes["numDoc"] = self._pede_str("Digite os numeros do seu CPF: ")
        informacoes["email"] = self._pede_str("Digite seu email: ")
        return informacoes

    def telaLogin(self):
        informacoes = {}
        informacoes["email"] = self._pede_str("Digite o seu email: ")
        informacoes["numDoc"] = self._pede_str("Digite o seu CPF: ")
        return informacoes


