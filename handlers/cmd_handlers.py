from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import  CommandStart, Command

from keyboards.reg_keyboards import kb_register
from utils.database import DataBase
from config import DB_NAME


db = DataBase(DB_NAME)


cmd_router = Router()


@cmd_router.message(CommandStart())
async def cmd_start(message: Message):
    users = db.get_user(message.from_user.id)
    if not users:
        msg = message.from_user
        db.add_new_user(msg.id, msg.username, msg.first_name, msg.last_name)
        await message.answer(text="Please, register!", reply_markup=kb_register)
    elif not users[6]:
        await message.answer(text="Please, register!", reply_markup=kb_register)
    else:
        await message.answer(f"<b><a href='https://t.me/{users[3]}'>{users[6]}</a>, welcome")


@cmd_router.message(Command('code'))
async def cmd_code(message: Message):
    s = ("This is a Python code:"
         "<pre><code language='python'>\n"
         "print('Hello world')"
         "</code></pre>")
    x = ("```\n"
         "print('dfghj')\n"
         "```")
    await message.answer(text=s)
    await message.answer(text=x, parse_mode=ParseMode.MARKDOWN_V2)