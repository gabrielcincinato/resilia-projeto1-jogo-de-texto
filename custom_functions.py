from time import sleep
from games import *
import random


def dramatic_print(text):
    """Um print um pouquinho mais demorado do que o original"""
    # print(text)
    for character in text:
        sleep(0.0005)
        print(character, end="")


def dramatic_line_print(text, sleeptime=0.3):
    """Print um pouquinho mais demorado, feito para arquivos de texto com o método .readlines()"""
    # print(text)
    for line in text:
        sleep(sleeptime)
        print(line.strip('\n'))


def skip():
    """Um simples input que serve como pausa"""
    input("\n\nPressione ENTER para pular")


def decision(A, B, question="O que você faz?"):
    """Função a ser usada na hora de escolher uma opção"""
    dramatic_print(f"""
{question}
    A - {A}
    B - {B}
""")
    choice = input("Escolha uma letra: ").lower()
    return choice


def intimidation():
    """Role uma tentativa de intimidação"""
    dice = random.randint(1, 20)
    if dice > 14:
        dramatic_print(f"""
    Rolagem de intimidação
    Necessário: 15
    Obtido: {dice}
    INTIMIDAÇÃO SUCEDIDA""")
        return True
    else:
        dramatic_print(f"""
    Rolagem de intimidação
    Necessário: 15
    Obtido: {dice}
    INTIMIDAÇÃO MALSUCEDIDA""")
        return False
