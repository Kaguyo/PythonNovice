# Logic gate AND

# Obs: O Python identifica '0' como falso, portanto o código pode apresentar falhas se as portas de entrada
# estiverem com o valor '0' por uma confusão na comunicação. O computador entende apenas 0 e 1, porem para representar o zero
# usaremos 1 na hora de atribuir valor para a função, e 2 para  representar verdadeiro(1).

# Composto por uma porta lógica, com simbolo GENERALIZADO similar a um D. Qual terá valores de entrada 
# indicando valor de 1 ou 0, quando todos forem iguais, terá resultado de saída positivo (1) por ex:


def logic_gate_and(x):
    return x, x, x

Entrada_A, Entrada_B, Entrada_C = logic_gate_and(1)
if Entrada_A == Entrada_B == Entrada_C: 
    print('Saida: 1')
else: print('Saida: 0')


# Logic gate OR

# Composto por uma porta lógica, com simbolo GENERALIZADO similar a um D, porém com as duas pontas curvas 
# para esquerda parecido com um formado de V curvo. Qual terá valores de entrada  indicando valor de 1 ou 0,
# quando ALGUM for positivo, terá resultado de saída positivo (1) por ex:

def logic_gate_or (x):
    return x, x, x+1

Entrada_A, Entrada_B, Entrada_C = logic_gate_or(1)
if Entrada_A > 1 or Entrada_B > 1 or Entrada_C > 1: 
    print('Saida: 1')
else: print('Saida: 0')

# Logic gate NOT/Nand

# Composto por uma porta lógica AND, em que se é aplicado a lógica 'NOT', Qual será um simbolo circular em 
# alguma das entradas ou da saida da porta, fazendo com que assim o valor da mesma entrada ou saída se inverta.



def  logic_gate_nand(a, b, c):
    return not (b)

Entrada_A = True
Entrada_B = False
Entrada_C = True

resultado = logic_gate_nand(Entrada_A, Entrada_B, Entrada_C)
print('Saida:', Entrada_A, Entrada_B, Entrada_C, ":", resultado)


# Logic gate XNor
def xnor(A, B, C):
    return (A == B) == C

# Exemplo de uso
A = True
B = True
C = False
resultado = xnor(A, B, C)
print(resultado)  # Saída: False, pois C é falso e AB é C
