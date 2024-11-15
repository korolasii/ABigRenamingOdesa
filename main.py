import asyncio
import logging
import sys
import json

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BotCommand

from searchStreetName import searchStreet

# Function to open JSON file and return its data
def open_json(name):
    with open(name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# Function to set bot commands
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Start"),
        BotCommand(command="/help", description="Help"),
    ]
    await bot.set_my_commands(commands)


dp = Dispatcher()


# Handler for the /start command
@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer("Good day, I am your assistant")


# Handler for the /help command
@dp.message(Command("help"))
async def help_handler(message: Message) -> None:
    await message.answer(
        """I am a bot that helps with street names.
        You can write me an old street name, and I will give you the new one and vice versa.
        I hope I can help you."""
    )


# General message handler for other messages
@dp.message()
async def answerBot(message: Message) -> None:
    try:
        response = searchStreet(message.text)  # Search for street name in the database
        if response == 'Нічого не найдено':  # If no results found
            await message.answer(response)
        else:
            # If a result is found, format and send the response
            answer = f'Old name - {response["oldName"]}\nNew name - {response["newName"]}\nHistory - {response["history"]}'
            await message.answer(answer)
    except TypeError:
        # If an error occurs, provide a general error message
        await message.answer("Something went wrong, you can send the error to email example@gmail.com")


# Main function to run the bot
async def main(TOKEN) -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))  # Initialize the bot with HTML format
    await set_commands(bot)  # Set the bot commands
    await dp.start_polling(bot)  # Start polling for messages


if __name__ == "__main__":
    # Load bot token from the JSON file
    TOKEN = open_json('bot_data.json').get('TOKEN')
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)  # Set up logging
    asyncio.run(main(TOKEN))  # Run the bot asynchronously
