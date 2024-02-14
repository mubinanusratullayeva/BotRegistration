from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from config import DB_NAME
from keyboards.reg_keyboards import kb_request_contact
from states.reg_states import RegisterStates
from utils.database import DataBase


db = DataBase(DB_NAME)


reg_router = Router()


@reg_router.message(F.text == 'Registration')
async def register_start(message: Message, state=FSMContext):
    users = db.get_user(message.from_user.id)
    if users[5]:
        await message.answer(
            f"{users[6]}, you've registered!",
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        await message.answer(
            "we'll start registration process!\n"
            "Please, enter your full name and surename:",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(RegisterStates.regName)


@reg_router.message(RegisterStates.regName)
async def register_name(message: Message, state=FSMContext):
    await message.answer(
        f"Nice {message.text}\nPlease, send you phone number",
        reply_markup=kb_request_contact
    )
    await state.update_data(regname=message.text)
    await state.set_state(RegisterStates.regPhone)

@reg_router.message(RegisterStates.regPhone)
async def register_phone(message: Message, state=FSMContext):
    try:
        await state.update_data(regphone=message.contact.phone_number)
        reg_data = await state.get_data()
        reg_name = reg_data.get('regname')
        reg_phone = reg_data.get('regphone')

        await message.answer(
            f"{reg_name}, you successfully registered",
            reply_markup=ReplyKeyboardRemove()
        )
        db.update_user(message.from_user_id, reg_name, reg_phone)
        await state.clear()
    except:
        await message.answer(
            f"Please, Send your phone number",
            reply_markup=kb_request_contact
        )