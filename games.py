from custom_functions import *
from elements import *
from fighter import Fighter
from time import sleep
import random


def rock_paper_scissors():
    """Jogue o jogo de pedra, papel e tesoura."""
    plays_list = ["Pedra", "Papel", "Tesoura"]

    computer_choice = random.choice(plays_list)
    player_choice = input(f"""
{plays_list[0]}
{plays_list[1]}
{plays_list[2]}

Escolha um: """).title()

    if player_choice == computer_choice:
        plays_list.remove(player_choice)
        computer_choice = random.choice(plays_list)

    winner_message = f"""
    Você escolheu: {player_choice}.
    Demônio escolheu: {computer_choice}.
    VOCÊ venceu."""
    loser_message = f"""
    Você escolheu: {player_choice}.
    Demônio escolheu: {computer_choice}.
    DEMÔNIO venceu."""

    if player_choice == "Pedra" and computer_choice == "Papel":
        print(loser_message)
        return False

    elif player_choice == "Pedra" and computer_choice == "Tesoura":
        print(winner_message)
        return True

    elif player_choice == "Papel" and computer_choice == "Tesoura":
        print(loser_message)
        return False

    elif player_choice == "Papel" and computer_choice == "Pedra":
        print(winner_message)
        return True

    elif player_choice == "Tesoura" and computer_choice == "Pedra":
        print(loser_message)
        return False

    elif player_choice == "Tesoura" and computer_choice == "Papel":
        print(winner_message)
        return True


def play_nicobulus_game():
    """Jogue as escolhas de Nicobulus"""
    # Etapa 1:
    first_choice = decision(A='"Ok, Senhor Demônio, muito obrigado pela oportunidade. Seria uma honra poder jogar com '
                              'o senhor."',
                            B='"Por favor, Senhor Demônio, estou com medo, deixe-me ir embora."')

    # A - "Ok, Senhor Demônio, aceito a honra de jogar contigo."
    if first_choice == 'a':
        # Etapa 2
        dramatic_print("""
    Demônio - Hm, você parece ser estúpido e sem graça. Não acho que me divertiria jogando qualquer tipo de jogo com
você... mas um trato é um trato. Vamos jogar um simples Pedra, Papel e tesoura.""")
        skip()

        # If winner
        if rock_paper_scissors():

            # Etapa 3
            skip()
            dramatic_print("""
    Demônio - Uma partida sem graça jogada contra uma pessoa sem graça. Arrependo-me amarguramente de tê-lo escolhido
como meu oponente. Tempo perdido que nunca mais retornará. Enfim, eu disse que iria lhe satisfazer um desejo. Diga-me
o que queres e eu concederei.""")
            skip()
            second_choice = decision(A='"O senhor vive dizendo que sou sem graça... pois bem, gostaria que o senhor me '
                                       'tornasse em uma pessoa carismática e interessante."',
                                     B='"Por favor, Senhor Demônio, tire-me deste lugar aterrorizante, é o meu único '
                                       'desejo."')

            # A - O senhor vive dizendo...
            if second_choice == 'a':
                # Resultado
                dramatic_print("""
    O demônio dá um sorriso malicioso.
    Demônio - Muito bem... se é isso que queres...
    Você imediatamente se sente mais extrovertido, carismático, interessante. O mundo é sua ostra agora, basta sair
desta maldita masmorra e viver a vida lá fora como uma nova pessoa. Porém, o demônio desapareceu e não lhe disse onde é 
a saída. Você procura e procura e nunca acha. Você encontra outros demônios e criaturas diabólicas na masmorra, mas
nenhuma te ataca, muito pelo contrário: eles se sentem atraídos por você e te acham o máximo. Realmente, você virou uma
pessoa super carismática e interessante, mas nunca conseguiu encontrar a saída da masmorra. Viveu o resto de sua vida 
dentro dela, sendo uma espécie de ídolo para as criaturas que lá residiam...""")
                skip()
                return False

            # B - Por favor, Senhor Demônio, tire-me deste lugar...
            elif second_choice == 'b':
                # Resultado
                dramatic_print("""
    O demônio demonstra insatisfação por um momento, mas obtém uma ideia.
    Demônio - É um prazer realizar o seu desejo.
    Você acorda em um lugar estranho, com clima estranho, pessoas estranhas e idioma estranho. Você pediu para o demônio
lhe tirar da masmorra, mas não especifou o local porque você é inocente e burro. Mas a boa parte é que você está fora 
daquele lugar e pode voltar para casa com uma ótima história para contar... se você conseguir.""")
                skip()
                return True

        # If loser
        elif not rock_paper_scissors():
            skip()
            dramatic_print("""
    Demônio - Como eu disse, trato é trato... e você perdeu. Sua alma parece ser tão sem gosto quanto você, mas ainda
sim é melhor que nada.
    Nicobulus - Ó não, Senhor Demônio, por favor, deixe-me ir embora, não sugue minha alma...
    Você implora mas não surte efeito. O demônio cumpre o trato e começa a sugar a sua alma. Você sente o mundo
escurer e o desespero crescendo enquanto tem a consciência de estar abandonando a vida na terra para uma triste 
existência sendo parte da terrível criatura. Sua partida foi tão patética quanto sua vida.""")
            skip()
            return False

    # B - Por favor, Senhor Demônio, deixe-me ir embora
    elif first_choice == "b":
        # Etapa 2
        dramatic_print("""\nDemônio - Mas é claro, amigo. Apenas siga em frente e vire à direita.""")
        skip()
        dramatic_print("""
    Você segue em frente conforme as instruções do demônio e prepara-se para virar à direita. Porém, ao observar o 
corredor, você vê inúmeras criaturas diabólicas esperando pela sua passagem com olhares nefastos e penetrantes.
""")
        dramatic_line_print(creatures, 0.1)
        sleep(1)
        second_choice = decision(A="Dá meia-volta e pede encarecidamente que o demônio dispense suas criaturas.",
                                 B="Presume que o demônio lhe deu passagem garantida e segue em frente.")
        # A - Dá meia volta e pede encarecidamente que o demônio dispense suas criaturas.(FIM)
        if second_choice == 'a':
            # Result
            dramatic_print("""
    Você tenta dar meia-volta, mas as criaturas investem contra você com força e velocidades impressionantes, perfurando
tuas costas com inúmeras alabardas. Não há mais volta, esté é o fim. Você veio em busca de um pouco de emoção, e foi
exatamente o que conseguiu: MEDO e DESESPERO. Tua morte foi tão patética quanto tua vida.""")
            skip()
            return False

        # B - Presume que o demônio lhe deu passagem garantida e segue em frente(FIM)
        elif second_choice == 'b':
            # Result
            dramatic_print("""
    Você, inocentemente, começa a seguir em frente e, ao chegar perto de uma das criaturas, é violentamente atacado por
todos os lados, com as alabardas dos seres diabólicos perfurando cada centímetro do seu corpo, causando-lhe dores
excruciantes.
    Ao perceber sua vida esvanecendo, em meio aos últimos suspiros, um pensamento surge em sua mente: \"Ó Deus, como fui
estúpido o suficiente para acreditar nas palavras de um DEMÔNIO?\"""")
            skip()
            return False


def play_quintinus_game():
    """Jogue as escolhas de Quintinus"""
    # Etapa 1
    first_choice = decision(A='"Eu te reconheço, criatura. Teu nome é Arzinnun. Já estudei sobre ti e conheço todas as '
                              'tuas artimanhas."',
                            B='[Fingir ignorância] "Tudo bem, eu aceito."')
    # B - [Fingir ignorância] Tudo bem, eu aceito.
    if first_choice == 'b':
        # Etapa 2
        dramatic_print(f"""
    Arzinnun - Hm, vejo sagacidade em você. Sei que não estou lidando com um ser estúpido. Testarei a sua 
inteligência. Basta passar no teste, e eu lhe concederei um desejo. Agora, responda-me:
{random_question}""")
        second_choice = decision(A=f"{random_question_A}",
                                 B=f"{random_question_B}",
                                 question="Qual é a sua resposta?")

        # B - Resposta certa
        if second_choice == "b":
            # Etapa 3
            dramatic_print(f"""
    Arzinnun - HA! Talvez você seja mais esperto do que imaginei. Diga-me, humano não-estúpido, como você chegou a essa
conclusão?
    Quintinus - {random_question_resolution}
    Arzinnun - Muito bem, humano não-estúpido. Trato é trato. Eu te prometi um desejo, portanto, concederei. Faça-o.""")
            third_choice = decision(A='"Quero retornar a minha casa com as melhores habilidades intelectuais da Terra."',
                                    B='"Quero que você MORRA."')

            # A - Quero retornar a minha casa com habilidades
            if third_choice == "a":
                # Resultado
                dramatic_print("""
    O demônio solta um grande "HA!", achando ser esperto.
    Arzinnun - Eu disse apenas um desejo, mas você quer retornar a sua casa e ter as melhores habilidades intelectuais
da Terra. Você só pode escolher um, humano não-estúpido.
    Quintinus - Escute bem, eu disse que quero retornar a minha casa COM as melhores habilidades intelectuais da Terra,
e não retornar a minha casa E ter as melhores habilidades intelectuais da Terra. Usei COM, não E. As duas condições andam
JUNTAS, como uma SÓ, portanto é apenas UM desejo.""")
                skip()
                dramatic_print("""
    O demônio usa o seu cérebro demoníaco para raciocinar a tua lógica, e chega a conclusão de que é correta. Com muita
relutância, ele cede ao teu desejo e te manda de volta para casa sendo a pessoa com as melhores habilidades intelectuais
da Terra.
    Ao receber a dávida das habilidades intelectuais, você percebe que havia inúmeras maneiras de vencer o desafio,
libertar seus colegas, destruir o demônio... enfim, não adianta preocupar-se com o passado, uma vida (talvez) brilhante
o espera.""")
                skip()
                return True

            # B - Quero que você MORRA
            elif third_choice == "b":
                # Resultado
                dramatic_print("""
    Ao ouvir o teu desejo, Arzinnun fica furioso.
    Arzinnun - Humano maldito, retire este desejo, agora!
    Quintinus - Eu sei como funciona este lugar! Se você morrer, todas as criaturas que aqui habitam vão junto, a
masmorra perde a sua mágica e torna-se apenas um lugar comum. Trato é trato, você é obrigado a cumpri-lo.
    Arzinnun - AAAAH!""")
                skip()
                dramatic_print("""
    Arzinnun nunca imaginou que um ser humano iria enxergar além de sua própria ganância e pedir algo do tipo. Ele
deveria ter sido mais cuidadoso com o humano não-estúpido, mas não foi.
    Ao ter o seu desejo realizado, a masmorra perdeu o seu ar misterioso e diabólico, todas as criaturas pereceram junto
com o seu mestre. As passagens clarearam e a saída revelou-se prontamente. Quintinus e seus colegas não tiveram
realmente o que queriam, mas pelo menos ninguém mais será vítima deste maldito lugar... como é bom não ser estúpido!.""")
                skip()
                return True

        # A - Resposta errada
        elif second_choice == "a":
            # Resultado
            dramatic_print("""
    Arzinnun - Talvez eu tenha me enganado, talvez você seja um estúpido. Enfim, resposta ERRADA, estúpido. Sua alma
será saborosa.
    "Droga! Como eu, um intelectual, errei uma questão tão idiota dessas? Será que o demônio está certo? Será que eu sou
realmente ESTÚPIDO? Se eu for, talvez eu mereça isto...
    O demônio prepara-se para sugar a tua alma. Você não luta, apenas aceita o teu destino merecido. Um ser humano capaz
de errar uma questão dessas não tem o intelecto de um humano, mas de um RATO. Todo esse tempo você gastou procurando o
conhecimento, mas no final, quando realmente foi necessário, ele o abandonou... triste fim.""")
            skip()
            return False

    # A - Eu te reconheço.
    elif first_choice == "a":
        # Resultado
        dramatic_print(f"""
    Arzinnun - HA! Então você é um desses espertos e arrogantes, hein? Acha que sabe tudo? Veremos. Um verdadeiro gênio
tem as respostas na ponta da língua. Este será o seu teste: far-te-ei uma pergunta e caso demore mais de um segundo para
respondê-la, SUGAREI tua alma.""")
        skip()
        dramatic_print(f'''
    Arzinnun - "Pois bem, gênio, responda-me isto: {random.choice(stupid_questions)}"''')
        skip()
        dramatic_print(f"""
    Você chega em uma resposta satisfatória, porém demorou mais de um segundo para concebê-la. O demônio Arzinnun
prepara-se para sugar a tua alma. Você diz: "Espere, eu sei a resposta, eu sei a resposta!", mas não adianta. Você
falhou no teste e todo o seu conhecimento será desperdiçado e nunca mais compartilhado com o mundo. Triste fim.""")
        skip()
        return False


def play_romanus_game():
    """Jogue as escolhas de Romanus"""
    # Etapa 1
    first_choice = decision(A='"Hm... um desejo. Certo, chifrudo, vamos brincar."',
                            B='[INTIMIDAR] "Cale esta maldita matraca, criatura, e mostre-me onde estão a saída e '
                              'as riquezas, não necessariamente nesta ordem!"')

    # B - [INTIMIDAR]
    if first_choice == "b":
        # Resultado
        if intimidation():
            skip()
            dramatic_print("""
    O demônio fica aterrorizado diante de tua demonstração de fúria e agressividade. Eis aí um espécimen humano VIRIL.
    Demônio - Ahn... sim, sim. Siga em frente para as riquezas, depois vire a esquerda e encontrará a saída.
    Você segue as instruções do demônio, tendo certeza de serem verdadeiras pela forma como ele ficou amedrontado diante
de sua demonstração crua de ferocidade. Ele não mentiu. Você achou tesouros valiosos e depois saiu da masmorra, como se 
nada tivesse acontecido.""")
            skip()
            return True
        else:
            skip()
            dramatic_print("""
    O demônio diverte-se com sua pífia tentativa de intimidá-lo.
    Demônio - Como queira...
    O demônio chama a sua horda para lhe atacar. Você consegue eliminar algumas criaturas, mas muitas outras vêm em sua
direção e no fim sua força cede. Você teve uma morte dolorosa e violenta, porém partiu lutando como um bom guerreiro.""")
            skip()
            return False

    # A - Certo, chifrudo
    elif first_choice == "a":
        # Etapa 2
        dramatic_print("""
    Demônio - Você aparenta ser um ser humano forte, de índole guerreira. Mas será que é a realidade ou apenas aparência?
O seu teste será de FORÇA. Ganhe-me na PORRADA, e eu concedo o teu desejo.
    Romanus - Pode vir, chifrudo!""")
        skip()

        # Creating fighter objects
        romanus = Fighter("Romanus")
        demonio = Fighter("Demônio")

        # Fighting routine
        while romanus.hp > 0 and demonio.hp > 0:
            if romanus.hp > 0:
                romanus.punch(demonio)
                romanus.show_hp(demonio)
                skip()
            else:
                break
            if demonio.hp > 0:
                demonio.punch(romanus)
                romanus.show_hp(demonio)
                skip()
            else:
                break

        # If winner
        if romanus.hp > 0:
            # Etapa 3
            dramatic_print("""
    Você e o demônio terminam de cair na porrada loucamente. Ao fim de tudo, você vê o demônio de joelhos enquanto você
ainda está de pé e triunfante.
    Demônio - HA! Definitivamente não é só aparência. Você é um lutador de respeito e isto foi divertido.
    Romanus - Avise quando quiser mais, demônio!
    Demônio - Tentador, mas não. Por mérito, você ganhou o direito a um desejo. Faça-o.""")
            second_choice = decision(A='"Quero ser o mais forte do UNIVERSO."',
                                     B='"Dê-me as riquezas que tanto quero!"',
                                     question="O que você deseja?")
            # A - Quero ser o mais forte do UNIVERSO
            if second_choice == 'a':
                dramatic_print("""
    O demônio tenta dar uma disfarçada.
    Demônio - Hm, então voce quer ser o mais forte do mundo... certo?
    Romanus - NÃO! Eu disse "O mais forte do UNIVERSO", não só do mundo, mas do UNIVERSO! Conceda-me meu prometido desejo.
    No fim, o demônio não achou que haveria muita diferença entre "mais forte do mundo" para "mais forte do universo",
porém o universo é grande, com outras civilização e raças mais avançadas do que as do mundo. Ao receber a maior força do 
universo, Romanus imediatamente obteu poder o suficiente para matar o demônio, juntar os colegas, obter as riquezas que
tanto queria e destruir a maldita masmorra com poquíssimo esforço. Ninguém em todo o universo conhecido conseguiria se
opor a ele agora. Enquanto viver, reinará absoluto. Pena que não pediu vida eterna...""")
                skip()
                return True
            # B - Dê-me as riquezas que tanto quero
            if second_choice == 'b':
                dramatic_print("""
    O demônio dá um leve sorriso malicioso.
    Demônio - É um prazer realizar o seu desejo. Basta seguir em frente e encontrará todas as riquezas que procura.
    Romanus seguiu em frente e realmente encontrou todas as riquezas que procurava, porém nenhuma saída. Ficou rondando
a masmorra até achar alguma escapatória, mas não conseguiu. Enfrentou e matou várias outras criaturas diabólicas, mas no
fim não aguentou a quantidade interminável de lutas sem sentido e acabou perecendo como o homem mais rico da maldita
masmorra.""")
                skip()
                return False

        # If loser
        else:
            dramatic_print("""
    Você cai no chão, derrotado.
    Demônio - Aparentemente é só aparência. Nenhuma força. O mundo não merece um ser humano tão fraco como você.
Considere isto como um favor.
    Ao som de risadas diabólicas, o demônio começa a devorar tua alma. Morrer desta forma, acabado e indefeso, nunca foi
digno de você... uma lástima.""")
            skip()
            return False
