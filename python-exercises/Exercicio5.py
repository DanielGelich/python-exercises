def remover_duplicatas(lista):

    conjunto_sem_duplicatas = set(lista)

    lista_sem_duplicatas = list(conjunto_sem_duplicatas)
    return lista_sem_duplicatas


minha_lista = [1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9]
nova_lista = remover_duplicatas(minha_lista)
print(nova_lista) 