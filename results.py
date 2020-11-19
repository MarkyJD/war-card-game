from tabulate import tabulate
import math


def print_game_results(results):
    print("\n" + tabulate(results, headers=["Game", "Winner", "Rounds", "Wars",
                                            "Longest War", "P1 most cards", "P1 least cards", "P2 most cards", "P2 least cards"]))
    print("------------------------------------------------------------------------------------------------------------------------")

    games_played = len(results)
    p1_wins = 0
    p2_wins = 0
    total_rounds = 0
    total_wars = 0
    average_war_length = 0

    for game in results:

        if game[1] == "p1":
            p1_wins += 1
        else:
            p2_wins += 1

        total_rounds += game[2]
        total_wars += game[3]
        average_war_length += game[4]

    if p1_wins > p2_wins:
        overall_winner = 'p1'
        win_percentage = p1_wins / games_played * 100
    elif p2_wins > p1_wins:
        overall_winner = 'p2'
        win_percentage = p2_wins / games_played * 100
    else:
        overall_winner = 'tie'
        win_percentage = 50

    winner = overall_winner + " (" + str(win_percentage) + "% win-rate)"

    average_rounds = round(total_rounds / games_played)
    average_wars = round(total_wars / games_played)
    average_war_length = round(average_war_length / games_played)

    print("Averages:\n")
    print("Overall Winner:     {:<10}\nAverage Rounds:     {:<10}\nAverage Wars:       {:<10}\nAverage War Length: {:<10}\n".format(
        winner, average_rounds, average_wars, average_war_length))
