from telegram.ext import Updater, CommandHandler


def start(update, context):

    update.message.reply_text('Hola, humanooooo!')


if __name__ == '__main__':

    updater = Updater(token='5336611309:AAHuqXhLcg52yEfZdDEMCNOO7ZQhh5pVFpQ', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start',start))

    updater.start_polling()
    updater.idle()
