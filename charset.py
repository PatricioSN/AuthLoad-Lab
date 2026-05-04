import itertools

# A ordem importa: letras → números → especiais
CHARSET = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%&*()_-="

def gerar_senhas(tamanho_max: int):

    for tamanho in range(1, tamanho_max + 1):
        for combinacao in itertools.product(CHARSET, repeat=tamanho):
            yield ''.join(combinacao)