# Constantes são geralmente definidas em letras maiúsculas para indicar que são valores fixos.
PI = 3.14159
TAXA_DE_DESCONTO = 0.1

# Exemplo de função que usa uma constante como argumento.
def calcular_area_do_circulo(raio):
    return PI * raio * raio

raio = 5
area = calcular_area_do_circulo(raio)
print(area)  # Saída: 78.53975

# Exemplo de função que utiliza uma constante internamente.
def calcular_preco_com_desconto(preco_original):
    return preco_original - (preco_original * TAXA_DE_DESCONTO)

preco = 100
preco_com_desconto = calcular_preco_com_desconto(preco)
print(preco_com_desconto)  # Saída: 90

# Exemplo de função que acessa uma constante global.
def calcular_circunferencia(raio):
    return 2 * PI * raio

circunferencia = calcular_circunferencia(raio)
print(circunferencia)  # Saída: 31.4159
