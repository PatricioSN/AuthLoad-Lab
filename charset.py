# GABS este arquivo serve para gerar as senhas

import itertools
# A ordem importa: letras → números → especiais

LETRAS_MINUSCULAS = "abcdefghijklmnopqrstuvwxyz"
LETRAS_MAIUSCULAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMEROS = "0123456789"
ESPECIAIS = "!@#$%&*()_-+="

# Montar_charset é definido pelo usuário qual o tipo de senha ele quer tentar
# ex: o User pode querer usar apenas letra na senha minusculas, então ele usa -l
def montar_charset(letras_min: bool, letras_mai: bool, numeros: bool, especiais: bool) -> str:
    charset = ""
    if not any ([letras_min, letras_mai, numeros, especiais]):
        # nenhuma flag = usa tudo
        return LETRAS_MINUSCULAS + LETRAS_MAIUSCULAS + NUMEROS + ESPECIAIS
    if letras_min:
        charset += LETRAS_MINUSCULAS
    if letras_mai:
        charset += LETRAS_MAIUSCULAS
    if numeros:
        charset += NUMEROS
    if especiais:
        charset += ESPECIAIS

    return charset

# Aqui, ele pega a string formada pelo "montar_charset", essa string se chama charset
def gerar_senhas(tamanho_max: int, letras_min: bool = False, letras_mai: bool = False,
                 numeros: bool = False, especiais: bool = False):
    charset = montar_charset(letras_min, letras_mai, numeros, especiais)
    print(f"Charset: '{charset}'\n")

    for tamanho in range(1, tamanho_max + 1):
        for combinacao in itertools.product(charset, repeat=tamanho):
            yield ''.join(combinacao)