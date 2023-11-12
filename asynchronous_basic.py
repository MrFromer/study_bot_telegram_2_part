import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import TOKEN_API
#19 урок асинхронное программирование и библиотека asyncio

# async def send_hello() -> None:
#     await asyncio.sleep(2)
#     print('Hello!')

# async def send_bye() -> None:
#     await asyncio.sleep(1)
#     print('Bye')

# async def main():
#     task_1 = asyncio.create_task(send_hello())
#     task_2 = asyncio.create_task(send_bye())

#     await task_1
#     await task_2

# asyncio.run(main())

#20 урок практика по теме asyncio 
# async def send_one() -> None:
#     n = 0
#     while True:
#         await asyncio.sleep(1)
#         n+=1
#         if n%3 !=0:
#             print(f'Прошло {n} секунд')
#         else:
#             pass
   

# async def send_three() -> None:
#     n_2 = 0
#     while True:
#         await asyncio.sleep(3)
#         n_2 +=3
#         print(f'Прошло ещё {n_2} секунды')

# async def main() -> None:
#     task_1 = asyncio.create_task(send_one())
#     task_2 = asyncio.create_task(send_three())
#     await task_1 
#     await task_2

# if __name__ == '__main__':
#     asyncio.run(main())

#21 урок практика по теме asyncio и асинхронному программированию
# async def send_time(sec: int) -> None:
#     while True:
#         await asyncio.sleep(sec)
#         print(f'Прошло {sec} секунд')

# #print(send_time(2), send_time(5), sep='\n')

# async def main() -> None:
#     task_1 = asyncio.create_task(send_time(2)) #это различные объекты корутин (асинхронной функции) и передавать в исполнение будет последовательно
#     task_2 = asyncio.create_task(send_time(5))
#     await task_1
#     await task_2


# if __name__ == '__main__':
#     asyncio.run(main())

#22 урок более подробно про CallBack запросы и CallbackQuery

# bot=Bot(token=TOKEN_API)
# dp = Dispatcher(bot)

# async def startup(_):
#     print('Бот был успешно запущен')

# ikb = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='❤️', callback_data='like'), InlineKeyboardButton(text='👎', callback_data='dislike')],
#     [],
# ])



# @dp.message_handler(commands=['start'])
# async def starter(message: types.Message) -> None:
#     await message.answer(text='Привет!', reply_markup=ikb)
#     await message.delete()

# @dp.callback_query_handler()
# async def ikb_cb_handler(callback: types.CallbackQuery):
#     if callback.data == 'like':
#         await callback.answer('Тебе понравилось!')
#     elif callback.data == 'dislike':
#         await callback.answer('Тебе не понравилось!')


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True, on_startup=startup)

#23 урок практика (создать бота, который будет отправлять конкретную фотографию, к которой будет прикреплена Inline клавиатура, состоящая из трёх опций: 1) убрать клавиатуру и фотографию 2) поставить лайк или дизлайк 3) при попытке нажать на конкретную опцию повторно, написать об этом"
bot=Bot(token=TOKEN_API)
dp = Dispatcher(bot)

async def startup(_):
    print('Бот был успешно запущен')

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='❤️',callback_data='like'),InlineKeyboardButton(text='👎',callback_data='dislike')],
    [InlineKeyboardButton(text='Закрыть клавиатуру', callback_data='close')]
])

flag1 = False
flag2 = False

@dp.message_handler(commands=['photo'])
async def sendphoto(message: types.Message):
    await bot.send_photo(chat_id = message.chat.id, photo='https://i.pinimg.com/originals/f7/24/82/f72482a5e66279d82ccf845ef103860f.jpg', caption='Как тебе эта фотография?', reply_markup=ikb)
    await message.delete()

@dp.callback_query_handler(text='close')
async def close_inlinekeyboard(callback: types.CallbackQuery) -> None:
    await callback.message.delete()
    
@dp.callback_query_handler()
async def callbacker(callback: types.CallbackQuery):
    global flag1
    global flag2
    if callback.data == 'like':
        if flag1 == True:
            await callback.answer('Ты уже лайкал данное фото', show_alert=True)
            
        else:
            #await callback.answer('Тебе понравилось данное фото!')
            await callback.answer('Тебе понравилось данное фото!', show_alert=True)
            flag1 = True

    elif callback.data == 'dislike':
        if flag2 == True:
            await callback.answer('Ты уже дизлайкал данное фото!', show_alert=True)
        else:
            await callback.answer('Тебе не понравилось данное фото!', show_alert=True)
            flag2 = True




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=startup)