from forex_python.converter import CurrencyRates


def currency_data():
    c = CurrencyRates()
    return c.get_rate('USD', 'PLN')


# FUTURE UPGRADE FOR 3 WAY BETS
def calculator(bets=None, first=True, a=0, b=0):
    position = 0
    position2 = 0

    if bets is not None:
        for i, bet in zip(range(len(bets)), bets):
            if bet["bookmaker_id"] == 23:
                position = i
            elif bet["bookmaker_id"] == 10:
                position2 = i

    bet1 = bets[position]
    bet2 = bets[position2]

    if first and bet1["koef"] <= 4 and bets is not None:
        a = 100
        b = round(((a * bet1["koef"]) / bet2["koef"]) / currency_data(), 1)
        amount = [a, b]
        return amount
    elif first and 5 >= bet1["koef"] > 4 and bets is not None:
        a = 30
        b = round(((a * bet1["koef"]) / bet2["koef"]) / currency_data(), 1)
        amount = [a, b]
        return amount
    elif first and 6 >= bet1["koef"] > 5 and bets is not None:
        a = 20
        b = round(((a * bet1["koef"]) / bet2["koef"]) / currency_data(), 1)
        amount = [a, b]
        return amount
    elif first and 10 >= bet1["koef"] > 6 and bets is not None:
        a = 10
        b = round(((a * bet1["koef"]) / bet2["koef"]) / currency_data(), 1)
        amount = [a, b]
        return amount
    elif first and 30 >= bet1["koef"] > 10 and bets is not None:
        a = 5
        b = round(((a * bet1["koef"]) / bet2["koef"]) / currency_data(), 1)
        amount = [a, b]
        return amount
    elif first and bet1["koef"] > 30 and bets is not None:
        a = 1
        b = round(((a * bet1["koef"]) / bet2["koef"]) / currency_data(), 1)
        amount = [a, b]
        return amount
    elif not first and bets is not None:
        b = round(((a * bet1["koef"]) / bet2["koef"]) / currency_data(), 1)
        amount = [a, b]
        return amount


# def switch_bad_book_position(book, bets, i):
#     if book == 23:
#         return bad_book_position(book, bets)
#     else:
#         return i
#
#
# # Future Upgrade for 3 way bets
# def bad_book_position(book, bets):
#     for i, bet in zip(range(len(bets)), bets):
#         if bet["bookmaker_id"] == book:
#             return i



# 1$ = 3.79 zl
#
# BAH 2.2 = 200zl
# 365 2.5 = x$
#
# 200x2.2/2.5/3.79=46.4

# 1BAH 3.1
# 2BAH 2.5
# BET365 4

# 2bah = 2.5x100 = 250
# 1bah = 2bah / 3.1 = 80.65
# Bet365 = 2bah / 4 / kurs3.79 = 16.5
