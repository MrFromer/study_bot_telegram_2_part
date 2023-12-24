import asyncio
from aiogram import Bot, Dispatcher, executor, types
<<<<<<< HEAD
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup, KeyboardButton
=======
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
>>>>>>> dcf7d57a65e5aa42170acfeb246fe02cc0909743
from config import TOKEN_API
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import BotBlocked
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
import hashlib
<<<<<<< HEAD
import uuid
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=storage)
=======
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage)
>>>>>>> dcf7d57a65e5aa42170acfeb246fe02cc0909743

async def startup(_):
    print('Бот был успешно запущен')

# #19 урок асинхронное программирование и библиотека asyncio

# # async def send_hello() -> None:
# #     await asyncio.sleep(2)
# #     print('Hello!')

# # async def send_bye() -> None:
# #     await asyncio.sleep(1)
# #     print('Bye')

# # async def main():
# #     task_1 = asyncio.create_task(send_hello())
# #     task_2 = asyncio.create_task(send_bye())

# #     await task_1
# #     await task_2

# # asyncio.run(main())

# #20 урок практика по теме asyncio 
# # async def send_one() -> None:
# #     n = 0
# #     while True:
# #         await asyncio.sleep(1)
# #         n+=1
# #         if n%3 !=0:
# #             print(f'Прошло {n} секунд')
# #         else:
# #             pass
   

# # async def send_three() -> None:
# #     n_2 = 0
# #     while True:
# #         await asyncio.sleep(3)
# #         n_2 +=3
# #         print(f'Прошло ещё {n_2} секунды')

# # async def main() -> None:
# #     task_1 = asyncio.create_task(send_one())
# #     task_2 = asyncio.create_task(send_three())
# #     await task_1 
# #     await task_2

# # if __name__ == '__main__':
# #     asyncio.run(main())

# #21 урок практика по теме asyncio и асинхронному программированию
# # async def send_time(sec: int) -> None:
# #     while True:
# #         await asyncio.sleep(sec)
# #         print(f'Прошло {sec} секунд')

# # #print(send_time(2), send_time(5), sep='\n')

# # async def main() -> None:
# #     task_1 = asyncio.create_task(send_time(2)) #это различные объекты корутин (асинхронной функции) и передавать в исполнение будет последовательно
# #     task_2 = asyncio.create_task(send_time(5))
# #     await task_1
# #     await task_2


# # if __name__ == '__main__':
# #     asyncio.run(main())

# #22 урок более подробно про CallBack запросы и CallbackQuery

# # bot=Bot(token=TOKEN_API)
# # dp = Dispatcher(bot)

# # async def startup(_):
# #     print('Бот был успешно запущен')

# # ikb = InlineKeyboardMarkup(inline_keyboard=[
# #     [InlineKeyboardButton(text='❤️', callback_data='like'), InlineKeyboardButton(text='👎', callback_data='dislike')],
# #     [],
# # ])



# # @dp.message_handler(commands=['start'])
# # async def starter(message: types.Message) -> None:
# #     await message.answer(text='Привет!', reply_markup=ikb)
# #     await message.delete()

# # @dp.callback_query_handler()
# # async def ikb_cb_handler(callback: types.CallbackQuery):
# #     if callback.data == 'like':
# #         await callback.answer('Тебе понравилось!')
# #     elif callback.data == 'dislike':
# #         await callback.answer('Тебе не понравилось!')


# # if __name__ == '__main__':
# #     executor.start_polling(dp, skip_updates=True, on_startup=startup)

# #23 урок практика (создать бота, который будет отправлять конкретную фотографию, к которой будет прикреплена Inline клавиатура, состоящая из трёх опций: 1) убрать клавиатуру и фотографию 2) поставить лайк или дизлайк 3) при попытке нажать на конкретную опцию повторно, написать об этом"
# bot=Bot(token=TOKEN_API)
# dp = Dispatcher(bot)

# async def startup(_):
#     print('Бот был успешно запущен')

# ikb = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='❤️',callback_data='like'),InlineKeyboardButton(text='👎',callback_data='dislike')],
#     [InlineKeyboardButton(text='Закрыть клавиатуру', callback_data='close')]
# ])

# flag1 = False
# flag2 = False

# @dp.message_handler(commands=['photo'])
# async def sendphoto(message: types.Message):
#     await bot.send_photo(chat_id = message.chat.id, photo='https://i.pinimg.com/originals/f7/24/82/f72482a5e66279d82ccf845ef103860f.jpg', caption='Как тебе эта фотография?', reply_markup=ikb)
#     await message.delete()

# @dp.callback_query_handler(text='close')
# async def close_inlinekeyboard(callback: types.CallbackQuery) -> None:
#     await callback.message.delete()
    
# @dp.callback_query_handler()
# async def callbacker(callback: types.CallbackQuery):
#     global flag1
#     global flag2
#     if callback.data == 'like':
#         if flag1 == True:
#             await callback.answer('Ты уже лайкал данное фото', show_alert=True)
            
#         else:
#             #await callback.answer('Тебе понравилось данное фото!')
#             await callback.answer('Тебе понравилось данное фото!', show_alert=True)
#             flag1 = True

#     elif callback.data == 'dislike':
#         if flag2 == True:
#             await callback.answer('Ты уже дизлайкал данное фото!', show_alert=True)
#         else:
#             await callback.answer('Тебе не понравилось данное фото!', show_alert=True)
#             flag2 = True



# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True, on_startup=startup)


#24 и 25 урок практика по созданию счётчика CallbackQuery, генерации случайного числа; (так-же рассмотрели задание Inline клавиатуры через функцию и задание фильтра для callback_data кнопок)

# from aiogram import types, executor, Dispatcher, Bot
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from config import TOKEN_API
# from random import randint


# bot = Bot(TOKEN_API)
# dp = Dispatcher(bot)

# async def startup(_):
#     print('Бот был успешно запущен')

# number = 0

# def get_inline_keyboard() -> InlineKeyboardMarkup:
#     ikb = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton('Increase', callback_data='btn_increase'), InlineKeyboardButton('Decrease', callback_data='btn_decrease'), InlineKeyboardButton('RandomInt', callback_data='btn_randint')],
#     ])

#     return ikb

# @dp.message_handler(commands=['start'])
# async def cmd_start(message: types.Message) -> None:
#     await message.answer(f'The current number is {number}', reply_markup=get_inline_keyboard())


# @dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('btn')) #callback_query - запрос колбэка
# async def ikb_cb_handler(callback: types.CallbackQuery) -> None:
#     global number 
    
    
#     if callback.data == 'btn_increase':
#         number += 1
#         await callback.message.edit_text(f'The current number is {number}',reply_markup=get_inline_keyboard())
#     elif callback.data == 'btn_decrease':
#         number -= 1
#         await callback.message.edit_text(f'The current number is {number}',reply_markup=get_inline_keyboard())
#     elif  callback.data == 'btn_randint':
#         randomint = randint(-1000,1000)
#         await callback.message.edit_text(f'Получилось вот такое рандомное число: {randomint}',reply_markup=get_inline_keyboard())
#     else:
#         1/0

# if __name__ == '__main__':
#     executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=startup)

# 26 урок Шаблон CallbackData() и callback_data
# from aiogram import types, executor, Dispatcher, Bot
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from config import TOKEN_API
# from aiogram.utils.callback_data import CallbackData

# bot = Bot(TOKEN_API)
# dp = Dispatcher(bot)

# async def startup(_):
#     print('Бот был успешно запущен')

# cb = CallbackData('ikb','action') #шаблон ikb - префикс (название для определённой работы, к примеру с числами или текстом) action - что нужно сделать (выполнить)

# ikb = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton('Button', callback_data=cb.new('push'))],
# ])

# @dp.message_handler(commands=['start'])
# async def cmd_start(message: types.Message) -> None:
#     await message.answer('text',reply_markup=ikb)
    

# @dp.callback_query_handler(cb.filter()) #можно задать фильр для cb, к примеру cb.filter(action=push) фильтр на кнопку pushs
# async def ikb_callback_handler(callback: types.CallbackQuery, callback_data: dict) -> None:
#     if callback_data['action'] == 'push':
#         await callback.answer('smth')
    


#27 урок Errors Handler (Ислючения Хэндлеров)

# @dp.message_handler(commands=['start'])
# async def cmd_start(message: types.Message) -> None:
#     await asyncio.sleep(10)
#     await message.answer('ddddd')

# @dp.errors_handler(exception=BotBlocked)
# async def error_bot_blocked(update: types.Update, exception: BotBlocked) -> bool:
#     print('Низя отправить сообщение, потому что нас заблокировали')
#     return True

#28-30 урок Inline режим; inline_query

#31 урок создаём Inline Echo бота

#ТУТ МЫ ДЕЛАЕМ БОТА С ФИЛЬРОМ НА ДЕЙСТВИЕ INLINE КНОПКИ
# cb = CallbackData('ikb', 'action')
# def inline_keyboard() -> InlineKeyboardMarkup:
#     ikb = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text='Button 1', callback_data=cb.new('push1')),InlineKeyboardButton(text='Button 2', callback_data=cb.new('push2'))],
#     ])
#     return ikb

# @dp.message_handler(commands=['start'])
# async def startbot(message: types.Message) -> None:
#     await bot.send_message(chat_id=message.chat.id, text='Салам братанам!', reply_markup=inline_keyboard())
#     #await message.delete()

# @dp.callback_query_handler(cb.filter(action='push1'))
# async def push_first(callback: types.CallbackQuery) -> None:
#     await callback.answer('Hello')

# @dp.callback_query_handler(cb.filter(action='push2'))
# async def push_second(callback: types.CallbackQuery) -> None:
#     await callback.answer('World!')

#СОЗДАЁМ ECHO BOTA ЧЕРЕЗ INLINE РЕЖИМ
# @dp.inline_handler() #процесс InlineQuery() формируется при помощи Telegram API
# async def inline_echo(inline_query: types.InlineQuery) -> None:
#     text = inline_query.query or 'Echo' #получили текст от пользователя
#     input_content = InputTextMessageContent(text) #формируем контент ответного сообщения
#     result_id = hashlib.md5(text.encode()).hexdigest() #берём сообщение --> переводим в двоичную сист. счисления --> кодируем --> переводим в 16-ти ричную (т.е мы просто из текст сделали уникальный id)
#     item = InlineQueryResultArticle(input_message_content=input_content, id=result_id, title='Echo') #формируем итоговый объект для ответа пользователю (ниже он стоит в result т.е то, что принимается в качестве ответа)
#     await bot.answer_inline_query(inline_query_id=inline_query.id, results=[item], cache_time=1)

#32 урок Inline Бот - Практическое видео на тему inline_query
# @dp.inline_handler()
# async def inline_answer(inline_query: types.InlineQuery) -> None:
#     text = inline_query.query or 'Echo' #создаём сам запрос
#     input_content = InputTextMessageContent(text) #принимаем на вход текст от пользователя
#     result_id = hashlib.md5(text.encode()).hexdigest()
    
#     if text =='photo':
#         input_content = InputTextMessageContent('This is a photo') #принимаем на вход текст от пользователя
        
#     item = InlineQueryResultArticle(input_message_content=input_content, id=result_id, title=text)

#     await bot.answer_inline_query(inline_query_id=inline_query.id, results=[item],cache_time=1)

<<<<<<< HEAD
#34 урок Urls Inline Бот | Title, Description - непонятная шняга
# class A:
#     x = 5
#     y = 2
#     def add(self, a: int, b: int) -> int:
#         return a + b
# a = A()
# print(a.add(5,3))
# A.add = classmethod(A.add)

#35 урок Практика по созданию echo бота через inline_query с функционалом выбора написать жирным шрифтом, курсивом или когда ничего не выбрал - Empty
# @dp.inline_handler()
# async def inline_answer(inline_query: types.InlineQuery) -> None:
#     text = inline_query.query or 'Empty'
#     input_bold = types.InputTextMessageContent(message_text=f'*{text}*', parse_mode='markdown') #чтобы текст, который введёт пользователь делался жирным
#     input_italic = types.InputTextMessageContent(message_text=f'_{text}_', parse_mode='markdown') #чтобы текст, который введёт пользователь делался курсивом
#     item_1 = types.InlineQueryResultArticle(id=str(uuid.uuid4()), input_message_content=input_bold, title='Bold', description=text, thumb_url='https://s.rbk.ru/v1_companies_s3/resized/1200xH/media/trademarks/3a072b7c-97fd-4cf4-be99-1cc9ba090933.jpg') 
#     #т.е тут через types мы создаём более расширенную версию InlineQuery в id через uuid индифицируем айдишник сообщения; далее в input_message вносим текст с параметром Bold; в description текст, который ввёл пользователь; в thump_url = картинку, которая будет отображаться в боте
#     item_2 = types.InlineQueryResultArticle(id=str(uuid.uuid4()), input_message_content=input_italic,  title='Italic', description=text, thumb_url='https://sgmsummers.files.wordpress.com/2014/10/italic.jpg')
#     await bot.answer_inline_query(inline_query_id=inline_query.id, results=[item_1,item_2],cache_time=1) #в results передаёт два параметра

#урок FSM машина состояний для телеграмм бота на Python
#storage = MemoryStorage() - объявил это в самом начале. Это временная память, для не особо важных элементов и работает это через машину состояний



storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot=bot,
                storage=storage)

def get_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Начать работу!'))

    return kb

def get_cancel() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/cancel'))


class ClientStatesGroup(StatesGroup):
    photo = State()
    desc = State()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Добро пожаловать', reply_markup=get_keyboard())


@dp.message_handler(commands=['cancel'], state='*')
async def cmd_start(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    await message.reply('Отменил', reply_markup=get_keyboard())
    await state.finish()


@dp.message_handler(Text(equals='Начать работу!', ignore_case=True), state=None)
async def start_work(message: types.Message) -> None:
    await ClientStatesGroup.photo.set()
    await message.answer('Сначала отправь нам фотографию!', reply_markup=get_cancel())


@dp.message_handler(lambda message: not message.photo, state=ClientStatesGroup.photo)
async def check_photo(message: types.Message):
    return await message.reply('Это не фотография!')


@dp.message_handler(lambda message: message.photo, content_types=['photo'], state=ClientStatesGroup.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await ClientStatesGroup.next()
    await message.reply('А теперь отправь нам описание!')


@dp.message_handler(state=ClientStatesGroup.desc)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['desc'] = message.text

    await message.reply('Ваша фотография сохранена!')

    async with state.proxy() as data:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'],
                             caption=data['desc'])

    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)
=======
#36 и 37 урок FSM - машина состояний автомат
def btn() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('/create'))
    return kb
class Profile(StatesGroup):
    photo = State()
    name = State()
    age = State()
    desc = State()
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Welcome and write /create',reply_markup=btn())
>>>>>>> dcf7d57a65e5aa42170acfeb246fe02cc0909743

@dp.message_handler(commands=['create'])
async def cmd_create(message: types.Message) -> None:
    await message.answer('Create your profile! And send me your photo')
    await Profile.photo.set()

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=startup)
