from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, db


@dp.message_handler(Command("email"))
async def add_email(m:types.Message, state=FSMContext):
    await m.answer("Send email")
    await state.set_state("email")


@dp.message_handler(state="email")
async def enter_email(m:types.Message, state=FSMContext):
    email = m.text
    db.update_email(email, m.from_user.id)

    user = db.select_user(id=m.from_user.id)
    await m.answer(f"Data updated. {user=}")

    await state.finish()