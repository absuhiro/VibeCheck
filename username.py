import random


class User:
    def __init__(self):
        self.alias = self.generate_alias()

    def generate_alias(self):
        adjectives = [
            "Alta",
            "Mystic",
            "Hidden",
            "Chill",
            "Curious"
        ]

        nouns = [
            "Student",
            "Coder",
            "Guy",
            "Ninja",
            "Viber"
        ]

        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randint(10, 99)

        return adjective + noun + str(number)

    def display(self):
        return self.alias