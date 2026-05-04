import subprocess
import time
from multiprocessing import Pool, cpu_count

UNRAR_PATH = r'C:\Program Files\WinRAR\UnRAR.exe'

def testar_senha(args):
    caminho_rar, senha = args
    resultado = subprocess.run(
        [UNRAR_PATH, "t", "-p" + senha, "-inul", "-y", caminho_rar],
        capture_output=True
    )
    return senha if resultado.returncode == 0 else None


def rodar_brute_force(caminho_rar: str, gerador_senhas):
    inicio = time.time()
    tentativas = 0
    # usa todos os núcleos do seu processador
    nucleos = cpu_count()
    print(f"Usando {nucleos} núcleos em paralelo\n")

    # Pool divide o trabalho entre os núcleos automaticamente
    with Pool(processes=nucleos) as pool:
        # imap processa em lotes sem carregar tudo na memória
        args = ((caminho_rar, senha) for senha in gerador_senhas)

        for resultado in pool.imap(testar_senha, args, chunksize=nucleos * 4):
            tentativas += 1
            if tentativas % 10 == 0:
                decorrido = time.time() - inicio
                velocidade = tentativas / decorrido if decorrido > 0 else 0
                print(f"  [{tentativas}] {velocidade:.0f} senhas/s", end="\r")

            if resultado is not None:
                pool.terminate()  # para todos os outros processos
                decorrido = time.time() - inicio
                print("\n" + "=" * 50)
                print(f"  SENHA ENCONTRADA: '{resultado}'")
                print(f"  Tentativas: {tentativas:,}")
                print(f"  Tempo: {decorrido:.2f}s")
                print("=" * 50)
                return resultado

    decorrido = time.time() - inicio
    print(f"\nSenha não encontrada. {tentativas:,} tentativas em {decorrido:.2f}s.")
    return None