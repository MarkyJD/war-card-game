from Deck import Deck
from Player import Player
from Card import Card
import sys
from results import print_game_results

# Default WAR amount
war_amount = 3

# Default games
games = 1
game_on = True
results = []

# Accecpt CLI arguments to set war amount and optionally how many games are played
if len(sys.argv) == 2:
    # Ensure only numbers are entered and catch any TypeError
    try:
        war_amount = int(sys.argv[1])
    except:
        pass
elif len(sys.argv) == 3:
    # Ensure only numbers are entered and catch any TypeError
    try:
        games = int(sys.argv[2])
    except:
        pass


for game_number in range(games):

    game_on = True
    # Setup new game
    player_one = Player('p1')
    player_two = Player('p2')

    player_one_won = False
    player_two_won = False

    # Create deck
    deck = Deck()
    deck.shuffle()

    # Deal cards out
    for i in range(26):
        player_one.add_cards(deck.deal_one())
        player_two.add_cards(deck.deal_one())

    # Track game stats
    round_num = 0
    war_counter = 0
    total_war_counter = 0
    war_longest = 0

    while game_on:

        round_num += 1

        if war_counter > war_longest:
            war_longest = war_counter

        war_counter = 0

        if len(player_one.all_cards) == 0:
            # Player 2 Wins
            player_two_won = True
            game_on = False
            break

        if len(player_two.all_cards) == 0:
            # Player 1 Wins
            player_one_won = True
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

                total_war_counter += 1

                if len(player_one.all_cards) < war_amount:

                    player_two_won = True
                    game_on = False
                    break

                elif len(player_two.all_cards) < war_amount:

                    player_one_won = True
                    game_on = False
                    break

                else:
                    war_counter += 1
                    for num in range(war_amount):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())

    if player_one_won:
        winning_player = player_one
    elif player_two_won:
        winning_player = player_two

    game_result = []
    game_result.append(game_number + 1)
    game_result.append(winning_player.name)
    game_result.append(round_num)
    game_result.append(total_war_counter)
    game_result.append(war_longest)
    game_result.append(player_one.highest_total)
    game_result.append(player_one.lowest_total)
    game_result.append(player_two.highest_total)
    game_result.append(player_two.lowest_total)

    # Append the game result to the list of results
    results.append(game_result)

# Print results
print_game_results(results)
