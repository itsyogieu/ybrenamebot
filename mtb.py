from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class mtb(object):
  
  START_TXT = """
  
<b>Hello {},π

=>I Can Rename Files With Permanant Thumbnail Support π₯

=>I Can Convert Files Too π

Use help Button For More Details

π§¨Devoloped & Maintained By : : <a href='https://bit.ly/3gwsct3'>β―Β°β’ Yogesh R β’Β°β―</a></b>\n
  """
  HELP_TXT = """
  
  **Hey πββοΈIt's Not Complicated To Use Me.

β© Send Me A Image To Save It As Custom Thumbnail permanently [ Optional ]

β© Then Send Me Your File Or Video Which You Want To Rename. 

β© Reply With File That File /rename [ Custom File Name ]

β© Then Wait For Sometime Until Bot Renames & Upload It..!! 

<\ Available Commands />
β’ /start - π Start Message
β’ /rename - πRename Telegram Files
β’ /showthumb - π To Saved Custom Permanent thumbnail
β’ /delthumb - β  Clears Saved Custom Thumbnail To Default

πPowerded By : @YogeshBots**
"""
  
  ABOUT_TXT = """
  
<b>πMy Name : <a href='https://t.me/YBRenameBot'>YB Rename Bot</a></b>\n
<b>π©βπ¦½Version : <a href='https://t.me/YBRenameBot'>0.9.2 beta</a></b>\n
<b>βSubscribe : <a href='https://bit.ly/3y3Ej6u'>Click Here</a></b>\n
<b>βοΈServer : <a href='https://heroku.com'>Heroku</a></b>\n
<b>π‘Library : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>\n
<b>πͺLanguage : <a href='https://www.python.org'>Python 3.9.4</a></b>\n
<b>πDeveloper : <a href='https://bit.ly/3gwsct3'>β―Β°β’ Yogesh R β’Β°β―</a></b>\n
<b>πChannel : <a href='https://t.me/YogeshBots'>π¬πΌπ΄π²ππ΅ ππΌππ</a></b>\n
"""
  
  START_BUTTONS = InlineKeyboardMarkup(
    [[
      InlineKeyboardButton("π¦π» π΄π π­πππππ", url="https://t.me/YogeshBots"),
      InlineKeyboardButton("βοΈ π―πππ", callback_data="help")
     ],[
      InlineKeyboardButton("π¨ππππ π", callback_data="about"),
      InlineKeyboardButton("πͺππππ π", callback_data="close")
    ]]
    )
      
  HELP_BUTTONS = InlineKeyboardMarkup(
    [[
      InlineKeyboardButton("π π©πππ", callback_data="home"),
      InlineKeyboardButton("πͺππππ π", callback_data="close")
    ]]
    )
  
  ABOUT_BUTTONS = InlineKeyboardMarkup(
    [[
      InlineKeyboardButton("π π©πππ", callback_data="home"),
      InlineKeyboardButton("πͺππππ π", callback_data="close")
    ]]
    )
  
