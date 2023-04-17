print("Jogo de Pedra, Papel e Tesoura\n")

while True:    
        jogada1 = input("Jogador 1, escolha pedra, papel ou tesoura: ")
        jogada2 = input("Jogador 2, escolha pedra, papel ou tesoura: ")

        if jogada1 == jogada2:
            print("Empate!")

        elif jogada1 == "pedra" and jogada2 == "tesoura":
            print("Jogador 1 venceu!")

        elif jogada1 == "tesoura" and jogada2 == "papel":
            print("Jogador 1 venceu!")

        elif jogada1 == "papel" and jogada2 == "pedra":
            print("Jogador 1 venceu!")

        else:
            print("Jogador 2 venceu!")

        jogar_novamente = input("Deseja jogar novamente? (s/n)")

        if jogar_novamente.lower() != "s":
            break