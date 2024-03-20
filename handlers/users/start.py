from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.keyboard import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Assalomu alaykum. Jizzax viloyat Iste’molchilar huquqlarini himoya qilish hududiy birlashmasining “Kafolatli tibbiy xizmat” telegram botiga xush kelibsiz.", reply_markup=menu)

@dp.message_handler(text="📑 Biz haqimizda")
async def bot_start(message: types.Message):
    await message.answer("Jizzax viloyat Iste'molchilar huquqlarini himoya qilish hududiy birlashmasi viloyat aholisining iste'molchilik huquqlarini himoya qilish, aholi orasida iste'mol madaniyatini oshirish maqsadida  faoliyat yuritib kelmoqda. Birlashmaning Jizzax viloyatidagi mavjud 11 ta tumanlarida ham jamiyatlari  mavjud bo'lib, ushbu jamiyatlar ham viloyat aholisining haq-huquqlarini himoya qilishni o'z oldiga maqsad qilib qo'ygan.")


@dp.message_handler(text="📑 Normativ-huquqiy hujjatlar")
async def bot_start(message: types.Message):
    await message.answer("""O'zbekiston Respublikasida iste'molchilar huquqlarini himoya qilishning aniq mexanizmlari ishlab chiqilgan bo'lib, iste'molchi va xizmat ko'rsatuvchi o'rtasidagi munosabatlar muayyan qonun-qoidalar asosida tartibga solinadi. Jumladan, 1996-yil 26-aprelda qabul qilingan O'zbekiston Respublikasining "Iste'molchilar huquqlarini himoya qilish to'g'risida"gi qonuni, shuningdek, O'zbekiston Respublikasi Vazirlar Mahkamasining 2002-yil 28- noyabrda qabul qilingan "Iste’molchilar huquqlarini himoya qilishda jamoatchilik ishtirokini kengaytirish chora tadbirlari to’g’risida" qarori shular jumlasidandir.""")


@dp.message_handler(text="📍 Manzil")
async def bot_start(message: types.Message):
    await message.answer("O'zbekiston Iste'molchilar huquqlarini himoya qilish jamiyatlari Federatsiyasining Jizzax viloyat hududiy birlashmasi Jizzax shahri Sharof Rashidov ko'chasi 63-uyda joylashgan.")

