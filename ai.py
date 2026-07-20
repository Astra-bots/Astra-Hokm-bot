from cards import compare_cards





class HokmAI:


    def __init__(self, player):

        self.player = player






    def choose_card(self, current_card, hokm):


        hand = self.player.hand



        # اگر اولین نفر است
        if current_card is None:


            return self.lowest_card_index()






        playable = self.get_playable_cards(

            current_card["suit"]

        )



        # اگر کارت قابل بازی ندارد
        if not playable:

            return self.lowest_card_index()





        # پیدا کردن کارت‌هایی که می‌توانند ببرند

        winning = []



        for index, card in playable:


            winner = compare_cards(

                current_card,

                card,

                hokm

            )


            if winner == card:

                winning.append(

                    (index, card)

                )





        # اگر می‌تواند ببرد
        if winning:


            winning.sort(

                key=lambda x: x[1]["power"]

            )


            return winning[0][0]





        # اگر نمی‌تواند ببرد
        playable.sort(

            key=lambda x: x[1]["power"]

        )


        return playable[0][0]








    def get_playable_cards(self, suit):


        result = []


        has_suit = any(

            card["suit"] == suit

            for card in self.player.hand

        )



        for index, card in enumerate(self.player.hand):


            if has_suit:


                if card["suit"] == suit:

                    result.append(

                        (index, card)

                    )


            else:

                result.append(

                    (index, card)

                )



        return result






    def lowest_card_index(self):


        lowest = min(

            enumerate(self.player.hand),

            key=lambda x: x[1]["power"]

        )


        return lowest[0]
