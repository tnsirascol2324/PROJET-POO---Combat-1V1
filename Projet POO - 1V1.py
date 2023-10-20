import random
"""
Duel PVP en Python

Ce programme est un jeu de duel en utilisant la programmation orientée objet (POO).

Classes:
- Element : Classe représentant les éléments du jeu (EAU, FEU, VENT) avec leurs attaques.
- Attack : Classe représentant les attaques avec leur nom.
- Player : Classe représentant les joueurs avec leur nom, élément, points de vie (HP), bouclier et utilisations de soin.

Méthodes:
- Player.attack(target) : Permet au joueur d'attaquer un adversaire avec une attaque aléatoire.
- Player.use_shield() : Permet au joueur d'utiliser un bouclier pour se protéger.
- Player.use_heal() : Permet au joueur de se soigner en récupérant des points de vie.
- Player.take_damage(damage) : Réduit les points de vie du joueur en fonction des dégâts infligés.

Utilisation:
- Créez deux joueurs en spécifiant leur nom et élément.
- Les joueurs s'affrontent en choisissant des actions (attaquer, se protéger, se soigner).
- Le combat se déroule jusqu'à ce que l'un des joueurs atteigne 0 HPs.

Exemple d'utilisation:

player1 = Player("Joueur 1", Element.EAU)
player2 = Player("Joueur 2", Element.FEU)
"""


class Element:
    def __init__(self, name, attacks):
        self.__name = name
        self.attacks = attacks

class Attack:
    def __init__(self, name):
        self.name = name

class Player:
    def __init__(self, name, element):
        self.name = name
        self.element = element
        self.hp = 200
        self.shield = 0
        self.heal_remaining = 3

    def take_damage(self, damage):
        self.hp -= damage

    def attack(self, target):
        print(f"{self.name} attaque avec {self.element.attacks[random.randint(0, 2)].name}")
        damage = random.randint(20, 50)
        target.take_damage(damage)
        print(f"{target.name} perd {damage} points de vie.")

    def use_shield(self):
        self.shield += 10
        print(f"{self.name} utilise un bouclier.")

    def use_heal(self):
        if self.heal_remaining > 0:
            healed_hp = min(40, 100 - self.hp)
            self.hp += healed_hp
            self.heal_remaining -= 1
            print(f"{self.name} se soigne de {healed_hp} points de vie.")
            if 

water_attacks = [Attack("Hydroblast"), Attack("Aqua Jet"), Attack("Tsunami")]
fire_attacks = [Attack("Fireball"), Attack("HellFlame"), Attack("Inferno")]
wind_attacks = [Attack("Gust"), Attack("Tornado"), Attack("Cyclone")]

water_element = Element("EAU", water_attacks)
fire_element = Element("FEU", fire_attacks)
wind_element = Element("VENT", wind_attacks)

player1_name = input("Joueur 1, entrez votre nom : ")
player1_element = input(f"{player1_name}, choisissez votre élément (EAU, FEU, VENT) : ").upper()

while player1_element not in ["EAU", "FEU", "VENT"]:
    player1_element = input("Choisissez un élément valide (EAU, FEU, VENT) : ").upper()

player1 = Player(player1_name, water_element if player1_element == "EAU" else (fire_element if player1_element == "FEU" else wind_element))

player2_name = input("Joueur 2, entrez votre nom : ")
player2_element = input(f"{player2_name}, choisissez votre élément (EAU, FEU, VENT) : ").upper()

while player2_element not in ["EAU", "FEU", "VENT"]:
    player2_element = input("Choisissez un élément valide (EAU, FEU, VENT) : ").upper()

player2 = Player(player2_name, water_element if player2_element == "EAU" else (fire_element if player2_element == "FEU" else wind_element))

print(f"{player1.name} affronte {player2.name} dans un duel")

while player1.hp > 0 and player2.hp > 0:
    print("-" * 40)  # Ligne de séparation avant chaque tour de combat
    print(f"{player1.name} - HP: {player1.hp} | Bouclier: {player1.shield} | Soins restants: {player1.heal_remaining}")
    print(f"{player2.name} - HP: {player2.hp} | Bouclier: {player2.shield} | Soins restants: {player2.heal_remaining}")

    while True:
        action1 = input(f"{player1.name}, que voulez-vous faire? (attack, shield, heal) : ").lower()
        if action1 in ["attack", "shield", "heal"]:
            break
        else:
            print("Choisissez une action valide (attack, shield, heal).")

    while True:
        action2 = input(f"{player2.name}, que voulez-vous faire? (attack, shield, heal) : ").lower()
        if action2 in ["attack", "shield", "heal"]:
            break
        else:
            print("Choisissez une action valide (attack, shield, heal).")

    if action1 == "attack":
        player1.attack(player2)
    elif action1 == "shield":
        player1.use_shield()
    elif action1 == "heal":
        player1.use_heal()

    if action2 == "attack":
        player2.attack(player1)
    elif action2 == "shield":
        player2.use_shield()
    elif action2 == "heal":
        player2.use_heal()

    print("-" * 40)  # Ligne de séparation après chaque tour de combat

# Fin du combat
if player1.hp <= 0:
    print(f"{player2.name} remporte la victoire!")
else:
    print(f"{player1.name} remporte la victoire!")
