from main import Moeda
from faker import Faker

faker = Faker()

def test_get_valor():
    # Variáveis estanciadas
    valor_aleatorio = faker.random_number() # Geração de valores aleatórios, teste flexível.
    moeda = Moeda(f"R$ {valor_aleatorio}", "R$", ",")
    # Variáveis de teste
    esperado = float(valor_aleatorio)/100
    resultado = moeda.get_valor()

    assert resultado == esperado

def test_alterar_moeda():
    # Variáveis estanciadas
    moeda = Moeda(f"R$ 87.240,35", "R$", ",")
    # Variáveis de teste
    esperado = "$ 87,240.35"
    resultado = moeda.alterar_moeda("$", ".")

    assert resultado == esperado
