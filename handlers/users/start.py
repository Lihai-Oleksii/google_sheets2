import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.opencatalog import main_menu
from loader import dp
from aiogram.dispatcher import FSMContext
from states.all_states import Texts,Acc,Other,Acc_FB
import datetime
from main import add_user


@dp.message_handler(text='/start',state='*')
async def get_accounts(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Введите пароль')
    await Other.Q1.set()


@dp.message_handler(state=Other.Q1)
async def get_accounts(message: types.Message, state: FSMContext):
    if message.text == 'mypassword':
        await message.answer('Принято.',reply_markup=main_menu)
        await Texts.Q1.set()


@dp.message_handler(state=Texts.Q1)
async def asd(message: types.Message):
    await message.answer('Нажмите "Добавить запись"')
    await Texts.Q2.set()


@dp.message_handler(text='Добавить запись')
async def get_address(message: types.Message, state: FSMContext):
    await message.answer('Укажите номер телефона клиента')
    await Texts.Q3.set()


@dp.message_handler(state=Texts.Q3)
async def get_address(message: types.Message, state: FSMContext):
    number = message.text
    await state.update_data(number=number)
    await message.answer('Укажите имя клиента')
    await Texts.next()


@dp.message_handler(state=Texts.Q4)
async def get_address(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer('Укажите город клиента')
    await Texts.next()


@dp.message_handler(state=Texts.Q5)
async def get_address(message: types.Message, state: FSMContext):
    city = message.text
    await state.update_data(city=city)
    await message.answer('Укажите исчтоник рекламы')
    await Texts.Q7.set()

@dp.message_handler(state=Texts.Q7)
async def get_address(message: types.Message, state: FSMContext):
    ist = message.text
    await state.update_data(ist=ist)
    await Texts.next()
    data = await state.get_data()
    number = data.get('number')
    ist = data.get('ist')
    city = data.get('city')
    name = data.get('name')
    now = datetime.datetime.now()
    await message.answer(f'Итого:'
                         f'\nДата: {(now)}'
                         f'\nномер: {number}'
                         f'\nимя: {name}'
                         f'\nиточник: {ist}'
                         f'\nгород: {city}')
    z = [now.strftime("%d-%m-%Y %H:%M"),number,name,city,ist]
    print(z)
    add_user(z)
    await state.finish()



    






