"""Aluna : Fernanda Santiago Camacho 
    Matrícula : 202308079344
    dia 23/10/2023"""

"""1- Faça um programa para imprimir o texto abaixo, para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha."""

"""def imprime_texto(num):
    for numero in range(1, num +1):
        print(" ".join([str(numero)]* numero))

imprime_texto (20)"""



""" 2- Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado."""

"""def informe_digitos(num):
           print(num)

informe_digitos(len(str(233498709887)))"""


"""3-Faça um programa que solicite ao usuário 2 números inteiros. A seguir, calcule e mostre a divisão do primeiro pelo segundo. Para resolver este problema, utilize a instrução try-except, particularmente analizando as exceções do tipo ValueError e ZeroDivisionError. Inclua uma instrução finally para exibir o resultado da operação."""

"""def numeros_int():
    divisao =()
    try:
        # divisao =num1/num2
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite um número: "))
        divisao = num1/num2
            
    except ValueError:
            print("O valor inserido não é válido")
    except ZeroDivisionError:
            print("A divisão por zero não é aceita")
    finally:
            print("resposta", divisao)

numeros_int()"""