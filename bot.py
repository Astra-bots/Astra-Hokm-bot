import os

from dotenv import load_dotenv

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)


from game import HokmGame
from ai import HokmAI
from cards import card_name



load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


games = {}





def suit_keyboard():

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "♥️ دل",
                    callback_data="hokm_♥️"
                ),

                InlineKeyboardButton(
                    "♦️ خشت",
                    callback_data="hokm_♦️"
                )
            ],
            [
                InlineKeyboardButton(
                    "♣️ گشنیز",
                    callback_data="hokm_♣️"
                ),

                InlineKeyboardButton(
                    "♠️ پیک",
                    callback_data="hokm_♠️"
                )
            ]
        ]
    )





def cards_keyboard(game):

    keyboard = []


    for index, card in enumerate(game.player.hand):

        keyboard.append(

            [
                InlineKeyboardButton(

                    card_name(card),

                    callback_data=f"card_{index}"

                )
            ]

        )


    return InlineKeyboardMarkup(keyboard)







async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):


    user_id = update.effective_user.id


    game = HokmGame()

    game.start()


    games[user_id] = game



    await update.message.reply_text(

        "🃏 Astra Hokm شروع شد!\n\n"
        "حکم را انتخاب کن:",

        reply_markup=suit_keyboard()

    )








async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):


    query = update.callback_query

    await query.answer()


    user_id = query.from_user.id


    if user_id not in games:

        return



    game = games[user_id]


    data = query.data





    # انتخاب حکم

    if data.startswith("hokm_"):


        suit = data.replace(
            "hokm_",
            ""
        )


        game.choose_hokm(suit)


        await query.edit_message_text(

            "✅ حکم انتخاب شد\n\n"
            "کارت خودت را بازی کن:",

            reply_markup=cards_keyboard(game)

        )


        return






    # بازی کارت

    if data.startswith("card_"):


        index = int(

            data.split("_")[1]

        )



        player_card = game.play_card(

            game.player,

            index

        )



        bot_ai = HokmAI(

            game.bot

        )


        bot_index = bot_ai.choose_card(

            player_card,

            game.hokm

        )



        game.play_card(

            game.bot,

            bot_index

        )



        winner = game.finish_round()



        score = game.score.get_score()



        if not game.can_continue():


            final = game.winner()


            await query.edit_message_text(

                f"🏆 برنده نهایی: {final}\n\n"
                f"امتیاز:\n"
                f"Player: {score['Player']}\n"
                f"Bot: {score['Bot']}"

            )

            return




        await query.edit_message_text(

            f"🎴 برنده این دست: {winner}\n\n"
            f"امتیاز:\n"
            f"Player: {score['Player']}\n"
            f"Bot: {score['Bot']}\n\n"
            "کارت انتخاب کن:",

            reply_markup=cards_keyboard(game)

        )








def main():


    app = Application.builder().token(TOKEN).build()



    app.add_handler(

        CommandHandler(
            "start",
            start
        )

    )


    app.add_handler(

        CallbackQueryHandler(play)

    )



    print("Astra Hokm Started 🃏")



    app.run_polling()






if __name__ == "__main__":

    main()
