string = input("Digite uma palavra ou frase: ")

if string == string[::-1]:
        print("A string digitada é um palíndromo.")

else:
        print("A string digitada não é um palíndromo.")