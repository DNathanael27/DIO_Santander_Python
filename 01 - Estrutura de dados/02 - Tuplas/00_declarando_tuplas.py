# Tuplas são coleções imutáveis em Python, ou seja, não podem ser alteradas após a criação.
# Diferente das listas (que usam colchetes [] e são mutáveis), tuplas usam parênteses () e são ideais para dados que não devem mudar.
# Exemplos abaixo:

frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)  # Exemplo de tupla de strings

letras = tuple("python")  # Cria uma tupla a partir de uma string (cada letra vira um elemento)
print(letras)

numeros = tuple([1, 2, 3, 4])  # Cria uma tupla a partir de uma lista
print(numeros)

pais = ("Brasil",)  # Tupla com um único elemento (atenção à vírgula)
print(pais)

# Resumindo: use tuplas quando quiser garantir que os dados não serão alterados, e listas quando precisar de uma coleção mutável.
