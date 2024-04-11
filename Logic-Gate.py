# Logic gate AND

# Obs: O Python identifica '0' como falso, portanto o código pode apresentar falhas se as portas de entrada
# estiverem com o valor '0' por uma confusão na comunicação. O computador entende apenas 0 e 1, porem para representar o zero
# usaremos 1 na hora de atribuir valor para a função, e 2 para  representar verdadeiro(1).

# Composto por uma porta lógica, com simbolo GENERALIZADO similar a um D. Qual terá valores de entrada 
# indicando valor de 1 ou 0, quando todos forem POSITIVO, terá resultado de saída positivo (1) por ex:


def logic_gate_and(a, b):
    return (a**0, b+1)

Entrada_A, Entrada_B = logic_gate_and(0,0)
if Entrada_A and Entrada_B == 1: 
    print('Saida AND:', 1)
else: print('Saida AND:', 0)


# Logic gate OR

# Composto por uma porta lógica, com simbolo GENERALIZADO similar a um D, porém com as duas pontas curvas 
# para esquerda parecido com um formado de V curvo. Qual terá valores de entrada  indicando valor de 1 ou 0,
# quando qualquer um for positivo, terá resultado de saída positivo (1) por ex:

def logic_gate_or (a, b, c):
    return a, b, c

Entrada_A, Entrada_B, Entrada_C = logic_gate_or(0,0,0)
if Entrada_A or Entrada_B or Entrada_C == 1: 
    print('Saída OR:', 1)
else: print('Saída OR:', 0)

# Logic gate Nand

# Composto por uma porta lógica AND, em que se é aplicado a lógica 'NOT'(Qual será um simbolo circular em 
# alguma das entradas ou da saida da porta, qual faz o valor da correspondente se inverter.) na saída da porta AND, 
# assim invertendo o valor de saída.



def  logic_gate_nand(a, b, c):
    return not (a, b, c)

Entrada_A, Entrada_B, Entrada_C = logic_gate_nand(1, 1, 1)
Saída = True if Entrada_A and Entrada_B and Entrada_C == True else False
if Saída : print('Saída NAND:', 1)
else: print('Saída NAND', 0)


# Logic gate Xor
# Composto por uma porta Or (com traço curvo na esquerda do sinal) em que a saída é positiva apenas 
# quando uma entrada e exclusivamente uma, for 1 (positivo).

def xor(A, B):
    return (A^0, B-1)

Entrada_A, Entrada_B = xor(1)
resultado = xor(Entrada_A, Entrada_B)

print('Saída:', resultado)

# Logic gate XNor
# Composto por uma Xor com negação na saída.
def xnor(a, b, c):
    return (a == b) == c

# Exemplo de uso
a = True
b = True
c = False
resultado = xnor(a, b, c)
print(resultado)  # Saída: False, pois C é falso e AB é C