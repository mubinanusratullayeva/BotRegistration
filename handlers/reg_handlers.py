from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from config import DB_NAME
from keyboards.reg_keyboards import kb_request_contact
from states.reg_states import RegisterStates


reg_router = Router()