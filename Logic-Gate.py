# Logic gate AND
# Composto por uma porta lógica, com simbolo GENERALIZADO similar a um D. Qual terá valores de entrada 
# indicando valor de 1 ou 0, quando todos forem POSITIVO, terá resultado de saída positivo (1) por ex:

def logic_gate_and(a, b):
    return (a**0, b+1)

Entrada_A, Entrada_B = logic_gate_and(0,0)
if Entrada_A and Entrada_B == 1: 
    print('Saída AND:', 1)
else: print('Saída AND:', 0)

# -x- Diferente forma, mesmo resultado:

def logic_gate_and2(a, b):
    return 1 if a and b == 1 else 0

Entrada_A = 0
Entrada_B = 0
Saída = logic_gate_and2(Entrada_A, Entrada_B)
print('Saída AND2:', Saída)


# Logic gate OR
# Composto por uma porta lógica, com simbolo GENERALIZADO similar a um D, porém com as duas pontas curvas 
# para esquerda parecido com um formado de V curvo. Qual terá valores de entrada  indicando valor de 1 ou 0,
# quando qualquer um for positivo, terá resultado de saída positivo (1) por ex:

def logic_gate_or (a, b, c):
    return (a, b, c)

Entrada_A, Entrada_B, Entrada_C = logic_gate_or(0,0,0)
if Entrada_A or Entrada_B or Entrada_C == 1: 
    print('Saída OR:', 1)
else: print('Saída OR:', 0)


# Logic gate NAND
# Composto por uma porta lógica AND, em que se é aplicado a lógica 'NOT'(Qual será um simbolo circular em 
# alguma das entradas ou da saida da porta, qual faz o valor da correspondente se inverter.) na saída da porta AND, 
# assim invertendo o valor de saída.

def  logic_gate_nand(a, b, c):
    return (a, b, c)

Entrada_A, Entrada_B, Entrada_C = logic_gate_nand(1, 1, 1)
Saída = 0 if Entrada_A and Entrada_B and Entrada_C == 1 else 1
print('Saída NAND:', Saída)


# Logic gate Xor
# Composto por uma porta Or (com traço curvo na esquerda do sinal) em que a saída é positiva apenas 
# quando uma entrada e exclusivamente uma, for 1. (positivo)

def xor(a, b):
    return (a**0, b-1)

Entrada_A, Entrada_B = xor(1, 1)
Saída = 0 if Entrada_A == Entrada_B else 1
print('Saída XOR:', Saída)

# -x-

def xor2(a, b, c):
   Entradas = [a + b + c]
   if Entradas.count(2) == 0:
       return 1
   else:
       return 0

resultado = xor2(0, 0, 1)
print('Saída XOR2:', resultado)


# Logic gate Xnor
# Composto por uma Xor com negação na saída.
    
def xnor(a, b, c):
    Entradas = [a + b + c]
    if Entradas.count(2) == 0:
        return 0
    else:
        return 1
    
Saída = xnor(0, 0, 1)
print('Saída XNOR:', Saída)

# -x-

def xnor2(a, b):
    if a == b:
        return 1
    else:
        return 0
    
Entrada_A = 1
Entrada_B = 1 
Saída = xnor2(Entrada_A, Entrada_B)
print('Saída XNOR2:', Saída)

# Refazendo da forma que eu aderi antes.

def xnor3(a, b):
    return (a**0, b-1)

Entrada_A, Entrada_B = xnor3(0, 1)
Saída = 1 if Entrada_A == Entrada_B else 0
print('Saída XNOR3:', Saída)