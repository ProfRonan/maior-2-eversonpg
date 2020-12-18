"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    número_1 = float(input("Digite um número\n"))
    número_2 = float(input("Digite outro número\n"))

    #maior
    if (número_1 >= número_2):
       maior = número_1
    else:
      maior = número_2
    print(f'{maior}')


if __name__ == '__main__':
    main()
