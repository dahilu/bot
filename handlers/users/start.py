import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
    name = message.from_user.full_name

    try:
        db.add_user(ids=message.from_user.id, name = name)
    except sqlite3.IntegrityError as err:
        print(err)

    count_users = db.count_users()[0]
    await message.answer(
        "\n".join([
            f"Hello, {message.from_user.full_name}",
            "You are added in db",
            f"Count users in db:<b>{count_users}</b>"

        ])
    )


