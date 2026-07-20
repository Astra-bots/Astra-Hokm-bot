class Score:


    def __init__(self):

        self.player = 0

        self.bot = 0





    def add_win(self, winner):


        if winner == "Player":

            self.player += 1


        elif winner == "Bot":

            self.bot += 1






    def get_score(self):

        return {

            "Player": self.player,

            "Bot": self.bot

        }







    def check_game_winner(self):


        if self.player >= 5:

            return "Player"



        if self.bot >= 5:

            return "Bot"



        return None
