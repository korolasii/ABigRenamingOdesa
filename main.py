import asyncio
import logging
import sys
import json

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

from searchStreetName import searchStreet

# Function to open JSON file and return its data
def open_json(name):
    with open(name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


dp = Dispatcher()

def moreInfo(urlMap):
    inline_kb_list = [
        [InlineKeyboardButton(text="Історія", callback_data="history")],
        [InlineKeyboardButton(text="Знайти на мапі", web_app=WebAppInfo(url=urlMap))], # type: ignore
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def start_keyBoard():
    button1 = KeyboardButton(text='🔍 Почати пошук вулиць')
    button_rows = [button1]
    keyboard = ReplyKeyboardMarkup(keyboard = [button_rows], resize_keyboard=True)
    return keyboard


# Handler for the /start command
@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer("Доброго дня, я ваш помічник, який допоможе вам знайти нові назви вулиць Одеси\nНапишіть мені стару назву, а я дам вам нову і навпаки\nЯ сподіваюся, що зможу вам допомогти.", reply_markup=start_keyBoard())


@dp.callback_query()
async def callback_handler(callback_query: CallbackQuery) -> None:
    action = callback_query.data
    message = callback_query.message.text
    original_text = message[message.find('-')+2:message.find("\n")]
    if action == "history":
        response = searchStreet(original_text)
        print(original_text)
        if response == 'Нічого не найдено':
            await callback_query.message.answer("Історія не знайдена.")
        else:
            await callback_query.message.answer(
                f'<strong>Історія</strong> : {response["history"]}'
            )
    await callback_query.answer() 

# General message handler for other messages
@dp.message()
async def answerBot(message: Message) -> None:
    if message.text == '🔍 Почати пошук вулиць':
        await message.answer('Введіть назву вулиці')
    else:
        try:
            response = searchStreet(message.text)  # Search for street name in the database
            if response == 'Нічого не найдено':  # If no results found
                await message.answer(response)
            else:
                # If a result is found, format and send the response
                answer = f'<strong>Стара назва</strong> - {response["oldName"]}\n<strong>Нова назва</strong> - {response["newName"]}'
                await message.answer(answer, reply_markup=moreInfo(response["url"]))
        except TypeError:
            # If an error occurs, provide a general error message
            await message.answer("Щось пішло не так, ви можете надіслати повідомлення про помилку на електронну пошту example@gmail.com")


# Main function to run the bot
async def main(TOKEN) -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))  # Initialize the bot with HTML format
    await dp.start_polling(bot)  # Start polling for messages


if __name__ == "__main__":
    # Load bot token from the JSON file
    TOKEN = open_json('bot_data.json').get('TOKEN')
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)  # Set up logging
    asyncio.run(main(TOKEN))  # Run the bot asynchronously
