import random

while True:
        num_aleatorio = random.randint(1, 9)
        num_usuario = input("Digite um número entre 1 e 9 ou digite 'sair' para encerrar o jogo: ")

        if num_usuario == "sair":
            break

try:
            num_usuario = int(num_usuario)

            if num_usuario < 1 or num_usuario > 9:
                print("Por favor, digite um número entre 1 e 9")

            elif num_usuario == num_aleatorio:
                print("Parabéns, você acertou o número!")

            elif num_usuario < num_aleatorio:
                print("O número é maior")

            else:
                print("O número é menor")
                
except ValueError:
        print("Por favor, digite um número válido ou 'sair'")