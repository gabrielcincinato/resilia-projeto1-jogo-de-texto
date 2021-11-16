import random


class Fighter:
    """Classe de lutador que permite dar soco em outro lutador"""
    def __init__(self, name):
        self.name = name
        self.hp = 100

    def punch(self, enemy):
        """Desfere soco em outro lutador"""
        punch = random.randint(20, 30)
        enemy.hp -= punch
        print(f"""
    {self.name} desferiu um soco em {enemy.name} e tirou {punch} pontos de vida!""")

    def show_hp(self, enemy):
        """Mostra o HP dos respectivos lutadores"""
        print(f"""
    {self.name} - {self.hp} HP
    {enemy.name} - {enemy.hp} HP""")
