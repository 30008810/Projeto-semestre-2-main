import controller as c
import time
import models.user_info as user

def MainOptions():
    print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")
    print("Seja bem vindo, selecione umas das seguintes opções para continuar:\n")
    print("1: Mostrar a sala\n2: Comprar um bilhete\n3: Estatisticas\n4: Mostrar e rever as informaçoes pessoais\n0: Retornar")
    print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")
    i = input()
    return int(i)
    

    #else:
        #print("Seleção inválida, por favor escolha uma das opções anteriores. ")


# index = verificar_espetaculo(...)
# verificar_lugar(..., index)