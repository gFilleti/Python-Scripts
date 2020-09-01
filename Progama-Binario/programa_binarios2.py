import menu_binarios2
import os


class Conversao:
    

    def converte_decimal(self,numero,base):

        if base == 16:
            hexadecimal = int(numero,16)
            numero = str(hexadecimal)
            lista_numero = list(numero)
            base = 10
        else:
            lista_numero = list(numero)
            
        soma = 0
        j = (len(lista_numero)-1)
        teste = 0

        for i in range(len(lista_numero)):
            digito = int(lista_numero[i]) 
            converte = digito * (base ** j)
            soma = soma + converte
            j = j -1

        return soma

        
    def converte_numero(self, numero,base_numero,base_convesao):

        decimal = self.converte_decimal(numero,base_numero)
        
        if base_convesao == 8:
            return ("\nNumero base octal é %s" % oct(decimal))

        elif base_convesao == 16:
            return ("\nNumero base hexadecimal é %s" % hex(decimal))

        elif base_convesao == 2:
            return ("\nNumero base binária é %s" % bin(decimal))

        else:
            return ("\nNumero base decimal é %d" % decimal)


    def main(self):
        print("\n---------------------------ÍNÍCIO CONVERSÃO BASES-------------------------------")
        numero = input("\nDigite Numero para converter: ")
        base_numero = int(input("\nDigite a base do numero: "))
        base_convesao = int(input("\nDigite a base de conversão: "))

        print(self.converte_numero(numero,base_numero,base_convesao))

        print("\n-------------------------------FIM--------------------------------------------\n")


        while True:
            escolha = input("\nPara continuar precione S."
                            "Para sair precione qualquer tecla:")

            if escolha == "s":
                os.system('cls' if os.name == 'nt' else 'clear')
                self.main()

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                menu_binarios2.main()

        
class Tabela_Verdade:
  
    def tabela_verdade(self,variaveis_equacao, total_variaveis, equacao):

        if variaveis_equacao == 3:
            A =[0, 0, 0, 0, 1, 1, 1, 1]
            B =[0, 0, 1, 1, 0, 0, 1, 1]
            C =[0, 1, 0, 1, 0, 1, 0, 1]

            return self.calculo_tres_variaveis(total_variaveis, equacao, A, B, C)

        if variaveis_equacao == 2:
            A =[0, 0, 1, 1]
            B =[0, 1, 0, 1]

            return self.calculo_duas_variaveis(total_variaveis, equacao, A, B)
        
            

    def test_xor(self,conversao):
        conversao = str(conversao)

        if conversao == "True":
            conversao = 1
            return conversao

        elif conversao == "False":
            conversao = 0
            return conversao
        
        else:
            return conversao

    def calculo_tres_variaveis(self,total_variaveis, equacao, A, B, C):

        if total_variaveis == 6:
            tabela =[]
            for i in range(8):
                conversao =eval(equacao % (i, i, i, i, i, i))
                
                tabela.append(self.test_xor(conversao))

            return tabela
                      
        
        if total_variaveis == 5:
            tabela =[]
            for i in range(8):
                conversao =eval(equacao % (i, i, i, i, i))
                
                tabela.append(self.test_xor(conversao))

            return tabela

        if total_variaveis == 4:
            tabela =[]
            for i in range(8):
                conversao =eval(equacao % (i, i, i, i))
                
                tabela.append(self.test_xor(conversao))

            return tabela

        if total_variaveis == 3:
            tabela =[]
            for i in range(8):
                conversao =eval(equacao % (i, i, i))
                
                tabela.append(self.test_xor(conversao))

            return tabela
        
        if total_variaveis == 2:
            tabela =[]
            for i in range(8):
                conversao =eval(equacao % (i, i))
                
                tabela.append(self.test_xor(conversao))

            return tabela

        if total_variaveis == 1:
            tabela =[]
            for i in range(8):
                conversao =eval(equacao % (i))
                
                tabela.append(test_xor(conversao))

            return tabela
            

    def calculo_duas_variaveis(self, total_variaveis, equacao, A, B):

        if total_variaveis == 6:
            tabela =[]
            for i in range(4):
                conversao =eval(equacao % (i, i, i, i, i, i))
                
                tabela.append(self.test_xor(conversao))

            return tabela
                      
        
        if total_variaveis == 5:
            tabela =[]
            for i in range(4):
                conversao =eval(equacao % (i, i, i, i, i))
                
                tabela.append(test_xor(conversao))

            return tabela

        if total_variaveis == 4:
            tabela =[]
            for i in range(4):
                conversao =eval(equacao % (i, i, i, i))
                
                tabela.append(self.test_xor(conversao))

            return tabela

        if total_variaveis == 3:
            tabela =[]
            for i in range(4):
                conversao =eval(equacao % (i, i, i))
                
                tabela.append(self.test_xor(conversao))

            return tabela
        
        if total_variaveis == 2:
            tabela =[]
            for i in range(4):
                conversao =eval(equacao % (i, i))
                
                tabela.append(self.test_xor(conversao))

            return tabela

        if total_variaveis == 1:
            tabela =[]
            for i in range(4):
                conversao =eval(equacao % (i))
                
                tabela.append(self.test_xor(conversao))

            return tabela
            
        
        
                              
            
    def main(self):
        print("---------------------------ÍNÍCIO TABELA VERDADE----------------------------------")

        print("As equações devem ser escritas com and, or, not and, not or, ^ .\n"
              "Lembrando que na equação deve trocar:"
              "(+ por or) , (* por and), (── por not), ( ⊕ por ^).\n"
              "Use A[%d],  B[%d] ou B[%d] para escrever a equação" 
              "\nEx:(A + B)(A + C)  = (A[%d] or B[%d]) and (A[%d] or C[%d])\n"
              )

        equacao = input("Digite Equação: \n")

            

        print("\nQuantas variaveis diferentes há nas esquações? \n"
              "Exemplo: (A + B)(A + C)  = 3 variaves diferente, A, B e C."
              "Digite 3 para tres variaveis (A,B,C). Ou digite 2 para duas ou uma variavel"
              " 3 para (A,B,C) ou 2 para (A,B,C) ou (A) \n")
              

        variaveis_equacao =int(input("Quantas variaveis diferentes tem a equação:"))


        print("\nQual total de variaveis há esquações? \n"
              "Exemplo: (A + B)(A + C)  = 4 variaves  no total, 2A, 1B e 1C.\n")
              

        total_variaveis = int(input("\nTotal de variaveis da equação:"))


        resultado = self.tabela_verdade(variaveis_equacao, total_variaveis, equacao)

        
        print("\nO resultado da equação %s, será: \n" % equacao)

        for i in range(len(resultado)):
            print("\t",resultado[i])


        print("---------------------------------FIM-----------------------------------------")


        while True:
            escolha = input("\nPara continuar precione S."
                        "Para sair precione qualquer tecla:")

            if escolha == "s":
                os.system('cls' if os.name == 'nt' else 'clear')
                self.main()

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                menu_binarios2.main()


            

class Tipo_Numerico:
    

    def comnversao (self, numero_sinal):
    
        lista_binario = []

                       
        numero = int(numero_sinal[1:])
        
        for i in range(numero):

            binario= numero % 2
            if numero > 0:
                lista_binario.append(binario)
            numero = numero // 2

        return lista_binario
    

    def sinal_magnetude(self,numero_sinal, bits):

        lista_binario = self.comnversao(numero_sinal)

        if (numero_sinal[0] == "+" or numero_sinal[0]) and bits > 0:

            bits_acress = bits - len(lista_binario) - 1
            for i in range(bits_acress):
                lista_binario.append(0)
            
        if numero_sinal[0] == "-":
            lista_binario.append(1)

        else:
            lista_binario.append(0)
        

        lista_binario.reverse()

        return lista_binario

    def flip(self,c):
        return '1' if (c == '0') else '0'
              

        
    def complemento_dois(self, numero_sinal, bits):

        complemento_positivo = self.sinal_magnetude(numero_sinal, bits)

        
        if numero_sinal[0] == "+":
            
            return complemento_positivo

        elif numero_sinal[0] == "-":
                       
            compl_um = ""
            compl_dois = ""
            lista_binario = self.comnversao(numero_sinal)
            n = len(lista_binario)

            for i in range(n):
                compl_um += self.flip(lista_binario[i]) 

            compl_um = list(compl_um .strip(""))
            compl_dois = list(compl_um)
            
            for i in range(n - 1, -1, -1):
                    
                if (compl_um[i] == '1'):
                    compl_dois[i] = '0'
                else:          
                    compl_dois[i] = '1'
                    break
            i -= 1

            if (i == -1):
                twos.insert(0, '1')
            
            complemeno_negativo = compl_dois
            
            
            return complemeno_negativo

        
        
        

    def ponto_flutuante(self,numero_sinal, bits_expo, bits_signi):
        a=5
        

        


    def main(self):
        print("--------------------------ÍNÍCIO TIPO DE NUMERO---------------------------------")

        print("\nDigite 1 para Sinal- Magnitude"
          "Digite 2 para Complemento de Dois\n"
          "Digite 3 para Ponto-Flutuante:"
          "(Sinal_Magnetude,Complemento de dois ou Ponto Flutuante)"
          )

        escolha= int(input("Digite numero: "))
                      
                      

        if escolha == 1:
            numero_sinal = input("\nDigite Numero com sinal (+ ou -): ")
            bits = int(input("\nDigite quantidade de bits do sinal: "))
            
            sinal_magnetude = self.sinal_magnetude(numero_sinal, bits)
            print("\nO sinal magnetude é: \n %s"
                  "comprimento_lista %d bits" % (sinal_magnetude,len(sinal_magnetude))
                  )

        elif escolha == 2:
            numero_sinal = input("\nDigite Numero com sinal (+ ou -): ")
            bits = int(input("\nDigite quantidade de bits do sinal: "))
            
            complemento_dois = self.complemento_dois(numero_sinal, bits)
            print(complemento_dois) 

        elif escolha == 3:
            numero_sinal = input("\nDigite Numero com sinal (+ ou -): ")
            bits_expo = int(input("\nDigite quantidade de bits do sinal: "))
            bits_signi = int(input("\nDigite quantidade de bits do sinal: "))
            
            ponto_flutuante = self.ponto_flutuante(numero_sinal, bits_expo, bits_signi)
            print(complemento_dois)

        


        
        

        print("---------------------------------FIM-----------------------------------------")


        while True:
            escolha = input("\nPara continuar precione S."
                        "Para sair precione qualquer tecla:")

            if escolha == "s":
                os.system('cls' if os.name == 'nt' else 'clear')
                self.main()

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                menu_binarios2.main()
            
                           

class Equacao_Binaria:

    def soma(lista_binaria1, lista_binaria2):
        
        soma =[]

        
            

        for i in range (len(lista_binaria1)-1,0,-1):

                        if lista_binaria1[i] == 1 and lista_binaria2[i] == 1:
                            soma.append(0)

                        elif lista_binaria1[i] == 1 and lista_binaria2[i] == 0:
                            soma.append(1)

                        elif lista_binaria1[i] == 0 and lista_binaria2[i] == 1:
                            soma.append(1)

                        elif lista_binaria1[i] == 0 and lista_binaria2[i] == 0:
                            soma.append(0)

        return soma
                        
                            

        
            
            
