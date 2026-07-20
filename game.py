from deck import create_hokm_hands
from player import Player
from cards import compare_cards
from score import Score



class HokmGame:


    def __init__(self):

        self.player = Player("Player")

        self.bot = Player("Bot")


        self.score = Score()


        self.hokm = None


        self.current_turn = "Player"


        self.round_cards = []


        self.started = False






    def start(self):


        hands = create_hokm_hands()


        self.player.add_cards(
            hands["player"]
        )


        self.bot.add_cards(
            hands["bot"]
        )


        self.started = True







    def choose_hokm(self, suit):

        self.hokm = suit







    def play_card(self, player, index):


        card = player.remove_card(index)


        self.round_cards.append(

            {
                "player": player.name,

                "card": card
            }

        )


        return card







    def finish_round(self):


        first = self.round_cards[0]

        second = self.round_cards[1]



        winner_card = compare_cards(

            first["card"],

            second["card"],

            self.hokm

        )



        if winner_card == first["card"]:

            winner = first["player"]

        else:

            winner = second["player"]




        self.score.add_win(winner)



        self.round_cards.clear()



        self.current_turn = winner



        return winner








    def can_continue(self):


        if self.score.check_game_winner():

            return False


        return True







    def winner(self):


        return self.score.check_game_winner()
