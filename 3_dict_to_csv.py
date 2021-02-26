"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv
import random

names = ['Mike', 'Peter', 'Anna', 'Maria', 'Natasha', 'Roman']
job = ['worker', 'manager', 'director', 'programmer', 'tester', 'writer']

def generate_workers_list():
    list = []
    for _ in range(6):
        worker = {}
        worker['name'] = random.choice(names)
        worker['age'] = random.randint(21, 65)
        worker['job'] = random.choice(job)
        list.append(worker)
    return list

def main():
    with open('workers.csv', 'w', newline='') as csvfile:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(csvfile, fieldnames=fields, delimiter=',')
        
        writer.writeheader()
        workers = generate_workers_list()
        for worker in workers:
            writer.writerow(worker)

if __name__ == '__main__':
    main()
