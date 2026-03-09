# import math
# import os
from typing import Union
import requests

from generators import filter_by_currency
from proccessing import filter_by_state, sort_by_date
from src import masks
from src import proccessing
from src import widget
from src.decorators import log
from src.utils import get_operations_list, get_transaction_sum
# from src.generators import card_number_generator, filter_by_currency
# from src.utils import get_operations_list, get_transaction_sum
from src.csv_excel_reader import read_csv, read_excel
# from tests.conftest import transactions
from src.reg_exp_funcs import process_bank_operations, process_bank_search
from utils import get_operations_list

if __name__ == "__main__":

    file_type = int(input('''Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n
    '''))

    current_operations = []

    if file_type == 1:
        print('Для обработки выбран JSON-файл\n')
        current_operations = get_operations_list('data/operations.json')
    elif file_type == 2:
        print('Для обработки выбран CSV-файл\n')
        current_operations = read_csv('data/transactions.csv')
    elif file_type == 3:
        print('Для обработки выбран XLSX-файл\n')
        current_operations = read_excel('data/transactions_excel.xlsx')

    status = ''

    while True:
        status = input('''Введите статус, по которому необходимо выполнить фильтрацию. 
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n''').upper()

        if status in ['EXECUTED', 'CANCELED', 'PENDING']:
            break
        else:
            print(f'Статус операции {status} недоступен\n')

    current_operations = filter_by_state(current_operations, status)

    print(f'Программа: Операции отфильтрованы по статусу {status}\n')

    date_sort_flag = 0

    while True:
        date_sort_str = input('Отсортировать операции по дате? Да/Нет\n')

        if date_sort_str.lower() == 'да':
            date_sort_flag = 1
            break
        elif date_sort_str.lower() == 'нет':
            date_sort_flag = 0
            break
        else:
            print(f'Ответ {date_sort_str} не некорректный!\n')

    asc_flag = True

    if date_sort_flag == 1:
        while True:
            asc_str = input('Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию')

            if asc_str.lower() == 'по возрастанию':
                asc_flag = False
                break
            elif asc_str.lower() == 'по убыванию':
                asc_flag = True
                break
            else:
                print(f'Ответ {asc_str} не некорректный!\n')

    current_operations = sort_by_date(current_operations, asc_flag)

    rouble_flag = 0

    while True:
        rouble_str = input('Выводить только рублевые транзакции? Да/Нет\n')

        if rouble_str.lower() == 'да':
            rouble_flag = 1
            break
        elif rouble_str.lower() == 'нет':
            rouble_flag = 0
            break
        else:
            print(f'Ответ {rouble_str} не некорректный!\n')

    if rouble_flag == 1:
        filtered_operations = []
        currency_gen = filter_by_currency(current_operations, 'RUB')

        for i in range(0, len(current_operations)):
            try:
                filtered_operation = next(currency_gen)
                print(filtered_operation)
                filtered_operations.append(filtered_operation)
            except StopIteration:
                break
        current_operations = filtered_operations

    word_search_flag = 0

    while True:
        word_search_str = input('Отфильтровать список транзакций по определенному слову в описании?')

        if word_search_str.lower() == 'да':
            word_search_flag = 1
            break
        elif word_search_str.lower() == 'нет':
            word_search_flag = 0
            break
        else:
            print(f'Ответ {word_search_str} не некорректный!\n')

    search_word = ''

    if word_search_flag == 1:
        search_word = input('Введите слово для фильтрации')

    current_operations = process_bank_search(current_operations, search_word)

    print(current_operations)
