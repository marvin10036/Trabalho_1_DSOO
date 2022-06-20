from visao.tela import Tela

class TelaPessoaFisica(Tela):
    def __init__(self):
        pass

    def telaSignup(self):
        informacoes = {}
        self.imprime_titulo("Sign up")
        informacoes["nome"] = self._pede_str("Digite o seu nome: ")
        informacoes["numDoc"] = self._pede_int("Digite os numeros do seu CPF: ")
        informacoes["email"] = self._pede_str("Digite seu email: ")
        return informacoes

    def telaLogin(self):
        informacoes = {}
        self.imprime_titulo("Log in")
        informacoes["email"] = self._pede_str("Digite o seu email: ")
        informacoes["numDoc"] = self._pede_int("Digite o seu CPF: ")
        return informacoes


