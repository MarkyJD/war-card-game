from Deck import Deck
from Player import Player
from Card import Card
import sys

# Game Setup
player_one = Player('p1')
player_two = Player('p2')

deck = Deck()
deck.shuffle()

# Deal cards out
for i in range(26):
    player_one.add_cards(deck.deal_one())
    player_two.add_cards(deck.deal_one())

game_on = True
round_num = 0

war_amount = 3

if len(sys.argv) > 1:
    try:
        war_amount = int(sys.argv[1])
    except:
        pass


while game_on:
    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.all_cards) == 0:
        print('Player 1 is out of cards! Player 2 wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player 1 is out of cards! Player 2 wins!')
        game_on = False
        break

    # Start round:
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # While at war
    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:

            print('WAR!')
            if len(player_one.all_cards) < war_amount:
                print('Player 1 unable to go to war!')
                print('Player 2 Wins!')
                game_on = False
                break

            elif len(player_two.all_cards) < war_amount:
                print('Player 2 unable to go to war!')
                print('Player 1 Wins!')
                game_on = False
                break

            else:
                for num in range(war_amount):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

print(war_amount)
