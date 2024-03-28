# Logic gate AND

# Composto por uma porta lógica, com simbolo GENERALIZADO similar a um D. Qual terá valores de entrada 
# indicando valor de 1 ou 0, quando todos forem iguais, terá resultado de saída positivo (1) por ex:



def logic_gate_and_pass (x):
    return x, x, x

Entrada_A, Entrada_B, Entrada_C = logic_gate_and_pass(0)
if Entrada_A == Entrada_B and Entrada_C: 
    print('Saida: 1')
else: print('Saida: 0')