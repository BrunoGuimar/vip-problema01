class Moeda:
    def __init__(self, valor: str, tipo_moeda: str, caractere: str):
        self.valor = valor
        self.tipo_moeda = tipo_moeda
        self.caractere = caractere

    # Retorna a string formatada {valor} no tipo float
    def get_valor(self):
        valor_formatado = self.valor.replace(",", "").replace(".", "").replace("R$", "").replace("$", "").strip()
        return float(int(valor_formatado)/100)

    # Recebe o tipo e caractere da moeda, substituindo pelos valores passado pelo parâmetro da função
    def alterar_moeda(self, tipo_moeda, caractere):
        moeda_aux = self.valor.replace("R$", "").replace("$", "").strip()
        moeda_final = f"{tipo_moeda} {moeda_aux.replace('.', f'{caractere}').replace(',', f'{caractere}')}"
        return moeda_final



