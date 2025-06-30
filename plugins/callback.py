from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from Script import text
from config import ADMIN

@Client.on_callback_query()
async def callback_query_handler(client, query: CallbackQuery):
    if query.data == "start":
        tb = await bot.get_me()
        await query.message.edit_text(
            text.START.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ⇆', url=f"https://telegram.me/{tb.username}?startgroup=join_otherbots&admin=post_messages+edit_messages+delete_messages+restrict_members+invite_users+pin_messages+promote_members+manage_video_chats+manage_chat")],
                [InlineKeyboardButton('ℹ️ ᴀʙᴏᴜᴛ', callback_data='about'),
                 InlineKeyboardButton('🛠️ ʜᴇʟᴘ', callback_data='help')],
                [InlineKeyboardButton('⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ⇆', url=f"https://telegram.me/{tb.username}?startchannel=join_otherbots&admin=post_messages+edit_messages+delete_messages+restrict_members+invite_users+pin_messages+promote_members+manage_video_chats+manage_chat")]
            ])
        )

    elif query.data == "help":
        await query.message.edit_text(
            text.HELP.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('ᴜᴩᴅᴀᴛᴇꜱ', url='https://telegram.me/TgMaster_Bots'),
                 InlineKeyboardButton('ꜱᴜᴩᴩᴏʀᴛ', url='https://telegram.me/ImTgMaster')],
                [InlineKeyboardButton('ʙᴀᴄᴋ', callback_data="start"),
                 InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data="close")]
            ])
        )

    elif query.data == "about":
        await query.message.edit_text(
            text.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('💥 ʜᴇʟᴘ', callback_data='help'),
                 InlineKeyboardButton('👨‍💻 ᴏᴡɴᴇʀ', user_id=int(ADMIN))],
                [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="start"),
                 InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")]
            ])
        )

    elif query.data == "close":
        await query.message.delete()
