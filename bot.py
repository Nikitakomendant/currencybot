import telebot

bot = telebot.TeleBot('6120969307:AAEcEZX28TqMw3k_CXMnQrlqS_Ab5MPp7Pk')

# Инициализация конвертов
necessityEnvelop = 0  # NEC, необхідні витрати
freedomEnvelop = 0    # FFA, фінансова свобода
educationEnvelop = 0  # EDU, освіта
longTermEnvelop = 0   # LTSS, резерв та на великі покупки
playEnvelop = 0       # PLAY, розваги
giveEnvelop = 0       # GIVE, подарунки

# Инициализация процентных ставок
necRate = 0.55
ffaRate = 0.1
eduRate = 0.1
ltssRate = 0.1
playRate = 0.1
giveRate = 0.05

expectedIncome = 1000
current_sum = 0

# Стартовое сообщение
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, """Hello.\nWe gonna fill your envelops by the money you input here!\nPlease input your amounts of money income and see the results.\n\n Enter the amount please:""")

# Обработка введённой суммы 
@bot.message_handler(func=lambda message: True)
def handle_income(message):
    global necessityEnvelop, freedomEnvelop, educationEnvelop, longTermEnvelop, playEnvelop, giveEnvelop, current_sum

    try:
        income = float(message.text)  # Пробуем преобразовать введённый текст в число
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")
        return

    current_sum += income

    # Распределение по конвертам
    necessityEnvelop += income * necRate
    freedomEnvelop += income * ffaRate
    educationEnvelop += income * eduRate
    longTermEnvelop += income * ltssRate
    playEnvelop += income * playRate
    giveEnvelop += income * giveRate

    if current_sum >= expectedIncome:
        # Финальный вывод
        bot.send_message(message.chat.id, "At the end we have:\n\    Necessity Envelop has:                       " + str(int(necessityEnvelop)) + "\n\    Financial Freedom Envelop has:               " + str(int(freedomEnvelop)) + "\n\    Education Envelop                            " + str(int(educationEnvelop)) + "\n\    Long Term Saving for Spending Envelop has:   " + str(int(longTermEnvelop)) + "\n\    Play Envelop has:                            " + str(int(playEnvelop)) + "\n\    Give Envelop has:                            " + str(int(giveEnvelop)) + "\n\    _______________________________________________________________\n\\    Thanks for using our software :)")

bot.polling(none_stop=True)