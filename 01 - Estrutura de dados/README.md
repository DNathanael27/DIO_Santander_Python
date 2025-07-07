# Estrutura de Dados em Python

Este repositório contém exemplos práticos dos principais conceitos de estruturas de dados em Python, organizados em pastas temáticas. Abaixo, um resumo de cada conceito abordado:

## 01 - Listas


Esta pasta contém exemplos de:
- Declaração e acesso a listas;
- Fatiamento e iteração;
- Compreensão de listas;
- Principais métodos (`append`, `remove`, `sort`, etc.);
- Exercícios práticos para fixação.

Exemplo de funcionalidade:
```python
# Criando e manipulando listas
frutas = ["maçã", "banana", "uva"]
frutas.append("laranja")  # Adiciona "laranja" ao final
print(frutas[1])  # banana
print(frutas[-1])  # laranja
```

## 02 - Tuplas


Esta pasta aborda:
- Como declarar tuplas (inclusive de um elemento);
- Conversão entre listas e tuplas;
- Acesso por índice e fatiamento;
- Iteração e exemplos práticos.

Exemplo de funcionalidade:
```python
# Declarando tuplas e acessando elementos
coordenadas = (10, 20)
print(coordenadas[0])  # 10
tupla_um_elemento = (5,)
```

## 03 - Conjuntos


Aqui você encontra exemplos de:
- Criação e manipulação de conjuntos;
- Operações matemáticas (união, interseção, diferença);
- Testes de subconjunto e superset;
- Métodos principais (`add`, `remove`, etc.);
- Exercícios práticos.

Exemplo de funcionalidade:
```python
# Operações com conjuntos
alunos = {"Ana", "João", "Maria"}
alunos.add("Carlos")
print(alunos)
aprovados = {"Ana", "Maria"}
print(alunos & aprovados)  # interseção
```


## 04 - Dicionários

Esta pasta explora:
- Como declarar e criar dicionários;
- Adição, remoção e atualização de itens;
- Acesso a valores e chaves;
- Métodos úteis como `fromkeys`, `get`, `keys`, `values`, `items`;
- Iteração sobre dicionários;
- Exemplos práticos e desafios para fixação do conteúdo.

Exemplo de funcionalidade:
```python
# Declarando e manipulando dicionários
pessoa = {"nome": "Guilherme", "idade": 28}
pessoa["telefone"] = "3333-1234"
print(pessoa["nome"])  # Guilherme
# Criando dicionário com fromkeys
resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
```

## 05 - Funções

Esta pasta apresenta exemplos de:
- Como declarar funções simples e com parâmetros;
- Retorno de valores e múltiplos valores;
- Argumentos nomeados, posicionais, *args e **kwargs;
- Parâmetros somente por posição e somente por nome;
- Funções como objetos de primeira classe (podem ser passadas como argumento);
- Escopo local e global de variáveis.

Exemplo de funcionalidades:
```python
# Função simples
def exibir_mensagem():
    print("Olá mundo!")

# Função com retorno de múltiplos valores
def retorna_antecessor_e_sucessor(numero):
    return numero - 1, numero + 1

# Função com *args e **kwargs
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    print(f"{data_extenso}\n\n{texto}\n\n{meta_dados}")

# Função como objeto de primeira classe
def somar(a, b):
    return a + b
def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")
exibir_resultado(10, 10, somar)

# Escopo global
salario = 2000
def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario
salario_bonus(500)
```


Esta pasta explora:
- Como declarar e criar dicionários;
- Adição, remoção e atualização de itens;
- Acesso a valores e chaves;
- Métodos úteis como `fromkeys`, `get`, `keys`, `values`, `items`;
- Iteração sobre dicionários;
- Exemplos práticos e desafios para fixação do conteúdo.

Exemplo de funcionalidade:
```python
# Declarando e manipulando dicionários
pessoa = {"nome": "Guilherme", "idade": 28}
pessoa["telefone"] = "3333-1234"
print(pessoa["nome"])  # Guilherme
# Criando dicionário com fromkeys
resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
```
