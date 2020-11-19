from Card import Card


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []
        self.highest_total = 0
        self.lowest_total = 26

    def remove_one(self):
        if len(self.all_cards) < self.lowest_total:
            self.lowest_total = len(self.all_cards)

        return self.all_cards.pop()

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

        if len(self.all_cards) > self.highest_total:
            self.highest_total = len(self.all_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
