SUITS = [
    "♥️",
    "♦️",
    "♣️",
    "♠️"
]


RANKS = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
    "A"
]


CARD_POWER = {

    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14

}





def create_card(suit, rank):

    return {

        "suit": suit,

        "rank": rank,

        "power": CARD_POWER[rank]

    }






def create_deck():

    deck = []


    for suit in SUITS:

        for rank in RANKS:

            deck.append(
                create_card(
                    suit,
                    rank
                )
            )


    return deck






def card_name(card):

    return (
        f"{card['suit']} {card['rank']}"
    )






def compare_cards(card1, card2, hokm):


    # اگر کارت دوم حکم باشد
    if card2["suit"] == hokm and card1["suit"] != hokm:

        return card2



    # اگر کارت اول حکم باشد
    if card1["suit"] == hokm and card2["suit"] != hokm:

        return card1



    # اگر خال یکی نباشد
    if card1["suit"] != card2["suit"]:

        return card2



    # مقایسه قدرت
    if card1["power"] > card2["power"]:

        return card1

    else:

        return card2
