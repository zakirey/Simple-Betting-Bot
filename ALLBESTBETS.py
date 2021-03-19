import json
from time import sleep
from random import uniform
from src.BetCalculator import calculator
from src.ArbsReader import arbs
from src.OpenBookmakers import bet_at_home, bet_365
from src.BetPlacer import bookmaker_bots
from src.ApiRequest import opt_api


TOKEN_API = 'f9dd70ced84c9e3ac2081fba68bcfd12'


def mygen(arr, start_index):
    for i in range(start_index, len(arr)):
        yield arr[i]
    for i in range(start_index):
        yield arr[i]


def user():
    b1 = bet_365('cyb3ria', 'MolodostVseProstit228')
    # b2 = bet_at_home('reginasklyarova@gmail.com', 'MolodostVseProstit22')
    #
    # bookmakers = {10: b1[0], 23: b2[0]}
    # capital_bet_at_home = b2[1]
    # capital_bet_365 = b1[1]
    #
    k = input("Give Start Command:")
    while k != "go":
        k = input("Again")
    #
    # search = {"football": 420809}
    # x = opt_api(TOKEN_API, search["football"])
    #
    # y = json.loads(x.text)
    # while y["total_by_filter"] == 0:
    #     print("No Games for selected filter")
    #     x = opt_api(TOKEN_API, search["football"])
    #     y = json.loads(x.text)
    #
    # while y["total_by_filter"] != 0:
    #     arb = arbs(x.text)
    #
    #     if not all(arb):
    #         sleep(uniform(30, 60))
    #         x = opt_api(TOKEN_API, search["football"])
    #         y = json.loads(x.text)
    #         continue
    #
    #     links = arb[0]
    #     bets = arb[1]
    #     books = arb[2]
    #     amounts = []
    #     bad_game = False
    #
    #     for link in links:
    #         if link == "Bad_game":
    #             bad_game = True
    #
    #     while not bad_game:
    #         # Future upgrade for 3 way bets
    #         if len(bets) == 2:
    #             amounts = calculator(bets)
    #             if capital_bet_at_home - amounts[0] <= 0 or capital_bet_365 - amounts[1] <= 0:
    #                 print("You don't have enough capital on accounts")
    #                 exit()
    #         if len(links) >= 2:
    #             position = 0
    #             for i in range(0, len(books)):
    #                 if books[i] == 23:
    #                     position = i
    #             first = True
    #             for book, bet, link, amount in zip(mygen(books, position), mygen(bets, position),
    #                                                mygen(links, position), amounts):
    #                 success = bookmaker_bots(bookmakers[book], book, bet, link, amount)
    #                 if success[0] == 0:
    #                     print("Check your {0} bot, it have issues!".format(book))
    #                     break
    #                 elif first and success[0] == 1:
    #                     new_amount = calculator(bets, False, success[1])
    #                     amounts = [new_amount[0], new_amount[1]]
    #                     if capital_bet_at_home - amounts[0] <= 0 or capital_bet_365 - amounts[1] <= 0:
    #                         print("You don't have enough capital on accounts")
    #                         exit()
    #                     else:
    #                         capital_bet_365 = capital_bet_365 - amounts[1]
    #                         capital_bet_at_home = capital_bet_at_home - amounts[0]
    #                         first = False
    #                     continue
    #                 elif not first:
    #                     break
    #             bad_game = True
    #         else:
    #             print(links)
    #
    #     # sleep(uniform(30, 60))
    #     k = input("Give Start Command:")
    #     while k != "Go":
    #         k = input("Again")
    #     x = opt_api(TOKEN_API, search["football"])
    #     y = json.loads(x.text)


if __name__ == '__main__':
    user()
