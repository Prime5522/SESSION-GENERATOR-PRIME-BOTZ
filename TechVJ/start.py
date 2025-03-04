from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import OWNER_ID, F_SUB
from TechVJ.db import db

@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot: Client, msg: Message):
    if not await db.is_user_exist(msg.from_user.id):
        await db.add_user(msg.from_user.id, msg.from_user.first_name)
    if F_SUB:
        try:
            await bot.get_chat_member(int(F_SUB), msg.from_user.id)
        except:
            try:
                invite_link = await bot.create_chat_invite_link(int(F_SUB))
            except:
                await msg.reply("**Make Sure I Am Admin In Your Channel**")
                return 
            key = InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("✇ Jᴏɪɴ Oᴜʀ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ✇", url=invite_link.invite_link),
                    InlineKeyboardButton("🍀 ʀᴇꜰʀᴇꜱʜ 🍀", callback_data="chk")
                ]]
            )
            await bot.send_photo(
                chat_id=msg.chat.id,
                photo="https://i.ibb.co.com/8nLtbXcs/IMG-20250304-184915-543.jpg",
                caption="**⚠️Access Denied!⚠️\n\nPlease Join My Update Channel To Use Me. If You Joined The Channel Then Click On Check Again Button To Confirm.**",
                reply_markup=key
            )
            return 

    me = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo="https://i.ibb.co.com/FRD1v1L/IMG-20250304-162149-080.jpg",
        caption=f"""<b>𝐇𝐞𝐲 {msg.from_user.mention}🍷,\n\nɪ ᴀᴍ {me},\nᴛʀᴜsᴛᴇᴅ 𝗦𝗧𝗥𝗜𝗡𝗚 𝗚𝗥𝗡𝗘𝗥𝗔𝗧𝗢𝗥 ʙᴏᴛ. ғᴜʟʟʏ sᴀғᴇ & sᴇᴄᴜʀᴇ.\nɴᴏ ᴀɴʏ ᴇʀʀᴏʀ\n\nMade With By : [VJ Botz](https://t.me/VJ_Botz) !</b>""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(text="ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ", callback_data="generate")
            ],[
                InlineKeyboardButton("🎬 ᴍᴏᴠɪᴇꜱ ᴄʜᴀɴɴᴇʟ 🎬", url="https://t.me/Prime_Movies4U"),
                InlineKeyboardButton("〆 ᴀʙᴏᴜᴛ 〆", callback_data="about")
            ],[
                InlineKeyboardButton("💬 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 💬", url="https://t.me/Prime_Botz_Support"),
                InlineKeyboardButton("〄 ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ 〄", url="https://t.me/Prime_Botz")
            ],[
                InlineKeyboardButton("✧ ᴄʀᴇᴀᴛᴏʀ ✧", url="https://t.me/Prime_Nayem")
            ]]
        )
    )

@Client.on_callback_query(filters.regex("chk"))
async def chk(bot: Client, cb: CallbackQuery):
    try:
        await bot.get_chat_member(int(F_SUB), cb.from_user.id)
    except:
        await cb.answer("🙅‍♂️ You are not joined my channel first join channel then check again. 🙅‍♂️", show_alert=True)
        return 
    me = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=cb.from_user.id,
        photo="https://i.ibb.co.com/FRD1v1L/IMG-20250304-162149-080.jpg",
        caption=f"""<b>𝐇𝐞𝐲 {cb.from_user.mention}🍷,\n\nɪ ᴀᴍ {me},\nᴛʀᴜsᴛᴇᴅ 𝗦𝗧𝗥𝗜𝗡𝗚 𝗚𝗥𝗡𝗘𝗥𝗔𝗧𝗢𝗥 ʙᴏᴛ. ғᴜʟʟʏ sᴀғᴇ & sᴇᴄᴜʀᴇ.\nɴᴏ ᴀɴʏ ᴇʀʀᴏʀ\n\nMade With By : [VJ Botz](https://t.me/VJ_Botz) !</b>""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(text="ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ", callback_data="generate")
            ],[
                InlineKeyboardButton("🎬 ᴍᴏᴠɪᴇꜱ ᴄʜᴀɴɴᴇʟ 🎬", url="https://t.me/Prime_Movies4U"),
                InlineKeyboardButton("〆 ᴀʙᴏᴜᴛ 〆", callback_data="about")
            ],[
                InlineKeyboardButton("💬 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 💬", url="https://t.me/Prime_Botz_Support"),
                InlineKeyboardButton("〄 ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ 〄", url="https://t.me/Prime_Botz")
            ],[
                InlineKeyboardButton("✧ ᴄʀᴇᴀᴛᴏʀ ✧", url="https://t.me/Prime_Nayem")
            ]]
        )
    )

@Client.on_callback_query(filters.regex("about"))
async def about_callback(bot: Client, cb: CallbackQuery):
    about_text = """<b><blockquote>⍟───[  <a href='https://t.me/Prime_Botz'>MY ᴅᴇᴛᴀɪʟꜱ ʙy ᴘʀɪᴍᴇ ʙᴏᴛz 🔥</a> ]───⍟</blockquote>
    
‣ ᴍʏ ɴᴀᴍᴇ : <a href='https://t.me/Prime_String_Generator_Bot'>sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ</a>
‣ ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ : <a href='tg://settings'>ᴛʜɪs ᴘᴇʀsᴏɴ</a> 
‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/Prime_Nayem'>ᴍʀ.ᴘʀɪᴍᴇ</a> 
‣ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Prime_Botz'>ᴘʀɪᴍᴇ ʙᴏᴛᴢ</a> 
‣ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Prime_Movies4U'>ᴘʀɪᴍᴇ ᴍᴏᴠɪᴇs</a> 
‣ ѕᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : <a href='https://t.me/Prime_Botz_Support'>ᴘʀɪᴍᴇ ʙᴏᴛᴢ ѕᴜᴘᴘᴏʀᴛ</a> 
‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a> 
‣ ʙᴏᴛ sᴇʀᴠᴇʀ : <a href='https://heroku.com'>ʜᴇʀᴏᴋᴜ</a> 
‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ2.7.1 [sᴛᴀʙʟᴇ]</b>"""

    await cb.message.edit_text(
        about_text,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back", callback_data="back_to_start")]
        ])
    )

@Client.on_callback_query(filters.regex("back_to_start"))
async def back_to_start(bot: Client, cb: CallbackQuery):
    me = (await bot.get_me()).mention
    await cb.message.edit_caption(
        caption=f"""<b>𝐇𝐞𝐲 {cb.from_user.mention}🍷,\n\nɪ ᴀᴍ {me},\nᴛʀᴜsᴛᴇᴅ 𝗦𝗧𝗥𝗜𝗡𝗚 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 ʙᴏᴛ. ғᴜʟʟʏ sᴀғᴇ & sᴇᴄᴜʀᴇ.\nɴᴏ ᴀɴʏ ᴇʀʀᴏʀ\n\nMade With By : [VJ Botz](https://t.me/VJ_Botz) !</b>""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("⚡ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ⚡", callback_data="generate")
            ],[
                InlineKeyboardButton("🎬 ᴍᴏᴠɪᴇꜱ ᴄʜᴀɴɴᴇʟ 🎬", url="https://t.me/Prime_Movies4U"),
                InlineKeyboardButton("〆 ᴀʙᴏᴜᴛ 〆", callback_data="about")
            ],[
                InlineKeyboardButton("💬 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 💬", url="https://t.me/Prime_Botz_Support"),
                InlineKeyboardButton("〄 ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ 〄", url="https://t.me/Prime_Botz")
            ],[
                InlineKeyboardButton("✧ ᴄʀᴇᴀᴛᴏʀ ✧", url="https://t.me/Prime_Nayem")
            ]]
        )
    )
