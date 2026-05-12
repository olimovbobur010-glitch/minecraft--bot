import telebot
from telebot import types

TOKEN = "8678284593:AAGZZKEuqSY9pe9apvHgo-0DAE8gp0fokcM"

bot = telebot.TeleBot(TOKEN)

users = []
KANAL = "@DrayVox_Chanel"

# START
@bot.message_handler(commands=['start'])
def start(message):

    user_id = message.from_user.id

    try:
        check = bot.get_chat_member(KANAL, user_id)

        if check.status == "left":

            join = types.InlineKeyboardMarkup()

            btn1 = types.InlineKeyboardButton(
                "📢 Kanalga Obuna",
                url="https://t.me/DrayVox_Chanel"
            )

            btn2 = types.InlineKeyboardButton(
                "✅ Tekshirish",
                callback_data="check_sub"
            )

            join.add(btn1)
            join.add(btn2)

            bot.send_message(
                message.chat.id,
                "❌ Botdan foydalanish uchun kanalga obuna bo‘ling.",
                reply_markup=join
            )
            return

    except:
        pass

    if message.chat.id not in users:
        users.append(message.chat.id)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("👾 Moblar")
    btn2 = types.KeyboardButton("⛏ Rudalar")

    btn3 = types.KeyboardButton("🐉 Bosslar")
    btn4 = types.KeyboardButton("🌍 Sirli Faktlar")

    btn5 = types.KeyboardButton("⚡ Survival")
    btn6 = types.KeyboardButton("📦 Secret Itemlar")

    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5, btn6)

    bot.send_message(
        message.chat.id,
        """🔥 Minecraft Ultimate Secret Bot 🔥

👾 Maxfiy moblar
⛏ Rudalar haqida sirlar
🐉 Bosslar
🌍 Hech kim bilmaydigan faktlar
⚡ Survival pro maslahatlar
📦 Secret itemlar

Kerakli bo‘limni tanlang 👇""",
        reply_markup=markup
    )

# KANAL TEKSHIRISH
@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "check_sub":

        user_id = call.from_user.id

        try:
            check = bot.get_chat_member(KANAL, user_id)

            if check.status != "left":

                bot.answer_callback_query(
                    call.id,
                    "✅ Obuna tasdiqlandi"
                )

                start(call.message)

            else:

                bot.answer_callback_query(
                    call.id,
                    "❌ Hali obuna bo‘lmadingiz"
                )

        except:
            pass

# HAMMAGA YUBORISH
@bot.message_handler(commands=['send'])
def send_all(message):

    admin_id = 6006856306

    if message.from_user.id != admin_id:
        return

    text = message.text.replace("/send ", "")

    for user in users:

        try:
            bot.send_message(
                user,
                f"📢 Yangilik:\n\n{text}"
            )

        except:
            pass

# MOB MENU
@bot.message_handler(func=lambda message: message.text == "👾 Moblar")
def mob_menu(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    b1 = types.KeyboardButton("👁 Enderman")
    b2 = types.KeyboardButton("💥 Creeper")

    b3 = types.KeyboardButton("🛑 Warden")
    b4 = types.KeyboardButton("🐷 Piglin")

    b5 = types.KeyboardButton("💀 Wither Skeleton")
    b6 = types.KeyboardButton("🕷 Cave Spider")

    back = types.KeyboardButton("⬅️ Orqaga")

    markup.add(b1, b2)
    markup.add(b3, b4)
    markup.add(b5, b6)
    markup.add(back)

    bot.send_message(
        message.chat.id,
        "👾 Moblardan birini tanlang:",
        reply_markup=markup
    )

# ORQAGA
@bot.message_handler(func=lambda message: message.text == "⬅️ Orqaga")
def back(message):
    start(message)

# JAVOBLAR
@bot.message_handler(func=lambda message: True)
def answer(message):

    text = message.text

    # ENDERMAN
    if text == "👁 Enderman":

        bot.send_message(
            message.chat.id,

"""👁 ENDERMAN SIRLARI 👁

🔥 Endermanlar originally "Farlander" deb nomlangan.

🌧 Yomg‘ir ularga zarar beradi.

👀 Ko‘ziga qarasangiz agressiv bo‘ladi.

📦 Ular bloklarni ko‘tarib yurishi mumkin.

🌌 End dimensionidagi Endermanlar oddiy dunyodagidan ko‘proq spawn bo‘ladi.

💡 Secret:
Agar boshingizga pumpkin kiysangiz Enderman sizga hujum qilmaydi.
"""
        )

    # CREEPER
    elif text == "💥 Creeper":

        bot.send_message(
            message.chat.id,

"""💥 CREEPER SIRLARI 💥

🐷 Creeper cho‘chqa modeli bugidan yaralgan.

⚡ Chaqmoq urganda Charged Creeperga aylanadi.

💀 Charged Creeper boshqa mob boshlarini tushira oladi.

🎵 Skeleton Creeperni o‘ldirsa music disk tushadi.

🔥 Creeperlar mushuklardan qo‘rqadi.

💡 Secret:
Shield ishlatsangiz Creeper damage deyarli qilolmaydi.
"""
        )

    # WARDEN
    elif text == "🛑 Warden":

        bot.send_message(
            message.chat.id,

"""🛑 WARDEN SIRLARI 🛑

🔥 Minecraftdagi eng kuchli moblardan biri.

👂 U tovush orqali topadi.

💀 Full Netherite armorni ham tez o‘ldira oladi.

🌑 Ancient Cityda spawn bo‘ladi.

⚡ Sonic Boom devor orqali ham uradi.

💡 Secret:
Snowball otib Wardenni chalg‘itish mumkin.
"""
        )

    # PIGLIN
    elif text == "🐷 Piglin":

        bot.send_message(
            message.chat.id,

"""🐷 PIGLIN SIRLARI 🐷

💰 Oltinni yaxshi ko‘radi.

🪙 Gold bersangiz barter qiladi.

⚔ Gold armor kiymasangiz hujum qiladi.

🔥 Soul Fire yonida raqs tushadi.

🌍 Netherda yashaydi.

💡 Secret:
Piglinlardan Ender Pearl olish mumkin.
"""
        )

    # WITHER
    elif text == "💀 Wither Skeleton":

        bot.send_message(
            message.chat.id,

"""💀 WITHER SKELETON 💀

☠ Wither effect beradi.

🔥 Nether Fortressda spawn bo‘ladi.

🗡 Tosh sword ushlab yuradi.

🎯 Boshi juda noyob tushadi.

🐷 Piglinlar ularga hujum qilmaydi.

💡 Secret:
Looting III bosh tushish imkonini oshiradi.
"""
        )

    # SPIDER
    elif text == "🕷 Cave Spider":

        bot.send_message(
            message.chat.id,

"""🕷 CAVE SPIDER 🕷

☠ Zaharlaydi.

⛏ Mineshaft ichida spawn bo‘ladi.

📏 Oddiy spiderdan kichikroq.

🌑 Kichik joylardan ham o‘ta oladi.

🔥 Fire Aspect zaharni to‘xtatmaydi.

💡 Secret:
Milk ichsangiz zahar ketadi.
"""
        )

    # RUDALAR
    elif text == "⛏ Rudalar":

        bot.send_message(
            message.chat.id,

"""⛏ RUDALAR ⛏

💎 Diamond:
Eng yaxshi qatlam Y=-59

🔥 Ancient Debris:
Y=15 eng yaxshi joy.

🟢 Emerald:
Faqat tog‘ biomida ko‘p.

⚡ Redstone:
XP uchun yaxshi.

💡 Secret:
2x1 tunnel usuli eng tez qazish usuli.
"""
        )

    # BOSSLAR
    elif text == "🐉 Bosslar":

        bot.send_message(
            message.chat.id,

"""🐉 BOSSLAR 🐉

👑 Ender Dragon
☠ Wither
🛑 Warden

💡 Secret:
Witherni bedrock ostida qamash mumkin.
"""
        )

    # FAKTLAR
    elif text == "🌍 Sirli Faktlar":

        bot.send_message(
            message.chat.id,

"""🌍 SIRLI FAKTLAR 🌍

🌕 Minecraftdagi oy kvadrat.

🐄 Mooshroom eng noyob moblardan biri.

🔥 Netherda suv ishlamaydi.

⚡ Charged Creeper juda noyob.

💡 Secret:
Torch gravelni tez tushiradi.
"""
        )

    # SURVIVAL
    elif text == "⚡ Survival":

        bot.send_message(
            message.chat.id,

"""⚡ SURVIVAL SIRLAR ⚡

🛡 Shield birinchi kecha juda muhim.

💎 Fortune III diamondni ko‘paytiradi.

🌋 Lava pool orqali tez Nether portal qilinadi.

🍖 Cooked food ko‘proq hunger to‘ldiradi.

💡 Secret:
Water bucket clutch yiqilishdan saqlaydi.
"""
        )

    # ITEMS
    elif text == "📦 Secret Itemlar":

        bot.send_message(
            message.chat.id,

"""📦 SECRET ITEMLAR 📦

🟪 Command Block
🟩 Barrier Block
⚡ Light Block
🔥 Structure Block

💡 Secret:
Barrier block ko‘rinmaydi.
"""
        )

# BOT INFO
bot.set_my_description(
    "🔥 Minecraft Ultimate Secret Bot\n\n"
    "👾 Maxfiy moblar\n"
    "⛏ Rudalar\n"
    "🐉 Bosslar\n"
    "🌍 Sirli faktlar\n"
    "⚡ Survival maslahatlar\n"
    "📦 Secret itemlar"
)

print("🔥 Minecraft Ultimate Secret Bot ishladi 🔥")

bot.infinity_polling()
