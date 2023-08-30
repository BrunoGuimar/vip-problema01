class Moeda:
    def __init__(self, valor: str, tipo_moeda: str, caractere: str):
        self._valor = valor
        self._tipo_moeda = tipo_moeda
        self._caractere = caractere

    # Retorna a string formatada {valor} no tipo float
    def get_valor(self):
        valor_formatado = self._formatar_moeda(self._valor).replace(",", "").replace(".", "").strip()
        return float(int(valor_formatado) / 100)

    # Recebe o tipo e caractere da moeda, substituindo pelos valores passados no parâmetro da função
    def alterar_moeda(self, tipo_moeda, caractere):
        moeda_alterada = self._formatar_moeda(tipo_moeda, caractere)
        return f"{moeda_alterada}"

    # Função privada responsável por formatar a moeda de acordo com os caracteres e o tipo informado
    # Implementada em casos mais flexíveis de valores
    def _formatar_moeda(self, tipo_moeda="", caractere=""):
        moeda_formatada = self._valor.replace("R$", "").replace("$", "")
        if tipo_moeda == "R$":  # "," VIRA "." - CASA DECIMAL == ","
            moeda_formatada = moeda_formatada.replace(",", ".")
            return f"{tipo_moeda}{moeda_formatada[:len(moeda_formatada) - 3]}{caractere}{moeda_formatada[len(moeda_formatada) - 2:]}"
        if tipo_moeda == "$":  # "." VIRA "," - CASA DECIMAL == "."
            moeda_formatada = moeda_formatada.replace(".", ",")
            return f"{tipo_moeda}{moeda_formatada[:len(moeda_formatada) - 3]}{caractere}{moeda_formatada[len(moeda_formatada) - 2:]}"
        return moeda_formatada
