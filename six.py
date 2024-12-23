import tracemalloc
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import random

# Включаем tracemalloc
tracemalloc.start()

# Состояние игроков
players = {}

# Генерация кнопок меню
def get_main_menu():
    keyboard = [
        [InlineKeyboardButton("Учиться", callback_data="study"),
         InlineKeyboardButton("Работать", callback_data="work")],
        [InlineKeyboardButton("Отдыхать", callback_data="rest"),
         InlineKeyboardButton("Купить еду", callback_data="buy_food")],
        [InlineKeyboardButton("Проверить состояние", callback_data="status")],
        [InlineKeyboardButton("Начать карьеру", callback_data="start_career")]
    ]
    return InlineKeyboardMarkup(keyboard)

# Начало игры
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    players[chat_id] = {
        "health": 100,
        "energy": 100,
        "knowledge": 0,
        "money": 50,
        "luck": random.uniform(0.5, 1.5),
        "exam_counter": 5,
        "turn": 0,
        "career": None
    }
    await update.message.reply_text(
        "Добро пожаловать в игру 'Жизнь студента'! Используй кнопки ниже для взаимодействия.",
        reply_markup=get_main_menu()
    )

# Проверка состояния
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id

    if chat_id not in players:
        await query.message.reply_text("Ты ещё не начал игру! Используй команду /start.")
        return

    player = players[chat_id]
    await query.message.reply_text(
        f"Текущее состояние:\n"
        f"Здоровье: {player['health']}\n"
        f"Энергия: {player['energy']}\n"
        f"Знания: {player['knowledge']}\n"
        f"Деньги: {player['money']}\n"
        f"Сессия через: {player['exam_counter']} ходов\n"
        f"Карьера: {player['career'] if player['career'] else 'Не выбрана'}",
        reply_markup=get_main_menu()
    )

# Учёба
async def study(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id

    player = players[chat_id]
    if player["energy"] >= 20:
        player["energy"] -= 20
        knowledge_gain = int(15 * player["luck"])
        player["knowledge"] += knowledge_gain
        player["exam_counter"] -= 1
        player["turn"] += 1
        await query.message.reply_text(
            f"Ты учился и получил {knowledge_gain} знаний. Энергия уменьшилась.",
            reply_markup=get_main_menu()
        )
    else:
        await query.message.reply_text(
            "Недостаточно энергии для учёбы. Отдохни!",
            reply_markup=get_main_menu()
        )
    await check_events(update, context)
    await check_exam(update, context)

# Работа
async def work(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id

    player = players[chat_id]
    if player["energy"] >= 30:
        player["energy"] -= 30
        money_gain = int(20 * player["luck"])
        player["money"] += money_gain
        player["exam_counter"] -= 1
        player["turn"] += 1
        await query.message.reply_text(
            f"Ты работал и заработал {money_gain} денег. Энергия уменьшилась.",
            reply_markup=get_main_menu()
        )
    else:
        await query.message.reply_text(
            "Недостаточно энергии для работы. Отдохни!",
            reply_markup=get_main_menu()
        )
    await check_events(update, context)
    await check_exam(update, context)

# Отдых
async def rest(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id

    player = players[chat_id]
    player["health"] += 10
    player["energy"] += 30
    player["turn"] += 1
    await query.message.reply_text(
        "Ты отдохнул и восстановил силы. Здоровье и энергия увеличились.",
        reply_markup=get_main_menu()
    )
    await check_events(update, context)

# Покупка еды
async def buy_food(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id

    player = players[chat_id]
    if player["money"] >= 20:
        player["money"] -= 20
        player["health"] += 30
        await query.message.reply_text(
            "Ты купил еду и восстановил здоровье. Деньги уменьшились.",
            reply_markup=get_main_menu()
        )
    else:
        await query.message.reply_text(
            "Недостаточно денег для покупки еды!",
            reply_markup=get_main_menu()
        )

# Начало карьеры
async def start_career(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id

    player = players[chat_id]
    if player["knowledge"] >= 50:
        career_options = ["Программист", "Инженер", "Менеджер"]
        player["career"] = random.choice(career_options)
        player["money"] += 100
        await query.message.reply_text(
            f"Ты начал карьеру: {player['career']}. Бонус: 100 денег.",
            reply_markup=get_main_menu()
        )
    else:
        await query.message.reply_text(
            "Недостаточно знаний для начала карьеры. Учись больше!",
            reply_markup=get_main_menu()
        )

# Проверка событий
async def check_events(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.callback_query.message.chat_id
    player = players[chat_id]

    events = {
        5: "Ты нашёл кошелёк на улице. Оставить себе?",
        11: "Друг предлагает поучаствовать в стартапе. Присоединиться?",
        20: "Тебе предложили стажировку. Пройти её?",
        27: "Профессор дал возможность выполнить бонусный проект. Взяться?",
        35: "Ты нашёл полезный ресурс для учёбы. Использовать?",
        42: "Кто-то предложил курс по саморазвитию. Записаться?",
        50: "Тебя пригласили на оплачиваемый проект. Принять?"
    }

    if player["turn"] in events:
        event_text = events[player["turn"]]
        keyboard = [
            [InlineKeyboardButton("Да", callback_data=f"event_yes_{player['turn']}"),
             InlineKeyboardButton("Нет", callback_data=f"event_no_{player['turn']}")]
        ]
        await update.callback_query.message.reply_text(
            event_text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

# Обработка событий
async def handle_event(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id
    player = players[chat_id]

    action = query.data.split('_')[1]
    event_turn = int(query.data.split('_')[-1])

    if action == "yes":
        if event_turn == 5:
            player["money"] += 50
            await query.message.reply_text("Ты оставил кошелёк себе и получил 50 денег.")
        elif event_turn == 11:
            player["luck"] += 0.2
            await query.message.reply_text("Ты присоединился к стартапу и повысил удачу!")
        elif event_turn == 20:
            player["knowledge"] += 30
            await query.message.reply_text("Ты прошёл стажировку и увеличил знания.")
        elif event_turn == 27:
            player["knowledge"] += 20
            await query.message.reply_text("Ты выполнил проект и улучшил знания.")
        elif event_turn == 35:
            player["knowledge"] += 15
            await query.message.reply_text("Ты воспользовался ресурсом и получил знания.")
        elif event_turn == 42:
            player["knowledge"] += 10
            await query.message.reply_text("Ты записался на курс и стал умнее.")
        elif event_turn == 50:
            player["money"] += 70
            await query.message.reply_text("Ты принял проект и получил деньги.")
    else:
        await query.message.reply_text("Ты решил ничего не делать.")

# Проверка экзамена
async def check_exam(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.callback_query.message.chat_id
    player = players[chat_id]

    if player['exam_counter'] <= 0:
        if player['knowledge'] >= 50:
            player['knowledge'] = 0
            player['exam_counter'] = 5
            await update.callback_query.message.reply_text(
                "Ты успешно сдал сессию!"
            )
        else:
            player['health'] -= 30
            player['exam_counter'] = 5
            await update.callback_query.message.reply_text(
                "Ты провалил сессию и потерял здоровье!"
            )

# Основной запуск
def main() -> None:
    application = Application.builder().token("7631428660:AAHfZiybtXP26bWvQgSKtk3nQRwsx6fePpQ").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(status, pattern="status"))
    application.add_handler(CallbackQueryHandler(study, pattern="study"))
    application.add_handler(CallbackQueryHandler(work, pattern="work"))
    application.add_handler(CallbackQueryHandler(rest, pattern="rest"))
    application.add_handler(CallbackQueryHandler(buy_food, pattern="buy_food"))
    application.add_handler(CallbackQueryHandler(start_career, pattern="start_career"))
    application.add_handler(CallbackQueryHandler(handle_event, pattern="event_.*"))

    application.run_polling()

if __name__ == "__main__":
    main()
