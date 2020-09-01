import programa_binarios2


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
            conversao = programa_binarios2.Conversao()
            conversao.main()
            


        elif escolha == 2:
            tab_verdade = programa_binarios2.Tabela_Verdade()
            tab_verdade.main()

        elif escolha == 3:
            tipo_numerico = programa_binarios2.Tipo_Numerico()
            tipo_numerico.main()


        else:
            break
    
            

main()
        




    


                   

    
    
    
