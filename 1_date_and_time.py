"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
import datetime

def print_days():
    today = datetime.date.today()
    print(f'Сегодня: {today.strftime("%Y-%m-%d")}')
    print(f'Вчера: {(today - datetime.timedelta(days=1)).strftime("%Y-%m-%d")}')
    print(f'Вчера: {(today - datetime.timedelta(days=30)).strftime("%Y-%m-%d")}')

def str_2_datetime(date_string):
    result = datetime.datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    return result

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
