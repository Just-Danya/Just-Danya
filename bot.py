import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config_reader import config
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types import URLInputFile

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Диспетчер
dp = Dispatcher()



# Для записей с типом Secret* необходимо 
# вызывать метод get_secret_value(), 
# чтобы получить настоящее содержимое вместо '*******'
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")






# Хэндлер на команду /start - начальное меню
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Беседа ИКТ-37", 
        url="https://t.me/+plICg8WcSl8zNTNi")
    )
    builder.row(types.InlineKeyboardButton(
        text="Написать разработчику",
        url="https://t.me/just_danya_kr")
    )
    builder.row(types.InlineKeyboardButton(
        text="Помощь",  callback_data="help") 
    )
    await message.answer(
        "<b><i>Мы вас приветсвуем, мы рады что вы реши нами воспользоваться)))</i> \n<u>Выбирите, что вы хотите сделать:</u></b>",
        reply_markup=builder.as_markup()
    )





# Хендлер help и для кнопки start - о командах бота
@dp.message(Command('help'))
async def help(message: types.Message):
    await message.reply('/start - для начального меню \n'
                        '/help - тут описаны все важные команды\n'
                        '/information - информация о боте\n'
                        '/students - про студентов IKT-37')
@dp.callback_query(F.data == 'help')
async def help(callback: types.CallbackQuery):
    await callback.message.answer('/start - для начала использования бота \n'
                        '/help - тут описаны все важные команды\n'
                        '/information - информация о боте\n'
                        '/students - про студентов IKT-37')
    await callback.answer()





# Хендлер information - информация о боте
@dp.message(Command('information'))
async def help(message: types.Message):
    image = URLInputFile('https://sun9-34.userapi.com/impg/wARHgJ5H368qnfFmpJpIY_mAqsQj7HGPi6sQjA/pWJXTxwyUH8.jpg?size=1440x2160&quality=95&sign=d8a86351a8cb61bc636e9e2217e7eed9&type=album')

    await bot.send_photo(message.chat.id, image , caption='<i><u><b>Разработчик бота</b> - Краснянский Даниил Михайлович</u>\n'
    'Этот бот создан для того чтобы лучше узнать, как кого зовут! Я выполнял этого бота для тренировки себя в программирование.</i>\n'
    'В этом боте рассказано про каждого студента группы IKT-37.')






# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())