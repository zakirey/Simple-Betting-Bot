import json

file = open("arb_backup.txt", 'r')
ARB_ID = json.loads(file.readline())
file.close()


def bet_at_home_link(bet, limiter):
    if bet["koef"] >= 1.7 and limiter:
        odd_id = bet["direct_link"]
        link = "https://affiliates.bet-at-home.com/processing/clickthrgh.asp?btag=a_74417b_23447&lang=EN&oddid={0}". \
            format(odd_id)
        return link
    elif not limiter:
        odd_id = bet["direct_link"]
        link = "https://affiliates.bet-at-home.com/processing/clickthrgh.asp?btag=a_74417b_23447&lang=EN&oddid={0}". \
            format(odd_id)
        return link
    else:
        return "Bad_game"


def bet_365_link(bet, limiter):
    odd_id = str(bet["direct_link"]).split("|")
    koef = str(bet["koef"])
    bookmaker_event_id = str(bet["bookmaker_event_direct_link"])
    link = "https://www.bet365.com/dl/sportsbookredirect?bs={0}-{1}~{2}&bet=1#{3}".format(odd_id[2], odd_id[0], koef,
                                                                                          bookmaker_event_id)
    return link


def arbs(x):
    # Loading response data and converting it to Dictionary.
    json_bet = json.dumps(x)
    # print(json_bet)
    obj_bet = json.loads(json_bet)
    obj_bet_again = json.loads(obj_bet)

    for event in obj_bet_again["arbs"]:

        links = []
        bets = []
        books = []

        arb_id = str(event["id"])

        if len(ARB_ID) == 0:
            print("First game")
        elif arb_id in ARB_ID:
            print("This game was already used")
            continue

        bet1_id = str(event["bet1_id"])
        bet2_id = str(event["bet2_id"])
        bet3_id = str(event["bet3_id"])
        percent = event["percent"]
        limiter = True

        if percent > 1:
            limiter = False

        first = True

        for bet in obj_bet_again["bets"]:
            if (bet["id"] == bet1_id) or (bet["id"] == bet2_id) or ((bet3_id != "null") and (bet["id"] == bet3_id)):
                if first:
                    book1 = bet["bookmaker_id"]
                    books.append(book1)
                    bets.append(bet)
                    first = False
                elif not first:
                    book2 = bet["bookmaker_id"]
                    books.append(book2)
                    bets.append(bet)
                elif (bet3_id != "null") and (bet["id"] == bet3_id):
                    book3 = bet["bookmaker_id"]
                    books.append(book3)
                    bets.append(bet)

        for book, bet in zip(books, bets):
            # print(book)
            # print(bet)
            link = bookmaker_links(book, bet, limiter)
            if link != "No Link found":
                links.append(link)
            else:
                continue
        ARB_ID.append(str(arb_id))
        savefile = open("arb_backup.txt", 'w')
        savefile.write(json.dumps(ARB_ID))
        savefile.close()
        return links, bets, books


def bookmaker_links(book, bet, limiter):
    if book == 10:
        return bet_365_link(bet, limiter)
    elif book == 23:
        return bet_at_home_link(bet, limiter)

# 'https://www.bet365.com/dl/sportsbookredirect?bs=95198485-1165361414~1.65&bet=1#/AC/B1/C1/D8'
# '/E95198485/F3/'

# https://affiliates.bet-at-home.com/processing/clickthrgh.asp?btag=a_74417b_23447&lang=EN&oddid=


# Bet365
# https://www.bet365.com/dl/sportsbookredirect?bs=94985302-1149248377~2.63&bet=1#/AC/B91/C20717648/D19/E10564558/F19/
# https://www.bet365.com/dl/sportsbookredirect?bs=95198485-1165361414~1.65&bet=1#/AC/B1/C1/D8/E95198485/F3/
