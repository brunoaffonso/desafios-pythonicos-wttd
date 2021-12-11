"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys


# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).
import fileinput

def read_file(filename):
    words_lists = []
    with open(filename) as f:
        for line in f.read().split():
            words_lists.append(line.lower())
    return words_lists

def alternative_read_file(filename):
    words_list = []
    for line in fileinput.input(filename):
        for i in line.split(" "):
            words_list.append(i.replace("\n", "").lower())
    return words_list

def union(full_list):
    results = set()
    for i in full_list:
        results.add(i)
    results = list(results)
    return results

def make_list_of_tuple(full_list, unique_values):
    results = []
    for i in unique_values:
        results.append((i, full_list.count(i)))
    return results

def print_results(list_of_tuple):
    for i in list_of_tuple:
        print(f'{i[0]} {i[1]}')

def print_words(filename):
    words = read_file(filename)
    values = union(words)
    results = make_list_of_tuple(words, values)
    results.sort()
    print_results(results)
    return None

def print_top(filename):
    words = read_file(filename)
    values = union(words)
    results = make_list_of_tuple(words, values)
    results.sort(key=lambda x : x[-1], reverse=True)
    print_results(results[:20])
    return None


# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
