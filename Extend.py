"""
O Método extend em Python

O método extend é usado em listas em Python para adicionar os elementos de uma outra lista 
(ou de qualquer iterável) à lista original. Como:

"""
#lista.extend(iteravel)

"""
lista: A lista à qual você deseja adicionar elementos.
iteravel: Um iterável (como outra lista) contendo os elementos que você deseja adicionar à 
lista original.

Funcionamento:

Modificação In-place:
O método extend modifica a lista original in-place, o que significa que a lista original é alterada
sem a necessidade de atribuir o resultado a uma nova variável.

Adição de Elementos:
O método extend adiciona os elementos do iterável fornecido ao final da lista original,
mantendo a ordem dos elementos.

Iterável:
O argumento passado para extend deve ser um iterável, como uma lista, tupla, conjunto,
ou qualquer objeto que possa ser iterado.

Exemplo:

Lista original
"""
lista1 = [1, 2, 3]

# Lista a ser adicionada
lista2 = [4, 5, 6]

# Usando extend para adicionar elementos de lista2 em lista1
lista1.extend(lista2)

print("lista1 após extend:", lista1)


# Saída: lista1 após extend: [1, 2, 3, 4, 5, 6]

# Explicação do Exemplo:

"""
A lista lista1 originalmente contém os elementos [1, 2, 3].
A lista lista2 contém os elementos [4, 5, 6].
Usando o método extend, os elementos de lista2 são adicionados ao final de lista1.
Após a execução de lista1.extend(lista2), lista1 agora contém [1, 2, 3, 4, 5, 6].


Importante:

O método extend não cria uma nova lista; ele apenas adiciona elementos à lista existente.
O método extend é mais eficiente do que a concatenação de listas usando o operador +, 
especialmente para listas grandes, pois não cria uma nova lista intermediária.
"""
