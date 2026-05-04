import argparse
from pathlib import Path
import rarfile

from charset import gerar_senhas
from cracker import rodar_brute_force

rarfile.UNRAR_TOOL = r'C:\Program Files\WinRAR\UnRAR.exe'

def main():
    # argparse permite passar argumentos direto na linha de comando
    # ex: python main.py target.rar --max 4
    parser = argparse.ArgumentParser(description="Brute force simples para arquivos RAR")
    parser.add_argument("arquivo", help="Caminho do arquivo .rar")
    parser.add_argument("--max", type=int, default=4, help="Comprimento máximo da senha (padrão: 4)")
    args = parser.parse_args()

    caminho = Path(args.arquivo)

    if not caminho.exists():
        print(f"Erro: arquivo '{caminho}' não encontrado.")
        return

    if caminho.suffix.lower() != ".rar":
        print("Aviso: o arquivo não tem extensão .rar. Continuando mesmo assim...")

    print(f"Arquivo: {caminho}")
    print(f"Comprimento máximo: {args.max}")
    print("Iniciando...\n")

    # Aqui está a separação limpa:
    # main não sabe como gerar senhas, só pede ao charset
    # main não sabe como testar senhas, só pede ao cracker
    gerador = gerar_senhas(args.max)
    rodar_brute_force(str(caminho), gerador)

if __name__ == "__main__":
    main()