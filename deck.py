import random

from cards import create_deck



def shuffle_deck(deck):

    random.shuffle(deck)

    return deck





def create_shuffled_deck():

    deck = create_deck()

    shuffle_deck(deck)

    return deck





def deal_cards(deck, amount):

    cards = []


    for _ in range(amount):

        if len(deck) > 0:

            cards.append(
                deck.pop()
            )


    return cards





def create_hokm_hands():

    deck = create_shuffled_deck()


    player_hand = deal_cards(
        deck,
        13
    )


    bot_hand = deal_cards(
        deck,
        13
    )


    return {

        "deck": deck,

        "player": player_hand,

        "bot": bot_hand

    }
