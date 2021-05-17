import os

class Messages():
      START_MSG = "**Yoo 🤟 [{}](tg://user?id={})!**\n\n🤖 I am an advanced bot created for playing music in the voice chats of Telegram Groups & Channels.\n\n✅ Send me /help for more info."
      HELP_MSG = [
        ".",
"""
**》 CoffinXmusic 《**
⚪️ DAISYXMUSIC plays music in your group's voice chat as well as channel voice chats
⚪️ Assistant name >> @CoffinXPlayer
""",

"""
**Setting up**
1) Make bot admin (Group and in channel if use cplay)
2) Start a voice chat
3) Try /play [song name] for the first time by an admin
*) If userbot joined enjoy music, If not add @CoffinXPlayer to your group and retry
**Commands**
**=>> Song Playing 🎧**
- /play: Play song using youtube music
- /play [yt url] : Play the given yt url
- /dplay: Play song via deezer
- /splay: Play song via jio saavn
**=>> Playback ⏯**
- /player: Open Settings menu of player
- /skip: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Stops media playback
- /current: Shows the current Playing track
- /playlist: Shows playlist
""",
        
"""
**=>> Channel Music Play 🛠**
⚪️ For linked group admins only:
- /cplay [song name] - play song you requested
- /cdplay [song name] - play song you requested via deezer
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat
channel is also can be used instead of c ( /cplay = /channelplay )
⚪️ If you donlt like to play in linked group:
1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add @DaisyXBot as Channel admin with full perms
4) Add @DaisyXhelper to the channel as an admin.
5) Simply send commands in your group.
""",

"""
**=>> More tools 🧑‍🔧**
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @CoffinXPlayer Userbot to your chat
*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
"""
      ]
