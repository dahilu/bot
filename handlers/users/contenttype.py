from aiogram import types

from loader import dp
import logging


@dp.message_handler(content_types=types.ContentType.TEXT)
async def catch_text(m:types.Message):
    try:
        await m.answer("This is text")
    except Exception as err:
        logging.info(f"{err}")


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def catch_photo(m:types.Message):
    await m.photo[-1].download()
    await m.answer(f"id:{m.photo[-1].file_id}")

