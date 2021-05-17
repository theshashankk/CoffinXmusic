# (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""ＹＯＯ!! 🤟\n there! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\n🔴 Do you want me to play music in your Telegram groups'voice chats? Please click the \'📜 User Manual 📜\' button below to know how you can use me.\n\n🔴 The Assistant must be in your group to play music in the voice chat of your group.\n\n🔴 More info & commands mentioned in the [User Manual](https://telegra.ph/Daisy-X-04-19)\n\nPowered By CoffinXmusic""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜 User Manual 📜", url="https://telegra.ph/Daisy-X-04-19"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👨‍💻 Updates 👨‍💻", url="https://t.me/CoffinX_updates"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Support Chat 🎙️", url="https://t.me/Coffinxsupport"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Take me to your group" url="https://t.me/CoffinXmusic_bot?start"
                     )
                  ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        """**🔴 Music player is online**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙️ Support Group 🎙️", url="https://t.me/CoffinX_Updates"
                    )
                ]
            ]
        ),
    )

    @Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '▶️', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = "https://t.me/coffinX_updates"
        button = [
            [InlineKeyboardButton(text = '📲 Channel', url="https://t.me/CoffinX_Updates"),
             InlineKeyboardButton(text = '💬 Group', url="https://t.me/Coffinxsupport")],
            [InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '▶️', callback_data = f"help+{pos+1}")
            ],
        ]
    return button
