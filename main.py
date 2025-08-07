
from telegram import Update
from telegram.ext import ApplicationBuilder, ChatMemberHandler, ContextTypes

TOKEN = "8099175254:AAGy9fULXMLNAz-eaMovLwv6Vmv8n2Tatq0"  # توکن رباتت
GROUP_ID = -1002383622279  # آیدی گروهت

async def kick_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    member_status = update.chat_member
    if member_status.new_chat_member.status == "member":
        await context.bot.ban_chat_member(chat_id=GROUP_ID, user_id=member_status.new_chat_member.user.id, until_date=0)
        await context.bot.unban_chat_member(chat_id=GROUP_ID, user_id=member_status.new_chat_member.user.id)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(ChatMemberHandler(kick_user, ChatMemberHandler.CHAT_MEMBER))
    app.run_polling()
