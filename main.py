from telegram.ext import Updater, MessageHandler, Filters
import os

TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID"))

def kick_user(update, context):
    if update.message.chat.id == GROUP_ID:
        user_id = update.message.from_user.id
        context.bot.kick_chat_member(GROUP_ID, user_id)
        context.bot.unban_chat_member(GROUP_ID, user_id)

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, kick_user))

updater.start_polling()
updater.idle()
