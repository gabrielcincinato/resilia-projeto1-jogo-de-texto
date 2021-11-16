import pandas as pd
import random

# ---------------------------------------------------FILES------------------------------------------------------------ #
with open("texts/logo.txt", 'r', encoding='utf-8') as file1:
    logo = file1.readlines()

with open("texts/demon.txt", 'r', encoding='utf-8') as file2:
    demon = file2.read()

with open("texts/death.txt", 'r', encoding='utf-8') as file3:
    death = file3.readlines()

with open("texts/creatures.txt", 'r', encoding='utf-8') as file4:
    creatures = file4.readlines()

with open("texts/end.txt", 'r', encoding='utf-8') as file5:
    end = file5.readlines()
# ----------------------------------------SINOPSIS AND DESCRIPTIONS--------------------------------------------------- #

sinopsis = """
    Três conhecidos ouvem falar de uma masmorra semi-secreta localizada em um lugar semi-secreto que, quando acessada
e devidamente explorada, promete satisfazer qualquer desejo do viajante. Mas ao chegar, os caminhos tornam-se
emaranhados, os três conhecidos se perdem e ficam isolados no lugar misterioso e perigoso."""

nicobulus_description = """
    A - Nicobulus Lovernius: Garoto jovem, muito educado. Decidiu participar desta aventura somente para tentar trazer
um pouco de emoção em sua vida pacata e sem graça."""

quintinus_description = """
    B - Quintinus Papus: Um intelectual e curioso. Decidiu seguir esta excursão para obter mais conhecimento e tornar-se
superior aos seus semelhantes"""

romanus_description = """
    C - Romanus Ennodius: Guerreiro e bruto. Pela sua experiência, lugares antigos e mal explorados sempre guardam algum
tipo de riqueza imaculada, o que torna esta excursão uma oportunidade perfeita para enriquecer, além de pôr suas
habilidades marciais em prática."""

# --------------------------------------RANDOM QUESTIONS FOR QUINTINUS GAME------------------------------------------- #
data = pd.read_csv("questions.csv")

stupid_questions = [
    "Porque é que existem pessoas que acordam os outros e depois perguntam se a pessoa estava dormindo?",
    "Porque a gente bota a calça e calça a bota?",
    "Como são chamadas as montanhas-russas na Rússia?",
    "Se o Pinóquio falasse: 'Meu nariz crescerá agora!', o que aconteceria?",
]

questions_dictionary = {row.question: {"A": row.A, "B": row.B, "Resolution": row.Resolution} for index, row in
                        data.iterrows()}

random_question = random.choice(list(questions_dictionary.keys()))
random_question_A = questions_dictionary[random_question]["A"]
random_question_B = questions_dictionary[random_question]["B"]
random_question_resolution = questions_dictionary[random_question]["Resolution"]
