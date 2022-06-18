from visao.tela import Tela

class TelaPessoaJuridica(Tela):
    def __init__(self):
        pass

    def telaSignin(self):
        informacoes = {}
        self.imprime_titulo("Sign in")
        informacoes["nome"] = self._pede_str("Digite o seu nome: ")
        informacoes["numDoc"] = self._pede_str("Digite os numeros do seu CNPJ: ")
        informacoes["email"] = self._pede_str("Digite seu email: ")
        informacoes["estabelecimento"] = self._pede_str("Digite seu estabelecimento: ")
        return informacoes

    def telaLogin(self):
        self.imprime_titulo("Log in")
        informacoes = {}
        informacoes["email"] = self._pede_str("Digite o seu email: ")
        informacoes["numDoc"] = self._pede_str("Digite o seu CNPJ: ")
        return informacoes

