from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalData(StatesGroup):
    fullName = State()
    murojat = State()
    phoneNum = State()
    chesk = State()