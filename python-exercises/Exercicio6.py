import string
import random

def gerar_senha(tamanho):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for i in range(tamanho))
        return senha

tamanho = int(input("Digite o tamanho da senha: "))
senha = gerar_senha(tamanho)

print("Senha gerada:", senha)