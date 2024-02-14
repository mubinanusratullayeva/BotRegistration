from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_register = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Registration')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Please, click button 'Registration'",
    one_time_keyboard=True
)

kb_request_contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text='Send telephone number',
                request_contact=True
            )
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Please, click button 'Send telephone number'",
    one_time_keyboard=True
)