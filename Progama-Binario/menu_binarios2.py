import programa_binarios2 as bin


def main():

    print("\n----------------------MENU PROGRAMA BINÁRIOS---------------------------------")

    print("\nDigite 1 para conversão de base (bin, hex, octl, dec)\n"
          "Digite 2 para tabela verdade de uma equação booleana\n"
          "Digite 3 para Tipos de numero:"
          "(Sinal_Magnetude,Complemento de dois ou Ponto Flutuante)"
          )

    escolha= int(input("Digite numero: "))

    teste = True

    while teste:

        if escolha == 1:
            conversao = bin.Conversao()
            conversao.main()



        elif escolha == 2:
            tab_verdade = bin.Tabela_Verdade()
            tab_verdade.main()

        elif escolha == 3:
            tipo_numerico = bin.Tipo_Numerico()
            tipo_numerico.main()


        else:
            break



main()
