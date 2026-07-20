from cards import card_name





class Player:


    def __init__(self, name):

        self.name = name

        self.hand = []

        self.wins = 0






    def add_cards(self, cards):

        self.hand.extend(cards)







    def remove_card(self, index):

        return self.hand.pop(index)







    def get_card_names(self):

        return [
            card_name(card)
            for card in self.hand
        ]







    def has_suit(self, suit):

        for card in self.hand:

            if card["suit"] == suit:

                return True


        return False







    def playable_cards(self, current_suit):


        # اگر خال بازی شده را دارد
        if self.has_suit(current_suit):

            return [

                card

                for card in self.hand

                if card["suit"] == current_suit

            ]


        # اگر ندارد همه کارت‌ها آزادند

        return self.hand.copy()
